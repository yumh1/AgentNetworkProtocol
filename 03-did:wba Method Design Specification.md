# did:wba Method Specification

## Abstract

The wba DID method is a web-based decentralized identifier (DID) specification designed to meet the requirements of cross-platform identity authentication and intelligent agent communication. This method extends and optimizes the did:web specification, named as did:wba, maintaining compatibility while enhancing adaptability for agent scenarios. In this specification, we design a process based on the did:wba method and HTTP protocol that enables servers to quickly verify client identities from other platforms without increasing interaction frequency.

## 1. Introduction 

### 1.1 Preface

The wba DID method specification complies with the requirements specified in Decentralized Identifiers V1.0 [[DID-CORE](https://www.w3.org/TR/did-core/)].

This specification builds upon the did:web method specification by adding DID document constraints, cross-platform identity authentication processes, and agent description service specifications, proposing a new method name did:wba (Web-Based Agent).

Considering that the did:web method specification is still a draft and may undergo changes unsuitable for agent communication scenarios, and that reaching consensus with the original authors on specification modifications is a long-term process, we have decided to use a new method name.

We do not rule out the possibility of merging the did:wba specification into the did:web specification in the future, and we will work towards achieving this goal.

The did:wba method references the did:web method specification at [https://w3c-ccg.github.io/did-method-web](https://w3c-ccg.github.io/did-method-web), version dated July 31, 2024. For management purposes, we have backed up a copy of the did:web method specification currently used by did:wba: [did:web Method Specification](/references/did_web%20Method%20Specification.html).

### 1.2 Design Principles

In designing the did:wba method, our core principle is to fully utilize existing mature technologies and robust Web infrastructure while achieving decentralization. Using did:wba enables email-like functionality where platforms can implement their account systems in a centralized manner while maintaining interoperability between platforms.

Furthermore, various types of identifier systems can add DID support, bridging interoperability between centralized, federated, and decentralized identifier systems. This means existing centralized identifier systems do not require complete restructuring; they can achieve cross-system interoperability by simply creating DIDs on top of their existing infrastructure, significantly reducing technical implementation complexity.
## 2. WBA DID Method Specification

### 2.1 Method Name
The method name string used to identify this DID method is: wba. DIDs using this method MUST begin with the following prefix: did:wba. According to the DID specification, this string MUST be lowercase. The remainder of the DID (after the prefix) is specified below.

### 2.2 Method-Specific Identifiers 
The method-specific identifier is a fully qualified domain name protected by TLS/SSL certificates, optionally including a path to the DID document. The formal rules describing valid domain name syntax are specified in [(RFC1035)](https://www.rfc-editor.org/rfc/rfc1035), [(RFC1123)](https://www.rfc-editor.org/rfc/rfc1123), and [(RFC2181)](https://www.rfc-editor.org/rfc/rfc2181).

The method-specific identifier MUST match the common name used in the SSL/TLS certificate and MUST NOT contain IP addresses. Port numbers may be included but colons must be percent-encoded to prevent conflicts with paths. Directories and subdirectories may be optionally included, using colons instead of forward slashes as separators.

wba-did = "did:wba:" domain-name
wba-did = "did:wba:" domain-name * (":" path)

```plaintext
example: wba method DID example

did:wba:example.com

did:wba:example.com:user:alice

did:wba:example.com%3A3000
```

### 2.4 Key Material and Document Processing

Due to how most web servers render content, specific did:wba documents are likely to be served with the media type application/json. When retrieving a document named did.json, the following processing rules should be followed:

1. If @context exists at the root of the JSON document, the document should be processed according to JSON-LD rules. If processing fails or cannot be performed, the document should be rejected as a did:wba document.

2. If @context exists at the root and the document is successfully processed as JSON-LD, and includes the context `https://www.w3.org/ns/did/v1`, it may be further processed as a DID document according to [[did-core specification section 6.3.2](https://www.w3.org/TR/did-core/#consumption-0)].

3. If @context does not exist, the document should be processed as a DID according to the normal JSON rules specified in [[did-core specification section 6.2.2](https://www.w3.org/TR/did-core/#consumption)].

4. When DID URLs appear in a did:wba document, they MUST be absolute URLs.

> Note: This includes URLs in embedded key material and other metadata, which prevents key confusion attacks.

### 2.5 DID Document Specification

Apart from the DID Core specification, most other specifications are still in draft stage. This section will demonstrate a subset of a DID document used for authentication. To enhance interoperability between systems, all fields marked as required MUST be supported by all systems; fields marked as optional MAY be selectively supported. Fields defined in other standards not listed here MAY be selectively supported.

**Example DID Document:**

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

**Field Descriptions:**

- **@context**: Required field. The JSON-LD context defines the semantics and data model used in the DID document, ensuring document comprehensibility and interoperability. `https://www.w3.org/ns/did/v1` is required. Others can be added as needed.

- **id**: Required field. Cannot contain IP addresses but may include ports. When ports are included, colons must be encoded as %3A. Paths are separated using colons.

- **verificationMethod**: Required field. Contains an array of verification methods that define public key information for verifying the DID subject.
  - **Sub-fields**:
    - **id**: Unique identifier for the verification method
    - **type**: Type of verification method
    - **controller**: DID that controls this verification method
    - **publicKeyJwk**: Public key information in JSON Web Key format

- **authentication**: Required field. Lists verification methods used for authentication, which can be strings or objects.
  - **Sub-fields**:
    - **id**: Unique identifier for the verification method
    - **type**: Type of verification method
    - **controller**: DID that controls this verification method
    - **publicKeyMultibase**: Public key information in Multibase format

- **keyAgreement**: Optional field. Defines public key information used for key agreement between DIDs for encrypted communication. Verification methods typically use key agreement algorithms suitable for key exchange, such as X25519KeyAgreementKey2019.
  - **Sub-fields**:
    - **id**: Unique identifier for the key agreement method
    - **type**: Type of key agreement method
    - **controller**: DID that controls this key agreement method
    - **publicKeyMultibase**: Public key information in Multibase format

### 2.5 DID Method Operations

#### 2.5.1 Create (Register)

The did:wba method specification does not specify specific HTTP API operations, but rather leaves the programmatic registration and management to each implementation based on their Web environment requirements.

Creating a DID requires the following steps:

1. Apply for a domain name with a domain name registrar
2. Store the location and IP address of the hosted service in the DNS query service
3. Create a DID document JSON-LD file containing the appropriate key pair and store the did.json file in the well-known URL on behalf of the entire domain name. If multiple DIDs need to be parsed under the same domain name, store them in the specified path.

For example, for the domain name example.com, the did.json will be available at the following URL:

```plaintext
Example: Create a DID
did:wba:example.com
 -> https://example.com/.well-known/did.json
```

If a specified optional path is used instead of the bare domain name, the did.json will be available at the specified path:

```plaintext
Example 5: Create a DID using an optional path
did:wba:example.com:user:alice
 -> https://example.com/user/alice/did.json
```

If a specified port is used on the domain name, the colons between the host and port must be percent-encoded to prevent conflicts with paths.

```plaintext
Example 6: Create a DID using an optional path and port
did:wba:example.com%3A3000:user:alice
 -> https://example.com:3000/user/alice/did.json
```

#### 2.5.2 Read (Parse)

The following steps must be performed to parse a Web DID from a DID document:

- Replace the ":" in the method-specific identifier with "/" to obtain the fully qualified domain name and optional path.
- If the domain name contains a port, decode the port.
- Generate an HTTPS URL by prefixing the expected location of the DID document with `https://`.
- If the URL does not specify a path, append `/.well-known`.
- Append `/did.json` to complete the URL.
- Use a proxy that can successfully negotiate a secure HTTPS connection to execute an HTTP GET request to the URL. The proxy enforces the security and privacy requirements described in [2.6 Security and Privacy Considerations](https://w3c-ccg.github.io/did-method-web/#security-and-privacy-considerations).
- Verify that the ID of the parsed DID document matches the Web DID being parsed.
- During the HTTP GET request, the client should use [[RFC8484](https://w3c-ccg.github.io/did-method-web/#bib-rfc8484)] to prevent tracking the identity being parsed.

#### 2.5.3 Update

To update the DID document, the DID corresponding did.json file must be updated. Note that the DID itself will remain unchanged, but the content of the DID document can be changed, such as adding new verification keys or service endpoints.

> Note:
> Using version control systems such as git and continuous integration systems such as GitHub Actions to manage the update of the DID document can provide support for identity verification and auditing history.

> Note: HTTP API
> The update process does not specify specific HTTP API, but rather leaves the programmatic registration and management to each implementation based on their needs.

#### 2.5.4 Deactivate (Revoke)

To delete the DID document, the did.json file must be removed, or it must no longer be publicly available for other reasons.

### 2.6 Security and Privacy Considerations

Security and privacy considerations are based on [[did:web method specification section 2.6](https://w3c-ccg.github.io/did-method-web/#security-and-privacy-considerations)].

## 3. Cross-Platform Identity Authentication Based on did:wba Method and HTTP Protocol

When a client makes a request to a service on different platforms, the client can use the domain name combined with TLS to authenticate the service. The service then verifies the identity of the client based on the verification methods in the client's DID document.

The client can include the DID and signature in the HTTP header during the first HTTP request. Without increasing the number of interactions, the service can quickly verify the identity of the client. After the initial verification is successful, the service can return a token to the client. The client can then carry the token in subsequent requests, and the service does not need to verify the client's identity each time, but only needs to verify the token.

<p align="center">
  <img src="/images/cross-platform-authentication.png" width="50%" alt="跨平台身份认证流程"/>
</p>

### 3.1 Initial Request

When the client first makes an HTTP request to the service, it needs to authenticate according to the following method.

#### 3.1.1 Request Header Format

The client sends the following information through the `Authorization` header field to the service:
- **DID**: The DID identifier of the client, used for identity verification.
- **Nonce**: A randomly generated string used to prevent replay attacks. It must be unique for each request. We recommend using a 16-byte random string.
- **Timestamp**: The time when the request is initiated, usually in UTC format using ISO 8601, accurate to seconds.
- **VerificationMethod**: Identifies the verification method used in the signature, which is the DID fragment of the verification method in the DID document. For example, for the verification method "did:wba:example.com%3A8800:user:alice#key-1", the verification method's DID fragment is "key-1".
- **Signature**: Signs the `nonce`, `timestamp`, service domain name, and client DID. The signature should be signed with the client's private key and include the following fields:
  - `nonce`
  - `timestamp`
  - `service` (the domain name of the service)
  - `did` (the DID of the client)

Client request example:

```plaintext
Authorization: DID did:wba:example.com%3A8800:user:alice Nonce <abc123> Timestamp <2024-12-05T12:34:56Z> VerificationMethod <key-1> Signature <base64(signature_of_nonce_timestamp_service_did)>
```

#### 3.1.2 Signature Generation Process

1. The client generates a string containing the following information:

```json
{ 
  "nonce": "abc123", 
  "timestamp": "2024-12-05T12:34:56Z", 
  "service": "example.com", 
  "did": "did:wba:example.com:user:alice" 
}
```

2. Use [JCS(JSON Canonicalization Scheme)](https://www.rfc-editor.org/rfc/rfc8785) to normalize the JSON string, generating a normalized string.

3. Use the SHA-256 algorithm to hash the normalized string, generating a hash value.

4. Use the client's private key to sign the hash value, generating a signature value `signature`, and encode it in Base64.

5. Construct the `Authorization` header in the above format and send it to the service.

### 3.2 Service Verification

#### 3.2.1 Verify Request Header

After receiving the client's request, the service performs the following verification:

1. **Verify Timestamp**: Check if the timestamp in the request is within a reasonable time range. The recommended time range is 1 minute. If the timestamp is out of range, the request is considered expired, and the service returns `401 Unauthorized` with a authentication challenge.

2. **Verify Nonce**: Check if the `nonce` in the request has been used or exists. If the `nonce` has been used or exists, it is considered a replay attack, and the service returns `401 Unauthorized` with a authentication challenge.

3. **Verify DID Permissions**: Verify if the DID in the request has the permission to access the resources of the service. If not, the service returns `403 Forbidden`.

4. **Verify Signature**:

- Read the DID document based on the client's DID.
- Find the corresponding verification method in the DID document based on the `VerificationMethod` in the request.
- Use the public key of the verification method to verify the signature in the request.

5. **Verification Result**: If the signature verification is successful, the request passes verification; otherwise, the service returns `401 Unauthorized` with a authentication challenge.

#### 3.2.2 Signature Verification Process

1. **Extract Information**: Extract `nonce`, `timestamp`, `service`, `did`, and `VerificationMethod` from the `Authorization` header.

2. **Build Verification String**: Construct a JSON string identical to the one constructed by the client:

```json
{ 
    "nonce": "abc123", 
    "timestamp": "2024-12-05T12:34:56Z", 
    "service": "example.com", 
    "did": "did:wba:example.com:user:alice" 
}
```

3. **Normalize String**: Use [JCS(JSON Canonicalization Scheme)](https://www.rfc-editor.org/rfc/rfc8785) to normalize the JSON string, generating a normalized string.

4. **Generate Hash Value**: Use the SHA-256 algorithm to hash the normalized string, generating a hash value.

5. **Get Public Key**: Obtain the corresponding public key from the DID document based on `did` and `VerificationMethod`.

6. **Verify Signature**: Use the obtained public key to verify the `Signature`, ensuring that it is generated by the corresponding private key.

#### 3.2.3 401 Response

When the service fails to verify the signature, it can return a 401 response and append a authentication challenge. The authentication challenge must contain the `nonce` field.

Additionally, if the service does not support recording the client's request Nonce or requires the client to use the service's generated Nonce for signing each time, the service can return a 401 response and append a authentication challenge for each initial request. However, this can increase the number of client requests, and implementers can choose whether to use this option.

The authentication challenge is returned through the `WWW-Authenticate` header field, as shown below:

```plaintext
WWW-Authenticate: Bearer error="invalid_nonce", error_description="Nonce has already been used. Please provide a new nonce.", nonce="xyz987"
```

The authentication challenge contains the following fields:

- **nonce**: Required field. The randomly generated string generated by the service to prevent replay attacks.
- **error**: Required field. The type of error.
- **error_description**: Optional field. The error description.

After receiving a 401 response, the client needs to use the service's nonce to generate a new signature and re-send the request, carrying the new nonce. The service then needs to verify the new nonce and signature.

Note that both the client and the service need to limit the number of retry attempts to prevent entering a dead loop.

#### 3.2.4 Authentication Success Return Token

After the service successfully verifies the client's identity, it can return a token in the response. The token is recommended to be in JWT (JSON Web Token) format. The client can then carry the token in subsequent requests, and the service does not need to verify the client's identity each time, but only needs to verify the token.

JWT generation method reference [RFC7519](https://www.rfc-editor.org/rfc/rfc7519).

1. **Generate Token**

Assuming the service uses **JWT (JSON Web Token)** as the token format, JWT typically contains the following fields:

- **header**: Specifies the signing algorithm
- **payload**: Stores user-related information
- **signature**: Signs the `header` and `payload` to ensure their integrity

The payload can include the following fields (other fields can be added as needed):
```json
{
  "sub": "did:wba:example.com:user:alice",  // User DID 
  "iat": "2024-12-05T12:34:56Z",            // Issued time
  "exp": "2024-12-06T12:34:56Z",            // Expiration time
}
```

Implementers can add other security measures in the payload, such as using scope or binding IP addresses.

2. **Return Token**
The generated header, payload, and signature are concatenated and Base64 encoded to form the final token. Then, the token is returned through the Authorization header:

```plaintext
Authorization: Bearer <token>
```

3. **Client Send Token**
The client sends the token through the Authorization header field to the service:

```plaintext
Authorization: Bearer <token>
```

4. **Service Verify Token**
After receiving the client's request, the service extracts the token from the Authorization header and verifies it, including verifying the signature, verifying the expiration time, and verifying the fields in the payload. The verification method is based on [RFC7519](https://www.rfc-editor.org/rfc/rfc7519).


## References

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
