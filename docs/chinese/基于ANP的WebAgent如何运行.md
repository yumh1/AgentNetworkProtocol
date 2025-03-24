# 基于ANP的WebAgent 使用指南：以天气智能体为例

## 概述

WebAgent 是专为 AI 访问设计的网络智能体，允许其他智能体通过标准化协议直接获取信息和服务。本文档以天气 WebAgent 为例，详细说明 WebAgent 的运行机制及使用方法。

## 1. WebAgent 发现机制

智能体可以通过两种方式发现 WebAgent：

### 1.1 主动发现（通过域名）

当知道 WebAgent 的域名时，可以通过访问规范化的路径获取智能体列表：

```
https://<域名>/.well-known/agent-descriptions
```

**示例**：访问 `https://agent-weather.xyz/.well-known/agent-descriptions` 会返回如下 JSON-LD 格式数据：

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

通过这个响应，智能体可获知域名下存在的 WebAgent 列表及其描述文件地址。

其中，https://agent-weather.xyz/ad.json 是天气智能体的描述文件地址。

### 1.2 被动发现（通过搜索服务）

WebAgent 可以将自己注册到智能体搜索服务中，使其他智能体能通过关键词搜索找到它。例如，搜索"天气"关键词可能返回天气 WebAgent 的信息。

## 2. WebAgent 描述文件解析

发现 WebAgent 后，下一步是获取并解析其描述文件（Agent Description）。

**示例**：天气智能体的描述文件 `https://agent-weather.xyz/ad.json` 包含：

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

**描述文件关键字段解析**：

- `name`, `description`：WebAgent 的名称和功能描述
- `owner`：WebAgent 所有者信息
- `securityDefinitions`：身份验证方式定义
- `security`：使用的验证方案名称
- `interfaces`：提供的接口列表，包含：
  - 结构化接口：用于天气查询、预订等功能
  - 自然语言接口：通过自然语言交互

通过描述信息，智能体可以了解到WebAgent的名称、功能、接口类型、接口地址、接口认证方式等信息。通过调用接口，智能体可以获取到天气信息、预订服务、订阅状态查询等功能。

## 3. 身份认证机制

访问 WebAgent 需要提供身份验证，确保请求来自可信任的智能体。

### 3.1 DID 身份认证流程

天气 WebAgent 使用 `did:wba` 方法进行身份验证：

1. **获取 DID**：每个智能体需要拥有自己的 DID，如 `did:wba:example.com:agent:weather123`
2. **准备 DID 文档**：包含公钥的 DID 文档需发布在特定域名路径
3. **签名请求**：调用方使用私钥对请求内容生成签名
4. **发送请求**：将签名添加到 `Authorization` 头中发送请求
5. **验证过程**：WebAgent 验证签名的有效性并决定是否授权访问

### 3.2 测试 DID

为方便开发者测试，ANP 提供了公共测试 DID：

- DID：`did:wba:agent-did.com:test:public`
- 位置：[ANP 示例代码库](https://github.com/agent-network-protocol/anp-examples/tree/main/use_did_test_public)
- 用途：仅用于测试，不可用于敏感操作

## 4. 与 WebAgent 交互

### 4.1 访问流程

使用天气 WebAgent 的标准流程：

1. **获取描述文件**：访问 `https://agent-weather.xyz/ad.json`
2. **解析接口信息**：从 `interfaces` 字段获取可用 API 接口
3. **获取接口定义**：下载 `weather-info.yaml` 等 OpenAPI 定义文件
4. **构建请求**：根据 API 定义创建符合格式的请求
5. **添加认证**：在请求头中添加 DID 签名认证信息
6. **发送请求**：向 WebAgent 发送 HTTP 请求
7. **处理响应**：解析返回的结构化数据（JSON/YAML）

### 4.2 代码示例

使用 ANP 工具与天气 WebAgent 交互的代码示例：

```python
# 以下代码展示如何使用 ANPTool 访问天气 WebAgent

async def query_weather(city):
    # 步骤 1：获取智能体描述文件
    ad_url = "https://agent-weather.xyz/ad.json"
    ad_response = await anp_tool.execute(url=ad_url)
    
    # 步骤 2：解析接口信息
    weather_api_url = None
    for interface in ad_response["ad:interfaces"]:
        if "weather" in interface["description"]:
            weather_api_url = interface["url"]
            break
    
    # 步骤 3：获取 API 定义
    api_def = await anp_tool.execute(url=weather_api_url)
    
    # 步骤 4-6：构建请求并发送
    # 注意：实际 URL 和参数需根据 API 定义确定
    weather_endpoint = "https://agent-weather.xyz/api/weather"
    weather_data = await anp_tool.execute(
        url=weather_endpoint,
        method="GET",
        params={"city": city}
    )
    
    # 步骤 7：处理响应
    return weather_data
```

### 4.3 使用 ANP Explorer 工具

ANP Explorer 是一个便捷的 WebAgent 交互工具：

- 网址：https://service.agent-network-protocol.com/anp-explorer/
- 功能：
  1. 以自然语言查询天气信息
  2. 浏览和探索 WebAgent 描述文档
- 使用方式：输入智能体描述文档 URL 或直接提问天气相关问题

## 5. WebAgent 技术特点总结

天气 WebAgent 体现了 ANP 协议的核心优势：

1. **结构化数据**：直接提供 JSON/YAML 格式的数据，无需解析 HTML
2. **自描述性**：智能体自带完整的接口说明，便于自动发现和使用
3. **去中心化认证**：使用 DID 提供跨平台认证，不需要每个智能体系统单独注册
4. **原生 AI 接口**：专为 AI 设计的接口模式，无需模拟人类操作

## 6. 开发自己的 WebAgent 客户端

要开发能与天气 WebAgent 交互的客户端，你需要：

1. 集成 ANP 工具，参考：https://github.com/agent-network-protocol/anp-examples
2. 实现 DID 身份验证功能
3. 编写智能体发现和描述文件解析逻辑
4. 基于接口定义构建请求生成器

只需一个提示词和一个 HTTP 函数，就能让 AI 智能体具备与 WebAgent 交互的能力。

## 参考资源

- ANP 协议规范：https://github.com/agent-network-protocol/AgentNetworkProtocol
- 示例代码库：https://github.com/agent-network-protocol/anp-examples
- 天气 WebAgent：https://agent-weather.xyz/
- ANP Explorer：https://service.agent-network-protocol.com/anp-explorer/
- 第一个专为AI访问而设计的WebAgent诞生了：[第一个专为AI访问而设计的WebAgent诞生了](/blogs/cn/第一个专为AI访问而设计的WebAgent诞生了.md)