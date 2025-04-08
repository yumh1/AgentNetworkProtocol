# Comparison of MCP and ANP: What Kind of Communication Protocol Do Agents Need?

**Core Ideas:**
- Building consumer-oriented personal assistants faces two bottlenecks: cost and information acquisition. The reasoning ability bottleneck is rapidly being resolved. A communication protocol for agents is needed to enable AI to access all information.
- Among current industry AI-related open-source communication protocols, Anthropic's MCP and our designed ANP are relatively complete in design and implementation.
- MCP and ANP differ significantly in protocol architecture, identity authentication, and information organization.
  - MCP is a typical Client-Server (CS) architecture, while ANP is a typical Peer-to-Peer (P2P) architecture.
  - MCP's identity authentication is based on the OAuth standard, facilitating client access to current internet resources. ANP's identity authentication is based on the W3C DID standard, focusing on cross-platform interoperability among agents, enabling seamless connectivity.
  - MCP organizes information using JSON-RPC technology, essentially API calls. ANP uses semantic web Linked-Data technology to build a data network that is easily accessible and understandable by AI.
- The biggest difference between MCP and ANP lies in their worldview:
  - MCP is model-centric, viewing the entire internet as its context and tool.
  - ANP is agent-centric, where each agent has equal status, forming a decentralized agent collaboration network.
- The type of communication protocol agents need depends on the future characteristics of the Agentic web. We have different views from MCP and are committed to the continuous development of ANP.

## Why Agent Communication Protocols Are Important

With the launch of Deepseek R1, OpenAI O3 Mini, and Deep Research, a clear trend emerges: the core bottleneck hindering agent construction—complex task reasoning capability—is rapidly disappearing.

Deep Research can essentially be considered a personal assistant for knowledge workers.

For consumer-oriented agents, two bottlenecks remain: cost, expected to decrease by one to two orders of magnitude by 2025, and information: how can personal assistants obtain sufficient information?

Information for knowledge workers is often stored in open databases or websites, easily accessible to AI. Consumer-oriented information is more complex, hindered by the current internet's data silo phenomenon, making information fragmented and poorly open.

How to enable personal assistants to efficiently and effectively obtain consumer-required information (tools can also be considered a form of information) is the problem that agent communication protocols aim to solve.

Note: For why communication protocols are needed instead of "Computer Use," refer to this article: [What Makes Agentic Web Different](./What-Makes-Agentic-Web-Different.md).

## Introduction to MCP and ANP

