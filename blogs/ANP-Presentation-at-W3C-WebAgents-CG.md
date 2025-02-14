
# Presentation on ANP at W3C-WebAgents-CG

On February 14, 2025, Chang Gaowei and James Waugh, representing the AgentNetworkProtocol (ANP) open-source community, delivered a presentation on ANP at the W3C WebAgents CG meeting.

The W3C WebAgents community focuses on designing web-based multi-agent systems (MAS) with the aim of developing a new type of MAS that is consistent with the web architecture. This MAS will inherit the global, open, and persistent characteristics of the web, while ensuring transparency and traceability to gain widespread acceptance. The community is particularly focused on using linked data and semantic web standards to create a hypermedia structure (hMAS) that enables unified interaction among diverse entities such as people, AI, devices, and digital services. Community website: [https://www.w3.org/community/webagents/](https://www.w3.org/community/webagents/).

ANP's technical philosophy aligns with many aspects of the WebAgents community, and similarly values linked data and semantic web technologies. During its design process, ANP also referenced discussions from the WebAgents community. This presentation introduced our thoughts and practices regarding ANP to the WebAgents community.

The presentation was jointly delivered by Chang Gaowei and James Waugh. Below are the presentation slides and script, as well as the topics discussed during the meeting.

## Presentation Content

PDF document：[ANP-Presentation-at-W3C-WebAgents-cg.pdf](../ANP-Presentation-at-W3C-WebAgents-cg.pdf)

### Page 1

![Page 1](../images/anp-in-w3c-20250214/page1.jpg)

Hello everyone! I'm XXX from the ANP Open Source Community. I'm honored to be here today to share with you about the Agent Network Protocol (ANP) project.

Our vision is to create "the HTTP protocol for the Agentic Web era". We are committed to defining how agents connect and communicate with each other, building an open, secure, and efficient collaboration network for intelligent agents.


### Page 2

![Page 2](../images/anp-in-w3c-20250214/page2.jpg)

Today's talk will cover several parts:
- First, we'll introduce the core assumptions of our ANP design, which form the basis of our thoughts and our vision for the future web.
- Next, we'll present the design of ANP's identity authentication scheme and how to use it for identity verification.
- Then, we'll discuss ANP's agent description scheme and how to use the agent description protocol to build a data network that is convenient for AI access.
- Finally, we'll showcase our demo

### Page 3

![Page 3](../images/anp-in-w3c-20250214/page3.jpg)

Let's first explore why we designed ANP. In the future Agentic Web era, we believe that agents will fundamentally transform how the internet is used. Personal assistants will replace humans in accessing the internet, while enterprise services will be taken over by agents. More importantly, these personal assistants are agents themselves, capable of directly connecting and interacting with other agents.

### Page 4

![Page 4](../images/anp-in-w3c-20250214/page4.jpg)

Our second core assumption is: Agents must be interconnected. The current data silos on the internet significantly hinder AI's full potential. To maximize AI capabilities, we need to ensure AI has access to complete contextual information and all tool capabilities. Moreover, the connectivity between agents will be far greater than the traditional internet.

### Page 5

![Page 5](../images/anp-in-w3c-20250214/page5.jpg)

Our third core assumption is: Agents should interact with each other through protocols. Direct processing of underlying data through protocols is the most efficient way for AI to interact with the internet. The current technology of Computer Use is transitional, and standardized agent communication protocols will emerge in the future - which is exactly what we are working on.

### Page 6

![Page 6](../images/anp-in-w3c-20250214/page6.jpg)

Based on these three core assumptions, we present ANP's goal: to become the HTTP/HTML of the Agentic Web era. Just as HTTP/HTML defined how humans access the internet, ANP will define how agents access the internet.

Our vision is to define the connectivity between agents and build an open, secure, and efficient collaboration network for billions of agents. This is not just a protocol - it's the infrastructure for the future internet of agents.

### Page 7

![Page 7](../images/anp-in-w3c-20250214/page7.jpg)

To achieve this vision, we've designed ANP with a three-layer architecture:

First, the Identity and Encrypted Communication Layer: Based on W3C DID, it builds a decentralized identity authentication solution with excellent scalability, capable of supporting billions of users.

Second, the Meta-Protocol Layer: A protocol for negotiating communication protocols between agents. It is key to evolving the agent network into an autonomous, self-negotiating, and highly efficient collaboration network.

Finally, the Application Protocol Layer: Based on Semantic Web standards, it enables agents to describe their public information, available capabilities, and supported interfaces. Other agents can discover and interact with them using this information. Today, we will focus on the identity layer and application layer.

### Page 8

![Page 8](../images/anp-in-w3c-20250214/page8.jpg)

Let's look at the goals and principles of agent identity design. Our core goal is simple: to enable all agents to authenticate each other's identity.

To achieve this goal, we follow three principles: Decentralization - identity should not be provided by a few vendors; Interoperability - identities between different systems should be easily authenticated with each other; and Scalability - the system should support large-scale user usage.

### Page 9

![Page 9](../images/anp-in-w3c-20250214/page9.jpg)

I believe everyone here is familiar with W3C DID. DID (Decentralized Identifier) is a user-controlled, self-sovereign digital identity identifier widely used in decentralized systems. It became a W3C Recommendation in 2022.

We chose DID as the foundation for our agent identity solution precisely because of its decentralization, interoperability, and privacy-security features, which align perfectly with our design principles.

### Page 10

![Page 10](../images/anp-in-w3c-20250214/page10.jpg)

We designed the Web-Based Agent DID method with practicality as our core principle.

First, we don't pursue complete decentralization, but prioritize feasibility. Second, we reuse existing web infrastructure to reduce implementation costs. Finally, we build upon the existing did:web method, adding agent-related features.

For example, did:wba:example.com:user:alice resolves to https://example.com/user/alice/did.json, making it simple and intuitive.

### Page 11

![Page 11](../images/anp-in-w3c-20250214/page11.jpg)

Let's look at the CRUD operations of did:wba. A key feature is that Create, Update, and Deactivate operations are performed internally within the system, while Read operations are cross-system.

For instance, when Alice's agent needs to access Bob's DID document, it simply makes an HTTP GET request. This design fully utilizes existing web infrastructure, capable of serving billions of users, and achieves decentralization and interoperability of agent identities.

### Page 12

![Page 12](../images/anp-in-w3c-20250214/page12.jpg)

Let's examine the identity verification process of did:wba. The process consists of three phases: initial subscription, first request, and subsequent requests.

First, A subscribes to B's service, and B records A's DID. In the first HTTP request, A includes its DID and signature in the header. Upon receiving the request, B retrieves A's DID document which contains A's public key, and uses it to verify the signature. After successful verification, B returns an access token. For subsequent requests, A only needs to use this token.

### Page 13

![Page 13](../images/anp-in-w3c-20250214/page13.jpg)

In terms of identity authentication technology, we still have several issues to explore.

First is the user permissions issue: How can we implement more granular permission control, instead of using a single ID for communication with all agents?

Second is the user authorization issue: How can we determine whether a request has been manually authorized by the user? Some sensitive actions should not be initiated autonomously by the agent.

Finally, there's the identity sovereignty issue: How can we ensure that users have full ownership of their identity, rather than relying on permissions granted by the platform?

### Page 14

![Page 14](../images/anp-in-w3c-20250214/page14.jpg)

Let's move on to another crucial module of ANP: the Agent Description Protocol (ADP).

What is ADP? It's a protocol used to define the Agent Description Document. This document serves as the agent's "homepage", similar to a website's homepage, through which all functionalities of the agent can be accessed.

What does an agent description document contain? It includes the identity of the entity to which the agent belongs, the owner, authentication methods, external interfaces, and public information. For example, if the agent represents a coffee shop, its public information would include location, business hours, product list, purchase interface, and other related details.

### Page 15

![Page 15](../images/anp-in-w3c-20250214/page15.jpg)

ADP design is based on three core principles.

First is AI-Oriented Design: The protocol is specifically designed for AI, making it easier for AI to understand and access.

Second is Semi-Structured Protocol: Overall, it adopts a structured design for programmatic processing, while fields can contain natural language for conveying personalized information.

Third is Multi-Agent Consensus: Enhances consistency in how agents understand data semantics.

In theory, ADP could entirely use natural language if the intelligence is strong enough. However, this approach currently has many drawbacks, such as cost and error probability.

### Page 16

![Page 16](../images/anp-in-w3c-20250214/page16.jpg)

Let's examine the specific design scheme of ADP.

First is the adoption of Linked-Data technology. We use this to link together all information about agents. The agent description document serves as an entry point, from which all related information can be traversed. We choose Json-LD as our primary document format.

Second is the application of Schema.org. The fields in Json-LD extensively use predefined fields from Schema.org. For undefined fields, we add definitions. This ensures consistency in how multiple agents interpret the same field while making it easier for programmatic processing.

Finally, the specification is divided into two parts: the core ADP specification and domain examples. The core specification describes ADP's basic framework and structure, while the domain examples provide AD document examples for various domains, such as a coffee shop AD document, which other agents can reference to generate their own.
### Page 17

![Page 17](../images/anp-in-w3c-20250214/page17.jpg)

Let's understand ADP through a concrete coffee shop AD document example. This document contains four important custom modules.

First is the identity authentication module (ad:securityDefinitions), which defines how authentication is performed using did:wba.

Second is the external interfaces module (ad:interfaces), which includes API definitions for natural language interaction and purchase interfaces.

Third is the domain entity module (ad:domainEntity), which describes the coffee shop information corresponding to this agent, such as name and address.

Fourth is the products module (ad:products), which lists the products offered by the coffee shop.

### Page 18

![Page 18](../images/anp-in-w3c-20250214/page18.jpg)

Let's look at the interaction flow of ADP.

First, users interact with other agents through their own agent. Once a user's agent has another agent's DID, it can find that agent's AD document URL in the DID document. Based on the AD document, the user's agent knows what capabilities the other agent provides and which protocols to use for interaction.

This means that as long as you have a DID, you can find the corresponding agent description document. And as long as you have the agent description document, you can interact with the agent.

In the future, we believe there will be a data network specifically designed for AI, making it easier for AI to access information.

### Page 19

![Page 19](../images/anp-in-w3c-20250214/page19.jpg)

Regarding ADP, there are two more important design considerations.

First is supporting ADP during LLM training. AD specifications, along with examples and interfaces from various industries, can be incorporated into the LLM through training data or fine-tuning. This enhances the LLM's speed and accuracy in processing ADP and reduces the length of prompts required.

Second is that agents can independently define and upload AD document examples for reference by other agents. Interestingly, the specification examples defined by agents may surpass those defined by humans.

### Page 20

![Page 20](../images/anp-in-w3c-20250214/page20.jpg)

Next, we will demonstrate how ANP works through a real-world scenario.

We will use a coffee ordering scenario to show how a personal assistant interacts with a coffee shop's agent using DID and Agent Description documents.

This demonstration will showcase the complete workflow of the ANP protocol, including agent discovery, identity verification, capability querying, and business interaction.

### Page 21

![Page 21](../images/anp-in-w3c-20250214/page21.jpg)

We have completed the open-source implementation of ANP, including identity and end-to-end encryption modules, meta-protocol modules, and ADP modules. You are welcome to visit and use it on GitHub.

### Page 22 Thanks

![Page 22](../images/anp-in-w3c-20250214/page22.jpg)

I would like to especially thank the historical meeting records of WebAgents, which provided valuable resources and inspiration for our design.

## Q&A 

### What is Not Pursuing Complete Decentralization

We believe that blockchain solutions represent complete decentralization, with no centralized modules in the entire structure. However, the scalability challenges of blockchain currently lack a good solution.

Therefore, the decentralization we pursue is not like blockchain's complete decentralization but more like email's decentralization. Any email account can send and receive emails with any other email account. Email service providers are centralized, but the entire business is decentralized, allowing communication between any accounts while serving billions of users.

Our decentralization design philosophy is the same as email. I believe this is the most suitable solution at this stage.

### JSON-LD to TTL/RDF Mapping Issue

**Detailed Question:** Do you have a JSON-LD to TTL/RDF mapping? In my view, JSON-LD designs usually have issues related to unrecognized blank nodes.

**Answer (supplemental response):** We currently do not have a JSON-LD to TTL/RDF mapping. We mainly use JSON-LD for its two capabilities:
- Data connectivity: It can connect data into a network that is easy for AI to access, rather than a network designed for humans.
- Semantic understanding consistency: By using Schema.org, which is already defined by semantic web technologies, we enhance semantic understanding consistency among different agents.

### How to Ensure Consistency in Data Understanding

**Detailed Question:** You mentioned coffee, how do you ensure that two agents have a consistent understanding of coffee?

**Answer:** In fact, even if we do nothing, agents currently can maintain a consistent understanding of coffee in 99% of scenarios. What we need to do is further enhance semantic understanding consistency to ensure consistent understanding of coffee between two agents.

The specific approach is to use a lot of Schema.org fields, already defined by the current semantic web, in the JSON-LD design of the agent description specification. This ensures that multiple agents have consistent understanding of the same fields and makes program processing easier.

If a field is undefined, we will redefine it and use Schema.org's definitions, our definitions, and our specifications as pre-training materials for LLMs to learn. This way, two LLMs can maintain consistent understanding of the same field.

### Can Agents Access IoT Devices

**Detailed Question:** Can agents access IoT devices?

**Answer:** Theoretically, they can. As long as the interfaces of IoT devices are defined and the interface descriptions are placed in the ADP (Agent Description Protocol) document, AI can understand and initiate schemes for IoT devices.

### HTTP and OpenAPI May Not Be Better Transmission Protocols

**Detailed Question:** In IoT scenarios, HTTP and OpenAPI may not be better transmission protocols, especially when facing asynchronous communication.

**Answer:** Yes. ANP theoretically has no requirements for the transport layer protocol. It is currently carried over HTTP, WSS, and can also be used with other protocols. However, the underlying protocol needs some modifications. For example, currently, HTTP authentication information is carried in the HTTP header, and using other protocols requires designing a new authentication scheme.

### How to Use Existing API Interfaces, Such as Existing OpenAPI Specifications

**Detailed Question:** In the agent description specification, can existing interfaces, such as existing OpenAPI interfaces, be used?

**Answer (supplemental response):** Yes. In the agent description specification, the interfaces provided by agents for external access are an open design. Existing specification interfaces, such as OpenAPI interface documents, can be placed in the agent description specification. AI can understand and initiate calls to these interfaces.

This is one situation. I think a more exciting situation is that two agents can negotiate the interfaces they want to use for communication and share the negotiated interfaces as standards with other agents. This is the role of the meta-protocol.

### Why Does the Agent Represent a Coffee Shop Instead of a Server

**Detailed Question (post-meeting question):** In the example, the agent represents a coffee shop, not a server?

**Answer:** An agent can represent any entity, including a person, organization, sub-organization within an organization, or even an object. In the example, the agent represents a coffee shop because our scenario is a person purchasing a cup of coffee, and the interaction object is the coffee shop. A person's agent can interact with the coffee shop's agent through natural language to solve after-sales issues or personalization issues. In this case, a structured API cannot solve the problem, and a personalized natural language interface is needed.

## Contact Us

If you are interested in this topic, feel free to contact us:

- Discord: [https://discord.gg/sFjBKTY7sB](https://discord.gg/sFjBKTY7sB)  
- Website: [https://agent-network-protocol.com/](https://agent-network-protocol.com/)  
- GitHub: [https://github.com/chgaowei/AgentNetworkProtocol](https://github.com/chgaowei/AgentNetworkProtocol)

