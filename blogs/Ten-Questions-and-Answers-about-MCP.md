
# Ten Questions and Answers about MCP

## Preface

During discussions, it became apparent that many people are not very familiar with MCP. Therefore, I quickly compiled this article to give you an overall understanding.

## Bonus Question: What is MCP?

MCP (Model Context Protocol) is an open protocol designed to standardize the interaction between large language models (LLMs) and external data sources, tools, and services.

Originally developed by Anthropic, it is now open source.

## Question 1: What does the 'P' in MCP stand for?

'P' stands for Protocol, which refers to a network protocol. Common examples include TCP/IP and HTTP, which are types of network protocols.

Network protocols define how two parties establish a connection, send data, define data formats, and handle errors.

MCP is a network protocol that defines the network communication data format for integrating AI models with external data sources and tools, including the transmission protocol, data format definition, and authentication methods.

## Question 2: What problem does MCP solve?

MCP addresses the fragmentation issue of integrating large language models with external data sources and tools. By providing a standardized interface, MCP enables AI applications to connect more reliably and efficiently to different data sources and tools, avoiding the hassle of developing a connector for each data source.

Simply put, a tool using the MCP protocol can be used by both Claude and cursor without needing to be developed twice.

## Question 3: Where does MCP fit in?

MCP sits between models and tools/resources. Models call functions through function calling, and these functions interact with external tools/resources via the MCP protocol.

## Question 4: Was MCP developed by Anthropic, and can other models use it?

Yes.

Although MCP was developed by Anthropic, it is an open protocol that any model can use. It is independent of the model. If a model's tool usage capability is weak, using MCP will not enhance it.

## Question 5: What is the difference between MCP and function calling?

They are not the same concept.

Function calling is the interaction method between large models and the external digital world. MCP is the interaction method between the MCP host (chatbot or AI tool) and external tools/resources.

Generally, a model first triggers a function call through function calling, which then triggers an MCP request within that function call.

## Question 6: How does MCP differ from previous OpenAI plugins?

They are very similar, but MCP is more standardized than previous plugins, with clear definitions for data formats, transmission protocols, authentication methods, and stronger capabilities.

## Question 7: What is the difference between MCP and GPTs?

GPTs are more like an application marketplace, currently designed for human use.

GPTs might be similar to the marketplace of an MCP server, but the MCP server is mainly for AI use, not directly for humans.

## Question 8: Will MCP become a standard?

In the short term, MCP has no competitors in integrating external resources and tools with models, and its ecosystem is growing.

However, it is uncertain whether OpenAI will support it or create its own standard. If they do, it must be better designed than MCP, or they will be criticized for creating a "walled garden."

In the long term, MCP has some design issues, such as complexity, client-server coupling, and distributed identity authentication, which need to be addressed.

## Question 9: Should we adopt MCP?

From a technical perspective, if used internally, you need to balance flexibility and cost. Internally, you can do whatever is most efficient; MCP may not be the optimal solution. However, if it involves interfacing with external (e.g., public network) tools, it's best to use a widely recognized protocol.

## Question 10: Will domestic internet platforms adopt MCP?

Platforms like Meituan, Didi, Taobao, and Pinduoduo are unlikely to adopt it in the short term. They won't create an upstream for themselves.

It's similar to when Taobao cut off traffic from Baidu and WeChat.

## Bonus Question: Is MCP suitable for agents?

MCP is not designed for agents; it is designed for models to connect with external resources and tools.

Several issues remain unresolved, such as MCP's centralized identity authentication technology, which is not suitable for agent-to-agent authentication. MCP's CS architecture (client-server architecture) means the server cannot actively connect to the client.

If there is a need for agent connections, you can try our ANP, which is specifically designed for agents.

## Contact Us

If you are interested in this topic, feel free to contact us.

The goal of AgentNetworkProtocol is to become the HTTP of the agent internet era. Our vision is to define the connection methods between agents and build an open, secure, and efficient collaboration network for billions of agents.

The ANP open-source technology community currently has 25 developers and is recruiting more. If you are interested in agent communication protocols, whether in development, product, or operations, you can join us to define agent connections and collaboration through open source.

Contact Information:
- GitHub: https://github.com/agent-network-protocol/AgentNetworkProtocol
- Discord: https://discord.gg/sFjBKTY7sB
- Website: https://agent-network-protocol.com/
- WeChat: flow10240

Finally, welcome to join the agent communication protocol discussion group. This might be the first group in China to discuss agent communication protocols, with over 200 protocol enthusiasts currently engaged in discussions. (Add me on WeChat to join)
