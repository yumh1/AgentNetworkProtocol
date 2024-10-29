# Agent Network Protocol Technical Blueprint

## Vision

In the new era of rapid AI development, we are entering a new epoch of intelligent agent networks. The Agent Network Protocol (ANP) will become the core technology of this era, building an open, secure, and efficient collaborative network for billions of intelligent agents.

Imagine the future: your personal assistant AI seamlessly communicates with the restaurant's intelligent system when ordering food; your smart home system collaborates with the energy management AI to optimize electricity usage; your investment advisor AI exchanges real-time information with global market analysis agents... This is the forthcoming era of intelligent agent networks.

The vision of the Agent Network Protocol (ANP) is to **define the connection method for the intelligent agent network era**, just as internet protocols have achieved in the information age. We believe that in the near future, billions of intelligent agents will build an unprecedented collaborative network through ANP, creating value greater than the existing internet. With the support of ANP, the intelligent agent network will eventually evolve into a self-organizing, self-negotiating efficient collaborative network, which is an exciting future.

## Protocol Architecture

The Agent Network Protocol (ANP) is designed as a three-layer architecture, from bottom to top: Identity and Encrypted Communication Layer, Meta-Protocol Layer, and Application Protocol Layer, as shown in the figure below:

![Protocol Layer Design](/images/protocol-layer-design.png)

### Identity and Encrypted Communication Layer

This is the most fundamental part of the entire protocol, mainly addressing two major challenges in intelligent agent communication: how agents authenticate each other and how to achieve end-to-end encrypted communication.

Based on the W3C DID (Decentralized Identifiers) specification, combined with blockchain technology and end-to-end encryption technology, the Agent Network Protocol (ANP) provides a groundbreaking solution:

- **Fully Decentralized**: Agents can fully control their own identity without being restricted by any platform.
- **Seamless Connection**: Supports identity authentication between agents on any platform, breaking down barriers between platforms.
- **Ultimate Security**: End-to-end encryption ensures communication security, and intermediate nodes cannot decrypt the content.
- **Low Cost and High Efficiency**: Quickly deployable based on existing web infrastructure, with very low costs.

The W3C DID is the cornerstone of the Identity and Encrypted Communication Layer of the Agent Network Protocol (ANP). Its decentralization and interoperability features enable the development of the ANP protocol, allowing any two agents to establish a connection through it, enabling us to build an open intelligent agent collaborative network.

