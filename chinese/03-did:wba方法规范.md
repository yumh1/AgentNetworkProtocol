# did:wba方法规范

## 摘要

wba DID方法是一种基于Web的去中心化标识符（DID）规范，旨在满足跨平台身份认证和智能体通信的需求。此方法在did:web基础上进行扩展和优化，命名为did:wba，保留其兼容性并增强针对智能体场景的适配性。在本规范中，我们设计了一个基于did:wba方法和HTTP协议的流程，在不增加交互次数的情况下，让服务端可以快速验证其他平台客户端的身份。

## 1. 引言

### 1.1 前言

wba DID方法规范符合去中心化标识符V1.0[[DID-CORE](https://www.w3.org/TR/did-core/)]中指定的要求。

本规范在did:web方法规范的基础上，添加了DID文档限定、跨平台身份认证流程、智能体描述服务等规范描述，提出了新的方法名did:wba(Web-Based Agent)。

考虑到did:web方法规范仍然是一个草案，未来可能会有不适宜智能体通信场景的改动。另外，我们对规范做了部分修改，和原作者就规范修改达成共识也是一个长期过程，所以我们决定使用一个新的方法名。

未来不排除将did:wba规范合并到did:web规范中的可能，我们会去推动这个目标的实现。

did:wba方法参考的did:web方法规范地址为[https://w3c-ccg.github.io/did-method-web](https://w3c-ccg.github.io/did-method-web)，版本日期为2024年7月31日。为了方便管理，我们备份了一份did:wba当前使用的did:web方法规范文档：[did:web方法规范](/references/did_web%20Method%20Specification.html)。

### 1.2 设计原则

设计did:wba方法时，我们的核心原则是即可以充分利用现有的成熟技术和完善的 Web 基础设施，又可以实现去中心化。使用did:wba，可以实现类似email特点，各个平台以中心化的方式实现自己的账户体系，同时，各个平台之间可以互联互通。

此外，各种类型的标识符系统都可以添加对 DID 的支持，从而在集中式、联合式和去中心化标识符系统之间架起互操作的桥梁。这意味着现有的中心化标识符系统无需彻底重构，只需在其基础上创建 DID，即可实现跨系统互操作，从而大大降低了技术实施的难度。

## 2. WBA DID 方法规范

### 2.1 方法名称
用于标识此DID方法的名称字符串是:wba。使用此方法的DID必须以以下前缀开头:did:wba。根据DID规范,此字符串必须是小写的。DID的其余部分(前缀之后)在下面指定。

### 2.2 方法特定标识符
方法特定标识符是由TLS/SSL证书保护的完全限定域名,可以选择包含DID文档的路径。描述有效域名语法的正式规则在[（RFC1035）](https://www.rfc-editor.org/rfc/rfc1035)、[（RFC1123）](https://www.rfc-editor.org/rfc/rfc1123)和[（RFC2181）](https://www.rfc-editor.org/rfc/rfc2181)中有说明。

方法特定标识符必须与SSL/TLS证书中使用的通用名称匹配,并且不得包含IP地址。可以包含端口号,但冒号必须进行百分比编码以防止与路径冲突。目录和子目录可以选择性地包含,使用冒号而不是斜杠作为分隔符。

wba-did = "did:wba:" domain-name
wba-did = "did:wba:" domain-name * (":" path)

```plaintext
示例3: wba方法DID示例
did:wba:example.com

did:wba:example.com:user:alice

did:wba:example.com%3A3000
```

### 2.4 密钥材料和文档处理

由于大多数Web服务器呈现内容的方式，特定的did:wba文档很可能会以application/json的媒体类型提供服务。如果检索到一个名为did.json的文档，应该遵循以下处理规则：

1. 如果JSON文档根部存在@context，则应根据JSON-LD规则处理该文档。如果无法处理，或者文档处理失败，则应拒绝将其作为did:wba文档。

2. 如果JSON文档根部存在@context，且通过JSON-LD处理，并且包含上下文`https://www.w3.org/ns/did/v1`，则可以按照[[did-core规范的6.3.2节](https://www.w3.org/TR/did-core/#consumption-0)]进一步将其处理为DID文档。

3. 如果不存在@context，则应按照[[did-core规范6.2.2节](https://www.w3.org/TR/did-core/#consumption)]中指定的正常JSON规则进行DID处理。

4. 当did:wba文档中出现DID URL时，必须是绝对URL。

> 注意：这包括嵌入的密钥材料和其他元数据中的URL，这可以防止密钥混淆攻击。

### 2.5 DID文档说明

除DID核心规范外，其他大部分规范尚处于草案阶段。本章节将展示一个用于身份验证的DID文档的子集。为了提高系统间的兼容性，所有标注为必须的字段，所有系统必须支持；标注为可选的字段，可以选择性支持。未列出的其他标准中定义的字段，可以选择性支持。

**DID文档示例如下：**

```json
{
    "@context": [
      "https://www.w3.org/ns/did/v1",
      "https://w3id.org/security/suites/jws-2020/v1",
      "https://w3id.org/security/suites/secp256k1-2019/v1",
      "https://w3id.org/security/suites/ed25519-2020/v1",
      "https://w3id.org/security/suites/x25519-2019/v1"
    ],
    "id": "did:wba:example.com%3A8800:user:alice",
    "verificationMethod": [
      {
        "id": "did:wba:example.com%3A8800:user:alice#WjKgJV7VRw3hmgU6--4v15c0Aewbcvat1BsRFTIqa5Q",
        "type": "EcdsaSecp256k1VerificationKey2019",
        "controller": "did:wba:example.com%3A8800:user:alice",
        "publicKeyJwk": {
          "crv": "secp256k1",
          "x": "NtngWpJUr-rlNNbs0u-Aa8e16OwSJu6UiFf0Rdo1oJ4",
          "y": "qN1jKupJlFsPFc1UkWinqljv4YE0mq_Ickwnjgasvmo",
          "kty": "EC",
          "kid": "WjKgJV7VRw3hmgU6--4v15c0Aewbcvat1BsRFTIqa5Q"
        }
      }
    ],
    "authentication": [
      "did:wba:example.com%3A8800:user:alice#WjKgJV7VRw3hmgU6--4v15c0Aewbcvat1BsRFTIqa5Q",
      {
        "id": "did:wba:example.com%3A8800:user:alice#key-1",
        "type": "Ed25519VerificationKey2020",
        "controller": "did:wba:example.com%3A8800:user:alice",
        "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
      }
    ],
    "keyAgreement": [
      {
        "id": "did:wba:example.com%3A8800:user:alice#key-2",
        "type": "X25519KeyAgreementKey2019", 
        "controller": "did:wba:example.com%3A8800:user:alice",
        "publicKeyMultibase": "z9hFgmPVfmBZwRvFEyniQDBkz9LmV7gDEqytWyGZLmDXE"
      }
    ]
}
```

**字段解释**：

- **@context**: 必须字段，JSON-LD 上下文定义了DID文档中使用的语义和数据模型，确保文档的可理解性和互操作性。`https://www.w3.org/ns/did/v1` 是必须的。其他根据需要添加。

- **id**: 必须字段，不可以携带IP，但是可以携带端口，携带端口时，冒号需要编码为%3A。后面使用冒号进行路径分割。

- **verificationMethod**: 必须字段，包含验证方法的数组，定义了用于验证DID主体的公钥信息。
  - **子字段**:
    - **id**: 验证方法的唯一标识符。
    - **type**: 验证方法的类型。
    - **controller**: 控制该验证方法的DID。
    - **publicKeyJwk**: 公钥信息，使用JSON Web Key格式。

- **authentication**: 必须字段，列出用于身份验证的验证方法，可以是字符串或对象。
  - **子字段**:
    - **id**: 验证方法的唯一标识符。
    - **type**: 验证方法的类型。
    - **controller**: 控制该验证方法的DID。
    - **publicKeyMultibase**: Multibase格式的公钥信息

- **keyAgreement**: 可选字段，定义了用于密钥协商的公钥信息，可以用于两个DID之间的加密通信。验证方法一般使用X25519KeyAgreementKey2019等可以用于密钥交换的密钥协商算法。
  - **子字段**:
    - **id**: 密钥协商方法的唯一标识符。
    - **type**: 密钥协商方法的类型。
    - **controller**: 控制该密钥协商方法的DID。
    - **publicKeyMultibase**: Multibase格式的公钥信息。


### 2.5 DID方法操作

#### 2.5.1 创建(注册)

did:wba方法规范没有指定具体的HTTP API操作，而是将程序化注册和管理留给各个实现方根据其Web环境的要求自行定义。

创建DID需要执行以下步骤：

1. 向域名注册商申请使用域名
2. 在DNS查询服务中存储托管服务的位置和IP地址
3. 创建DID文档JSON-LD文件，包含合适的密钥对，并将did.json文件存储在well-known URL下以代表整个域名，或者如果在该域名下需要解析多个DID，则存储在指定路径下。

例如，对于域名example.com，did.json将在以下URL下可用：

```plaintext
示例：创建DID
did:wba:example.com
 -> https://example.com/.well-known/did.json
```

如果指定了可选路径而不是裸域名，did.json 将在指定的路径下可用：

```plaintext
示例5：使用可选路径创建DID
did:wba:example.com:user:alice
 -> https://example.com/user/alice/did.json
```

如果在域名上指定了可选端口，则必须对主机和端口之间的冒号进行百分比编码，以防止与路径发生冲突。

```plaintext
示例6：使用可选路径和端口创建DID
did:wba:example.com%3A3000:user:alice
 -> https://example.com:3000/user/alice/did.json
```


#### 2.5.2 读取(解析)

必须执行以下步骤来从Web DID解析DID文档:

- 将方法特定标识符中的“:”替换为“/”以获得完全限定的域名和可选路径。
- 如果域名包含端口，则对冒号进行百分比解码。
- 通过在预期的DID文档位置前加上`https://` 生成HTTPS URL。
- 如果URL中未指定路径，则附加`/.well-known`。
- 附加`/did.json`以完成URL。
- 使用能够成功协商安全HTTPS连接的代理执行对URL的HTTP GET请求，该代理强制执行[2.6节安全和隐私注意事项](https://w3c-ccg.github.io/did-method-web/#security-and-privacy-considerations)描述的安全要求。
- 验证解析的DID文档的ID是否与正在解析的Web DID匹配。
- 在HTTP GET请求期间执行DNS解析时，客户端应使用[[RFC8484](https://w3c-ccg.github.io/did-method-web/#bib-rfc8484)]以防止跟踪正在解析的身份。

#### 2.5.3 更新

要更新 DID 文档，需要更新DID对应 did.json 文件。请注意，DID 本身将保持不变，但 DID 文档的内容可以更改，例如，添加新的验证密钥或服务端点。

> 注意：
> 使用诸如 git 之类的版本控制系统和诸如 GitHub Actions 之类的持续集成系统来管理 DID 文档的更新，可以为身份验证和审计历史提供支持。

> 注意：HTTP API
> 更新过程没有指定具体的 HTTP API，而是将程序化注册和管理留给各个实现方根据其需求自行定义。

#### 2.5.4 停用（撤销）
要删除DID文档，必须移除did.json文件，或者由于其他原因使其不再公开可用。

### 2.6 安全和隐私注意事项

安全与隐私注意事项参考[[did:web 方法规范2.6节](https://w3c-ccg.github.io/did-method-web/#security-and-privacy-considerations)]。

## 3. 基于did:wba方法和HTTP协议的跨平台身份认证

当客户端向不同平台的服务端发起请求时，客户端可以使用域名结合TLS对服务端进行身份认证，而服务端则根据客户端DID文档中的验证方法验证客户端的身份。

客户端可以在首次HTTP请求时，在HTTP头中携带DID和签名。在不增加交互次数的情况下，服务端可以快速验证客户端的身份。首次验证通过后，服务端可以返回token，客户端后续请求中携带token，服务端不用每次验证客户端的身份，而只要验证token即可。

<p align="center">
  <img src="/images/cross-platform-authentication.png" width="50%" alt="跨平台身份认证流程"/>
</p>

### 3.1 初始请求

当前客户端首次向服务端发起HTTP请求时，需要按照以下方法进行身份认证。

#### 3.1.1 请求头部格式

客户端将以下信息通过 `Authorization` 头字段发送到服务端：
- **DID**：请求中包含客户端的 DID 标识符，用于身份验证。
- **Nonce**：一个随机生成的字符串，用于防止重放攻击。每次请求必须唯一。推荐使用16字节随机字符串。
- **时间戳（Timestamp）**：请求发起时的时间，通常使用 ISO 8601 格式的 UTC 时间，精确到秒。
- **验证方法（VerificationMethod）**：标识请求中签名使用的验证方法，为DID文档中验证方法的DID fragment。以验证方法id "did:wba:example.com%3A8800:user:alice#key-1"的验证方法为例，验证方法的DID fragment为"key-1"。
- **签名（Signature）**：对 `nonce`、`timestamp` 、服务端域名、客户端DID进行签名。签名应使用客户端的私钥，并包括以下字段：
  - `nonce`
  - `timestamp`
  - `service`（服务的域名）
  - `did`（客户端的 DID）

客户端请求示例：

```plaintext
Authorization: DID did:wba:example.com%3A8800:user:alice Nonce <abc123> Timestamp <2024-12-05T12:34:56Z> VerificationMethod <key-1> Signature <base64(signature_of_nonce_timestamp_service_did)>
```

#### 3.1.2 签名生成流程

1. 客户端生成包含以下信息的字符串：

```json
{ 
  "nonce": "abc123", 
  "timestamp": "2024-12-05T12:34:56Z", 
  "service": "example.com", 
  "did": "did:wba:example.com:user:alice" 
}
```

2. 使用[JCS(JSON Canonicalization Scheme)](https://www.rfc-editor.org/rfc/rfc8785)对上面的json字符串进行规范化，生成规范化字符串。

3. 使用SHA-256算法对规范化字符串进行哈希，生成hash值。

4. 使用客户端的私钥对hash值进行签名，生成签名值 `signature`，并进行Base64编码。

5. 将 `Authorization` 头部构建成上述格式，发送到服务端。

### 3.2 服务端验证

#### 3.2.1 验证请求头部

服务端收到客户端请求后，进行以下验证：

1. **验证时间戳**：检查请求中的时间戳是否在合理的时间范围内，建议时间范围为1分钟。如果请求的时间戳超出范围，认为请求过期，返回 `401 Unauthorized`，并附加挑战信息。

2. **验证Nonce**：检查请求中的 `nonce` 是否已被使用或存在重复。若 `nonce` 已存在，则认为是重放攻击，返回 `401 Unauthorized`，并附加挑战信息。

3. **验证DID权限**：验证请求中的DID是否具备访问服务端资源的权限。如果没有权限，则返回 `403 Forbidden`。

4. **验证签名**：

- 根据客户端的DID，读取DID文档。
- 根据请求中的 `VerificationMethod`，在DID文档中找到对应的验证方法。
- 使用验证方法中的公钥对请求中的签名进行验证。

5. **验证结果**：如果签名验证成功，则请求通过验证；否则，返回 `401 Unauthorized`，并附加挑战信息。


#### 3.2.2 验证签名过程

1. **提取信息**：从 `Authorization` 头部提取 `nonce`、`timestamp`、`service`、`did`、`VerificationMethod` 和 `Signature`。

2. **构建验证字符串**：使用提取的信息构建与客户端相同的JSON字符串：

```json
{ 
    "nonce": "abc123", 
    "timestamp": "2024-12-05T12:34:56Z", 
    "service": "example.com", 
    "did": "did:wba:example.com:user:alice" 
}
```

3. **规范化字符串**：使用[JCS(JSON Canonicalization Scheme)](https://www.rfc-editor.org/rfc/rfc8785)对JSON字符串进行规范化，生成规范化字符串。

4. **生成哈希值**：使用SHA-256算法对规范化字符串进行哈希，生成hash值。

5. **获取公钥**：根据 `did` 和 `VerificationMethod`，从DID文档中获取对应的公钥。

6. **验证签名**：使用获取的公钥对 `Signature` 进行验证，确保签名是由对应的私钥生成的。

#### 3.2.3 401响应

当服务端验证签名失败，需要客户端重新发起请求时，可以返回401响应，并附加挑战信息。挑战信息中必须包含 `nonce` 字段。

同时，如果服务端不支持记录客户端请求的Nonce，或者要求客户端每次必须使用服务端生成的Nonce进行签名，则可以在客户端每次首次请求时，均返回401响应，并附加挑战信息。但是这样会增加客户端的请求次数，实现者可以自行选择是否使用。

挑战信息通过 `WWW-Authenticate` 头字段返回，示例如下：

```plaintext
WWW-Authenticate: Bearer error="invalid_nonce", error_description="Nonce has already been used. Please provide a new nonce.", nonce="xyz987"
```

挑战信息包含以下字段：

- **nonce**：必须字段，服务端生成的随机字符串，用于防止重放攻击。
- **error**：必须字段，错误类型。
- **error_description**：可选字段，错误描述。

客户端收到401响应后，需要使用服务端的Nonce重新生成签名，并且重新发起请求，携带新的Nonce。服务端收到新的请求后，需要验证新的Nonce与签名。

需要注意的是，客户端和服务端在各自的实现上，需要对重试次数进行限制，防止进入死循环。

#### 3.2.4 认证成功返回token

服务端验证成功后，可以在响应中返回token，token建议采用JWT（JSON Web Token）格式。客户端后续请求中携带token，服务端不用每次验证客户端的身份，而只要验证token即可。

JWT生成方法参考[RFC7519](https://www.rfc-editor.org/rfc/rfc7519)。

1. **生成 Token**

假设服务端采用 **JWT (JSON Web Token)** 作为 Token 格式，JWT 通常包含以下字段：

- **header**：指定签名算法
- **payload**：存放用户的相关信息
- **signature**：对 `header` 和 `payload` 进行签名，确保其完整性

payload中可以包含以下字段（其他字段根据需要添加）：
```json
{
  "sub": "did:wba:example.com:user:alice",  // 用户 DID 
  "iat": "2024-12-05T12:34:56Z",            // 签发时间
  "exp": "2024-12-06T12:34:56Z",            // 过期时间
}
```

实现者可以根据需要，在payload中添加其他的安全措施，比如使用scope、绑定IP地址等。

2. **返回 Token**
将生成的 header、payload 和 signature 通过 Base64 编码拼接，形成最终的 Token。然后通过 Authorization 头返回给客户端：

```plaintext
Authorization: Bearer <token>
```

3. **客户端发送 Token**
客户端在后续请求中将该 Token 通过 Authorization 头字段发送到服务端：

```plaintext
Authorization: Bearer <token>
```

4. **服务端验证 Token**
服务端收到客户端请求后，从 Authorization 头中提取 Token，进行验证，包括验证签名、验证过期时间、验证payload中的字段等。验证方法参考[RFC7519](https://www.rfc-editor.org/rfc/rfc7519)。


## 参考文献

1. **DID-CORE**. Decentralized Identifiers (DIDs) v1.0. Manu Sporny; Amy Guy; Markus Sabadello; Drummond Reed. W3C. 19 July 2022. W3C Recommendation. Retrieved from [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/)

2. **did:web**. Retrieved from [https://w3c-ccg.github.io/did-method-web/](https://w3c-ccg.github.io/did-method-web/)

3. **JSON Canonicalization Scheme (JCS)**. Retrieved from [https://www.rfc-editor.org/rfc/rfc8785](https://www.rfc-editor.org/rfc/rfc8785)

4. **RFC 1035**. Domain names - implementation and specification. P. Mockapetris. IETF. November 1987. Internet Standard. Retrieved from [https://www.rfc-editor.org/rfc/rfc1035](https://www.rfc-editor.org/rfc/rfc1035)

5. **RFC 1123**. Requirements for Internet Hosts - Application and Support. R. Braden, Ed. IETF. October 1989. Internet Standard. Retrieved from [https://www.rfc-editor.org/rfc/rfc1123](https://www.rfc-editor.org/rfc/rfc1123)

6. **RFC 2119**. Key words for use in RFCs to Indicate Requirement Levels. S. Bradner. IETF. March 1997. Best Current Practice. Retrieved from [https://www.rfc-editor.org/rfc/rfc2119](https://www.rfc-editor.org/rfc/rfc2119)

7. **RFC 2181**. Clarifications to the DNS Specification. R. Elz; R. Bush. IETF. July 1997. Proposed Standard. Retrieved from [https://www.rfc-editor.org/rfc/rfc2181](https://www.rfc-editor.org/rfc/rfc2181)

8. **RFC 8174**. Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words. B. Leiba. IETF. May 2017. Best Current Practice. Retrieved from [https://www.rfc-editor.org/rfc/rfc8174](https://www.rfc-editor.org/rfc/rfc8174)

9. **RFC 8484**. DNS Queries over HTTPS (DoH). P. Hoffman; P. McManus. IETF. October 2018. Proposed Standard. Retrieved from [https://www.rfc-editor.org/rfc/rfc8484](https://www.rfc-editor.org/rfc/rfc8484)

10. **DID Use Cases**. Decentralized Identifier Use Cases. Joe Andrieu; Kim Hamilton Duffy; Ryan Grant; Adrian Gropper. W3C. 24 June 2021. W3C Note. Retrieved from [https://www.w3.org/TR/did-use-cases/](https://www.w3.org/TR/did-use-cases/)

11. **DID Extensions**. Decentralized Identifier Extensions. Orie Steele; Manu Sporny. W3C. 24 June 2021. W3C Note. Retrieved from [https://www.w3.org/TR/did-extensions/](https://www.w3.org/TR/did-extensions/)

12. **DID Extension Properties**. Decentralized Identifier Extension Properties. Orie Steele; Manu Sporny. W3C. 24 June 2021. W3C Note. Retrieved from [https://www.w3.org/TR/did-extensions-properties/](https://www.w3.org/TR/did-extensions-properties/)

13. **DID Extension Methods**. Decentralized Identifier Extension Methods. Orie Steele; Manu Sporny. W3C. 24 June 2021. W3C Note. Retrieved from [https://www.w3.org/TR/did-extensions-methods/](https://www.w3.org/TR/did-extensions-methods/)

14. **DID Extension Resolution**. Decentralized Identifier Extension Resolution. Orie Steele; Manu Sporny. W3C. 24 June 2021. W3C Note. Retrieved from [https://www.w3.org/TR/did-extensions-resolution/](https://www.w3.org/TR/did-extensions-resolution/)


15. **Controller Document**. Controller Document. Manu Sporny; Markus Sabadello. W3C. 24 June 2021. W3C Note. Retrieved from [https://www.w3.org/TR/controller-document/](https://www.w3.org/TR/controller-document/)
