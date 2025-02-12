
# ANP W3C Talk Script / ANP W3C 演讲稿

## Page 1 

大家好！我是XXX，来自ANP开源社区。今天非常荣幸能在这里跟大家分享Agent Network Protocol（简称ANP）项目。

我们的愿景是打造"Agentic Web时代的HTTP协议"。我们致力于定义Agent之间如何互联互通，构建一个开放、安全、高效的智能体协作网络。

Hello everyone! I'm XXX from the ANP Open Source Community. I'm honored to be here today to share with you about the Agent Network Protocol (ANP) project.

Our vision is to create "the HTTP protocol for the Agentic Web era". We are committed to defining how agents connect and communicate with each other, building an open, secure, and efficient collaboration network for intelligent agents.


## Page 2

今天的演讲分几部分：
- 首先介绍下我们设计ANP的核心假设是什么，这是我们的基础与核心思考，也是我们对未来web的设想。
- 然后介绍下ANP身份认证的方案设计，以及如何使用它来进行身份认证。
- 接下来介绍下ANP的智能体描述方案，以及如何使用智能体描述协议，构建一个便于AI访问的数据网络。
- 最后展示下我们的demo

Today's talk will cover several parts:
- First, we'll introduce the core assumptions of our ANP design, which form the basis of our thoughts and our vision for the future web.
- Next, we'll present the design of ANP's identity authentication scheme and how to use it for identity verification.
- Then, we'll discuss ANP's agent description scheme and how to use the agent description protocol to build a data network that is convenient for AI access.
- Finally, we'll showcase our demo

## Page 3

让我们先来看看为什么要设计ANP。在未来的Agentic Web时代，我们认为智能体将彻底改变互联网的使用方式。个人助手将替代人类访问互联网，企业服务也将被智能体取代。更重要的是，这些个人助手本身就是智能体，它们会直接与其他智能体进行连接和交互。

Let's first explore why we designed ANP. In the future Agentic Web era, we believe that agents will fundamentally transform how the internet is used. Personal assistants will replace humans in accessing the internet, while enterprise services will be taken over by agents. More importantly, these personal assistants are agents themselves, capable of directly connecting and interacting with other agents.

## Page 4

第二个核心假设是：智能体必须实现互联互通。当前互联网上的数据孤岛严重阻碍了AI的发展潜力。为了充分发挥AI的能力，我们需要确保AI能够获取完整的上下文信息，访问所有工具能力。更重要的是，智能体之间的连接度将远超过去的互联网。

Our second core assumption is: Agents must be interconnected. The current data silos on the internet significantly hinder AI's full potential. To maximize AI capabilities, we need to ensure AI has access to complete contextual information and all tool capabilities. Moreover, the connectivity between agents will be far greater than the traditional internet.

## Page 5

第三个核心假设是：智能体之间应该通过协议来交互。让AI通过协议直接处理底层数据，是其与互联网交互最高效的方式。当前的Computer Use方案只是一种过渡形态，未来会出现标准化的智能体通信协议，这正是我们正在做的事情。

Our third core assumption is: Agents should interact with each other through protocols. Direct processing of underlying data through protocols is the most efficient way for AI to interact with the internet. The current technology of Computer Use is transitional, and standardized agent communication protocols will emerge in the future - which is exactly what we are working on.

## Page 6

基于这三个核心假设，我们提出了ANP的目标：打造Agentic Web时代的HTTP/HTML。就像HTTP/HTML定义了人类如何访问互联网一样，ANP将定义智能体如何访问互联网。

我们的愿景是：定义智能体之间的连接方式，为数以亿计的智能体构建一个开放、安全、高效的协作网络。这不仅仅是一个协议，而是未来智能体互联网的基础设施。

Based on these three core assumptions, we present ANP's goal: to become the HTTP/HTML of the Agentic Web era. Just as HTTP/HTML defined how humans access the internet, ANP will define how agents access the internet.

Our vision is to define the connectivity between agents and build an open, secure, and efficient collaboration network for billions of agents. This is not just a protocol - it's the infrastructure for the future internet of agents.

## Page 7

为了实现这个愿景，我们设计了ANP的三层架构：

首先是身份与加密通信层：基于W3C DID标准，我们构建了一个去中心化的身份认证方案，具有出色的扩展性，能支持数十亿用户规模。

其次是元协议层：这是一个用于协商智能体之间通信协议的协议，是智能体网络进化为自组织、自协商、高效协作网络的关键。

