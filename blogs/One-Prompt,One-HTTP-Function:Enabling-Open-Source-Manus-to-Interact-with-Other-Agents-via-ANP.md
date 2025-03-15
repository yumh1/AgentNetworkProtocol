# One Prompt, One HTTP Function: Enabling Open-Source Manus to Interact with Other Agents via ANP

This week, members of the ANP open-source technology community completed a task by adding support for the ANP protocol to the two most popular open-source Manus projects (owl and OpenManus), allowing open-source Manus to access the internet via ANP. (Thanks again to the community developers for their contributions!)

We first conducted a small-scale test within our developer community and agent communication protocol exchange group, and today we are officially releasing it to the public.

During the integration process, we observed the strengths of ANP compared to MCP. With just one prompt and one HTTP function, agents can communicate and collaborate with any other agent.

Key points are as follows:
- ANP has two main features compared to MCP that make it more suitable for agent communication: decentralized identity authentication and a P2P protocol architecture.
- The integration process is simple. Agents only need an anp_tool.py file (one prompt, one HTTP function) to connect and communicate with any other agent.
- The simplicity of the integration process is due to the streamlined protocol design. In the ANP protocol, two agents are completely decoupled, and the protocol has no complex concepts and supports stateless protocols.
- After running the ANP process for the first time, we were still a bit amazed: ANP is a completely AI Native protocol, and agents can fix their own errors during the connection process.
- AI not only changes the software development model but also changes the software operation and collaboration model. In the future, software may not need much complex logic. Agents will accelerate the replacement of existing software.

## What is ANP, and how does it differ from MCP?

ANP is an open-source communication protocol designed for agents, providing decentralized identity authentication and data exchange and collaboration based on semantic web technology.

If MCP is the USB interface for models, allowing models to connect to various resources and tools, then ANP is the email for agents. As long as you have the other party's ID, you can use your own account to actively send a request to establish a connection.

MCP:
<p align="center">
  <img src="/blogs/images/mcp-usb.png" width="50%" alt="mcp-usb"/>
</p>

ANP:
<p align="center">
  <img src="/blogs/images/anp-email.png" width="50%" alt="anp-email"/>
</p>

Compared to MCP, ANP has two main features that make it more suitable for agent communication scenarios.

1. Decentralized Identity Authentication

Similar to email, communicating with another agent based on the ANP protocol only requires knowing the other party's ID, without needing to register an account on the other party's system or platform. This greatly simplifies the cost of collaboration between two agents.

<p align="center">
  <img src="/blogs/images/did-wba-auth.png" width="50%" alt="did-wba-auth"/>
</p>

2. P2P (Peer to Peer) Protocol Architecture

The architecture of the ANP protocol is P2P, and any agent can actively establish a connection with another agent.

<p align="center">
  <img src="/blogs/images/agentic-web.png" width="50%" alt="agentic-web"/>
</p>

>

Note: For detailed differences between ANP and MCP, you can refer to this article: [Comparison of MCP and ANP: What Kind of Communication Protocol Do Agents Need](/blogs/cn/MCP与ANP对比：智能体需要什么样的通信协议.md)

## What Can Open-Source Manus Do After Integrating ANP?

After integrating ANP, open-source Manus can interact with other agents through ANP. For example, there is a hotel agent that provides hotel inquiry and booking services. After Manus obtains the hotel agent's ADs (Agent Description), it can interact with the hotel agent through ANP to inquire about hotel information and book hotels.

## The Process of Integrating ANP into Open-Source Manus

ANP, as a tool for agents, can be integrated into open-source Manus, whether it is owl or OpenManus, by simply adding the anp_tool.py module.

The code of anp_tool.py is very simple, with the core being a tool description (used in the prompt) and an HTTP function (used to handle ANP requests).

**Tool description is as follows:**

```plaintext
Use Agent Network Protocol (ANP) to interact with other agents.
1. For the first time, please enter the URL: https://agent-search.ai/ad.json, which is an agent search service that can use the interfaces inside to query agents that can provide hotels, tickets, and attractions.
2. After receiving the agent's description document, you can crawl the data according to the data link URL in the agent's description document.
3. During the process, you can call the API to complete the service until you think the task is completed.
4. Note that any URL obtained using ANPTool must be called using ANPTool, do not call it directly yourself.
```

