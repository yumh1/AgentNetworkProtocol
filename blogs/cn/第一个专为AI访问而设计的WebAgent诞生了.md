# 第一个专为AI访问而设计的 WebAgent 诞生了

越来越多的**智能体**开始尝试直接从互联网获取信息，目前有很多技术可以用，比如Computer Use、Browser Use等。然而传统网站主要面向人类用户设计，AI 想要利用这些网站常常需要模拟人类浏览器行为（例如像爬虫那样解析 HTML 页面），效率低且复杂。

为了解决这一痛点，也许我们需要构建一个**WebAgent**。

本文将介绍什么是 WebAgent，以及第一个 WebAgent 上线的意义和技术细节。介绍如何发现WebAgent并与其交互，WebAgent的身份认证机制，以及接入相关协议的代码示例，最后介绍如何构建一个专为 AI 打造的数据网络。

## 什么是 WebAgent

WebAgent 是一种利用现有 Web 基础设施（如PKI、DNS、HTTP、CDN、搜索引擎等）构建的智能体，它在 Web 上运行，旨在使其他智能体能够通过 Web 方式对其进行访问和交互。与传统以人类用户为核心设计的网站不同，WebAgent 专为 AI 设计，提供AI可读可理解的公开信息，以及包含结构化、自然语言等多种类型的接口，而无需用户界面。

与传统网站相比，WebAgent 有以下显著区别：

- **面向对象不同**：传统网站主要服务于人类用户，用户通过浏览器进行访问和交互；而 WebAgent 专为 AI 设计，旨在使其他智能体能够通过 Web 方式对其进行访问和交互。
- **数据格式结构化**：WebAgent 返回的数据是结构化格式（如 JSON、YAML 等），方便 AI 直接读取和处理，而传统网站通常返回 HTML，需要额外解析才能提取所需信息。
- **自描述能力**：每个 WebAgent 都提供描述文件，详细说明其功能、接口格式、调用方法等，方便其他智能体理解如何与之交互。
- **身份校验机制**：WebAgent 内置了对访问方的身份验证支持，以防止信息、接口被滥用。现有的网站往往面临被网络爬虫随意爬取信息的问题。

对于 AI 而言，WebAgent 的出现具有重要意义。过去 AI 访问网页信息，需要模拟人类浏览网页，复杂且低效。而 WebAgent 是专为 AI 设计的“原生网站”，AI 可以像调用应用程序服务一样，通过标准接口直接获得数据或执行任务。这使 AI 更高效、准确地利用互联网信息，开发者也能针对 AI 优化服务，不再局限于人类的浏览模式。WebAgent 将成为构建智能体互联网（Agentic Web）的基础组件，让 AI 能够直接通信与协作。

## 第一个 WebAgent 诞生

我们开发了第一个基于ANP的WebAgent，它是一个提供天气信息服务的智能体网站。

作为示范，这个 WebAgent 在遵循 AI 原生设计的同时，也特地增加了一个简单的首页，以便人类开发者能直观了解它的存在（尽管对于 AI 而言并不需要首页界面）。

下图展示了该 WebAgent 首页的示意图，你也可以通过访问连接 https://agent-weather.xyz/ 来查看：

![WebAgent 示例](/blogs/images/first-web-agent.png)

*（图：第一个 WebAgent —— 天气智能体的演示界面。实际交互中，AI 将通过其提供的 API 接口获取天气数据。）*

这个天气 WebAgent 命名为 **“天气智能体”**，里面设计了一个虚拟人物"小晴"，托管在专用域名上。天气智能体的设计完全符合ANP的规范。通过这个实例，我们会展示一个基于ANP的WebAgent是如何运行的，希望能够为WebAgent的开发者和使用者提供一个参考。

需要说明的是，在理想情况下 WebAgent 并不需要有人类可访问的网页界面；AI 完全可以通过协议与其通信。但为了便于调试和让人类开发者理解 WebAgent 的工作原理，首个 WebAgent 还是提供了一个可访问的主页，展示其基本信息和功能简介。

## 如何找到一个 WebAgent

既然 WebAgent 不以人为访问者为中心，我们该如何**发现和定位**这些面向 AI 的智能体服务呢？

为此，ANP引入了一套 **智能体发现机制**，使得给定一个域名，AI 就能找到域名下有哪些 WebAgent 以及它们的描述文件。本质上ANP的智能体发现机制也是基于DNS的，和网站的发现机制类似。