最后是应用协议层：基于语义网标准，使智能体能够描述自己的公开信息、可用能力和支持的接口，其他智能体可以据此发现并与之交互。今天我们将重点介绍身份层和应用层。

To achieve this vision, we've designed ANP with a three-layer architecture:

First, the Identity and Encrypted Communication Layer: Based on W3C DID, it builds a decentralized identity authentication solution with excellent scalability, capable of supporting billions of users.

Second, the Meta-Protocol Layer: A protocol for negotiating communication protocols between agents. It is key to evolving the agent network into an autonomous, self-negotiating, and highly efficient collaboration network.

Finally, the Application Protocol Layer: Based on Semantic Web standards, it enables agents to describe their public information, available capabilities, and supported interfaces. Other agents can discover and interact with them using this information. Today, we will focus on the identity layer and application layer.

## Page 8

让我们先来看看智能体身份设计的目标与原则。我们的核心目标很简单：让所有智能体都能够相互认证对方的身份。

为了实现这个目标，我们遵循三个原则：去中心化，身份不应由少数厂商提供；互操作性，不同系统间的身份应该能够轻松地相互认证；可扩展性，系统应能支持大规模用户使用。

Let's look at the goals and principles of agent identity design. Our core goal is simple: to enable all agents to authenticate each other's identity.

To achieve this goal, we follow three principles: Decentralization - identity should not be provided by a few vendors; Interoperability - identities between different systems should be easily authenticated with each other; and Scalability - the system should support large-scale user usage.

## Page 9

相信在座的各位对W3C DID都不陌生。DID全称Decentralized Identifier，是一种用户自主管理、自主控制的数字身份标识符，在去中心化系统中广泛应用。它于2022年成为W3C正式推荐标准。

我们选择DID作为智能体身份方案的基础，正是看中了它的去中心化、互操作性和隐私安全特性，这与我们的设计原则不谓而合。

I believe everyone here is familiar with W3C DID. DID (Decentralized Identifier) is a user-controlled, self-sovereign digital identity identifier widely used in decentralized systems. It became a W3C Recommendation in 2022.

We chose DID as the foundation for our agent identity solution precisely because of its decentralization, interoperability, and privacy-security features, which align perfectly with our design principles.

## Page 10

我们设计了Web-Based Agent DID方法，其核心设计原则是务实可行。

首先，我们不追求完全去中心化，而是将可行性放在首位。其次，我们重用现有的Web基础设施，以降低实现成本。最后，我们基于现有的did:web方法进行扩展，增加了智能体相关特性。

比如，did:wba:example.com:user:alice就会解析到https://example.com/user/alice/did.json，这种方式简单直观。

We designed the Web-Based Agent DID method with practicality as our core principle.

First, we don't pursue complete decentralization, but prioritize feasibility. Second, we reuse existing web infrastructure to reduce implementation costs. Finally, we build upon the existing did:web method, adding agent-related features.

For example, did:wba:example.com:user:alice resolves to https://example.com/user/alice/did.json, making it simple and intuitive.

## Page 11

让我们来看看did:wba的CRUD操作。这里有个重要特点：创建、更新、停用这三个操作都是在系统内部进行的，而读取操作是跨系统的。

比如，当Alice的智能体要访问Bob的DID文档时，只需发起一个HTTP GET请求就可以了。这种设计充分利用了现有的Web基础设施，能够支持数十亿用户规模，并实现了智能体身份的去中心化和互操作性。

Let's look at the CRUD operations of did:wba. A key feature is that Create, Update, and Deactivate operations are performed internally within the system, while Read operations are cross-system.

For instance, when Alice's agent needs to access Bob's DID document, it simply makes an HTTP GET request. This design fully utilizes existing web infrastructure, capable of serving billions of users, and achieves decentralization and interoperability of agent identities.

## Page 12

让我们来看看did:wba的身份认证流程。整个过程分为三个阶段：初始订阅、首次请求和后续请求。

首先，A调用API订阅B的服务，B记录A的DID。然后在首次HTTP请求时，A在请求头中包含其DID和签名。B收到请求后，会获取A的DID文档，DID文档中包含有A的公钥，B使用A的公钥验证签名。验证成功后，B会返回一个访问令牌。在后续请求中，A只需使用这个令牌即可。

Let's examine the identity verification process of did:wba. The process consists of three phases: initial subscription, first request, and subsequent requests.