Detailed technical documentation: [GitHub](https://github.com/chgaowei/AgentNetworkProtocol)

### Meta-Protocol Layer

With the support of the meta-protocol, the intelligent agent network may evolve into a self-organizing, self-negotiating efficient collaborative network, which is an exciting future.

The so-called meta-protocol is a protocol for negotiating the communication protocol to be used. In the Meta-Protocol Layer, we mainly refer to and draw from the [Agora Protocol](https://arxiv.org/html/2410.11905v1).

In the current digital world, there are huge data silos, with data flow concentrated within the silos and only a small amount of data flowing between silos. This result is due to commercial reasons and significant technical limitations: heterogeneous networks (different architectures, functions, designs) often incur huge costs to interoperate through protocols. The fundamental reason lies in the "impossible triangle" of heterogeneous network communication proposed in the Agora Protocol paper (Versatility, Efficiency, Portability).

The combination of intelligent agents empowered by LLM and the meta-protocol is a good solution to this problem:

- Agents first use natural language to communicate their capabilities, data exchange formats, and protocols used, determining the protocol details for communication between agents.
- Based on the negotiation results, agents use LLM to construct and process protocol messages or use agents to generate code to handle protocol messages.
- Agents conduct protocol joint debugging, using LLM to determine whether protocol messages comply with the negotiated specifications. If not, they resolve it through natural language interaction.
- Finally, agents use the final protocol for communication.

We believe that with the natural language understanding and code generation capabilities of LLM, and the promotion of meta-protocol technology, the intelligent agent network will eventually evolve into a self-organizing, self-negotiating efficient collaborative network. Many communication protocols will be agreed upon between agents, far exceeding the number of protocols formulated by humans.

### Application Protocol Layer

Application layer protocols are divided into two categories: existing industry standards, such as email protocols, RTC-related standards, W3C existing standards, and consensus protocols automatically negotiated by the intelligent agent network. Their goal is to enable agents to collaborate to complete a specific business.

In terms of data types transmitted by protocols, they can be roughly divided into three categories: text, files, and real-time multimedia data streams. These three types can cover almost all current business types.

Agents can extend protocols based on their data or business characteristics on top of the basic protocol. The role of standard specifications in the intelligent agent network is mainly to reduce the complexity of negotiation rather than enforce standards. We believe that agents can negotiate the most suitable personalized protocol for their business scenarios.

## AgentConnect: The Open Source Implementation of Agent Network Protocol (ANP)

We have open-sourced a project, AgentConnect (https://github.com/chgaowei/AgentConnect), to implement the functions of the Agent Network Protocol (ANP). The project architecture is shown in the figure below:

![Project Architecture](/images/agent-connect-architecture.png)

Corresponding to the three-layer architecture of the Agent Network Protocol, AgentConnect mainly includes the following parts:

1. **Identity Authentication Module and End-to-End Encryption Module**
   Mainly implements identity authentication and end-to-end encrypted communication based on W3C DID, including the generation, verification, and retrieval of DID documents, as well as the implementation of end-to-end encrypted communication schemes based on DID and ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).

2. **Meta-Protocol Module**
   The Meta-Protocol Module needs to be implemented based on LLM (Large Language Model) and the meta-protocol. The main functions include application protocol negotiation based on the meta-protocol, protocol code implementation, protocol joint debugging, and protocol processing.

3. **Application Layer Protocol Integration Framework**
   The main purpose is to manage the protocol specification documents and protocol codes for communication with other agents, including application protocol loading, application protocol unloading, application protocol configuration, and application protocol processing. Using this framework, agents can conveniently and on-demand load the required existing protocols, speeding up the agent protocol negotiation process.

In addition to the above functions, AgentConnect will also focus on performance and multi-platform support in the future:

- **Performance**: As a fundamental codebase, we hope to provide extreme performance. In the future, we will rewrite the core parts of the code in Rust.
- **Multi-Platform**: Currently supports macOS, Linux, and Windows. In the future, it will support mobile and browser platforms.

## Milestones

Whether it is the protocol or the open-source code implementation, we are advancing step by step in the following order:

- Build the identity authentication and end-to-end encrypted communication protocol and implementation. This is the foundation and core of our entire project. The current protocol design and code are basically complete.
- Design and implement the meta-protocol and meta-protocol code. This will help the intelligent agent network evolve into a self-organizing, self-negotiating efficient collaborative network. This is what we are currently working on, and it will be an exciting feature. We expect to release the first version soon.
- Develop the application layer protocol integration framework. This will help the Agent Network Protocol (ANP) provide services for agents in various scenarios.

In addition, we will follow the principle of overall first, then details. In the early stages, we will focus on building the overall architecture, constructing an overall outline for each major module, and getting it running quickly, rather than building individual exquisite but non-functional modules.

Finally, during the design process, we gradually realized that blockchain might be a more suitable network infrastructure for intelligent agents. In the future, we may actively explore and experiment in this direction.

## Why Choose Agent Network Protocol (ANP)?

- **Open Connectivity**: Decentralized identity authentication based on W3C DID allows agents to break platform restrictions and achieve free and secure connections.
- **Technological Innovation**: By integrating blockchain and DID technology, it innovatively solves the problem of cross-platform agent authentication.
- **Efficient Implementation**: Based on existing web infrastructure, it achieves low-cost, rapid deployment, helping the ecosystem develop quickly.
- **Future-Oriented**: Builds infrastructure for the intelligent agent network era, driving the evolution and innovation of self-organizing collaborative networks.
- **Professional Team**: The core team consists of experienced engineers and researchers with rich experience in distributed systems, protocol design, and artificial intelligence.
