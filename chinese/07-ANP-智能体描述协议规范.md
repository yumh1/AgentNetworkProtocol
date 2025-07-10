# ANP-智能体描述协议规范（Draft）

## 摘要

本规范定义了智能体描述协议（Agent Description Protocol, ADP），这是一个用于描述智能体的标准化协议。它定义了一个智能体如何对外发布其公开信息、支持的Interface等。其他智能体获得这个智能体的描述后，就可以与这个智能体进行信息的交换以及协作。

本规范定义了基于ANP协议，两个智能体之间的信息交互模式。

规范的核心内容包括：
1. 使用JSON作为基础数据格式，支持链接数据和语义网特性
2. 定义了智能体基本信息、产品、服务、接口等核心词汇
3. 采用did:wba方法作为统一的安全机制，实现跨平台身份认证。身份认证方法也是可扩展的，后期可以支持其他的方法
4. 支持与现有标准协议（如OpenAPI、JSON-RPC）的互操作性

本规范旨在提高智能体之间的互操作性和通信效率，为构建智能体网络提供基础支持。

信息交互模式的设计，兼容性的设计，

## 概述

智能体描述（Agent Description,AD）文档是访问一个智能体的入口，类似于一个网站的首页。其他的智能体基于此AD文档，获得智能体的名字、所属实体、功能、产品、服务、交互API或协议等信息。借助这些信息，可以实现智能体之间的数据通信与协作。

本规范主要解决两个问题，一是定义两个智能体之间的信息交互模式，另外一个是定义智能体描述文档的格式。

### 信息交互模式

ANP采用的是类似“网络爬虫”的信息交互模式，即智能体使用URL将对外提供的数据（文件、API等）以及数据的描述连接成一个网络，其他的智能体可以像爬虫一样，根据数据的描述信息，选择读取合适的数据到本地，并且在本地进行决策和处理。如果是一个API文件，也可以调用API和智能体进行交互。

![anp-information-interact](/images/anp-information-interact.png)

“网络爬虫”模式的信息交互模式具有以下几个优点：
- 与现有互联网架构类似，便于搜索引擎对智能体公开信息进行索引，创建一个高效的智能体数据网络
- 将远端数据拉取到本地，作为模型上下文进行处理，将有助于避免用户隐私的泄漏。任务分包的交互模式，会在任务中泄漏用户隐私。
- 天然的分级结构，便于智能体与大量其他的智能体进行交互。

### 核心概念

Information和Interface是ANP智能体描述规范的核心概念。

information是智能体对外提供的数据，包括文本文件、图片、视频、音频、表格等。

interface是智能体对外提供的接口，Interface分为两类接口：
- 一类是自然语言接口，可以让智能体提供更加个性化的服务；
- 一类是结构化接口，可以让智能体提供更加高效、标准化的服务。

虽然使用模型的能力，自然语言接口可以满足绝大部分的场景，但是结构化接口在很多场景中，可以提高智能体之间的通信效率。

## 智能体描述文档格式

受益于AI能力的提升，智能体描述文档

一下是个智能体描述文档示例：


