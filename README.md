# AgentNetworkProtocol(ANP)

[中文版](README.cn.md)

## Vision

In this new era of rapid artificial intelligence development, we are entering a new epoch of agent networks. Imagine the future: your personal assistant agent seamlessly communicates with restaurant agents when ordering meals; your smart home agent collaborates with energy management agents to optimize power usage; your investment advisor agent exchanges real-time information with global market analysis agents... This is the upcoming era of agent networks.

However, as Bill Gates mentioned in [a blog post](https://www.gatesnotes.com/AI-agents), there is currently no standard protocol that allows agents to communicate with each other. This is the problem that Agent Network Protocol (ANP) aims to solve.

The vision of Agent Network Protocol (ANP) is to **define how agents connect with each other and build an open, secure, and efficient collaboration network for billions of agents**. Just as the development of Internet standard protocols has enabled the information age over the past three decades, we believe that in the near future, billions of agents will build unprecedented collaboration networks through ANP, creating greater value than the existing Internet. Empowered by AI technology and ANP, the agent network will eventually evolve into a **self-organizing, self-negotiating** efficient collaboration network - an incredibly exciting future.

## Challenges

Agent Network Protocol (ANP) aims to address three major challenges in connectivity:

- How agents authenticate and establish end-to-end encrypted communication
- How agents negotiate protocols to evolve into a self-organizing, self-negotiating network
- How to uniformly manage consensus protocols reached in the agent network to accelerate protocol negotiation between agents

## Protocol Architecture

To address these three major challenges, Agent Network Protocol (ANP) is designed as a three-layer architecture, consisting of Identity and Encrypted Communication Layer, Meta-Protocol Layer, and Application Protocol Layer from bottom to top, as shown below:

<p align="center">
  <img src="/images/protocol-layer-design.png" width="50%" alt="Protocol Layer Design"/>
</p>

### Identity and Encrypted Communication Layer

This is the most fundamental part of the entire protocol, mainly addressing two major challenges in agent communication: how agents authenticate each other and how to achieve end-to-end encrypted communication.

Based on the W3C DID (Decentralized Identifiers) specification, integrating blockchain technology and end-to-end encryption technology, the Agent Network Protocol (ANP) provides a groundbreaking solution:

- **Fully Decentralized**: Agents can fully control their own identity without being restricted by any platform.
- **Seamless Connection**: Supports agent identity authentication across any platform, breaking down barriers between platforms.
- **Ultimate Security**: End-to-end encryption ensures communication security, with intermediate nodes unable to decrypt the content.
- **Low Cost and High Efficiency**: Quickly deployable based on existing web infrastructure, with very low cost.

W3C DID is the cornerstone of the Identity and Encrypted Communication Layer of the Agent Network Protocol (ANP). Its decentralization and interoperability features enable the openness of the ANP protocol, allowing any two agents to establish a connection through it, enabling us to build an open agent collaborative network.

### Meta-Protocol Layer

With the support of the meta-protocol, the agent network may evolve into a self-organizing, self-negotiating efficient collaborative network, which is an exciting future.

The so-called meta-protocol is a protocol for negotiating the communication protocol to be used. In the Meta-Protocol Layer, we mainly refer to and draw from the [Agora Protocol](https://arxiv.org/html/2410.11905v1).

In the current digital world, there is a significant phenomenon of data silos, where data flow is concentrated within the silos, and there is only a small amount of data flow between silos. This result arises not only due to commercial reasons but also due to technical limitations: heterogeneous networks (different architectures, functions, designs) often incur huge costs to interoperate through protocols. The fundamental reason lies in the "impossible trinity" of heterogeneous network communication proposed in the Agora Protocol paper (Versatility, Efficiency, Portability).

The combination of LLM-powered agents and the meta-protocol is a good solution to this problem:

- Agents first use natural language to communicate their capabilities, data exchange formats, protocols used, etc., to determine the protocol details for communication between agents.
- Based on the negotiation results, agents use LLM to construct and process protocol messages, or use agents to generate code to handle protocol messages.
- Agents conduct protocol joint debugging, using LLM to determine whether protocol messages conform to the negotiated specifications. If not, they resolve it through natural language interaction.
- Finally, agents use the final protocol for communication.

We believe that with the natural language understanding and code generation capabilities of LLM, and the promotion of meta-protocol technology, the agent network will eventually evolve into a self-organizing, self-negotiating efficient collaborative network. Many communication protocols will be agreed upon between agents, and the number of these protocols will far exceed the number of protocols formulated by humans.

### Application Protocol Layer

Application layer protocols are divided into two categories: existing industry standards, such as email protocols, RTC-related standards, W3C existing standards, etc., and consensus protocols automatically negotiated by the agent network. Their goal is to enable agents to collaborate to complete a specific task.

In terms of the types of data transmitted by the protocol, they can be roughly divided into three categories: text, files, and real-time multimedia data streams. These three types can cover almost all current business types.

Agents can extend the protocol based on their data or business characteristics on top of the basic protocol. The role of standard specifications in the agent network is mainly to reduce the complexity of negotiation rather than enforce standards. We believe that agents can negotiate the most suitable personalized protocol for their business scenarios.

## Technical Documentation



## Technical Documentation

- [AgentNetworkProtocol Technical Blueprint](00-AgentNetworkProtocol%20Technical%20Blueprint.md) - Technical blueprint, overall solution introduction
- [AgentNetworkProtocol Technical White Paper](01-AgentNetworkProtocol%20Technical%20White%20Paper.md) - Overview of the technical solution
- [did:all Method Design Specification](02-did%3Aall%20Method%20Design%20Specification.md) - Detailed DID method design
- [End-to-End Encrypted Communication Technology Protocol](03-End-to-End%20Encrypted%20Communication%20Technology%20Protocol%20Based%20on%20did%3Aall%20Method.md) - Encrypted communication protocol description
- [Message Service Protocol](04-Message%20Service%20Protocol%20Based%20on%20did%3Aall%20Method.md) - Message service protocol description

## Milestones

Whether it is the protocol or the open-source code implementation, we are advancing step by step according to the following sequence:

- Build the identity authentication and end-to-end encrypted communication protocol and implementation. This is the foundation and core of our entire project. The current protocol design and code are basically complete.
- Meta-protocol design and meta-protocol code implementation. This will help the agent network evolve into a self-organizing, self-negotiating efficient collaborative network. This is what we are currently working on, and it will be an exciting feature. We expect to release the first version soon.
- Development of the application layer protocol integration framework. This will help the Agent Network Protocol (ANP) provide services to agents in various scenarios.

In addition, we will follow the principle of overall first, then details. In the early stages, we will focus on building the overall architecture, constructing an overall outline for each major module, and getting it running quickly, rather than building individual exquisite but non-functional modules.

To promote the Agent Network Protocol (ANP) as an industry standard, we will establish an ANP Standardization Committee at an appropriate time, dedicated to promoting ANP as an industry standard recognized by international standardization organizations such as W3C.

Finally, during the design process, we gradually realized that blockchain might be a more suitable infrastructure for the agent network. In the future, we may make some active attempts and explorations in this direction.

## Why Choose Agent Network Protocol (ANP)?

- **Open Interconnection**: Decentralized identity authentication based on W3C DID allows agents to break platform restrictions and achieve free and secure connections.
- **Technological Innovation**: By integrating blockchain and DID technology, we have innovatively solved the problem of cross-platform agent authentication.
- **Efficient Implementation**: Based on existing web infrastructure, achieving low-cost, rapid deployment, and promoting the rapid development of the ecosystem.
- **Future-Oriented**: Building infrastructure for the era of agent networks, driving the evolution and innovation of self-organizing collaborative networks.
- **Professional Team**: A core team composed of experienced engineers and researchers with rich experience in distributed systems, protocol design, and artificial intelligence fields.

## Contact Information

Author: Gaowei Chang  
Email: chgaowei@gmail.com  
- Discord: [https://discord.gg/SuXb2pzqGy](https://discord.gg/SuXb2pzqGy)  
- Website: [https://agent-network-protocol.com/](https://agent-network-protocol.com/)  
- GitHub: [https://github.com/chgaowei/AgentNetworkProtocol](https://github.com/chgaowei/AgentNetworkProtocol)

## Code

We are developing an open-source implementation of the AgentNetworkProtocol, named AgentConnect.
Repository: [https://github.com/chgaowei/AgentConnect](https://github.com/chgaowei/AgentConnect)

## Contributing

We welcome any form of contribution. Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is open-source under the MIT License. For details, please refer to the [LICENSE](LICENSE) file.

## Acknowledgements

Thanks to everyone who has contributed to the Agent Network Protocol (ANP).

Thanks to the authors of the [Agora Protocol](https://agoraprotocol.org/) paper, whose research on agent meta-protocols has greatly helped us.