**1. 通过域名和 `.well-known` 路径主动发现（Active Discovery）：** 类似于某些互联网服务使用 `.well-known` 路径提供元数据（例如 `.well-known/robots.txt`、`.well-known/openid-configuration` 等），WebAgent 也遵循这一思路。在约定上，每个托管 WebAgent 的域名下，可以提供一个**智能体列表**：

```
https://<域名>/.well-known/agent-descriptions
```

访问该路径将返回一个 JSON-LD 格式的**发现文档**，罗列该域名下公开的所有 WebAgent 描述文件的地址。详细定义在 [ANP 智能体发现协议规范](https://github.com/agent-network-protocol/AgentNetworkProtocol/blob/main/08-ANP-Agent-Discovery-Protocol-Specification.md)（Agent Discovery Protocol）。

例如，对于我们的天气智能体域名 `agent-weather.xyz`，访问 **`https://agent-weather.xyz/.well-known/agent-descriptions`**，会返回类似下面的内容：

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "ad": "https://agent-network-protocol.com/ad#"
  },
  "@type": "CollectionPage",
  "url": "https://agent-weather.xyz/.well-known/agent-descriptions",
  "items": [
    {
      "@type": "ad:AgentDescription",
      "name": "天气智能体",
      "@id": "https://agent-weather.xyz/ad.json"
    }
  ]
}
```

上例表明在 `agent-weather.xyz` 这个域名下，有一个名为“天气智能体”的 Agent，其描述文件位于 `https://agent-weather.xyz/ad.json`（通常我们也简称这个描述文件为 **AD（Agent Description）**）。如果有多个智能体，它们都将列在 `items` 中。通过这种方式，AI 知道了下一步该去获取哪个 URL 来了解智能体详情。

值得一提的是，采用 `.well-known/agent-descriptions` 作为入口，意味着**只要知道域名**，AI 就能发现其中的 WebAgent 列表，而不需要人为提供具体路径。这也方便搜索引擎对其进行索引。

**2. 被动发现（Passive Discovery）：** 除了主动查询域名的 .well-known 路径外，WebAgent 也可以将自己的信息提交给专门的智能体搜索服务或注册表，从而**被动地**被发现。例如，一个 WebAgent 可以将自己的描述文件 URL 提交到公共的 Agent 搜索引擎，使得别的 Agent 可以通过关键词（比如“天气”）搜索到它。这属于被动发现的一种，它让 WebAgent 主动**登记**自身，从而方便网络中智能体互相查找。

利用ANP设计的两种发现机制，一个智能体可以很方便的通过域名或者搜索引擎，找到它想要访问的WebAgent。

## 如何与 WebAgent 交互

找到了 WebAgent 后，接下来就是**如何与之交互**。这时候就要用到 WebAgent 提供的**描述文件**（即上面找到的 `ad.json`）。

智能体描述文件详述了该 WebAgent 的能力和接口定义，相当于一份**说明书**。AI 在读取这个说明书后，就能按照里面提供的数据与接口，获得智能体能够提供的能力，并且与智能体进行通信。

