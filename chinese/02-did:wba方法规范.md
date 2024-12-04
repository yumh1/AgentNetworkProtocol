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

基本方法规范涉及以下方面：ToDo：增加链接到具体内容
- 方法ID设计
- DID文档存储
- DID方法操作，包括创建、更新、停用、读取
- 身份验证与授权
- DID文档完整性验证
- DNS安全注意事项
- 传输安全
- 跨域资源共享

需要注意的是，在应用的时候，需要将方法名修改为“wba”。  


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
    "id": "did:web:example.com%3A8800:user:alice",
    "verificationMethod": [
      {
        "id": "did:web:example.com%3A8800:user:alice#key-0",
        "type": "EcdsaSecp256k1VerificationKey2019",
        "controller": "did:web:example.com%3A8800:user:alice",
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
      "did:web:example.com%3A8800:user:alice#key-0",
      {
        "id": "did:web:example.com%3A8800:user:alice#key-1",
        "type": "Ed25519VerificationKey2020",
        "controller": "did:web:example.com%3A8800:user:alice",
        "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
      }
    ],
    "keyAgreement": [
      {
        "id": "did:web:example.com%3A8800:user:alice#key-2",
        "type": "X25519KeyAgreementKey2019", 
        "controller": "did:web:example.com%3A8800:user:alice",
        "publicKeyMultibase": "z9hFgmPVfmBZwRvFEyniQDBkz9LmV7gDEqytWyGZLmDXE"
      }
    ]
}
```


did文档的示例，最简单的示例
字段怎么用
是否要支持path
使用http进行身份认证的过程
  - 单方认证
  - 双方认证
用例










