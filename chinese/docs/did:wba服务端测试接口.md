
# did:wba服务端测试接口

未来方便进行did:wba的测试，我们开发了一个用于测试的服务端，设计了多个http接口，用于上传、获取，以及DID功能测试。

服务端的测试域名是：`pi-unlimited.com`（后面会改成`agent-network-protocol.com`）。

你可以自己在本地生成DID文档，然后上传到我们的服务器，这样就可以生成一个可以使用的DID。

比如，你上传的路径是`https://pi-unlimited.com/wba/user/2i3dg4dtf908cde0/did.json`，那么你生成的DID就是`did:wba:pi-unlimited.com:wba:user:2i3dg4dtf908cde0`。

## 1. 上传 JSON 文件（PUT 请求）

### 请求路径
`https://pi-unlimited.com/wba/user/2i3dg4dtf908cde0/did.json`

注意：
- "2i3dg4dtf908cde0" 是一个唯一标识，未来防止冲突，建议使用16为随机字符串。
- 如果id在服务端已经存在，会返回409 Conflict。
- 此接口暂时只用于测试用途，每个IP限定最多put50个文件。

### 请求格式示例
```plaintext
PUT /wba/user/2i3dg4dtf908cde0/did.json HTTP/1.1
Host: pi-unlimited.com
Content-Type: application/json
Content-Length: <文件长度>

<DID文档json>
```

## 2. 获取 JSON 文件（GET 请求）

### 请求路径
`https://pi-unlimited.com/wba/user/2i3dg4dtf908cde0/did.json`

### 请求格式示例
```plaintext
GET /wba/user/2i3dg4dtf908cde0/did.json HTTP/1.1
Host: pi-unlimited.com
```

### 响应格式示例
```plaintext
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: <文件长度>

<DID文档json>
```

### 错误响应
- 404 Not Found: 指定的资源不存在。

## 3. 测试did:wba身份验证正常功能

提供了一个服务端测试接口，用于测试用户的did:wba身份验证是否正常。

### 请求路径
`https://pi-unlimited.com/wba/test`

### 请求格式示例
```plaintext
GET /wba/test HTTP/1.1
Host: pi-unlimited.com
Authorization: DID did:wba:example.com%3A8800:user:alice Nonce <abc123> Timestamp <2024-12-05T12:34:56Z> VerificationMethod <key-1> Signature <base64url(signature_of_nonce_timestamp_service_did)>
```

http请求头中的Authorization字段，按照did:wba方法规范进行签名。
如果是验证token流程，Authorization填写服务端首次请求返回的token。示例：

```plaintext
Authorization: Bearer <token>
```

### 响应格式示例
```plaintext
HTTP/1.1 200 OK
Authorization: Bearer <token>
Content-Type: application/text
Content-Length: <文件长度>

OK
```

首次请求中，携带的Authorization字段，包含用于后续http请求的token。

### 错误响应
- 403 Forbidden: 鉴权失败



## 4. 测试did:wba身份验证401功能

提供了一个服务端测试接口，用于测试用户的did:wba身份验证在服务端返回401的时候，客户端是否能够正常处理。

### 请求路径
`https://pi-unlimited.com/wba/test401`

### 请求格式示例
```plaintext
GET /wba/test401 HTTP/1.1
Host: pi-unlimited.com
Authorization: DID did:wba:example.com%3A8800:user:alice Nonce <abc123> Timestamp <2024-12-05T12:34:56Z> VerificationMethod <key-1> Signature <base64url(signature_of_nonce_timestamp_service_did)>
```

http请求头中的Authorization字段，按照did:wba方法规范进行签名。
如果是验证token流程，Authorization填写服务端首次请求返回的token。示例：

```plaintext
Authorization: Bearer <token>
```

### 响应格式示例
```plaintext
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer error="invalid_nonce", error_description="Nonce has already been used. Please provide a new nonce.", nonce="xyz987"
Content-Type: application/json
Content-Length: 0
```

WWW-Authenticate字段，包含用于后续http请求签名的nonce。





