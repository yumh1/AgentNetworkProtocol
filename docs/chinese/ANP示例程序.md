# 示例程序清单 / Demo list

[English](#english) | [中文](#chinese)

<a name = "chinese"></a>
## [目录]

  - [X] 示例程序 1：[ANP网络探索工具](#demo1)
  - [X] 示例程序 2：[ANP天气智能体服务-服务端](#demo2)
  - [X] 示例程序 3：[ANP智能体通信示例](#demo3)

<a name = "demo1"></a>
## 示例程序 1：ANP网络探索工具
### 简介

    本示例程序展示了 ANP 协议在天气查询场景下的应用。通过自然语言驱动 Agent，用户能够轻松查询天气信息，体验未来科技带来的便捷交互。

### 展示要点

    自然语言交互‌：用户可以使用自然语言与 Agent 进行沟通，无需复杂的指令输入。
  
    透明查询过程‌：程序透明展示查询过程及 Agent 访问记录，让用户清晰了解信息获取途径。
  
    便捷访问方式‌：提供网页直接访问和本地代码运行两种方式，满足不同用户的需求。

### 链接地址

    网页访问地址‌：https://service.agent-network-protocol.com/anp-demo/

    代码仓库地址‌：https://github.com/agent-network-protocol/anp-examples

<a name = "demo2"></a>
## 示例程序 2：ANP天气智能体服务-服务端
### 简介

    本示例程序展示了 ANP天气智能体服务中的服务端应用。通过集成第三方天气查询API接口，能够被demo1中的ANP网络探索工具发现，并为其提供查询天气信息服务。DEMO1与DEMO2的关系参见下图所示。
  
![demo关系](/images/relationship.png)

### 展示要点

    集成第三方API‌ ：服务端集成了第三方天气查询API接口，能够提供实时的天气信息查询服务。
  
    与客户端协同工作‌ ：服务端能够被 ANP网络探索工具 （客户端）发现，并为其提供查询天气信息服务。
  
    灵活部署方式 ：服务端支持多种部署方式，包括本地运行和云服务器部署，满足不同场景的需求。

### 链接地址

    网页访问地址‌：https://agent-weather.xyz/ad.json

    代码仓库地址‌：https://github.com/agent-network-protocol/anp-weather-agent

<a name = "demo3"></a>
## 示例程序 3：ANP智能体通信示例
### 简介

    本示例程序展示了如何构建和使用符合 ANP 协议的远程智能体及配套客户端。通过 FastANP 框架，开发者可以快速创建具备身份认证、服务发现和 JSON-RPC 调用能力的智能体应用。

### 展示要点

    远程智能体服务‌：基于 FastANP 构建的服务端，提供 echo 和 greeting 两个示例接口，支持 JSON-RPC 协议调用。
  
    多种客户端实现‌：包括基础的 ANPCrawler 脚本客户端和集成 LLM 的智能客户端，展示不同的交互模式。
  
    DID 身份认证‌：完整的 DID 文档和 JWT 签名示例，演示智能体间的安全认证流程。
  
    灵活部署方式‌：支持本地开发测试和云端部署，提供在线可访问的演示环境。

### 链接地址

    在线演示地址‌：https://agent-connect.ai/agents/test/ad.json

    代码仓库地址‌：https://github.com/agent-network-protocol/anp-agent-example

# 更多DEMO敬请期待...

<a name = "english"></a>
## [Catalog]

  - [X] DEMO 1：[ANP Network Exploration Tool](#demo1-en)
  - [X] DEMO 2：[ANP Weather Agent Service - Server](#demo2-en)
  - [X] DEMO 3：[ANP Agent Communication Example](#demo3-en)

<a name = "demo1-en"></a>
## DEMO 1：ANP Network Exploration Tool
### Overview

    This example program demonstrates the application of ANP protocol in weather query scenarios. Through natural language driven agents, users can easily query weather information and experience the convenient interaction brought by future technology.

### Feature

    Natural language interaction: Users can communicate with agents using natural language without the need for complex command inputs.
  
    Transparent query process: The program transparently displays the query process and Agent access records, allowing users to clearly understand the ways to obtain information.
  
    Convenient access method: Provides two ways to access web pages directly and run local code to meet the needs of different users.

### Link address

    Web page access address : https://service.agent-network-protocol.com/anp-demo/

    Github address : https://github.com/agent-network-protocol/anp-examples

<a name = "demo2-en"></a>
## DEMO 2：ANP Weather Agent Service - Server
### Overview

    This example program demonstrates the server-side application of ANP weather intelligent agent service.

    By integrating a third-party weather query API interface, it can be discovered by the ANP network exploration tool in demo1 and provided with weather information query services. 

    The relationship between DEMO1 and DEMO2 is shown in the following figure.

![relationship of demo](/images/relationship.png)

### Feature

    Integrated third-party API: The server integrates a third-party weather query API interface, which can provide real-time weather information query services.
    
    Collaborate with the client: The server can be discovered by the ANP network exploration tool (client) and provide weather information query services for it.
    
    Flexible deployment method: The server supports multiple deployment methods, including local operation and cloud server deployment, to meet the needs of different scenarios.

### Link address

    Web page access address : https://agent-weather.xyz/ad.json

    Github address : https://github.com/agent-network-protocol/anp-weather-agent

<a name = "demo3-en"></a>
## DEMO 3：ANP Agent Communication Example
### Overview

    This example program demonstrates how to build and exercise ANP-compliant remote agents and companion clients. Through the FastANP framework, developers can quickly create agent applications with identity authentication, service discovery, and JSON-RPC invocation capabilities.

### Feature

    Remote agent service: FastANP-powered server providing echo and greeting sample interfaces, supporting JSON-RPC protocol invocation.
    
    Multiple client implementations: Includes basic ANPCrawler scripted client and LLM-integrated intelligent client, demonstrating different interaction modes.
    
    DID identity authentication: Complete DID document and JWT signing examples, demonstrating secure authentication flows between agents.
    
    Flexible deployment options: Supports local development testing and cloud deployment, with online accessible demo environment.

### Link address

    Online demo address : https://agent-connect.ai/agents/test/ad.json

    Github address : https://github.com/agent-network-protocol/anp-agent-example

# Stay tuned for more demos...