我们以天气智能体的描述文件 [`https://agent-weather.xyz/ad.json`](https://agent-weather.xyz/ad.json) 为例：

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "did": "https://w3id.org/did#",
    "ad": "https://agent-network-protocol.com/ad#"
  },
  "@type": "ad:AgentDescription",
  "@id": "https://agent-connect.ai/agents/travel/weather/ad.json",
  "name": "天气智能体",
  "description": "天气智能体，提供全国城市天气信息查询服务。",
  "version": "1.0.0",
  "owner": {
    "@type": "Organization",
    "name": "agent-connect.ai",
    "@id": "https://agent-connect.ai"
  },
  "ad:securityDefinitions": {
    "didwba_sc": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "ad:security": "didwba_sc",
  "ad:interfaces": [
    {
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/weather-info.yaml",
      "description": "提供天气查询服务的OpenAPI的YAML文件。"
    },
    {
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/booking-interface.yaml",
      "description": "提供天气信息预订服务的OpenAPI的YAML文件。"
    },
    {
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/subscription-status-interface.yaml",
      "description": "提供天气订阅状态查询服务的OpenAPI的YAML文件。"
    },
    {
      "@type": "ad:NaturalLanguageInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/nl-interface.yaml",
      "description": "提供通过自然语言与智能代理交互的接口。"
    }
  ],
  "status_code": 200,
  "url": "https://agent-connect.ai/agents/travel/weather/ad.json"
}
```

上述示例中，智能体描述文件采用的是 JSON-LD 格式。该格式使用了 Schema.org 提供的通用词汇，使不同智能体对数据含义的理解更加一致和清晰。此外，WebAgent 也通过自定义扩展（如ad字段）来补充特定的智能体交互规范。

通过解析这些字段，AI 基本就了解了如何使用这个 WebAgent。例如，根据天气智能体的 `ad:interfaces` 列表，我们看到几个 OpenAPI YAML 文件链接，其中一个 `weather-info.yaml` 提供了“天气查询服务”的API定义。

AI 获取这个 YAML 文件后，就能知道天气智能体支持哪些HTTP接口，比如可能定义了 `GET /weather?city={城市名称}` 这样的端点，以及返回的天气信息数据格式。如果 AI 想查询天气，只需按照该 OpenAPI规范构造HTTP请求即可。

**交互示例：** 假设描述文件告诉我们天气智能体有一个获取天气的接口，那么AI可以进行如下步骤：
1. 读取描述文件，确定需要使用 DID 身份验证（如果 `security` 要求的话）以及找到提供天气查询的接口定义。
2. 根据接口定义，形成具体请求。例如，“查询杭州当前天气”对应于一个 GET 请求：`GET https://agent-weather.xyz/api/weather?city=杭州`（此URL只是示例，实际端点需根据接口定义文件确定）。
3. 在请求头中加入身份认证信息（具体见下节），然后向 WebAgent 发送请求。
4. WebAgent 返回结构化的天气数据（例如 JSON 格式的温度、湿度、天气状况等信息），AI 直接解析该数据并可用于后续推理或呈现给用户。

通过描述文件，AI 可以逐层深入了解 WebAgent 提供的能力：先是发现有哪些接口，然后再根据接口描述获取API文档，最后调用具体API完成任务。这种设计使得**AI 可以自主爬取 WebAgent 提供的所有机器可读资源**，一步步完成复杂任务，而无需人工干预。

## 访问 WebAgent 的身份认证机制

考虑到 WebAgent 面向的是自动化的 AI 访问者，开放的接口可能会面临恶意滥用或过度调用的问题，比如最近大家诟病比较多的大模型训练公司对网站数据疯狂爬取行为。

因此，**WebAgent 通常要求调用方提供身份验证**，以确保请求是来自受信任的主体，并可对其进行权限管理或配额限制。这与人类访问网站时需要密码、 API Key 或 OAuth 授权有异曲同工之处。

不过，WebAgent 采用了一种更适合智能体生态的解决方案：基于 **W3C DID（Decentralized Identifier，去中心化身份标识）** 标准的认证机制。可以让智能体使用自己的 DID 作为身份标识访问WebAgent，而不需要每个智能体都在对方系统上额外注册账户。

