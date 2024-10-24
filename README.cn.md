# AgentNetworkProtocol

AgentNetworkProtocol 是一个基于W3C DID (去中心化标识符)的跨平台身份认证和端到端加密通信技术方案。

## 项目愿景

我们的愿景是为智能体提供通信能力，让智能体和智能体相互连接成一个智能体协作网络。

智能体是继个人电脑和移动终端之后的新一代平台。我们相信未来将出现数十亿规模的智能体，它们大多数并不直接与人交互，而是通过与其他智能体协作来完成任务。

然而，智能体要互相协作，就需要进行身份认证和加密通信。当前互联网的主流身份认证方案存在两个关键问题：
- 无法跨平台
- 认证成本较高

虽然基于区块链的方案完美解决了中心化和跨平台的问题，但受限于区块链技术的扩展性，目前难以大规模应用。

为此，我们设计了全新的**智能体网络协议（Agent Network Protocol）**。该协议基于 W3C 最新的 DID 规范，结合区块链技术和端到端加密通信技术，为智能体提供了创新的身份认证和加密通信解决方案。它使智能体能够：
- 完全控制自己的身份标识
- 与任意其他智能体进行身份认证
- 实现智能体之间端到端的安全加密通信

我们并没有完全的推倒原有的技术，而是基于现有的web基础设施之上，在应用层提供了一套全新的智能体网络协议。这有助于我们快速构建智能体协作网络，并降低智能体之间的协作成本。

## 核心特性

- **跨平台身份认证**: 基于 W3C DID 规范设计的 did:all 方法,实现低成本的跨平台身份互通
- **端到端加密通信**: 借鉴 TLS 协议设计的安全高效的加密通信方案
- **开放 协作**: 支持智能体之间基于标准协议进行安全高效的协作

## 技术文档

- [AgentNetworkProtocol 技术白皮书](chinese/01-AgentNetworkProtocol技术白皮书.md) - 技术白皮书，方案整体介绍
- [did:all 方法设计规范](chinese/02-did:all方法设计规范.md) - DID 方法详细设计规范
- [端到端加密通信技术协议](chinese/03-基于did:all方法的端到端加密通信技术协议.md) - 端到端加密通信协议说明
- [消息服务协议](chinese/04-基于did:all方法的消息服务协议.md) - 消息服务协议说明

## 联系方式

作者：常高伟  
邮箱：chgaowei@gmail.com  
- Discord: [https://discord.gg/SuXb2pzqGy](https://discord.gg/SuXb2pzqGy)  
官网：[https://agent-network-protocol.com/](https://agent-network-protocol.com/)  
GitHub：[https://github.com/chgaowei/AgentNetworkProtocol](https://github.com/chgaowei/AgentNetworkProtocol)

## 代码

我们正在开发一个开源的 AgentNetworkProtocol 实现，并将其命名为 AgentConnect。
仓库地址：[https://github.com/chgaowei/AgentConnect](https://github.com/chgaowei/AgentConnect)

## 贡献

我们欢迎任何形式的贡献，包括但不限于：
- 代码贡献
- 文档改进
- 问题反馈
- 功能建议

## 许可证

本项目基于 MIT 许可证开源，详情请参考 [LICENSE](LICENSE) 文件。
