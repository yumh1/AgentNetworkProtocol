# 05-AgentNetworkProtocol元协议的设计规范

备注：
- 本章节内容为草稿阶段，后续可能会根据实际情况进行大幅调整。

## 背景

**元协议（Meta-Protocol）**，即协商通信使用协议的协议，具体来说是一种定义协议如何操作、解析、组合和交互的协议。它提供协议的规则和模式，帮助设计通用、扩展性强的通信机制。元协议通常不处理具体的数据传输，而是定义通信框架和协议运行的基本约束。

元协议能够极大的提高智能体之间的通信效率，降低智能体之间通信成本。智能体之间如果采用自然语言传递数据，在智能体内部需要使用LLM对数据进出处理，信息处理效率低，成本高。使用元协议，结合AI生成代码处理协议的代码，可以：
- 提高数据传输效率：在数据进入LLM之前，先进行协议协商，可以减少LLM处理的数据量，提高数据传输效率。
- 提高数据理解的准确性：通过数据源对数据结构化，而非直接让LLM处理非结构化的数据，可以提高数据理解的准确性。
- 降低数据处理复杂度：特定领域数据复杂度高，当前行业已经有大量协议规范，无法使用自然语言传递，比如音视频数据。

同时，在人工智能加持下的元协议，能够让智能体网络变成一个自组织、自协商的协作网络。自组织、自协商是指智能体网络中的各个智能体能够自主地进行相互连接、协议协商、协议共识达成。通过自然语言和元协议，智能体可以互相沟通各自的能力、数据格式和使用的协议，最终选出最优的通信协议，确保整个网络的高效协作和信息传递。

在元协议层，我们主要参考和借鉴了Agora Protocol（https://arxiv.org/html/2410.11905v1）的思路，结合协议在具体场景中的最佳实践与挑战，设计了AgentNetworkProtocol的元协议规范。

## 元协议协商流程

### 当前协议是如何协商的

在现在的软件系统中，如果对外提供的开发的API，一般会给出API调用方法，包含API的调用参数、返回值、使用的协议等。这个过程本质上就是协议协商的过程。它有以下缺点：
- 需要人工设计协议，并且编写协议处理代码。如果没有相应的协议，则无法进行通信。
- 协议的对接需要大量的人工参与，中间需要进行多次的沟通和确认。
- 如果行业没有标准规范，多个系统使用不同的定义，调用者需要分别进行协商和对接

### 元协议协商流程

LLM加持的智能体结合元协议可以有限的解决现有软件系统协议协商的问题，它的主要流程如下：

```plaintext
  Agent (A)                                       Agent (B)
    |                                                 |
    | -- Initiate Protocol Negotiation Process -->    |
    |                                                 |
    |      (Exchange Capabilities and Data Formats)   |
    |                                                 |
    | <---- Capabilities and Formats Exchanged ----   |
    |                                                 |
    |       (Determine Protocol details)              |
    |                                                 |
    |                   ......                        |
    |      (Multiple negotiations may occur)          |
    |                                                 |
    |---------------                                  |
    |              |                                  |
    |   Protocol Code Generated                       |
    |              |                                  |
    | <-------------                                  |
    |                                                 |---------------  
    |                                                 |              |
    |                                                 |   Protocol Code Generated
    |                                                 |              |
    |                                                 | <-------------  
    |                                                 |
    |  <--------- Interoperability Test ----------->  |
    |                                                 |
    |           (Resolve Issues if Any)               |
    |                                                 |
    |  <----- Protocol Negotiation Completed ------>  |
    |                                                 |
    |                                                 |
    |    (Start Communication Using Final Protocol)   |
    |                                                 |
    | ---- Communication Started ---->                |
    |                                                 |
    |      (Send and Receive Messages)                |
    |                                                 |
    | <---- Messages Exchanged ----                   |
    |                                                 |
```

