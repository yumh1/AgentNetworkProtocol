<div align="center">
  
[English](README.md) | [中文](README.cn.md)

</div>

## AgentNetworkProtocol(ANP)

> TL;DR: ANP 致力于成为智能体互联网时代的 HTTP。

<!-- TOC -->
### 目录

- [愿景定位](#愿景定位)
- [为什么需要 ANP](#为什么需要-anp)
- [协议三层架构](#协议三层架构)
- [快速上手](#快速上手)
- [协议 SDK](#协议-sdk)
- [深入阅读](#深入阅读)
- [里程碑](#里程碑)
- [联系我们](#联系我们)
- [贡献](#贡献)
  - [贡献者](#贡献者)
- [许可证](#许可证)
- [版权声明](#版权声明)

## 愿景定位

AgentNetworkProtocol(ANP)是一个开源的智能体通信协议。

AgentNetworkProtocol(ANP)的目标是成为**智能体互联网时代的HTTP**。

我们的愿景是**定义智能体之间的连接方式，为数十亿智能体构建一个开放、安全、高效的协作网络**。

<p align="center">
  <img src="/images/agentic-web3.png" width="50%" alt="Agentic Web"/>
</p>

我们相信，智能体互联网是继人类互联网之后的新一代信息基础设施，将彻底改变数字世界的连接方式与协作模式。在这个愿景中：

- **从平台中心到协议中心**：当前互联网生态系统是以平台为中心的模式，数据和服务被锁在"数字孤岛"中。智能体互联网将重塑这种不平衡格局，让互联网从封闭、碎片化的状态，回归开放、自由连接的本源。

- **连接即力量**：在真正开放、互联的网络中，节点间的自由交互能最大限度激发创新潜力并创造巨大价值。未来每个智能体都将同时是信息消费者和服务提供者，每个节点都能无障碍地发现、连接并与网络中任何其他节点交互。

- **AI原生网络**：不同于为人类设计的网页与界面，智能体互联网将构建一个面向AI友好的原生数据网络，所有节点都是可描述、可发现、可调用的智能体或数据单元，每个链接都是语义明确、结构统一的协议连接。

这个愿景需要一个类似HTTP之于人类互联网的基础协议——这正是ANP诞生的原因。

**备注**：本项目未在任何平台、任何区块链发布数字货币。

## 为什么需要 ANP

当前互联网基础设施虽已相当完善，但针对智能体网络的特殊需求，当下仍缺乏最适合的通信和连接方案。我们致力于解决智能体网络面临的三大挑战：

- 🌐 **互联互通**：让所有的智能体相互之间都能够进行通信，打破数据孤岛，让AI能够获得完整的上下文信息。
- 🖥️ **原生接口**：AI无需模仿人类访问互联网，AI应该用它最擅长的方式（API或通信协议）与数字世界交互。
- 🤝 **高效协作**：利用AI，智能体之间可以自组织、自协商，构建比现有互联网更低成本、更高效率的协作网络。

## 协议三层架构

<p align="center">
  <img src="/images/anp-architecture.png" width="50%" alt="协议分层图"/>
</p>

- 🔒 **身份与加密通信层**：基于W3C DID（Decentralized Identifiers，去中心化标识符）规范，在现有成熟的Web基础设施上，构建一个去中心化的身份认证方案和端到端加密通信方案。它可以让任意平台之间的智能体进行身份认证，而不依赖于任何中心化系统。
- 🌍 **元协议层**：元协议即协商智能体之间通信协议的协议。是智能体网络演进为自组织、自协商的高效协作网络的关键。
- 📡 **应用协议层**：基于语义网相关规范，让智能体能够描述其他能力与支持的应用协议，并且高效的管理这些协议。

## 快速上手

如果你想快速了解ANP的基本概念和使用方法，可以查看我们的入门指南：[ANP入门指南](docs/chinese/ANP入门指南.md)

如果你想快速的运行ANP相关demo，可以查看我们的示例程序说明文档：[ANP示例程序](docs/chinese/ANP示例程序.md)

## 协议 SDK

我们正在开发一个开源的 AgentNetworkProtocol 实现，仓库地址：[https://github.com/agent-network-protocol/AgentConnect](https://github.com/agent-network-protocol/AgentConnect)

## 深入阅读

- 完整资料见 [拓展阅读](docs/links.md)  
- 查看详细设计请阅读 [ANP 技术白皮书](chinese/01-AgentNetworkProtocol技术白皮书.md)  
- 协议开源实现 [AgentConnect 示例](https://github.com/agent-network-protocol/AgentConnect)
## 里程碑

无论是协议还是开源代码实现，我们整体式是按照以下的顺序逐步的推进：

- [x] 构建身份认证与端到端加密通信协议与实现。这是我们整个项目的基础与核心，当前协议设计和代码基本完成。
- [x] 元协议设计与元协议代码实现。当前协议设计和代码开发基本完成。
- [x] 应用层协议设计与开发。
  - [x] 支持智能体描述。
  - [x] 支持智能体发现。
  - [ ] 特定领域使用的应用协议设计

## 联系我们

我们已经成立了一个ANP开源技术社区，以开源社区的方式推进ANP的建设。诚挚的邀请您加入我们的开源技术社区，我们的创始委员会、社区顾问、技术委员会、发展委员会、企业观察员等团队持续招募中。

邮箱：chgaowei@gmail.com  
- Discord: [https://discord.gg/sFjBKTY7sB](https://discord.gg/sFjBKTY7sB)  
- 官网：[https://agent-network-protocol.com/](https://agent-network-protocol.com/)  
- GitHub：[https://github.com/agent-network-protocol/AgentNetworkProtocol](https://github.com/agent-network-protocol/AgentNetworkProtocol)
- 微信：flow10240

## 贡献

我们欢迎任何形式的贡献，请参考 [CONTRIBUTING.cn.md](CONTRIBUTING.cn.md) 文件。

### 贡献者

我们向所有为 Agent Network Protocol 项目做出贡献的人表示衷心的感谢。您可以在这里查看完整的贡献者列表：

- [贡献者名单 (Chinese)](CONTRIBUTORS.cn.md)

## 许可证

本项目基于 MIT 许可证开源，详情请参考 [LICENSE](LICENSE) 文件。但版权归属于常高伟（GaoWei Chang）。任何使用本项目的用户必须保留原始版权声明和许可证文件。

## 版权声明  
Copyright (c) 2024 GaoWei Chang
本文件依据 [MIT 许可证](./LICENSE) 发布，您可以自由使用和修改，但必须保留本版权声明。