First, A subscribes to B's service, and B records A's DID. In the first HTTP request, A includes its DID and signature in the header. Upon receiving the request, B retrieves A's DID document which contains A's public key, and uses it to verify the signature. After successful verification, B returns an access token. For subsequent requests, A only needs to use this token.

## Page 13

在身份认证技术上，我们还有一些待探索的问题。

首先是用户权限问题：如何实现更细粒度的权限控制，而不是使用单一ID与所有智能体通信？

其次是用户授权问题：如何判断一个请求是否由用户手动授权？某些敏感操作不应由智能体自主发起。

最后是身份主权问题：如何确保用户对其身份有完全的所有权，而不是依赖于平台授予的权限？

In terms of identity authentication technology, we still have several issues to explore.

First is the user permissions issue: How can we implement more granular permission control, instead of using a single ID for communication with all agents?

Second is the user authorization issue: How can we determine whether a request has been manually authorized by the user? Some sensitive actions should not be initiated autonomously by the agent.

Finally, there's the identity sovereignty issue: How can we ensure that users have full ownership of their identity, rather than relying on permissions granted by the platform?

## Page 14

让我们进入ANP的另一个重要模块：Agent Description Protocol（ADP）。

什么是ADP？它是用来定义智能体描述文档的协议。这个文档可以被看作是智能体的“主页”，就像网站的主页一样，通过它可以访问智能体的所有功能。

一个智能体描述文档包含哪些内容？它包含了智能体所属实体的身份、所有者、认证方式、外部接口以及公开信息。比如，如果这个智能体代表一家咖啡店，那么它的公开信息就会包括地点、营业时间、产品列表、购买接口等信息。

Let's move on to another crucial module of ANP: the Agent Description Protocol (ADP).

What is ADP? It's a protocol used to define the Agent Description Document. This document serves as the agent's "homepage", similar to a website's homepage, through which all functionalities of the agent can be accessed.

What does an agent description document contain? It includes the identity of the entity to which the agent belongs, the owner, authentication methods, external interfaces, and public information. For example, if the agent represents a coffee shop, its public information would include location, business hours, product list, purchase interface, and other related details.

## Page 15

ADP的设计基于三个核心原则。

第一是AI导向设计：协议专门为AI设计，使其更容易被AI理解和访问。

第二是半结构化协议：总体上采用结构化设计，便于程序处理；同时字段可以包含自然语言，便于传递个性化信息。

第三是多智能体共识：增强智能体之间对数据语义的理解一致性。

理论上，只要智能水平足够高，ADP可以完全使用自然语言。但这种方法在当前阶段有许多缺点，如成本、错误率等。

ADP design is based on three core principles.

First is AI-Oriented Design: The protocol is specifically designed for AI, making it easier for AI to understand and access.

Second is Semi-Structured Protocol: Overall, it adopts a structured design for programmatic processing, while fields can contain natural language for conveying personalized information.

Third is Multi-Agent Consensus: Enhances consistency in how agents understand data semantics.

In theory, ADP could entirely use natural language if the intelligence is strong enough. However, this approach currently has many drawbacks, such as cost and error probability.

## Page 16

让我们来看看ADP的具体设计方案。

首先是Linked-Data技术的采用。我们使用这个技术将智能体的信息连接在一起。智能体描述文档作为入口点，可以遍历到所有相关信息。我们选择Json-LD作为主要文档格式。

其次是Schema.org的应用。Json-LD中的字段大量使用Schema.org的预定义字段。如果遇到未定义的字段，我们会添加定义。这样可以确保多个智能体对同一字段的理解一致，并且更利于程序处理。

最后，规范分为两部分：核心ADP规范和领域示例。核心规范描述了ADP的基本框架和结构，而领域示例部分则提供了各个领域的AD文档示例，比如咖啡店的AD文档，其他智能体可以参考这些示例来生成自己的文档。

Let's examine the specific design scheme of ADP.

First is the adoption of Linked-Data technology. We use this to link together all information about agents. The agent description document serves as an entry point, from which all related information can be traversed. We choose Json-LD as our primary document format.

Second is the application of Schema.org. The fields in Json-LD extensively use predefined fields from Schema.org. For undefined fields, we add definitions. This ensures consistency in how multiple agents interpret the same field while making it easier for programmatic processing.

Finally, the specification is divided into two parts: the core ADP specification and domain examples. The core specification describes ADP's basic framework and structure, while the domain examples provide AD document examples for various domains, such as a coffee shop AD document, which other agents can reference to generate their own.