如图所示，智能体A向智能体B发起协议协商过程如下：
- 智能体A首先使用自然语言，向智能体B发起协议协商，携带A的需求、能力、期望协议规范等，可能有多个选项供B选择
- 智能体B收到A的协商请求后，根据A提供的信息，使用自然语言，向A回复B的能力、确定的协议规范等
- 智能体A和智能体B之间可能经过多轮协商，最终确定智能体之间通信使用的协议规范
- 根据协商结果，智能体A和B使用AI生成处理协议的代码。为了安全考虑，生成的代码建议在沙盒中运行
- 智能体之间进行协议互通测试，使用AI判断协议消息是否符合协商规范，如果不符合，则通过自然语言交互进行自动解决
- 最后，确定最终使用协议，智能体A和B使用最终的协议进行通信

通过以上的流程我们可以看到，智能体使用元协议进行协议协商，结合代码生成技术，可以极大的提高协议协商的效率，降低协议协商的成本。同时，也让智能体网络变成一个自组织、自协商的协作网络。

### 流程消息格式定义

协商消息基于[端到端加密](03-基于did%3Aall方法的端到端加密通信技术协议.md)消息的encryptedData进行扩展，属于加密消息的上层消息。

加密消息encryptedData的ciphertext解密后的消息格式设计如下：

```plaintext
0               1               2               3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 0 ...
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|PT |  Reserved |              Protocol data                    | ...
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

```
- PT: Protocol Type，2bit，表示协议类型
    - 00：meta protocol，元协议
    - 01：application protocol，应用协议
    - 10：natural language protocol，自然语言协议
    - 11：verification protocol，验证协议
- Reserved: 6bit，保留字段，暂未使用
- Protocol Data: 变长，表示协议的具体内容

所有的消息都有一个二进制的头，大小为1个字节，头中主要的信息是协议数据的协议类型：
- 如果协议类型值为00，则表示此消息是元协议，用于进行协议的协商；
- 如果协议类型值为01，则表示此消息是应用协议，用于进行实际的数据传输；
- 如果协议类型值为10，则表示此消息是自然语言协议，直接使用自然语言进行数据传输；
- 如果协议类型值为11，则表示此消息是验证协议，用于进行协商协议的验证，验证通过后，则使用此协议进行数据传输，验证协议并非真正的用户数据。

当前二进制头是一个字节，如果后期一个字节无法满足需求，可以扩展为多个字节。通过在Hello消息中携带消息格式版本信息，可以保持前后兼容。

#### 元协议协商消息定义

当协议类型（PT）为00时，消息的Protocol Data携带元协议消息，用于协商两个智能体之间通信使用的协议。元协议的协商过程是预先定义的，不用进行协商。预定义的文档即为本文档。

元协议消息我们定义为半结构化的格式，核心的协议协商部分使用自然语言，保持协商的灵活性，同时在流程控制上，使用结构化的json，保持协议协商过程可控。

元协议协商消息分为几类：
- 协议协商消息：用于协商协议内容
- 代码生成消息：用于生成处理协议的代码
- 调试协议消息：用于协商调试协议
- 自然语言消息：用于协商双方使用自然语言进行协商