AgentNetworkProtocol (ANP) 提出了专门的 DID 方法 —— **`did:wba`** (WebAgent DID)。根据 [ANP 身份认证规范](https://github.com/agent-network-protocol/AgentNetworkProtocol/blob/main/03-did%3Awba-method-design-specification.md)（DID:WBA 方法规范），`did:wba` 利用现有的 Web 基础设施实现了去中心化的身份认证，专为智能体之间的认证设计。简单来说，每个智能体（或使用 WebAgent 的实体）都可以拥有一个 `did:wba:` 开头的身份标识符，例如：  

```
did:wba:example.com:agent:weather123
``` 

这个标识类似于一个邮箱地址或用户ID，包含域名信息。在 WebAgent 的认证体系中，有点像“对方只需知道你的 DID，就能通过现有网络基础设施确认你的身份”，而不需要每个智能体在对方系统上额外注册账户。这大大简化了跨平台的 AI-Agent 协作。

`did:wba` 的身份认证流程可以概括为：
- **DID 文档发布：** 每个 DID 对应一个可解析的 DID Document（DID 文档），里面包含公钥等验证材料。`did:wba` 方法规定DID文档托管在对应域名的特定路径上，便于通过 HTTP 获取。例如 DID `did:wba:agent-did.com:user:alice` 可以解析出其 DID 文档（其中会有 Alice 的公钥）。
- **请求附带签名：** 当一个 AI 智能体访问 WebAgent 时，如果该 WebAgent 要求 DID 身份认证，它会在请求过程中要求对方提供证明身份的签名。具体来说，请求方使用自己的私钥对某个挑战字符串或请求内容签名，并将签名附加在 HTTP 请求头（如 `Authorization`）中发送。
- **验证过程：** WebAgent 服务端收到请求后，会根据请求方提供的 DID，从对应的 DID 文档中提取公钥，验证签名是否有效，从而确认请求者的身份。如果验证通过，则认为此请求是来自该 DID 所代表的实体，接着根据策略决定给予访问或服务。验证失败则返回 401 未授权错误等。

由于 DID 是去中心化的，**任意两个智能体可以在不依赖中心化用户数据库的情况下互信**。这有点像电子邮件的体系 —— 你给对方发邮件不需要在对方邮件服务器上注册账户，只要对方能通过 DNS 找到你的域名并信任相应的公钥即可。`did:wba` 的出现，让 WebAgent 网络中的身份验证变得灵活且无平台障碍。对比传统的 OAuth或者 API Key 方案，DID 更适合**大规模、多主体**的智能体生态，因为每个 Agent 可以自有身份，一处认证，处处可用【当然，为了兼容现有系统，WebAgent 也不妨支持传统 API Key 等方式，但 DID 显然是面向未来的方案】。

**防滥用与权限控制：** 通过要求调用方提供 DID 身份，WebAgent 可以做到：
- 对每个 DID 分配调用配额、权限级别。比如一些敏感操作只有获得特定信任级别的 DID 才能调用。
- 出现问题时可以追溯到具体的 DID 身份，而不是面对匿名的爬虫流量无计可施。
- 建立智能体之间的信誉系统，不良行为的 DID 可以被加入黑名单，而良好记录的 DID 可能享受更高的权限。

值得注意的是，为了降低开发者的门槛，ANP 社区还提供了一个**测试用的公共 DID**。这个 DID 为 `did:wba:agent-did.com:test:public`，对应的 DID 文档和私钥已经公开，用于测试和体验 WebAgent 的身份认证过程。任何人都可以使用这对公私钥来尝试调用要求身份认证的 WebAgent（只用于测试，无法进行真实交易等敏感操作）。

在实际开发中，我们可以通过引入这套公共测试 DID，快速地验证 WebAgent 接口调用流程。在 [ANP 示例代码库](https://github.com/agent-network-protocol/anp-examples/tree/main/use_did_test_public) 的 `use_did_test_public` 目录下，就提供了这个测试 DID 的 DID 文档 (`did.json`) 和私钥文件 (`key-1_private.pem`) 以及示范如何使用它。下节的代码实例也将展示如何利用该测试身份来调用 WebAgent 接口。

# 访问ANP WebAgent 的工具

我们开发了一个用于和ANP WebAgent 交互的工具ANP Explorer，地址：https://service.agent-network-protocol.com/anp-explorer/。

![ANP Explorer](/blogs/images/anp-explorer.png)

它有两个功能：
- 可以作为一个AI个人助手，通过自然语言与个人助手交互，个人助手通过WebAgent的描述文档，调用WebAgent的接口，并返回结果。
- 提供对智能体描述文档的探索工具，可以输入智能体描述文档的URL，然后拉取文档以及文档中链接的其他文档。

这个工具使用ANP公开测试DID（`did:wba:agent-did.com:test:public`）访问WebAgent.

## 代码示例：如何接入 ANP 协议

理解了 WebAgent 的发现、描述和认证机制后，我们来看一个**实际代码示例**，演示如何通过简单的代码让你的 AI Agent 具备访问 WebAgent 的能力。代码已经开源：[anp-examples](https://github.com/agent-network-protocol/anp-examples)。这个代码就是上面的ANP Explorer的代码。

好消息是，这个过程非常简洁——正如社区所说：“*只需要一个提示词（Prompt）和一个 HTTP 函数*”就可以与任意 WebAgent 通信。

先让我们看提示词，代码地址 https://github.com/agent-network-protocol/anp-examples/blob/main/anp_examples/simple_example.py：

```plaintext
1. 您将收到一个起始URL（{{initial_url}}），这是一个智能体的描述文件。
2. 您需要了解该智能体描述文件的结构、功能和API使用方法。
3. 您需要像网络爬虫一样不断发现和访问新的URL和API端点。
4. 您可以使用anp_tool获取任何URL的内容。
5. 该工具可以处理多种格式的响应，包括：
   - JSON格式：将直接解析为JSON对象。
   - YAML格式：将返回文本内容，您需要分析其结构。
   - 其他文本格式：将返回原始文本内容。
6. 阅读每个文档以查找与任务相关的信息或API端点。
7. 您需要自行决定爬取路径，不要等待用户指示。
8. 注意：您最多可以爬取10个URL，超过此限制后必须结束爬取。
......
```

这段描述指导 AI 模型像一个爬虫一样，不断的调用anp_tool工具，爬取智能体的文档或接口，循环这一过程，直到满足获得所需要的信息。

接下来是 HTTP 函数部分。`anp_tool.py` 定义了一个异步方法 `execute(...)`，其作用是执行实际的 HTTP 请求，并处理身份认证逻辑。

具体的代码可以参考：https://github.com/agent-network-protocol/anp-examples/blob/main/anp_examples/anp_tool.py

可以看到，借助 `ANPTool`，一个 AI Agent 与 WebAgent 通信的流程就像普通的HTTP调用一样简单。而对基于大模型的智能体来说，只需在其工具列表中添加这样一个具备ANP功能的工具，并通过提示让模型明白如何使用，它就能自主完成跨智能体的操作。

例如，一个具备 ANP 能力的对话Agent在收到用户问“帮我订明天上海的酒店”时，完全可以：先用 ANPTool 找到酒店预订Agent -> 获取其描述和接口 -> 按流程完成预订，并返回结果给用户。这一切都归功于 WebAgent 提供的标准化、自描述的接口，以及 ANP 协议的简洁设计。

## 构建一个专为 AI 访问的数据网络

随着第一个 WebAgent 的上线，我们看到了未来互联网的一种新形态：一个**无需界面、仅对 AI 开放**的数据服务网络。这个网络的构建基于本文介绍的三大关键要素：

- **智能体发现**：通过标准的发现协议和 `.well-known` 入口，AI 可以自动索引互联网上的智能体服务，无需人工目录。
- **智能体描述**：每个 WebAgent 自包含其功能描述和接口规范，使AI能够自主理解如何调用服务，形成高度自描述的网络。
- **身份认证**：通过去中心化身份（DID）机制，确保了网络交互的安全和可信，支持跨平台的权限管理，保障网络健康运行。

这个“AI 数据网络”具有一些显著的特性：

- **专为 AI 设计，UI-less**：网络中的服务不再面向人类直接提供页面或图形界面，所有交互都发生在智能体之间。省去了传统的人机界面，减少系统复杂性，使网络服务完全聚焦于数据本身，专注为 AI 提供高效的数据交换环境。
- **半结构化数据**：WebAgent 提供的数据以结构化的格式为主（如 JSON、YAML），便于 AI 智能体进行快速解析和处理；同时局部采用自然语言表述，以承载个性化的描述信息，帮助智能体更好地理解服务内容或表达个性化特征。
- **自描述能力**：WebAgent 自带标准化的描述文件，详细说明自身提供的服务、接口定义和调用方法。AI 智能体在发现服务时，能够自主理解服务的具体功能和交互方式，无需人工介入或额外的接口文档。
- **安全可靠**：考虑到 WebAgent 面向的是自动化的 AI 访问者，开放的接口可能会面临恶意滥用或过度调用的风险（如近期被广泛诟病的，大模型公司对网页数据的疯狂爬取行为）。因此，WebAgent 内置了基于去中心化身份（DID）的身份验证和权限管理机制，有效避免数据滥用并保障接口安全。通过身份追踪与访问授权，建立起可信赖的智能体网络环境。

可以想象，在不远的将来，各行各业的数据和服务都可能以 WebAgent 的形式对 AI 开放：天气、新闻、知识库、交易平台、商家……AI 将成为主要的“用户”，直接通过网络接口完成我们如今通过APP或网页才能完成的任务。而人类用户将与AI协作，更多地让AI去调用这些 WebAgent 完成复杂的目标。

