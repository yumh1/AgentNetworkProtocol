# 智能体描述协议规范（Draft）

## 摘要

本规范定义了智能体描述协议（Agent Description Protocol, ADP），这是一个用于描述智能体的标准化协议。该协议基于JSON-LD格式，结合schema.org词汇表和自定义词汇表，为智能体提供了统一的描述方式。

协议的核心内容包括：
1. 使用JSON-LD作为基础数据格式，支持链接数据和语义网特性
2. 定义了智能体基本信息、产品、服务、接口等核心词汇
3. 采用did:wba方法作为统一的安全机制，实现跨平台身份认证
4. 支持与其他协议（如OpenAPI、JSON-RPC）的互操作性

本规范旨在提高智能体之间的互操作性和通信效率，为构建智能体网络提供基础支持。

## 引言

智能体描述（Agent Description,AD）是智能体入口点，其他的智能体基于AD，可以获得这个智能体的名字、所属实体、功能、产品、服务、交互API或协议等信息。借助这些信息，可以实现智能体之间的数据通信与协作。

随着AI能力的不断提升，AI理解自然语言的能力也在提升，理论上，使用无固定规范要求的纯自然语言也可以对智能体的信息进行描述，但是这样会增加智能体之间通信的成本、降低两个智能体之间信息理解的一致性。因此，为了提高智能体之间的通信效率，需要一种能够描述智能体的规范，使得智能体之间信息交互的一致性得到保证。

## 概述

我们使用[JSON-LD](https://www.w3.org/TR/json-ld11/)(JavaScript Object Notation for Linked Data)作为智能体描述的格式，JSON-LD是一种用于表示链接数据（Linked Data）和语义网数据的标准格式。它基于JSON（JavaScript Object Notation）的语法，并且允许在JSON对象中嵌入链接，以便表示数据之间的关系和结构。

这样，我们就可以将智能体的所有的信息存储为多个文件，然后使用智能体描述文档，将这些文件链接到一起。智能体描述文档就可以作为智能体的入口点，其他的智能体可以基于这个描述文档，来获取智能体的所有信息。

为了提高智能体对描述文档理解的一致性，我们定义了一些列标准词汇（Vocabulary）。同时，在描述产品、服务等资源时，我们建议使用schema.org的词汇，以提高文档理解的一致性。如果schema.org的词汇无法满足需求，用户也可以自定义词汇。使用schema.org的词汇的另外一个好处是，数据能够被代码直接处理，而不是只能够让AI处理。

JSON-LD也需要和其他协议配合使用。比如，接口描述协议可以使用yaml格式描述的OpenAPI，也可以使用JSON-RPC格式描述的RPC协议。

一下是个智能体描述文档示例：

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "did": "https://w3id.org/did#",
    "ad": "https://agent-network-protocol.com/ad#"
  },
  "@type": "ad:AgentDescription",
  "@id": "https://agent-network-protocol.com/agents/smartassistant",
  "name": "SmartAssistant",
  "did": "did:wba:example.com:user:alice",
  "owner": {
    "@type": "Organization",
    "name": "Hangzhou Bit Intelligence Technology Co., Ltd.",
    "@id": "https://agent-network-protocol.com"
  },
  "description": "SmartAssistant is an intelligent agent solution for individuals and enterprises, providing various natural language processing and cross-platform connectivity capabilities.",
  "version": "1.0.0",
  "created": "2024-12-31T12:00:00Z",
  "products": [
    {
      "@type": "Product",
      "name": "AI Assistant Pro",
      "description": "A high-end AI assistant offering advanced customization services.",
      "@id": "https://agent-network-protocol.com/products/ai-assistant-pro"
    },
    {
      "@type": "Product",
      "name": "Agent Connector",
      "description": "A cross-platform connectivity solution for intelligent agents.",
      "@id": "https://agent-network-protocol.com/products/agent-connector"
    }
  ],
  "interfaces": [
    {
      "@type": "ad:NaturalLanguageInterface",
      "protocol": "YAML",
      "url": "https://agent-network-protocol.com/api/nl-interface.yaml",
      "description": "A YAML file for interacting with the intelligent agent through natural language."
    },
    {
      "@type": "ad:APIInterface",
      "protocol": "JSON-RPC 2.0",
      "url": "https://agent-network-protocol.com/api/api-interface.json",
      "description": "A JSON-RPC 2.0 file for interacting with the intelligent agent through APIs."
    }
  ]
}

```

下面是一个产品的描述示例：
```json
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Product",
  "@id": "https://agent-network-protocol.com/products/ai-assistant-pro",
  "name": "AI Assistant Pro",
  "description": "A high-end AI assistant offering advanced customization services.",
  "version": "2.1.3",
  "brand": {
    "@type": "Brand",
    "name": "SmartTech"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://agent-network-protocol.com/store/ai-assistant-pro"
  }
}