```json
{
  "protocolType": "ANP",
  "protocolVersion": "1.0.0",
  "type": "AgentDescription",
  "url": "https://agent-network-protocol.com/agents/smartassistant",
  "name": "SmartAssistant",
  "did": "did:wba:example.com:user:alice",
  "owner": {
    "type": "Organization",
    "name": "Hangzhou Bit Intelligence Technology Co., Ltd.",
    "url": "https://agent-network-protocol.com"
  },
  "description": "SmartAssistant is an intelligent agent solution for individuals and enterprises, providing various natural language processing and cross-platform connectivity capabilities.",
  "version": "1.0.0",
  "created": "2024-12-31T12:00:00Z",
  "securityDefinitions": {
    "didwba_sc": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "security": "didwba_sc",
  "products": [
    {
      "type": "Product",
      "name": "AI Assistant Pro",
      "description": "A high-end AI assistant offering advanced customization services.",
      "url": "https://agent-network-protocol.com/products/ai-assistant-pro"
    },
    {
      "type": "Product",
      "name": "Agent Connector",
      "description": "A cross-platform connectivity solution for intelligent agents.",
      "url": "https://agent-network-protocol.com/products/agent-connector"
    }
  ],
  "interfaces": [
    {
      "type": "NaturalLanguageInterface",
      "protocol": "YAML",
      "url": "https://agent-network-protocol.com/api/nl-interface.yaml",
      "description": "A YAML file for interacting with the intelligent agent through natural language."
    },
    {
      "type": "StructuredInterface",
      "protocol": "YAML",
      "humanAuthorization": true,
      "url": "https://agent-network-protocol.com/api/purchase-interface.yaml",
      "description": "A YAML file for interacting with the intelligent agent through purchase."
    },
    {
      "type": "StructuredInterface",
      "protocol": "JSON-RPC 2.0",
      "url": "https://agent-network-protocol.com/api/api-interface.json",
      "description": "A JSON-RPC 2.0 file for interacting with the intelligent agent through APIs."
    }
  ],
  "proof": {
    "type": "EcdsaSecp256r1Signature2019",
    "created": "2024-12-31T15:00:00Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:wba:example.com:user:alice#keys-1",
    "challenge": "1235abcd6789",
    "proofValue": "z58DAdFfa9SkqZMVPxAQpic7ndSayn1PzZs6ZjWp1CktyGesjuTSwRdoWhAfGFCF5bppETSTojQCrfFPP2oumHKtz"
  }
}

```









---------------------------------
原有的智能体描述文档格式，如下：


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
  "securityDefinitions": {
    "didwba_sc": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "security": "didwba_sc",
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
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "humanAuthorization": true,
      "url": "https://agent-network-protocol.com/api/purchase-interface.yaml",
      "description": "A YAML file for interacting with the intelligent agent through purchase."
    },
    {
      "@type": "ad:StructuredInterface",
      "protocol": "JSON-RPC 2.0",
      "url": "https://agent-network-protocol.com/api/api-interface.json",
      "description": "A JSON-RPC 2.0 file for interacting with the intelligent agent through APIs."
    }
  ],
  "proof": {
    "type": "EcdsaSecp256r1Signature2019",
    "created": "2024-12-31T15:00:00Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:wba:example.com:user:alice#keys-1",
    ""
    "challenge": "1235abcd6789",
    "proofValue": "z58DAdFfa9SkqZMVPxAQpic7ndSayn1PzZs6ZjWp1CktyGesjuTSwRdoWhAfGFCF5bppETSTojQCrfFPP2oumHKtz"
  }
}

```

下面是一个产品的描述示例：
```json
{
  "protocolType": "ANP",
  "protocolVersion": "1.0.0",
  "type": "Product",
  "url": "https://agent-network-protocol.com/agents/lkcoffe/roasted-coconut-latte/roasted-coconut-latte.json",
  "identifier": "rl-29ab8cf9",
  "name": "Roasted Coconut Latte",
  "description": "Roasted at approximately 135°C for a unique coconut sugar flavor, suitable for winter consumption. This drink combines coconut pulp juice and roasted coconut granules, offering five 'zero' light enjoyment health options, using master-customized Espresso from IIAC gold award coffee beans.",
  "brand": {
    "type": "Brand",
    "name": "Luckin Coffee"
  },
  "additionalProperty": [
    {
      "type": "PropertyValue",
      "name": "Feature",
      "value": "Coconut pulp juice & roasted coconut granules blend, five 'zero' light enjoyment (0 lactose, 0 creamer, 0 sucrose solids, 0 trans fats, 0 added flavors), master-customized Espresso from IIAC gold award coffee beans"
    },
    {
      "type": "PropertyValue",
      "name": "Slogan",
      "value": "Winter Special Drink Warm Return"
    },
    {
      "type": "PropertyValue",
      "name": "Additional Info",
      "value": "Coconut flavor from memory"
    }
  ],
  "offers": {
    "type": "Offer",
    "price": "13",
    "priceCurrency": "CNY",
    "availability": "https://schema.org/InStock"
  },
  "nutrition": {
    "type": "NutritionInformation",
    "calories": "150",
    "fatContent": "0g",
    "sugarContent": "0g",
    "proteinContent": "0g",
    "cholesterolContent": "0mg",
    "carbohydrateContent": "0g"
  },
  "ingredients": "Coconut milk, espresso, roasted coconut syrup",
  "category": "Beverage",
  "sku": "LK-COCONUT-LATTE",
  "image": [
    {
      "type": "ImageObject",
      "url": "https://agent-network-protocol.com/agents/lkcoffe/roasted-coconut-latte/instruction.jpg",
      "caption": "Roasted Coconut Latte - Winter Special Drink Warm Return",
      "description": "Using 135°C high-temperature roasting process, perfectly blending coconut pulp juice and roasted coconut granules, paired with Espresso made from IIAC gold award coffee beans, bringing a unique blend of roasted coconut aroma and coffee aroma"
    },
    {
      "type": "ImageObject",
      "url": "https://agent-network-protocol.com/agents/lkcoffe/roasted-coconut-latte/feature.jpg",
      "caption": "Roasted Coconut Latte - Coconut flavor from memory",
      "description": "Coconut flavor from memory"
    }
  ],
  "audience": {
    "type": "Audience",
    "audienceType": "Coffee Enthusiasts",
    "geographicArea": "China"
  },
  "manufacturer": {
    "type": "Organization",
    "name": "Luckin Coffee",
    "url": "https://luckincoffee.com"
  },
  "customizationOptions": {
    "type": "CustomizationOptions",
    "options": [
      {
        "type": "PropertyValue",
        "name": "Temperature",
        "isRequired": true,
        "value": ["Iced", "Hot"]
      },
      {
        "type": "PropertyValue",
        "name": "Sugar Level",
        "isRequired": true,
        "value": ["Standard Sweet", "Less Sweet", "Slightly Sweet", "No Additional Sugar"]
      }
    ]
  }
}


