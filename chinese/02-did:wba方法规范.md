# did:wba方法规范

## 摘要


## 1. 引言

本规范在did:web方法规范([https://w3c-ccg.github.io/did-method-web](https://w3c-ccg.github.io/did-method-web))的基础上，添加了跨平台身份认证流程、智能体描述服务等规范描述，提出了新的方法名did:wba(Web-Based Agent)。

考虑到did:web方法规范仍然是一个草案，未来可能会有不适宜智能体通信场景的改动，和原作者就规范修改达成共识也是一个长期过程，所以我们决定使用一个新的方法名。

未来不排除将did:wba规范合并到did:web规范中的可能。

## 2. WBA DID 方法规范

### 2.1 基本方法规范

WBA DID基本方法规范全部继承自did:web方法规范，规范地址为[https://w3c-ccg.github.io/did-method-web/#web-did-method-specification](https://w3c-ccg.github.io/did-method-web/#web-did-method-specification)，版本日期为2024年7月31日。

为了方便管理，我们备份了一份当前使用的did:web方法规范文档：[did:web方法规范](/references/did_web%20Method%20Specification.html)。

基本方法规范涉及以下方面：
- (方法标识符规范)[https://w3c-ccg.github.io/did-method-web/#method-specific-identifier]
- (加密材料和DID文档处理)[https://w3c-ccg.github.io/did-method-web/#key-material-and-document-handling]
- (DID方法操作，包括创建、更新、停用、读取)[https://w3c-ccg.github.io/did-method-web/#did-method-operations]
- （安全注意事项）[https://w3c-ccg.github.io/did-method-web/#security-and-privacy-considerations]

需要注意的是，在应用的时候，需要将方法名修改为“wba”。  


TODO: 添加CURD的规范。

添加安全注意事项

添加DID生成的规则



### 2.2 did:wba DID文档示例

除DID核心规范外，其他大部分规范尚处于草案阶段。本章节将展示一个用于身份验证的DID文档的子集。为了提高系统间的兼容性，所有标注为必须的字段，所有系统必须支持；标注为可选的字段，可以选择性支持。未列出的其他标准中定义的字段，可以选择性支持。

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

- **@context**: 必须字段，JSON-LD 上下文定义了DID文档中使用的语义和数据模型，确保文档的可理解性和互操作性。"https://www.w3.org/ns/did/v1"是必须的。其他根据需要添加。

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

## 3. 跨平台身份认证流程

### 3.1 读取DID文档

参考[did:web方法规范](https://w3c-ccg.github.io/did-method-web/#read-resolve)，使用HTTP协议读取DID文档。具体如下：
- 将方法特定标识符中的“:”替换为“/”以获得完全限定的域名和可选路径。
- 如果域名包含端口，则对冒号进行百分比解码。
- 通过在预期的DID文档位置前加上https://生成HTTPS URL。
- 如果URL中未指定路径，则附加/.well-known。
- 附加/did.json以完成URL。
- 使用能够成功协商安全HTTPS连接的代理执行对URL的HTTP GET请求，该代理强制执行(2.6节安全和隐私注意事项中)[https://w3c-ccg.github.io/did-method-web/#security-and-privacy-considerations]描述的安全要求。
- 验证解析的DID文档的ID是否与正在解析的Web DID匹配。
- 在HTTP GET请求期间执行DNS解析时，客户端应使用[（RFC8484）[https://w3c-ccg.github.io/did-method-web/#bib-rfc8484]]以防止跟踪正在解析的身份。

举例:
- 解析”did:wba:example.com%3A8800:user:alice“的DID文档，转换后的URL为：https://example.com:8800/user/alice/did.json。
- 解析“did:wba:example.com”的DID文档，转换后的URL为：https://example.com/.well-known/did.json。

### 3.2 基于HTTP的单方认证

单方认证是指在客户端与服务端模式中，客户端可以通过服务端的域名验证服务端的身份，而服务端使用DID验证客户端的身份。比如，客户端使用HTTP请求访问资源服务器，资源服务器使用DID文档中的验证方法验证客户端的身份。

！！！！todo：添加http only的包含？？？？

#### 3.2.1 初始请求

当前客户端首次向服务端发起HTTP请求时，需要按照以下方法进行身份认证。

##### 3.2.1.1 请求头部格式

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
```
Authorization: DID did:wba:example.com%3A8800:user:alice Nonce <abc123> Timestamp <2024-12-05T12:34:56Z> VerificationMethod <key-1> Signature <base64(signature_of_nonce_timestamp_service_did)>
```

##### 3.2.1.2 签名生成流程

1. 客户端生成包含以下信息的字符串：

```json
{ 
  "nonce": "abc123", 
  "timestamp": "2024-12-05T12:34:56Z", 
  "service": "example.com", 
  "did": "did:wba:example.com:user:alice" 
}
```

2. 使用(JCS(JSON Canonicalization Scheme))[https://www.rfc-editor.org/rfc/rfc8785]对上面的json字符串进行规范化，生成规范化字符串。

3. 使用SHA-256算法对规范化字符串进行哈希，生成hash值。

4. 使用客户端的私钥对hash值进行签名，生成签名值 `signature`，并进行Base64编码。

5. 将 `Authorization` 头部构建成上述格式，发送到服务端。

#### 3.2.1.3 服务端验证

##### 3.2.1.3.1 验证请求头部

服务端收到客户端请求后，进行以下验证：

1. **验证时间戳**：检查请求中的时间戳是否在合理的时间范围内，建议时间范围为1分钟。如果请求的时间戳超出范围，认为请求过期，返回 `401 Unauthorized`，并附加挑战信息。

2. **验证Nonce**：检查请求中的 `nonce` 是否已被使用或存在重复。若 `nonce` 已存在，则认为是重放攻击，返回 `401 Unauthorized`，并附加挑战信息。

3. **验证DID权限**：验证请求中的DID是否具备访问服务端资源的权限。如果没有权限，则返回 `403 Forbidden`。

4. **验证签名**：
- 根据客户端的DID，读取DID文档。
- 根据请求中的 `VerificationMethod`，在DID文档中找到对应的验证方法。
- 使用验证方法中的公钥对请求中的签名进行验证。

5. **验证结果**：如果签名验证成功，则请求通过验证；否则，返回 `401 Unauthorized`，并附加挑战信息。


##### 3.2.1.3.2 验证签名过程

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

3. **规范化字符串**：使用(JCS(JSON Canonicalization Scheme))[https://www.rfc-editor.org/rfc/rfc8785]对JSON字符串进行规范化，生成规范化字符串。

4. **生成哈希值**：使用SHA-256算法对规范化字符串进行哈希，生成hash值。

5. **获取公钥**：根据 `did` 和 `VerificationMethod`，从DID文档中获取对应的公钥。

6. **验证签名**：使用获取的公钥对 `Signature` 进行验证，确保签名是由对应的私钥生成的。

##### 3.2.1.3.3 401响应

当服务端验证签名失败，需要客户端重新发起请求时，可以返回401响应，并附加挑战信息。挑战信息中必须包含 `nonce` 字段。

同时，如果服务端不支持记录客户端请求的Nonce，或者要求客户端每次必须使用服务端生成的Nonce进行签名，则可以在客户端每次首次请求时，均返回401响应，并附加挑战信息。但是这样会增加客户端的请求次数，实现者可以自行选择是否使用。

挑战信息通过 `WWW-Authenticate` 头字段返回，示例如下：
```
WWW-Authenticate: Bearer error="invalid_nonce", error_description="Nonce has already been used. Please provide a new nonce.", nonce="xyz987"
```

挑战信息包含以下字段：
- **nonce**：必须字段，服务端生成的随机字符串，用于防止重放攻击。
- **error**：必须字段，错误类型。
- **error_description**：可选字段，错误描述。

客户端收到401响应后，需要使用服务端的Nonce重新生成签名，并且重新发起请求，携带新的Nonce。服务端收到新的请求后，需要验证新的Nonce与签名。

需要注意的是，客户端和服务端在各自的实现上，需要对重试次数进行限制，防止进入死循环。

##### 3.2.1.3.4 认证成功返回JWT

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

2. **返回 Token**
将生成的 header、payload 和 signature 通过 Base64 编码拼接，形成最终的 Token。然后通过 Authorization 头返回给客户端：

```
Authorization: Bearer <token>
```

3. **客户端发送 Token**
客户端在后续请求中将该 Token 通过 Authorization 头字段发送到服务端：

```
Authorization: Bearer <token>
```

4. **服务端验证 Token**
服务端收到客户端请求后，从 Authorization 头中提取 Token，进行验证，包括验证签名、验证过期时间、验证payload中的字段等。验证方法参考[RFC7519](https://www.rfc-editor.org/rfc/rfc7519)。

### 3.3 基于HTTP的双方认证

使用一个http请求专门进行双方的认证





## 智能体描述

## 用例

跨平台访问文件。通过在资源服务器提前配置信任DID列表，资源服务器可以识别出请求的客户端是否可信。 

双向认证用例？？

## 总结

安全性依赖域名。







## 参考文献

[1]JSON Canonicalization Scheme (JCS), https://www.rfc-editor.org/rfc/rfc8785