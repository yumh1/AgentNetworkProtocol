<div align="center">
  
[English](README.md) | [中文](README.cn.md)

</div>

## AgentNetworkProtocol(ANP)

### Vision

AgentNetworkProtocol(ANP) aims to become **the HTTP of the Intelligent Agent Internet era**.

Our vision is to **define how agents connect with each other, building an open, secure, and efficient collaboration network for billions of intelligent agents**.

While current internet infrastructure is well-established, there's still a lack of optimal communication and connection solutions for the specific needs of agent networks. We are committed to addressing three major challenges faced by agent networks:

- 🌐 **Interconnectivity**: Enable communication between all agents, break down data silos, and ensure AI has access to complete contextual information.
- 🖥️ **Native Interfaces**: AI shouldn't need to mimic human internet interaction; instead, it should interact with the digital world through its most proficient means (APIs or communication protocols).
- 🤝 **Efficient Collaboration**: Leverage AI for self-organization and self-negotiation among agents, creating a more cost-effective and efficient collaboration network than the existing internet.


### Protocol Architecture

<p align="center">
  <img src="/images/protocol-layer-design.png" width="50%" alt="Protocol Layer Design"/>
</p>

- **Identity and Encrypted Communication Layer**: Built on W3C DID (Decentralized Identifiers) specifications, establishing a decentralized authentication scheme and end-to-end encrypted communication solution on existing web infrastructure.
- **Meta-Protocol Layer**: A protocol for negotiating communication protocols between agents, crucial for evolving the agent network into a self-organizing, self-negotiating efficient collaboration network.
- **Application Protocol Layer**: Based on semantic web specifications, enabling agents to describe their capabilities and supported application protocols, and manage these protocols efficiently.

### Code Implementation

We are developing an open-source implementation of AgentNetworkProtocol at: [https://github.com/chgaowei/AgentConnect](https://github.com/chgaowei/AgentConnect)

### Documentation Map

For further understanding, you can refer to these documents:

- For our overall design philosophy and concepts, see our technical white paper: [AgentNetworkProtocol Technical White Paper](01-AgentNetworkProtocol%20Technical%20White%20Paper.md)
- We've designed a decentralized authentication scheme that leverages existing web infrastructure while maintaining decentralization. We believe this is currently the optimal solution for agent authentication: [did:wba Method Specification](03-did:wba%20Method%20Design%20Specification.md)
- Based on DID, we've designed an end-to-end encrypted communication protocol for agents, distinct from TLS as intermediate relay nodes cannot decrypt the content: [DID-based End-to-End Encrypted Communication](04-End-to-End%20Encrypted%20Communication%20Technology%20Protocol%20Based%20on%20did.md)
- We've designed a meta-protocol for negotiating communication protocols between agents, enabling them to autonomously negotiate their communication protocols: [Meta-Protocol Design Specification](06-AgentNetworkProtocol%20Meta-Protocol%20Design%20Specification(draft).md)
- Additional specifications are currently under development.

Here are some of our blogs:

- A brief introduction to did:wba: [did:wba - Web-Based Decentralized Identifiers](blogs/did:wba,%20a%20Web-based%20Decentralized%20Identifier.md)

### Milestones

Both protocol development and open-source implementation are progressing in the following order:

- [x] Build identity authentication and end-to-end encrypted communication protocol and implementation. This foundational core is essentially complete in both protocol design and code.
- [x] Meta-protocol design and implementation. Protocol design and code development are basically complete.
- [ ] Application layer protocol design and development. Currently in progress.

To establish Agent Network Protocol(ANP) as an industry standard, we plan to form an ANP Standardization Committee at an appropriate time, working towards recognition by international standardization organizations like W3C.

### Contact Us

Author: Gaowei Chang  
Email: chgaowei@gmail.com  
- Discord: [https://discord.gg/SuXb2pzqGy](https://discord.gg/SuXb2pzqGy)  
- Website: [https://pi-unlimited.com/](https://pi-unlimited.com/)  
- GitHub: [https://github.com/chgaowei/AgentNetworkProtocol](https://github.com/chgaowei/AgentNetworkProtocol)
WeChat: flow10240

### Contributing

We welcome contributions of any form. Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### License

This project is open-sourced under the MIT License. See [LICENSE](LICENSE) file for details.