```

## 命名空间

在本规范中，与智能体描述相关的词汇术语始终以其紧凑的形式呈现。它们的扩展形式可以通过命名空间 IRI https://agent-network-protocol.com/ad# 访问。

## AD 信息模型

### 概述

AD的信息模型建立在词汇表https://agent-network-protocol.com/ad#和schema.org的词汇表之上。

其中命名空间“ad”定义了智能体描述的关键词汇，schema.org定义了智能体描述的一些常用词汇，这些词汇可以被用户自定义，也可以被AI自动识别。

### 词汇表定义

#### 核心词汇定义

##### Agent（智能体）
智能体是一个物理或虚拟实体的抽象，其元数据和接口通过智能体描述（AD）文档进行描述。虚拟实体可以是一个或多个智能体的组合。

表1：智能体级别的词汇术语

| 词汇术语 | 描述 | 是否必需 | 类型 |
|---------|------|---------|------|
| @context | JSON-LD关键字，用于定义在AD文档中使用的简写名称（术语）。 | 必需 | anyURI或Array |
| @type | JSON-LD关键字，用于为对象添加语义标签（或类型）。 | 可选 | string或Array of string |
| @id | 智能体的标识符，采用URI [RFC3986]格式（如稳定URI、临时和可变URI、带本地IP地址的URI、URN等）。 | 可选 | anyURI |
| did | 智能体的去中心化标识符（DID），用于唯一标识智能体的身份。 | 可选 | string |
| name | 提供基于默认语言的人类可读名称（如用于UI展示的文本）。 | 必需 | string |
| description | 基于默认语言提供额外的（人类可读）信息。 | 可选 | string |
| version | 提供版本信息。 | 可选 | VersionInfo |
| created | 提供AD实例创建时间信息。 | 可选 | dateTime |
| modified | 提供AD实例最后修改时间信息。 | 可选 | dateTime |
| owner | 提供智能体所有者信息。可以是个人或组织。 | 可选 | Person或Organization |
| products | 智能体提供的所有产品列表。 | 可选 | Array of Product |
| services | 智能体提供的所有服务列表。 | 可选 | Array of Service |
| interfaces | 智能体提供的所有接口定义。 | 可选 | Array of Interface |
| security | 安全定义名称集合，从securityDefinitions中选择。访问资源时必须满足所有安全要求。 | 必需 | string或Array of string |
| securityDefinitions | 命名安全配置集合（仅定义）。仅在security名称-值对中使用时才实际应用。 | 必需 | Map of SecurityScheme |

对于@context，AD实例定义了以下规则：

1. @context 名值对必须包含anyURI https://agent-network-protocol.com/ad# 以标识文档为AD文档。
2. 当@context是一个数组时，可以包含多个anyURI或Map类型的元素，建议将所有名值对包含在一个Map中。
3. @context数组中的Map可以包含名值对，其中值是anyURI类型的命名空间标识符，名称是表示该命名空间的术语或前缀。
4. @context数组中的一个Map应包含定义AD默认语言的名值对，其中名称是术语@language，值是符合[BCP47]定义的语言标签（如en、zh-CN、zh-TW等）。

##### Interface（接口）
接口定义了与智能体进行交互的方式。基本接口类型包括：

1. NaturalLanguageInterface：自然语言接口，用于通过自然语言与智能体交互
2. APIInterface：API接口，用于通过特定的API协议与智能体交互

表5：接口级别的词汇术语

| 词汇术语 | 描述 | 是否必需 | 类型 |
|---------|------|---------|------|
| @type | 接口类型。 | 必需 | string |
| @id | 接口的唯一标识符。 | 必需 | anyURI |
| name | 接口名称。 | 必需 | string |
| description | 接口的详细描述信息。 | 必需 | string |
| protocol | 接口使用的协议，当前支持YAML、JSON-RPC 2.0。 | 必需 | string |
| url | 接口定义文档的URL。 | 必需 | anyURI |
| version | 接口版本信息。 | 可选 | string |
| security | 接口的安全要求。 | 可选 | SecurityScheme |

### 安全机制

智能体描述协议使用did:wba方法作为其安全机制。did:wba方法是一种基于Web的去中心化标识符（DID）规范，旨在满足跨平台身份认证和智能体通信的需求。

#### DIDWBASecurityScheme（DID WBA安全方案）

描述基于did:wba方法的安全机制配置的元数据。

表2：安全方案级别的词汇术语

| 词汇术语 | 描述 | 是否必需 | 类型 |
|---------|------|---------|------|
| @type | JSON-LD关键字，用于为对象添加语义标签。 | 可选 | string或Array of string |
| description | 基于默认语言提供额外的（人类可读）信息。 | 可选 | string |
| scheme | 安全机制的标识，固定为"didwba"。 | 必需 | string |
| did | 智能体的did:wba标识符。 | 必需 | string |

以下是一个使用did:wba方法的安全配置示例：

```json
{
    "securityDefinitions": {
        "didwba_sc": {
            "scheme": "didwba",
            "did": "did:wba:example.com:user:alice"
        }
    },
    "security": "didwba_sc"
}
```

AD中的安全配置是必需的。必须通过智能体级别的security成员激活安全定义。此配置是与智能体交互所需的安全机制。安全定义也可以在form元素级别通过在form对象中包含security成员来激活，这将覆盖（即完全替换）智能体级别激活的定义。
