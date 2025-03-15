
# 一个提示词一个HTTP函数：让开源Manus通过ANP与其他智能体交互

ANP开源技术社区的同学这周完成了一项工作，在两个当下最流行的开源Manus（owl和OpenManus）开源项目基础之上，增加了ANP协议的支持，让开源Manus能够通过ANP访问互联网。（再次感谢社区开发者的贡献！）

我们先在我们开发者社区和智能体通信协议交流社群中小范围的测试了一下，今天正式对外发布。

接入过程看到了ANP不同于mcp的强大之处，只要一个提示词，一个http函数，就可以让智能体与任意智能体进行通信与协作。

第一次跑通之后的感想

AI不但改变了软件的开发模式，也改变了软件的运行模式、协作模式。智能体会加速取代现有软件。



## ANP是什么，和MCP有什么差异

ANP是一个面向智能体设计的开源通信协议，为智能体提供了去中心化的身份认证、基于语义网技术的数据交换与协作。

如果说MCP是模型的USB接口，能够让模型连接到多种资源和工具，那么ANP就是智能体的email，只要有对方的ID，就可以用自己的账号，主动向对方发送请求建立连接。

MCP:
<p align="center">
  <img src="/blogs/images/mcp-usb.png" width="50%" alt="mcp-usb"/>
</p>

ANP:
<p align="center">
  <img src="/blogs/images/anp-email.png" width="50%" alt="anp-email"/>
</p>

相比于MCP，ANP有两大特点，使其更适合智能体通信场景。

1、去中心化的身份认证

类似与email，基于ANP协议和另外一个智能体通信，只需要知道对方ID即可，不用在对方的系统或平台注册账号。这极大的简化了两个智能体之间的协作的成本。

<p align="center">
  <img src="/blogs/images/did-wba-auth.png" width="50%" alt="did-wba-auth"/>
</p>

2、P2P（Peer to Peer，点对点）的协议架构

ANP协议的架构是P2P的，任意一个智能体，都可以主动和另外一个智能体建立连接。

<p align="center">
  <img src="/blogs/images/agentic-web.png" width="50%" alt="agentic-web"/>
</p>


备注：ANP与MCP详细的差异，可以看这篇文章： [MCP与ANP的对比：智能体需要什么样的通信协议](/blogs/cn/MCP与ANP对比：智能体需要什么样的通信协议.md)

## 开源Manus接入ANP后能做什么

开源Manus接入ANP之后，可以通过ANP与其他的智能体进行交互。比如，有一个酒店智能体，提供酒店的查询与预订服务，Manus获得酒店智能体的ADs（Agent Description）之后，就可以通过ANP与酒店智能体进行交互，查询酒店信息、预订酒店。

## ANP的代码接入开源Manus的过程

ANP作为智能体的一种工具接入开源Manus，无论是owl还是OpenManus，都只需要添加anp_tool.py模块即可。

anp_tool.py的代码非常简单，核心是一个工具描述（用于提示词中）、一个http函数（用于处理ANP请求）。

**工具描述如下：**

```plaintext
Use Agent Network Protocol (ANP) to interact with other agents.
1. For the first time, please enter the URL: https://agent-search.ai/ad.json, which is an agent search service that can use the interfaces inside to query agents that can provide hotels, tickets, and attractions.
2. After receiving the agent's description document, you can crawl the data according to the data link URL in the agent's description document.
3. During the process, you can call the API to complete the service until you think the task is completed.
4. Note that any URL obtained using ANPTool must be called using ANPTool, do not call it directly yourself.
```

这段描述的核心是告诉模型：从一个智能体描述文档URL开始，下载文档，根据文档描述中的信息以及自己的任务，使用文档中的URL进一步的爬取新的文档或API。中间可以调用文档中的API。以此不断的搜索智能体对外公开的信息，直到任务完成或判定结束。

**http函数如下：**

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

http函数的核心就是一个http请求发送接口，唯一不同的是发送的过程中，使用到了ANP协议的身份认证机制。

<p align="center">
  <img src="/blogs/images/anp-interaction-flow.png" width="75%" alt="anp-interaction-flow"/>
</p>

**智能体身份：**

在测试脚本中，我们为Manus生成了一个用于测试的DID身份"did:wba:agent-did.com:test:public"，DID文档和私钥保存在文件夹"did_test_public_doc"中。

这是一个公开的测试DID，任何人都可以使用它体验ANP协议，但是无法用它预订产品。如果你想进一步体验全部的产品，欢迎联系我们。

## 接入过程与MCP的差异

上面是接入ANP协议的所有过程，并且只需要接入一次，就可以与任意类型的智能体进行交互，所需要更改只有用户的意图以及智能体描述文档URL。

这正是ANP协议设计的简洁之处：
- 智能体与智能体之间完全解耦，不需要知道对方内部设计与实现
- 通过语义网技术，为数据添加语义描述，让AI能够更好的理解数据
- 通过Linked-Data技术，让数据连接成一个数据网络，便于AI进行数据爬取

ANP协议没有MCP的资源、工具、提示词、文件、sampling等概念。ANP最核心的概念是智能体描述文档，描述文档中可以包含智能体对外提供的信息与接口。

由于ANP完全是一个网络协议，本地只要安装ANP的SDK agent-connect包即可，其他都无需安装。

除此之外，我们在发布的第一天就支持了去中心化的身份认证，两个智能体通信，无需在对方系统中申请账号，直接用自己的账号就可以与对方通信。这也是MCP所不具备的。

owl调用MCP的过程可以参考这里做一个对比：https://mp.weixin.qq.com/s/i6tbSc5fspkV9qxFotZEKw。