**MCP (Model Context Protocol):** An open protocol that enables LLM applications to seamlessly integrate with external data sources and tools. Whether building AI-driven IDEs, enhancing chat interfaces, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the necessary context. [MCP Specification](https://spec.modelcontextprotocol.io/)

**AgentNetworkProtocol (ANP):** An open protocol framework designed for the Agentic Web. ANP implements decentralized identity authentication, allowing any two agents to connect. It also designs an agent description specification for more efficient data exchange and collaboration among agents. [ANP on GitHub](https://github.com/agent-network-protocol/AgentNetworkProtocol)

In the current landscape of agent communication protocols, ANP is possibly the first open-source communication protocol specifically designed for agents on the internet. We initially released the code first, with the protocol documentation in Feishu, which was later migrated to GitHub.

If you know of other good open-source projects, feel free to introduce them to me.

## Differences Between MCP and ANP

Below, I will elaborate on the differences between MCP and ANP in three aspects: protocol architecture, identity authentication, and information organization, followed by the differences in design philosophy and the reasons behind them.

### Protocol Architecture: CS vs. P2P

#### MCP Protocol Architecture

MCP is a typical Client-Server architecture. Clients use the MCP protocol to connect to the MCP Server, then use the protocol to access various information and tool capabilities from the Server.

<p align="center">
  <img src="/blogs/images/mcp-architecture.png" width="50%" alt="mcp-architecture"/>
</p>

Client and Server can establish a bidirectional communication link via stdio or HTTP. When using HTTP, the Client sends messages using HTTP POST and receives server event notifications using HTTP SSE.

<p align="center">
  <img src="/blogs/images/mcp-http-sse.png" width="50%" alt="mcp-http-sse"/>
</p>

#### ANP Protocol Architecture

ANP is a typical Peer-to-Peer architecture, meaning any agent can use ANP to connect to another agent.

<p align="center">
  <img src="/blogs/images/anp-architecture.png" width="50%" alt="anp-architecture"/>
</p>

ANP currently uses the HTTP protocol at its core. An agent can connect to other agents using HTTP and also receive messages from other agents via HTTP. WebSocket and private transport layer protocols are theoretically supported.

The main reason for ANP's choice of P2P architecture is to allow agents to both actively initiate requests to other agents and receive requests from other agents at any time.

In MCP's CS architecture, if a client is not connected to the server, the server cannot send messages to the client. Of course, if a client can also act as a server, MCP can be considered a P2P architecture, albeit awkwardly.

A true P2P architecture involves not only physical connections but also roles and positioning as P2P, which is the core of P2P.

### Identity Authentication: OAuth vs. DID

Identity authentication is a crucial and challenging part of agent communication protocols. It addresses the problem of cross-platform identity authentication among agents, enabling agents to collaborate with all other agents.

#### MCP Identity Authentication

When MCP was first released, it did not support identity authentication, making remote server connections inconvenient. The latest draft version supports identity authentication between clients and servers.

MCP's identity authentication scheme is technically centered around the OAuth2 standard.

OAuth is an open standard authorization framework designed to provide a secure, convenient, and flexible way for third-party applications to access user resources at another service provider with user authorization, without obtaining sensitive information like usernames and passwords. Common examples include logging into third-party applications using Google or WeChat accounts, which are based on OAuth technology and widely used on the internet.

The draft protocol released by MCP is the community's second version. Compared to the first version, it has the following improvements:
- Uses OAuth 2.1 (still in draft status), simplifying the protocol and enhancing security
- Supports authorization server discovery, using the OAuth 2.0 Authorization Server Metadata protocol, allowing clients to automatically discover and obtain relevant configuration information of the authorization server, such as authorization endpoints, token endpoints, supported authorization types, encryption algorithms, etc.
- Supports OAuth 2.0 Dynamic Client Registration (DCR) Protocol, enabling clients to automatically register with the server without prior manual server registration, simplifying client-server integration costs.

The overall process is as follows:

<p align="center">
  <img src="/blogs/images/mcp-authorization.png" width="50%" alt="mcp-authorization"/>
</p>

#### ANP Identity Authentication

ANP's identity authentication scheme is technically centered around the W3C DID specification.

The [W3C DIDs](https://www.w3.org/TR/did-core/) standard, published as a W3C recommendation in 2022, is a new type of identifier supporting verifiable, decentralized digital identity. Based on DIDs, users can truly control their identities and improve interoperability between different applications.

Many applications are currently using the W3C DID specification, notably the popular Bluesky, whose underlying protocol, the AT Protocol, uses W3C DID as its identity authentication scheme.

The overall process of ANP identity authentication is as follows:

<p align="center">
  <img src="/blogs/images/anp-authorization.png" width="50%" alt="anp-authorization"/>
</p>

The biggest advantage of using DID as an identity authentication technology is interoperability. Agents on different platforms can authenticate each other using DID without needing to use a single platform account or perform mutual registration.

Because DID is inherently designed for decentralized identity.

Related articles on ANP DID identity authentication:
- [Comparison of did:wba with OpenID Connect and API keys](./Comparison%20of%20did:wba%20with%20OpenID%20Connect%20and%20API%20keys.md)
- [did:wba method specification](/03-did:wba%20Method%20Design%20Specification.md)

Comparing MCP and ANP identity authentication, we can identify several differences:
- MCP's identity authentication scheme is a good choice for AI connecting to the existing internet, as many major applications currently support OAuth.
- ANP uses DID technology, a relatively new specification, less widespread than OAuth, requiring applications to modify code for support.
- OAuth addresses how models access user resources on existing internet applications, while DID addresses how agents on different platforms authenticate each other.

In terms of interoperability, the DID-based scheme is simpler and involves less interaction:
- OAuth requires the client to register an ID with the server, while the DID scheme directly uses its own ID to interact with the other party, eliminating the registration process and the management cost of different server-generated IDs.
- During identity authentication, DID involves less interaction and can achieve 0-RTT (zero round-trip time, i.e., carrying identity verification information in the first business request). OAuth requires multiple interactions.

The fundamental reason is that OAuth is not specifically designed for identity interoperability. DID is inherently a decentralized identity technology, more friendly to interoperability.

Regarding agent identity, this is indeed a challenging issue. Many problems still need to be addressed:
- How to achieve cross-platform identity authentication without compromising user privacy while obtaining necessary identity information?
- How to achieve finer-grained permission control for users, instead of using a single ID to communicate with all agents?
- How to determine whether a request from an agent has been manually authorized by the user? Some sensitive operations should not be initiated autonomously by agents.
- How to ensure that users fully control their identity ownership, rather than using platform-granted permissions?

These new issues may be easier to solve based on W3C DID. We have initial solutions for many problems and will gradually improve and release them.

### Information Organization: RPC vs. Linked-Data

MCP and ANP adopt different technologies for organizing information output to the outside world.

#### MCP Information Organization

MCP uses JSON-RPC to read/operate server resources and tool capabilities. JSON-RPC (JavaScript Object Notation - Remote Procedure Call) is a remote procedure call (RPC) protocol based on JSON format. It allows clients to call methods on remote servers and receive returned JSON results.

Using MCP, the server can list all resources or tool lists, then read specified resources or call specified tools. Clients can also subscribe to resources, and the server proactively notifies clients when resource states change.

The format of resources or tools is customized by the server, with the model determining which resources and tools to read and operate.

The way MCP servers provide information output can essentially be understood as a special API.

#### ANP Information Organization

ANP's organization of information output to the outside world is centered on semantic web Linked-Data technology.

Linked Data is a technology for structured data sharing and interconnection, based on web standards (such as RDF, SPARQL, URI), aiming to connect data from different sources through unique identifiers (URI) to make it machine-readable and semantically understandable.

In implementation, we define an agent description specification ([Agent Description](/07-ANP-Agent%20Description%20Protocol%20Specification.md)), used to describe an agent's identity, capabilities, entity information, API interfaces, etc.

Agent description documents use the JSON-LD format. JSON-LD is a Linked Data format based on JSON, allowing different data to be linked into a data network, while being machine-readable.

For example, an agent description document for a coffee shop describes the coffee shop's name, owner, location, working hours, etc. The document also contains URLs for multiple products on sale. Through these URLs, AI can continue to access JSON-LD documents of products to obtain detailed product information. Similarly, detailed product information may also contain new JSON-LD URLs.

Thus, as long as there is an agent description document, all public information exposed by this agent can be obtained, thereby constructing a new data network linked together using JSON-LD, convenient for AI access. This corresponds to the existing internet linked together by web pages, designed for human access. Eventually, two networks will form: one designed for human access, the other for AI access.

In addition to data connection, Linked Data technology has another core feature: semantic understanding. The JSON-LD documents we design use schema.org as the semantic foundation. Schema.org defines a set of semantic models for describing the modern web, allowing two agents to have the same understanding of the same field, improving the accuracy of information understanding between agents and facilitating program processing.

Using Linked Data technology, the public information of agents can be easily crawled by search engines. Users can quickly find agents that can provide services through search engines, then interact and collaborate with agents based on the agent description document.

### Differences in Design Philosophy

The above are the differences in design details between MCP and ANP.

If we abstractly summarize, the biggest difference between MCP and ANP lies in their worldview:
- MCP is model-centric, viewing the entire internet as its context and tool.
- ANP is agent-centric, where each agent has equal status, forming a decentralized agent collaboration network.

<p align="center">
  <img src="/blogs/images/mcp-vs-anp-core.png" width="75%" alt="mcp-vs-anp-core"/>
</p>

Why are there such differences?

The main reason is the different purposes of MCP and ANP.

Strictly speaking, MCP is not a communication protocol for agents. Its name indicates that it is a model context protocol, aimed at providing context capabilities for models, making it easier for models to access the current internet and enrich chatbot product capabilities.

When we designed ANP, we did not have our own product. We directly stood on the future, designing ANP based on our understanding of the future Agentic web. Our goal is to build a new agent network that fully unleashes the capabilities of AI.

## What Kind of Communication Protocol Do Agents Need?

We believe MCP is an excellent protocol and the best current solution for models accessing the internet, more viable than the "Computer Use" solution. Anthropic also used their influence to show the industry the advantages of this solution.

However, we believe MCP may be a transitional form, the best solution for AI accessing the internet at present. If the internet changes significantly due to agents, MCP may not be the best solution.

Therefore, the kind of communication protocol agents need depends on the future characteristics of the Agentic web. We have summarized a few points (for details, see this article: [What Makes Agentic Web Different](./What-Makes-Agentic-Web-Different.md)):
- Agents will permeate every corner of the internet, with individuals or organizations possibly having multiple agents serving them.
- All agents can interconnect, which is a necessary condition for unleashing AI capabilities.
- Personal assistants become the new entry point to the internet, with connections between agents far exceeding those between humans and agents.
- The network becomes more flattened, with agents able to connect directly without third-party platforms.

These points form the core foundation of our ANP design.

Of course, MCP may also evolve and iterate, which we welcome. No organization or individual can independently complete such an important industry standard, nor can we. We are willing to cooperate with everyone in the industry.

## Common Questions

Regarding the relationship with MCP, there are often a few questions:
- Why create ANP after MCP already exists: When we started, MCP had not been released. Strictly speaking, we should be the first open-source communication protocol for agents, and we released earlier.
- Why continue with ANP after MCP was released: Because we have a different vision for the future.