```

备注：产品描述中，image中的属性可以放到一个数组中，来表示多个值，这也是符合schema.org的规范的。

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

表1：智能体级别的词汇术语。以下术语可以用于子文档中。

| 词汇术语 | 描述 | 是否必需 | 类型 |
|---------|------|---------|------|
| protocolType | 协议类型标识，固定值为"ANP"。 | 必需 | string |
| protocolVersion | 协议版本信息。 | 必需 | string |
| type | 对象类型标识，用于为对象添加语义标签。 | 必需 | string |
| url | 智能体的URL标识符，采用URI [RFC3986]格式（如稳定URI、临时和可变URI、带本地IP地址的URI、URN等）。 | 可选 | anyURI |
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
| proof | 完整性校验信息，防止AD文档被篡改 | 可选 | Proof |

对于protocolType和protocolVersion，AD实例定义了以下规则：

1. protocolType 必须设置为"ANP"以标识文档为ANP协议的智能体描述文档。
2. protocolVersion 必须指定当前使用的ANP协议版本号。
3. type 字段用于标识文档类型，对于智能体描述文档应设置为"AgentDescription"。
4. url 字段用于标识智能体的网络位置，采用URI格式。

##### Interface（接口）
接口定义了与智能体进行交互的方式。基本接口类型包括：

1. StructuredInterface：结构化接口，用于通过特定的API协议与智能体交互
2. NaturalLanguageInterface：自然语言接口，用于通过自然语言与智能体交互


表5：接口级别的词汇术语

| 词汇术语 | 描述 | 是否必需 | 类型 |
|---------|------|---------|------|
| type | 接口类型。 | 必需 | string |
| url | 接口定义文档的URL。 | 必需 | anyURI |
| name | 接口名称。 | 可选 | string |
| description | 接口的详细描述信息。 | 可选 | string |
| protocol | 接口使用的协议，当前支持YAML、JSON-RPC 2.0。 | 必需 | string |
| version | 接口版本信息。 | 可选 | string |
| security | 接口的安全要求。 | 可选 | SecurityScheme |
| humanAuthorization | 接口是否需要人类手动授权 | 可选 | bool |

### 安全机制

智能体描述协议当前使用did:wba方法作为其安全机制。did:wba方法是一种基于Web的去中心化标识符（DID）规范，旨在满足跨平台身份认证和智能体通信的需求。

未来可以根据需求扩展其他的身份认证方案。

#### DIDWBASecurityScheme（DID WBA安全方案）

描述基于did:wba方法的安全机制配置的元数据。分配给scheme名称的值必须在智能体描述中包含的词汇表中定义。

对于所有安全方案，任何密钥、密码或其他直接提供访问权限的敏感信息都不得存储在AD中，而应通过其他机制以带外方式共享和存储。AD的目的是描述如何访问智能体（如果消费者已经获得授权），而不是用于授予该授权。

安全方案通常需要额外的认证参数，例如数字签名等。这些信息的位置由与name关联的值指示，通常与in的值结合使用。与in关联的值可以采用以下值之一：

- header：参数将在协议提供的头部中给出，头部的名称由name的值提供。在did:wba方法中，身份验证信息通过Authorization头部传递。
- query：参数将作为查询参数附加到URI，查询参数的名称由name提供。
- body：参数将在请求负载的主体中提供，使用的数据模式元素由name提供。
- cookie：参数存储在由name值标识的cookie中。
- uri：参数嵌入在URI本身中，由相关交互中定义的URI模板变量（由name的值定义）进行编码。
- auto：位置作为协议的一部分确定或协商。如果SecurityScheme的in字段设置为auto值，则不应设置name字段。

表2：安全方案级别的词汇术语

| 词汇术语 | 描述 | 是否必需 | 类型 |
|---------|------|---------|------|
| type | 对象类型标识，用于为对象添加语义标签。 | 可选 | string |
| description | 基于默认语言提供额外的（人类可读）信息。 | 可选 | string |
| scheme | 安全机制的标识 | 必需 | string |
| in | 认证参数的位置。 | 必需 | string |
| name | 认证参数的名称。 | 必需 | string |

以下是一个使用did:wba方法的安全配置示例：

```json
{
    "securityDefinitions": {
        "didwba_sc": {
            "scheme": "didwba",
            "in": "header",
            "name": "Authorization"
        }
    },
    "security": "didwba_sc"
}
```

AD中的安全配置是必需的。必须通过智能体级别的security成员激活安全定义。此配置是与智能体交互所需的安全机制。

当security出现在AD文档的顶层时，表示所有的资源在访问是必须使用此安全机制进行验证。出现在某个资源内部时，表示只有在满足此安全机制的情况下才能访问该资源。如果顶层指定的security和资源中指定的security不相同，以资源中指定的security为准。

### 人类手动授权

如果一个接口在调用的时候，必须经过人类的手动授权，比如购买接口。这个时候可以在接口定义中添加字段humanAuthorization。true表示接口调用需要经过人类的手动授权才能够访问。

### Proof（完整性校验）

为了防止AD文档被恶意篡改、假冒或重复使用，我们在AD文档中增加了校验信息Proof。Proof定义可以参考规范：[https://www.w3.org/TR/vc-data-integrity/#defn-domain](https://www.w3.org/TR/vc-data-integrity/#defn-domain)。

其中：
- domain: 定义了AD文档的存储的域名。使用者在获得文档后，必须要判断获得文档的域名是否与domain中定义的域名相同。如果不相同，则此文档可能是假冒的。
- challenge: 定义了校验的挑战信息，用于防止篡改。在指定domain的时候，需要同时指定challenge。
- verificationMethod：定义了校验的方法，当前使用的是did:wba文档中的验证方法。未来可以扩展更多的方法。
- proofValue: 携带数字签名。生成规则如下：
  - 生成不含有proofValue字段的网站的AD文档
  - 使用[JCS(JSON Canonicalization Scheme)](https://www.rfc-editor.org/rfc/rfc8785)对上面的AD文档进行规范化，生成规范化字符串。
  - 使用SHA-256算法对规范化字符串进行哈希，生成hash值。
  - 使用客户端的私钥对hash值进行签名，生成签名值，并进行URL 安全的Base64编码。
  - 签名校验过程是上面过程的反向操作。


## 常用定义规范化

对于一个具体的产品或服务，比如一杯咖啡、一个玩具，可以使用schema.org的Product属性的子集，定义一个特定的类型，明确产品的描述方式。这样所有智能体在构造产品数据的时候，都可以使用统一的定义，以便在不同的智能体之间进行互操作。

对于接口也可以使用类似的方式。比如产品购买接口，我们可以定义一个统一购买接口规范，所有的智能体都可以使用统一的购买接口，以便在不同的智能体之间进行互操作。






## 版权声明  
Copyright (c) 2024 GaoWei Chang  
本文件依据 [MIT 许可证](./LICENSE) 发布，您可以自由使用和修改，但必须保留本版权声明。  
