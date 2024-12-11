## AgentNetworkProtocol(ANP)

### 愿景

AgentNetworkProtocol(ANP)的目标是成为**智能体互联网时代的HTTP**。我们的愿景是**定义智能体之间的连接方式，为数十亿智能体构建一个开放、安全、高效的协作网络**。

当前互联网基础设施虽已相当完善，但针对智能体网络的特殊需求，当下仍缺乏最适合的通信和连接方案。我们致力于解决智能体网络面临的三大挑战：

- **互联互通**：让所有的智能体相互之间都能够进行通信，打破数据孤岛，让AI能够获得完整的上下文信息。
- **原生接口**：AI无需模仿人类访问互联网，AI应该用它最擅长的方式（API或通信协议）与数字世界交互。
- **高效协作**：利用AI，智能体之间可以自组织、自协商，构建比现有互联网更低成本、更高效率的协作网络。

### 协议架构

<p align="center">
  <img src="/images/protocol-layer-design.png" width="50%" alt="协议分层图"/>
</p>

- **身份与加密通信层**：基于W3C DID（Decentralized Identifiers，去中心化标识符）规范，在现有Web基础设施上，构建一个去中心化的身份认证方案和端到端加密通信方案。
- **元协议层**：元协议即协商智能体之间通信协议的协议。是智能体网络演进为自组织、自协商的高效协作网络的关键。
- **应用协议层**：基于语义网相关规范，让智能体能够描述其他能力与支持的应用协议，并且高效的管理这些协议。

### 代码实现

我们正在开发一个开源的 AgentNetworkProtocol 实现，仓库地址：[https://github.com/chgaowei/AgentConnect](https://github.com/chgaowei/AgentConnect)

### 文档地图

如果你想进一步了解，可以查看相关的文档：

- 如果你想了解我们整体的设计思路和理念，可以查看我们的技术白皮书：[AgentNetworkProtocol技术白皮书](chinese/01-AgentNetworkProtocol技术白皮书.md)
- 我们设计了一个去中心化的身份验证方案，既可以利用当前成熟的web基础设施，又兼具去中心化特点。我们认为这是当前智能体身份认证的最佳方案：[did:wba身份证方案](chinese/03-did:wba方法规范.md)
- 基于DID我们设计了一个用于智能体之间的端到端加密通信协议，不同于TLS，中间转发节点无法解密：[基于did的端到端加密通信](chinese/04-基于did的端到端加密通信技术协议.md)
- 我们设计了一个用于智能体之间协商通信协议的元协议，它能够让智能体之间自己协商他们之间的通信协议：[元协议设计规范](chinese/06-AgentNetworkProtocol元协议设计规范(draft).md)
- 还有一些规范我们正在设计和完善中。

这里有一些我们的blogs：

- 这是一个did:wba的简要介绍：[did:wba-基于web的去中心化身份标识符](blogs/did:wba-基于web的去中心化身份标识符.md)

### 里程碑

无论是协议还是开源代码实现，我们整体式是按照以下的顺序逐步的推进：

[x] 构建身份认证与端到端加密通信协议与实现。这是我们整个项目的基础与核心，当前协议设计和代码基本完成。
[x] 元协议设计与元协议代码实现。当前协议设计和代码开发基本完成。
[ ] 应用层协议设计与开发。目前正在进行中。

为了推动Agent Network Protocol(ANP)成为行业的标准，我们将会在合适的时间组建ANP标准化委员会，致力于推动ANP成为W3C等国际标准化组织认可的行业标准。

### 联系我们

作者：常高伟  
邮箱：chgaowei@gmail.com  
- Discord: [https://discord.gg/SuXb2pzqGy](https://discord.gg/SuXb2pzqGy)  
- 官网：[https://pi-unlimited.com/](https://pi-unlimited.com/)  
- GitHub：[https://github.com/chgaowei/AgentNetworkProtocol](https://github.com/chgaowei/AgentNetworkProtocol)
微信：flow10240

### 贡献

我们欢迎任何形式的贡献，请参考 [CONTRIBUTING.cn.md](CONTRIBUTING.cn.md) 文件。

### 许可证

本项目基于 MIT 许可证开源，详情请参考 [LICENSE](LICENSE) 文件。
