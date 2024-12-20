# 最适合智能体的身份认证技术：对比OpenID Connect、API keys、did:wba


# 大纲

- 前言，介绍did是什么wba是什么，为什么要和另外两个做对比。对比的前提是那种方式更适应智能体通信的需求。
    - 在一个场景下对比：智能体通信
    - 智能体通信对身份认证的最大挑战是什么：互联互通。为什么？AI 只有获得完整的上下文，才能够进行决策。现有的Computer Use方案，以及Anthropic mcp都是为了做到这一点，但是这不是最高效的方式。
    - 当前主流的跨平台的身份认证有哪些，对比下这些与我们设计的方案。  

- 主流跨平台身份认证
    - OpenID Connect（OIDC）

    - API keys


- did:wba
设计理念、流程，特点，优势

0rtt
不用注册

- 对比

    - did:wba vs openID connect / oauth2.0

    - did:wba vs api keys

## 智能体需要新的身份认证技术

智能体对身份认证技术提出了新的需求，其中最重要的一个就是互联互通。

其中的原理很简单：AI必须**具备获得完整上下文信息的能力，具备调用所有工具的能力**，才能够作出正确的决策，采取合适的行动。现在很多厂商试图使用Computer Use方案解决这个问题。

<p align="center">
  <img src="/blogs/images/computer-use-product.png" width="50%" alt="computer use product"/>
</p>

但是我们认为这不是AI与互联网交互最高效的方式。这是让AI模仿人的方式访问互联网，AI应该用它最擅长的方式（API或通信协议）与数字世界交互。

<p align="center">
  <img src="/blogs/images/agent-interview-Internet.png" width="50%" alt="agent-interview-Internet"/>
</p>

这就涉及一个互联互通的问题：在智能体使用API或协议，与互联网或者其他智能体交互的时候，如何进行身份验证？特别进行跨平台的身份验证，以让任何智能体之间都能够进行连接。

## 当前主流跨平台身份认证技术

我们在互联网上的身份账号，很多时候是不能跨平台使用的。比如你的微信账号，在钉钉系统中是无法识别的，反之亦然。

不过现在互联网也有很多跨平台的身份认证技术，比如我们常见的SSO（单点登录），你可以用你的谷歌账户登录很多网站。还有API keys，比如你可以使用OpenAI给你的key，访问OpenAI的API。下面我来简单的介绍下这两种技术，看看是否适合智能体的身份认证。

### OpenID Connect（OIDC）

OpenID Connect (OIDC) 是一种基于 OAuth 2.0 构建的身份验证协议，它允许客户端应用程序验证用户身份，并获取用户的基本信息（如姓名、邮箱）。OIDC 在 OAuth 2.0 的基础上增加了标准化的身份层，使其更适合于登录和单点登录（SSO）场景。

[OpenID Connect 官方规范](https://openid.net/specs/openid-connect-core-1_0.html)。

下面我们以使用谷歌账号登录三方网站为例来介绍下OIDC的流程。[谷歌OIDC官方文档地址。](https://developers.google.com/identity/protocols/oauth2/openid-connect)。

<p align="center">
  <img src="/blogs/images/openid-connect-fllow.png" width="50%" alt="openid-connect-fllow"/>
</p>

使用谷歌账号登录三方网站包括两部分，前置流程和Oauth2.0流程：
- 前置流程
  - 注册谷歌平台账号
  - 创建项目/应用
  - 配置项目/应用，包括重定向URI
  - 获取OAuth 2.0的client id和client secret
- Oauth2.0流程（以授权码流程为例）
  - 获取授权码
  - 使用授权码获取access token和id token，id token中包含用户信息
  - 使用access token和id token访问获取用户的详细信息（可选）。在OpenID Connect流程中，用户的详细信息可以认为是一种受保护的资源。

OpenID Connect的优点是：
- 能够简化用户的身份验证流程
- 使用非常广泛，相关基础设施也比较完善。
- 安全性较高

站在智能体互联互通的场景看，OpenID Connect有几个不足：
- OpenID Connect本质上是让三方应用能够使用身份服务器（比如谷歌）对用户进行身份验证。两个三方应用之间无法使用身份服务器实现他们之间的身份验证。
- OpenID Connect是一个中心化的方案，用户使用的时候需要去身份服务器进行注册等操作，前置操作流程复杂。
- 流程交互复杂，需要多次交互。

### API keys

API Keys（API 密钥）是用于验证应用程序或用户访问应用程序编程接口（API）的简单凭证。它是一种字符串形式的身份标识符，通常由随机生成的字母和数字组成，类似于密码的功能。它可以用于身份验证、访问控制、使用监控等场景。

<p align="center">
  <img src="/blogs/images/api-keys-flow.png" width="50%" alt="api-keys-flow"/>
</p>

使用API Keys验证用户身份的流程：
- 前置流程
  - 去平台注册账号
  - 获取API Keys
- API keys验证流程
  - 在类似https的安全协议请求头中添加API keys
  - 服务端验证客户端的API keys


API keys的优点是：
- 简单，易于实现，交互少
- 支持跨平台身份认证，两个应用只要相互有对方API keys，就可以验证身份
- 广泛用于API服务当中，比如OpenAI、国内的模型API等，大部分使用API keys进行身份验证。

站在智能体互联互通的场景看，API keys有几个不足：   
- 安全性较低。有很多使用API keys做身份验证的MCP server，往往要求用户将API keys写在配置文件中，存在泄漏风险。

<p align="center">
  <img src="/blogs/images/mcp-server-api-key-example.png" width="50%" alt="mcp-server-api-key-example"/>
</p>

- 仍然需要前置流程，需要用户登录注册等操作。

## 基于DID的身份认证技术：did:wba