## Page 17

让我们通过一个具体的咖啡店AD文档来理解ADP。这个文档包含四个重要的自定义模块。

第一个是身份认证信息模块（ad:securityDefinitions），定义了使用did:wba进行认证的方式。

第二个是外部接口模块（ad:interfaces），包含了自然语言交互和购买接口的API定义。

第三个是领域实体模块（ad:domainEntity），描述了该智能体对应的咖啡店信息，如名称、地址等。

第四个是产品信息模块（ad:products），列出了咖啡店提供的产品。

Let's understand ADP through a concrete coffee shop AD document example. This document contains four important custom modules.

First is the identity authentication module (ad:securityDefinitions), which defines how authentication is performed using did:wba.

Second is the external interfaces module (ad:interfaces), which includes API definitions for natural language interaction and purchase interfaces.

Third is the domain entity module (ad:domainEntity), which describes the coffee shop information corresponding to this agent, such as name and address.

Fourth is the products module (ad:products), which lists the products offered by the coffee shop.

## Page 18

让我们来看看ADP的交互流程。

首先，用户通过智能体与其他的智能体进行交互。用户的智能体有了另外一个智能体的DID后，可以在DID文档中找到它的智能体的AD文档的URL，根据AD文档，用户的智能体就知道，另外一个智能体提供了哪些能力，用什么样的协议交互。

这意味着只要有DID，就能找到相应的智能体描述文档。只要有智能体描述文档，就可以和智能体进行交互。

在未来，我们认为会出现一个数据网络，一个专门面向AI设计，使得AI更容易访问的数据网络。

Let's look at the interaction flow of ADP.

First, users interact with other agents through their own agent. Once a user's agent has another agent's DID, it can find that agent's AD document URL in the DID document. Based on the AD document, the user's agent knows what capabilities the other agent provides and which protocols to use for interaction.

This means that as long as you have a DID, you can find the corresponding agent description document. And as long as you have the agent description document, you can interact with the agent.

In the future, we believe there will be a data network specifically designed for AI, making it easier for AI to access information.

## Page 19

关于ADP，还有两个重要的设计考虑。

第一是在LLM训练中支持ADP。我们可以将AD规范以及各行业的示例和接口，通过训练数据或精调的方式引入到LLM中。这样可以提高LLM处理ADP的速度和准确性，减少所需的提示词长度。

第二是智能体可以自主定义和上传AD文档示例，供其他智能体参考。有趣的是，智能体定义的规范示例可能会超越人类定义的。

Regarding ADP, there are two more important design considerations.

First is supporting ADP during LLM training. AD specifications, along with examples and interfaces from various industries, can be incorporated into the LLM through training data or fine-tuning. This enhances the LLM's speed and accuracy in processing ADP and reduces the length of prompts required.

Second is that agents can independently define and upload AD document examples for reference by other agents. Interestingly, the specification examples defined by agents may surpass those defined by humans.

## Page 20

接下来，我们通过一个实际的场景来演示ANP的工作原理。

我们将通过一个咖啡点单的场景，来展示个人助理如何使用DID和智能体描述文档与咖啡店的智能体进行交互。

这个演示将展示整个ANP协议的工作流程，包括智能体发现、身份认证、能力查询和业务交互等环节。

Next, we will demonstrate how ANP works through a real-world scenario.

We will use a coffee ordering scenario to show how a personal assistant interacts with a coffee shop's agent using DID and Agent Description documents.

This demonstration will showcase the complete workflow of the ANP protocol, including agent discovery, identity verification, capability querying, and business interaction.

## Page 21

我们已经完成了ANP的开源实现，包括身份和端到端加密模块、元协议模块、ADP模块。欢迎大家在GitHub上访问和使用。

We have completed the open-source implementation of ANP, including identity and end-to-end encryption modules, meta-protocol modules, and ADP modules. You are welcome to visit and use it on GitHub.

## Page 22 Thanks

我要特别感谢WebAgents的历史会议记录，为我们的设计提供了宝贵的参考和灵感。

I would like to especially thank the historical meeting records of WebAgents, which provided valuable resources and inspiration for our design.

## Page 23 Finally

ANP目前还处于早期阶段，如果可能的话，我们希望能将ANP贡献给WebAgents，在WebAgents的框架下推进它的发展。

ANP is still in its early stages, and if possible, we are willing to contribute ANP and continue improving it together with everyone in WebAgents.

