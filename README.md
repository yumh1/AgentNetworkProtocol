# AgentNetworkProtocol

[中文版](README.cn.md)

AgentNetworkProtocol is a cross-platform identity authentication and end-to-end encrypted communication technology solution based on W3C DID (Decentralized Identifier).

## Project Vision

Our vision is to provide communication capabilities for agents, enabling them to connect with each other and form an agent collaboration network.

Agents represent the next generation platform following personal computers and mobile terminals. We believe that billions of agents will emerge in the future, most of which won't directly interact with humans but rather collaborate with other agents to complete tasks.

However, for agents to collaborate, they need identity authentication and encrypted communication. Current mainstream internet authentication solutions have two key issues:
- Lack of cross-platform compatibility
- High authentication costs

While blockchain-based solutions perfectly address centralization and cross-platform issues, they are currently difficult to implement on a large scale due to blockchain technology's scalability limitations.

Therefore, we designed the new **Agent Network Protocol**. Based on the latest W3C DID specification, this protocol combines blockchain technology and end-to-end encrypted communication technology to provide an innovative identity authentication and encrypted communication solution for agents. It enables agents to:
- Maintain complete control over their identity
- Authenticate with any other agent
- Achieve end-to-end secure encrypted communication between agents

Rather than completely replacing existing technology, we've built a new agent network protocol at the application layer on top of existing web infrastructure. This helps us quickly build an agent collaboration network while reducing collaboration costs between agents.

## Core Features

- **Cross-platform Authentication**: Implements low-cost cross-platform identity interoperability using the did:all method based on W3C DID specification
- **End-to-End Encrypted Communication**: Secure and efficient encrypted communication solution inspired by the TLS protocol
- **Open Collaboration**: Supports secure and efficient collaboration between agents based on standard protocols

## Technical Documentation

- [AgentNetworkProtocol Technical White Paper](01-AgentNetworkProtocol%20Technical%20White%20Paper.md) - Overview of the technical solution
- [did:all Method Design Specification](02-did%3Aall%20Method%20Design%20Specification.md) - Detailed DID method design
- [End-to-End Encrypted Communication Technology Protocol](03-End-to-End%20Encrypted%20Communication%20Technology%20Protocol%20Based%20on%20did%3Aall%20Method.md) - Encrypted communication protocol description
- [Message Service Protocol](04-Message%20Service%20Protocol%20Based%20on%20did%3Aall%20Method.md) - Message service protocol description
## Contact Information

Author: Gaowei Chang  
Email: chgaowei@gmail.com  
Discord: [https://discord.gg/SuXb2pzqGy](https://discord.gg/SuXb2pzqGy)  
Website: [https://agent-network-protocol.com/](https://agent-network-protocol.com/)  
GitHub: [https://github.com/chgaowei/AgentNetworkProtocol](https://github.com/chgaowei/AgentNetworkProtocol)

## Code

We are developing an open-source implementation of AgentNetworkProtocol called AgentConnect.
Repository: [https://github.com/chgaowei/AgentConnect](https://github.com/chgaowei/AgentConnect)

## Contributing

We welcome all forms of contributions, including but not limited to:
- Code contributions
- Documentation improvements
- Issue reporting
- Feature suggestions

## License

This project is open-source under the MIT License. For details, please refer to the [LICENSE](LICENSE) file.