下面协议所用的json格式，均符合json规范[RFC8259](https://tools.ietf.org/html/rfc8259)。

##### 协议协商消息定义

协议协商消息的json格式如下：
```json
{
    "action": "protocolNegotiation",
    "sequenceId": 0,
    "candidateProtocols": "",
    "modificationSummary": "",
    "status": "negotiating"
}
```

字段说明：
- action：固定为protocolNegotiation
- sequenceId：协商序号，用于标识协商轮次。
  - 从0开始，每次协商消息的sequenceId都需要在原有的基础上加1。
  - 为了防止协商轮次过大，代码实现人员可以根据业务场景设定协商轮次上限。建议不超过10次。
  - 同时在处理sequenceId的时候，需要判断对方返回的sequenceId是否按照规范递增。
- candidateProtocols：候选协议
  - 是一段自然语言文本，用于描述候选协议的目的、流程、数据格式、错误处理等。
  - 这段文本一般会使用AI处理，建议使用markdown格式，保持清晰、简洁。
  - 候选协议可以描述全部的协议内容，也可以基于已有的协议进行修改，携带已有协议的URI，以及修改的内容。
  - 候选协议每次必须携带全量协议内容。
- modificationSummary：协议修改摘要
  - 是一段自然语言文本，用于描述在协商过程中，当前的候选协议相对上次的候选协议修改了哪些内容。
  - 这段文本一般会使用AI处理，建议使用markdown格式，保持清晰、简洁。
  - 首次发起协商时，可以不携带此字段。
- status：协商状态，用于标识当前协商的状态，状态值如下：
  - negotiating：协商中
  - rejected：协商失败
  - accepted：协商成功
  - timeout：协商超时

协商双方在协商轮次超出最大限制前，可以反复协商，直到任意一方判定对方给出的协议满足自己的需求，则协商成功，否则协商失败，可以反馈给人类工程师，介入协商过程。

###### candidateProtocols示例

- candidateProtocols携带全量协议描述示例如下：

```plaintext
# 需求
获取商品信息

# 流程描述
请求者携带商品id或名字，发送给商品提供者，商品提供者根据商品id或名字，返回商品详细信息。
异常处理：
- 错误码使用HTTP的错误码
- 错误信息使用自然语言描述
- 15秒内没有返回，则认为超时

# 数据格式描述
请求和响应均采用json格式，使用规范https://tools.ietf.org/html/rfc8259。

## 请求消息
请求json schema定义如下：
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ProductInfoRequest",
  "type": "object",
  "properties": {
    "messageId": {
      "type": "string",
      "description": "A random string identifier for the message"
    },
    "type": {
      "type": "string",
      "description": "Indicates whether the message is a REQUEST or RESPONSE"
    },
    "action": {
      "type": "string",
      "description": "The action to be performed"
    },
    "productId": {
      "type": "string",
      "description": "The unique identifier for a product"
    },
    "productName": {
      "type": "string",
      "description": "The name of the product"
    }
  },
  "required": ["messageId", "type", "action", "productId"]
}

## 响应消息
响应json schema定义如下：
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ProductInfoResponse",
  "type": "object",
  "properties": {
    "messageId": {
      "type": "string",
      "description": "The messageId from the request json"
    },
    "type": {
      "type": "string",
      "description": "Indicates whether the message is a REQUEST or RESPONSE"
    },
    "status": {
      "type": "object",
      "properties": {
        "code": {
          "type": "integer",
          "description": "HTTP status code"
        },
        "message": {
          "type": "string",
          "description": "Status message"
        }
      },
      "required": ["code", "message"]
    },
    "productInfo": {
      "type": "object",
      "properties": {
        "productId": {
          "type": "string",
          "description": "The unique identifier for a product"
        },
        "productName": {
          "type": "string",
          "description": "The name of the product"
        },
        "productDescription": {
          "type": "string",
          "description": "A detailed description of the product"
        },
        "price": {
          "type": "number",
          "description": "The price of the product"
        },
        "currency": {
          "type": "string",
          "description": "The currency of the price"
        }
      },
      "required": ["productId", "productName", "productDescription", "price", "currency"]
    }
  },
  "required": ["messageId", "type", "status", "productInfo"]
}

```

- candidateProtocols基于已有协议进行修改示例如下：

```plaintext
# 需求
获取商品信息

# 流程描述
该流程基于已有协议（URI: https://agent-network-protocol.com/protocols/product-info-0-1-1）实现。

# 修改内容
- 在响应消息中增加自定义错误码
  - 100001：商品缺货中
  - 100002：商品下架中
  - 100003：商品价格未知

```

###### modificationSummary示例

modificationSummary也是自然文本，示例如下：

```plaintext

修改点：
- 响应中增加字段：productImageUrl, productVideoUrl, productTags
- 明显响应超时时间：15秒。15秒内没有返回，则认为超时

```

##### 协议代码生成消息定义

协商完成协议后，智能体需要准备处理协议的代码，代码可能是AI生成或从网络加载。在代码就绪之前，如果收到用户的消息，可能会导致协议处理失败。

因此，协商完成后，智能体双方都需要回复对方代码生成消息，通知对方代码已生成，可以进行消息处理。

如果长时间没有收到代码生成消息，则认为代码生成失败，通信终止。建议超时时长15秒。

```json
{
    "action": "codeGeneration",
    "status": "generated"
}
```

字段说明：
- action：固定为codeGeneration
- status：状态
  - generated，表示代码已生成
  - error，表示代码生成失败，通信终止

##### 测试用例协商消息定义

协议协商完成、代码完成后，两个智能体是否能够基于此正常通信，可能需要一个测试过程。测试用例协商消息主要为此设计，用来让两个智能体协商测试用例，并通知对方进行测试。

测试用例协商消息并非流程中的必须支持功能，如果智能体或者人类工程师认为协议无需测试，可以跳过此步骤，直接进行后面的通信过程。

测试用例协商消息的json格式如下：

```json
{
    "action": "testCasesNegotiation",
    "testCases": "",
    "modificationSummary": "",
    "status": "negotiating"
}
```

字段说明：
- action：固定为testCasesNegotiation
- testCases：测试用例集，一段自然语言文本，用于描述测试用例集的内容，包括多个测试用例，每个测试用例包含测试请求数据、测试响应数据、测试预期结果。
- modificationSummary：测试用例修改摘要，一段自然语言文本，用于描述在协商过程中，当前的测试用例集相对上次的测试用例集修改了哪些内容。
- status：协商状态，用于标识当前协商的状态，状态值如下：
  - negotiating：协商中
  - rejected：协商失败
  - accepted：协商成功

testCases示例：

```plaintext
 # 测试用例1

 - **测试请求数据**：
 {
   "messageId": "msg001",
   "type": "REQUEST",
   "action": "getProductInfo",
   "productId": "P12345"
 }

 - **测试响应数据**：
 {
   "messageId": "msg001",
   "type": "RESPONSE",
   "status": {
     "code": 200,
     "message": "成功"
   },
   "productInfo": {
     "productId": "P12345",
     "productName": "高性能笔记本电脑",
     "productDescription": "配备最新处理器和大容量内存的高性能笔记本电脑。",
     "price": 1299.99,
     "currency": "USD"
   }
 }

 - **测试预期结果**：
 成功获取产品信息，状态码为200。

 # 测试用例2

 - **测试请求数据**：
 {
   "messageId": "msg002",
   "type": "REQUEST",
   "action": "getProductInfo",
   "productId": "P99999"
 }

 - **测试响应数据**：
 {
   "messageId": "msg002",
   "type": "RESPONSE",
   "status": {
     "code": 404,
     "message": "产品未找到"
   },
   "productInfo": null
 }

 - **测试预期结果**：
 请求的产品不存在，返回状态码404，产品信息为空。

```

##### 修复错误协商消息定义

在协议的测试或实际的运行过程中，如果发现对方的消息不符合协议定义或有错误，则需要通知对方错误信息，并一起协商修复错误。这个过程也可能会经过多轮，协议对接过程中的错误可能是双方都存在问题，需要一起协商修复。

比如，智能体A发送错误修复消息，指出智能体B发送的消息不符合协议定义或有错误，智能体B收到错误修复消息后，根据错误信息和协议定义，分析自己是否有错误。如果有错误，则接受错误并修改代码，进入代码生成过程。如果没有错误，则回复错误修复消息，拒绝修改并告知智能体A详细的原因。

修复错误协商消息的json格式如下
```json
{
    "action": "fixErrorNegotiation",
    "errorDescription": "",
    "status": "negotiating"
}
```

字段说明：
- action：固定为fixErrorNegotiation
- errorDescription：错误描述，一段自然语言文本，用于描述错误信息。
- status：协商状态，用于标识当前协商的状态，状态值如下：
  - negotiating：协商中
  - rejected：协商失败
  - accepted：协商成功

errorDescription示例：

```plaintext
# 错误描述
- 响应消息中，status字段缺少code字段

```

##### 自然语言协商消息

使用上面定义的协议协商、代码生成、修复错误等消息，已经能够满足大部分智能体之间的协商过程。不幸的是经验告诉我们，现实世界往往是非常复杂且有很多我们考虑不到的地方。之前我们很难解决这个问题，现在基于生成式AI和自然语言，这个问题可以得到很好的解决。

所以我们设计了一个纯自然语言交互的消息，用于解决那些无法使用我们预先定义的消息进行协商的问题。

自然语言协商消息非必须支持消息，智能体可以自由选择是否支持。我们建议优先使用预定义的消息进行协商，这样协商消息更高。

自然语言交互消息采用请求响应模式，json格式如下：

```json
{
    "action": "naturalLanguageNegotiation",
    "type": "REQUEST",
    "messageId": "",
    "message": ""
}
```

字段说明：
- action：固定为naturalLanguageNegotiation
- type：消息类型，用于标识消息的类型，值为REQUEST或RESPONSE
- messageId：消息ID，16位随机字符串，用于标识消息，在对方回复时，需要携带相同的messageId。
- message：自然语言内容，一段自然语言文本，智能体可以在message中携带自己的关于协议协商、通信等特殊的需求。

#### 应用协议消息定义

当协议类型（PT）为01时，消息的Protocol Data携带应用协议消息，用于传递两个智能体之间的交互数据。消息的格式，取决于协议协商流程中协商出的具体协议。它可以是二进制数据，也可以是json、xml等结构化数据。

#### 自然语言协议消息定义

当协议类型（PT）为02时，消息的Protocol Data携带自然语言协议消息，用于传递两个智能体之间的交互数据。

在某些特殊的情况下，智能体之间仅进行少量、低频甚至单次的交互，为了达到最高通信效率，可以跳过协议协商流程，直接使用自然语言进行数据交互。

Protocol Data中的数据为UTF-8编码的自然语言文本，为了方便AI处理，建议使用markdown格式，使用清晰、简洁的描述。

此消息非必须支持消息，智能体可以自由选择是否支持。

自然语言协议消息示例：

请求示例：
```plaintext
# 需求
获取商品信息，根据商品ID，返回商品的详细信息，包括商品ID、商品名称、商品描述、商品价格、商品货币单位。

# 输入
- 商品ID：P12345
```

响应示例：
```plaintext
# 输出
- 商品ID：P12345
- 商品名称：高性能笔记本电脑
- 商品描述：配备最新处理器和大容量内存的高性能笔记本电脑。
- 商品价格：1299.99
- 商品货币单位：USD
```

#### 验证协议消息

当协议类型（PT）为03时，消息的Protocol Data携带验证协议消息，用于传递两个智能体之间的验证数据。消息的格式，取决于协议协商流程中协商出的具体协议。验证协议消息不是实际的业务数据，而是为了验证协议流程是否正常，验证协议消息的内容一般在协议协商流程中通过verificationProtocol消息协商。

此消息非必须支持消息，智能体可以自由选择是否支持。

## 元协议能力协商机制与扩展性设计

上面的协议协商流程展示了两个智能体是如何协商出具体协议的，但是出于现实中的各种原因，智能体可能未必能够支持所有的元协议能力，比如有的智能体不支持自然语言协议，有的智能体不支持验证协议。

为了解决这个问题，我们设计了元协议能力协商机制，用于智能体在连接前协商元协议能力，告知对方自己支持的元协议能力，避免协商失败。

这个问题和元协议的扩展性本质上属于一个问题，所以放在一起讨论。当我们需要对元协议流程进行升级的时候，比如将一个字节的协议类型扩展为两个字节，会产生新的元协议版本，这个时候需要考虑新老版本兼容问题。

我们的方案是，在连接握手消息，即sourceHello和destinationHello消息中，携带元协议的版本、以及在此版本上，支持的元协议能力。如果一个智能体支持V1版本，另外一个智能体支持V1和V2版本，则双方使用V1版本元协议进行协商。

关于元协议能力的协商，我们要求所有的智能体必须要支持基本的元协议能力，而对于可选的元协议能力，比如自然语言协议、验证协议等，智能体可以自由选择是否支持。

对sourceHello和destinationHello消息的修改如下：

```json
{
  "version": "1.0",
  "type": "sourceHello",  // destinationHello同理
  "metaProtocol": {
    "version": "1.0",
    "supportedCapabilities": [
        "naturalLanguageProtocol",
        "verificationProtocol",
        "naturalLanguageNegotiation",
        "testCasesNegotiation",
        "fixErrorNegotiation"
    ]
  },
  //其他字段省略
}
```

字段说明：
- version：元协议版本，当前版本为1.0
- supportedCapabilities：支持的元协议能力，数组类型，数组中每个元素为支持的元协议能力名称，对应功能如下：
  - naturalLanguageProtocol：自然语言协议
  - verificationProtocol：验证协议
  - naturalLanguageNegotiation：自然语言协商
  - testCasesNegotiation：测试用例协商
  - fixErrorNegotiation：错误修复协商

## 元协议协商效率优化

调整：如何0rtt协商、如何准确无歧义协商、如何复用之前的协商成果

基于标准协议进行协商

基于共识协议进行协商

基于上次协商结果进行协商
- 在公开的地方获取智能体支持的协议类型，比如三方索引服务、或者DID文档等

并非所有的流程要进行协商，有些标准流程可以免协商，直接使用。

如果使用标准或共识协议能够完成，则直接使用标准或共识协议，不再进行协商。如果对方回复不支持，则启动协商。

在Hello的时候携带加密并且符合协议的数据，early data。




元协议的协商：比如是否支持自然语言协议等。智能体支持什么协议，可以外展现出来，这样一个智能体在连接这个智能体的时候，就知道了。这是我们可以提供的服务。


初稿：
- hello消息中，可以携带期望的协议类型、协议URL、协议版本，进行协商
- 如果协商通过，则建立连接后，直接发送协议的内容，不在进行协商过程
- 协议的数据定义，使用二进制，签名有单个字节的头，签名两bit表示协议类型：00表示元协议、01表示Debug协议、10表示实际协议，后面是具体的内容
- 扩展性：如果后面单字节无法满足需求，需要扩展，则在hello消息中添加对payload的描述

ws在很多的时候是有点复杂的。我们是把ws封装到我们的内部，在外部让用户有http类似的使用效果，即一个接口搞定一切。
还有，是否可以改造http？可能要对http的库进行改造这个工程量有点大。先基于ws跑通流程，后面可以这样考虑。


ToDo：
- 后来更多的还是以非多路复用连接为主。多路复用和非多路复用两种都可以支持。如果是服务器和服务器对接，多路复用也许效率更高。
- 先建立ws连接，然后协商秘钥，然后进行消息传递，传递消息的时候，就不用携带did、secretKeyId等字段了，他们和连接绑定
- 再进行协议的协商。如果使用标准协议，不用协商，直接发送即可；或者直接发送自然语言，这也算是标准协议的一种。
- 如果要进行协商，则发送协商消息，协商后，这个连接只收发协商的协议信息，不发送其他类型的信息
- 两个did之间协商的结果，可以进行缓存，后续直接使用缓存的结果，不用再进行协商，可以加快连接速度
- 也就是说，加密和协议协商，都是可以缓存的，都可以不用每次都进行。


设计需要考虑RTT的影响，当前协议，比如quic，已经在追求0RTT，如果我们设计的协议有很多的RTT，则需要进行优化。这里可以考虑在source hello中，携带early data(包含上次协议协商结果)，这样就可以减少RTT。

这样来看，未来的智能体网络，和现在有很大的区别。现在的互联网架构，是一个中心化的网络，比如淘宝、微信的后台系统，所有的人、店铺都连接到后台系统，然后后台系统再和外部系统进行连接。未来智能体是一个扁平的网络，人或者店铺的智能体和智能体之间直接相连，流量更加的分散、扁平。

现在最大的问题是，protocol id怎么设计，这个id是否需要全网唯一，还是两个did之间唯一


智能体可以将对外公开支持协议类型，这样在请求的时候直接使用，不用再协商。如果遇到不支持具体场景的协议，再对我协商。这个协议应该是人们定义的，或者是智能体网络通过共识算法选择的协议。
这个可以做成一个云端的服务。


## 未来

未来是否所有的协议都是自然语言，所有消息的处理都使用LLM？

如果是这样的话，元协议是否还有存在的必要？


有了元协议的加持，智能体网络有可能会演进成一个自组织、自协商的高效协作网络，并且会诞生非常多智能体之间达成共识的通信协议，这些协议的数量将会大大超过人类制定协议的数量。

怎么设计激励机制，让智能体能够上报他们协商的共识协议？协商后，记录下来这个协议，并且可以在其他类似的通信中使用。