The core of this description is to instruct the model to start from a URL of an agent description document, download the document, and based on the information in the document and its own tasks, use the URLs in the document to further crawl new documents or APIs. During this process, it can call the APIs in the document. This way, it continuously searches for publicly available information from agents until the task is completed or deemed finished.

**The HTTP function is as follows:**

```python   
async def execute(
    self, 
    url: str, 
    method: str = "GET", 
    headers: Dict[str, str] = None, 
    params: Dict[str, Any] = None, 
    body: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Execute HTTP requests to interact with other agents
    
    Args:
        url (str): URL of the agent description file or API endpoint
        method (str, optional): HTTP method, default is "GET"
        headers (Dict[str, str], optional): HTTP request headers
        params (Dict[str, Any], optional): URL query parameters
        body (Dict[str, Any], optional): Request body for POST/PUT requests
        
    Returns:
        Dict[str, Any]: Response content
    """
```
The core of the HTTP function is an interface for sending HTTP requests, with the unique aspect being the use of ANP protocol's identity authentication mechanism during the process.

<p align="center">
  <img src="/blogs/images/anp-interaction-flow.png" width="75%" alt="anp-interaction-flow"/>
</p>

**Agent Identity:**

In the test script, we generated a DID identity "did:wba:agent-did.com:test:public" for Manus, with the DID document and private key stored in the "did_test_public_doc" folder.

This is a public test DID, which anyone can use to experience the ANP protocol, but it cannot be used to book products. If you wish to experience the full range of products, please contact us.

## Differences in Integration Process with MCP

The above outlines the entire process of integrating the ANP protocol, which only needs to be done once to interact with any type of agent. The only changes required are the user's intent and the agent description document URL.

This simplicity is a hallmark of the ANP protocol design:
- Agents are completely decoupled from each other, with no need to know the internal design and implementation of the other.
- Semantic web technology is used to add semantic descriptions to data, allowing AI to better understand it.
- Linked-Data technology connects data into a network, facilitating AI data crawling.

The ANP protocol lacks the concepts of resources, tools, prompts, files, sampling, etc., found in MCP. The core concept of ANP is the agent description document, which can include information and interfaces provided by the agent.

Since ANP is entirely a network protocol, locally, you only need to install the ANP SDK agent-connect package, with no other installations required.

Additionally, from the first day of release, we supported decentralized identity authentication, allowing two agents to communicate without needing to register an account in the other system, using their own account instead. This is something MCP does not offer.

For a comparison, you can refer to the process of owl calling MCP here: https://mp.weixin.qq.com/s/i6tbSc5fspkV9qxFotZEKw.

## AI Native Protocol and Connection

After the ANP process was first successfully executed, I was somewhat amazed: I discovered an interesting point because, in the agent implementation, the model was allowed to assemble HTTP requests and handle HTTP responses on its own.

When the model's first HTTP request contained a field error and another agent returned a failure, the model automatically identified this error and reissued the HTTP request, with the second request succeeding.

This amazed me for two reasons:
- An **AI Native** protocol and connection are fundamentally different from the protocols and connection methods we currently use on the internet.
- AI not only **changes the software development model** but also **changes the software operation and collaboration model**. In the future, software may not need much complex logic, as agents will accelerate the replacement of existing software.

## Experience the Effects of Open-Source Manus + ANP

### owl

GitHub address: https://github.com/agent-network-protocol/owl_anp

For operation methods, please refer to: README_anp_example.md

### OpenManus

GitHub address: https://github.com/agent-network-protocol/OpenManus-ANP

For operation methods, please refer to the original readme file: README_zh.md

When entering a query, you can input: Please help me book a hotel in Hangzhou for April 1, 2025, for one night.

## Contact Us

If you are interested in this topic, please contact us.

The goal of AgentNetworkProtocol is to become the HTTP of the agent internet era. Our vision is to define the connection methods between agents, building an open, secure, and efficient collaborative network for billions of agents.

The ANP open-source technology community currently has 25 developers and is recruiting more. If you are interested in agent communication protocols, whether in development, product, or operations, you can join us to **define agent connections and collaboration in an open-source way**.

Contact information:
- GitHub: https://github.com/agent-network-protocol/AgentNetworkProtocol
- Discord: https://discord.gg/sFjBKTY7sB
- Official website: https://agent-network-protocol.com/
- WeChat: flow10240

Finally, you are welcome to join the agent communication protocol discussion group. This may be the first group in China to discuss agent communication protocols, with over two hundred protocol enthusiasts currently engaged in discussions. (Add me on WeChat to join)






