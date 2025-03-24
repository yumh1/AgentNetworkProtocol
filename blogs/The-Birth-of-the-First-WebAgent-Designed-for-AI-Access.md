# The Birth of the First WebAgent Designed for AI Access

An increasing number of **agents** are attempting to directly acquire information from the internet. Currently, there are many technologies available, such as Computer Use and Browser Use. However, traditional websites are primarily designed for human users, and AI often needs to simulate human browser behavior (like parsing HTML pages as a crawler would), which is inefficient and complex.

To address this issue, we might need to construct a **WebAgent**.

This article will introduce what a WebAgent is, the significance and technical details of the first WebAgent going live, how to discover and interact with a WebAgent, the identity authentication mechanism of WebAgents, and provide code examples for integrating related protocols. Finally, it will discuss how to build a data network specifically designed for AI.

## What is a WebAgent

A WebAgent is an agent built using existing web infrastructure (such as PKI, DNS, HTTP, CDN, search engines, etc.) that operates on the web, aiming to allow other agents to access and interact with it via the web. Unlike traditional websites designed with human users at the core, WebAgents are designed specifically for AI, providing publicly accessible information that is readable and understandable by AI, and offering interfaces in various formats, including structured and natural language, without requiring a user interface.

Compared to traditional websites, WebAgents have the following notable differences:

- **Different Target Audience**: Traditional websites primarily serve human users who access and interact through browsers, whereas WebAgents are designed specifically for AI, allowing other agents to access and interact with them via the web.
- **Structured Data Format**: WebAgents return data in structured formats (such as JSON, YAML, etc.), making it easy for AI to directly read and process, while traditional websites usually return HTML, which requires additional parsing to extract the needed information.
- **Self-Descriptive Capability**: Each WebAgent provides a description file that details its functions, interface formats, and invocation methods, making it easier for other agents to understand how to interact with it.
- **Identity Verification Mechanism**: WebAgents have built-in support for identity verification of the accessing party to prevent misuse of information and interfaces. Existing websites often face issues with information being freely crawled by web crawlers.

For AI, the emergence of WebAgents is of great significance. In the past, AI needed to simulate human browsing to access web information, which was complex and inefficient. WebAgents, designed as "native websites" for AI, allow AI to obtain data or perform tasks directly through standard interfaces, similar to calling application services. This enables AI to utilize internet information more efficiently and accurately, and developers can optimize services specifically for AI, no longer limited to human browsing modes. WebAgents will become foundational components in building the Agentic Web, allowing AI to communicate and collaborate directly.

## The Birth of the First WebAgent

We have developed the first ANP-based WebAgent, which is an agent website providing weather information services.

As a demonstration, this WebAgent adheres to AI-native design while also adding a simple homepage to allow human developers to intuitively understand its existence (although a homepage interface is unnecessary for AI).

The following image shows a schematic of the WebAgent's homepage, which you can also view by visiting https://agent-weather.xyz/:

![WebAgent Example](/blogs/images/first-web-agent.png)

*(Image: The first WebAgent — a demonstration interface of the weather agent. In actual interactions, AI will obtain weather data through the provided API interface.)*

This weather WebAgent is named **"Weather Agent"**, featuring a virtual character "Sunny," hosted on a dedicated domain. The design of the Weather Agent fully complies with ANP specifications. Through this example, we will demonstrate how an ANP-based WebAgent operates, hoping to provide a reference for WebAgent developers and users.

It should be noted that, ideally, a WebAgent does not require a human-accessible web interface; AI can communicate with it entirely through protocols. However, to facilitate debugging and help human developers understand the working principles of a WebAgent, the first WebAgent still provides an accessible homepage to showcase its basic information and functionality.
## How to Find a WebAgent

Since WebAgents are not centered around human visitors, how can we **discover and locate** these AI-oriented agent services?

To address this, ANP introduces an **agent discovery mechanism** that allows AI to find WebAgents and their description files under a given domain. Essentially, ANP's agent discovery mechanism is also based on DNS, similar to how websites are discovered.

**1. Active Discovery via Domain and `.well-known` Path:** Similar to how some internet services use the `.well-known` path to provide metadata (e.g., `.well-known/robots.txt`, `.well-known/openid-configuration`), WebAgents follow this approach as well. By convention, each domain hosting WebAgents can provide an **agent list**:

```
https://<domain>/.well-known/agent-descriptions
```
Accessing this path will return a JSON-LD formatted **discovery document**, listing the addresses of all WebAgent description files publicly available under that domain. The detailed definition can be found in the [ANP Agent Discovery Protocol Specification](https://github.com/agent-network-protocol/AgentNetworkProtocol/blob/main/08-ANP-Agent-Discovery-Protocol-Specification.md).

For example, for our weather agent domain `agent-weather.xyz`, accessing **`https://agent-weather.xyz/.well-known/agent-descriptions`** will return content similar to the following:

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "ad": "https://agent-network-protocol.com/ad#"
  },
  "@type": "CollectionPage",
  "url": "https://agent-weather.xyz/.well-known/agent-descriptions",
  "items": [
    {
      "@type": "ad:AgentDescription",
      "name": "天气智能体",
      "@id": "https://agent-weather.xyz/ad.json"
    }
  ]
}
```
The above example indicates that under the domain `agent-weather.xyz`, there is an agent named "Weather Agent," with its description file located at `https://agent-weather.xyz/ad.json` (commonly referred to as the **AD (Agent Description)**). If there are multiple agents, they will all be listed under `items`. This method allows AI to determine which URL to access next to learn more about the agent's details.

Notably, using `.well-known/agent-descriptions` as an entry point means that **as long as the domain is known**, AI can discover the list of WebAgents within it without needing a manually provided specific path. This also facilitates indexing by search engines.

**2. Passive Discovery:** In addition to actively querying the domain's .well-known path, a WebAgent can also submit its information to specialized agent search services or registries, thereby being **passively** discovered. For instance, a WebAgent can submit its description file URL to a public agent search engine, allowing other agents to find it through keywords (such as "weather"). This is a form of passive discovery, enabling a WebAgent to actively **register** itself, thus making it easier for agents within the network to locate each other.

By utilizing the two discovery mechanisms designed by ANP, an agent can easily find the WebAgent it wants to access through a domain or search engine.

## How to Interact with a WebAgent

Once a WebAgent is found, the next step is **how to interact with it**. This requires using the **description file** provided by the WebAgent (i.e., the `ad.json` found above).

The agent description file details the capabilities and interface definitions of the WebAgent, serving as a kind of **manual**. After reading this manual, AI can use the data and interfaces provided within to access the capabilities offered by the agent and communicate with it.

Let's take the Weather Agent's description file [`https://agent-weather.xyz/ad.json`](https://agent-weather.xyz/ad.json) as an example:

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "did": "https://w3id.org/did#",
    "ad": "https://agent-network-protocol.com/ad#"
  },
  "@type": "ad:AgentDescription",
  "@id": "https://agent-connect.ai/agents/travel/weather/ad.json",
  "name": "Weather Agent",
  "description": "Weather Agent providing weather information query services for cities nationwide.",
  "version": "1.0.0",
  "owner": {
    "@type": "Organization",
    "name": "agent-connect.ai",
    "@id": "https://agent-connect.ai"
  },
  "ad:securityDefinitions": {
    "didwba_sc": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "ad:security": "didwba_sc",
  "ad:interfaces": [
    {
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/weather-info.yaml",
      "description": "OpenAPI YAML file providing weather query services."
    },
    {
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/booking-interface.yaml",
      "description": "OpenAPI YAML file providing weather information booking services."
    },
    {
      "@type": "ad:StructuredInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/subscription-status-interface.yaml",
      "description": "OpenAPI YAML file providing weather subscription status query services."
    },
    {
      "@type": "ad:NaturalLanguageInterface",
      "protocol": "YAML",
      "url": "https://agent-connect.ai/agents/travel/weather/api_files/nl-interface.yaml",
      "description": "Interface for interacting with intelligent agents through natural language."
    }
  ],
  "status_code": 200,
  "url": "https://agent-connect.ai/agents/travel/weather/ad.json"
}
```
In the example above, the agent description file is in JSON-LD format. This format uses the common vocabulary provided by Schema.org, ensuring a more consistent and clear understanding of data semantics among different agents. Additionally, WebAgent supplements specific agent interaction specifications through custom extensions, such as the "ad" field.

By parsing these fields, AI can essentially understand how to use this WebAgent. For instance, according to the `ad:interfaces` list of the weather agent, we see several OpenAPI YAML file links, one of which, `weather-info.yaml`, provides the API definition for "weather query services."

Once the AI retrieves this YAML file, it can determine which HTTP interfaces the weather agent supports, such as a possible endpoint defined as `GET /weather?city={city_name}`, and the data format of the returned weather information. If the AI wants to query the weather, it simply needs to construct an HTTP request according to this OpenAPI specification.

**Interaction Example:** Suppose the description file informs us that the weather agent has an interface for obtaining weather information. In that case, the AI can proceed with the following steps:
1. Read the description file to determine the need for DID authentication (if required by `security`) and locate the interface definition for weather queries.
2. Formulate a specific request based on the interface definition. For example, "query the current weather in Hangzhou" corresponds to a GET request: `GET https://agent-weather.xyz/api/weather?city=Hangzhou` (this URL is just an example; the actual endpoint should be determined based on the interface definition file).
3. Include authentication information in the request header (details in the next section), then send the request to the WebAgent.
4. The WebAgent returns structured weather data (e.g., JSON format with temperature, humidity, weather conditions, etc.), which the AI can directly parse for further reasoning or presentation to the user.

Through the description file, AI can progressively understand the capabilities provided by the WebAgent: first discovering available interfaces, then obtaining API documentation based on interface descriptions, and finally calling specific APIs to complete tasks. This design allows **AI to autonomously crawl all machine-readable resources provided by the WebAgent**, completing complex tasks step by step without human intervention.

## Authentication Mechanism for Accessing WebAgent

Considering that WebAgent is aimed at automated AI visitors, open interfaces may face issues of malicious abuse or excessive calls, such as the recent criticism of large model training companies for aggressively scraping website data.

Therefore, **WebAgent typically requires the caller to provide authentication** to ensure that requests come from trusted entities and to manage permissions or quota limits. This is similar to how humans need passwords, API Keys, or OAuth authorization when accessing websites.

However, WebAgent adopts a solution more suitable for the agent ecosystem: an authentication mechanism based on the **W3C DID (Decentralized Identifier)** standard. This allows agents to use their own DID as an identity marker to access WebAgent, without needing each agent to register an account on the counterpart's system.

AgentNetworkProtocol (ANP) has proposed a specific DID method — **`did:wba`** (WebAgent DID). According to the [ANP Authentication Specification](https://github.com/agent-network-protocol/AgentNetworkProtocol/blob/main/03-did%3Awba-method-design-specification.md) (DID:WBA Method Specification), `did:wba` utilizes existing web infrastructure to achieve decentralized identity authentication, specifically designed for authentication between agents. Simply put, each agent (or entity using WebAgent) can have an identity identifier starting with `did:wba:`, for example:  

```
did:wba:example.com:agent:weather123
``` 

This identifier is akin to an email address or user ID, containing domain information. In the WebAgent authentication system, it's somewhat like "the other party only needs to know your DID to verify your identity through existing network infrastructure," without requiring each agent to register an account on the counterpart's system. This greatly simplifies cross-platform AI-Agent collaboration.

The `did:wba` identity authentication process can be summarized as follows:
- **DID Document Publication:** Each DID corresponds to a resolvable DID Document containing verification materials such as public keys. The `did:wba` method specifies that DID documents are hosted at a specific path on the corresponding domain, making them easily accessible via HTTP. For example, the DID `did:wba:agent-did.com:user:alice` can be resolved to its DID document, which includes Alice's public key.
- **Request with Signature:** When an AI agent accesses a WebAgent, if the WebAgent requires DID identity authentication, it will request a signature to prove identity during the request process. Specifically, the requester uses their private key to sign a challenge string or request content and attaches the signature in the HTTP request header (such as `Authorization`).
- **Verification Process:** Upon receiving the request, the WebAgent server extracts the public key from the corresponding DID document provided by the requester to verify the signature's validity, thereby confirming the requester's identity. If the verification is successful, the request is considered to be from the entity represented by the DID, and access or service is granted based on policy. If verification fails, a 401 Unauthorized error is returned.

Since DID is decentralized, **any two agents can trust each other without relying on a centralized user database**. This is somewhat like the email system—sending an email doesn't require registering an account on the recipient's mail server, as long as the recipient can find your domain via DNS and trust the corresponding public key. The emergence of `did:wba` makes identity verification in the WebAgent network flexible and platform-independent. Compared to traditional OAuth or API Key solutions, DID is more suitable for **large-scale, multi-entity** agent ecosystems, as each agent can have its own identity, authenticated once and usable everywhere [of course, to be compatible with existing systems, WebAgent may also support traditional API Key methods, but DID is clearly a future-oriented solution].

**Abuse Prevention and Access Control:** By requiring the caller to provide a DID identity, WebAgent can:
- Allocate call quotas and permission levels for each DID. For example, some sensitive operations can only be called by DIDs with a specific trust level.
- Trace issues back to specific DID identities, rather than being helpless against anonymous crawler traffic.
- Establish a reputation system among agents, where DIDs with bad behavior can be blacklisted, while those with good records may enjoy higher privileges.

Notably, to lower the barrier for developers, the ANP community also provides a **public test DID**. This DID is `did:wba:agent-did.com:test:public`, with its DID document and private key publicly available for testing and experiencing the WebAgent identity authentication process. Anyone can use this pair of public and private keys to attempt calling WebAgents that require identity authentication (for testing purposes only, not for real transactions or sensitive operations).

In actual development, we can quickly verify the WebAgent interface call process by introducing this public test DID. The `use_did_test_public` directory in the [ANP example code repository](https://github.com/agent-network-protocol/anp-examples/tree/main/use_did_test_public) provides the DID document (`did.json`) and private key file (`key-1_private.pem`) for this test DID, along with demonstrations on how to use it. The code examples in the next section will also show how to utilize this test identity to call WebAgent interfaces.

# Tool for Accessing ANP WebAgent

We have developed a tool for interacting with ANP WebAgent called ANP Explorer, available at: https://service.agent-network-protocol.com/anp-explorer/.

![ANP Explorer](/blogs/images/anp-explorer.png)

It has two main functions:
- It can act as a personal AI assistant, allowing interaction through natural language. The assistant uses the WebAgent's description documents to call the WebAgent's interfaces and return results.
- It provides a tool for exploring agent description documents. You can input the URL of an agent description document, and it will fetch the document along with other linked documents.

This tool uses the ANP public test DID (`did:wba:agent-did.com:test:public`) to access WebAgent.

## Code Example: How to Integrate with the ANP Protocol

After understanding the discovery, description, and authentication mechanisms of WebAgent, let's look at a **practical code example** demonstrating how to enable your AI Agent to access WebAgent with simple code. The code is open-source: [anp-examples](https://github.com/agent-network-protocol/anp-examples). This is the code for the ANP Explorer mentioned above.

The good news is that the process is very straightforward—as the community says: "*All you need is a prompt and an HTTP function*" to communicate with any WebAgent.

Let's first look at the prompt, code available at https://github.com/agent-network-protocol/anp-examples/blob/main/anp_examples/simple_example.py:

```plaintext
1. You will receive a starting URL ({{initial_url}}), which is a description file of an agent.
2. You need to understand the structure, functionality, and API usage of this agent description file.
3. You should continuously discover and access new URLs and API endpoints like a web crawler.
4. You can use the anp_tool to retrieve the content of any URL.
5. This tool can handle responses in various formats, including:
   - JSON format: which will be directly parsed into a JSON object.
   - YAML format: which will return text content, and you need to analyze its structure.
   - Other text formats: which will return the raw text content.
6. Read each document to find information or API endpoints relevant to the task.
7. You need to determine the crawling path on your own, without waiting for user instructions.
8. Note: You can crawl up to 10 URLs, and must stop crawling after exceeding this limit.
......
```

This description guides AI models to operate like a crawler, continuously using the anp_tool to fetch documents or interfaces of agents, repeating this process until the required information is obtained.

Next is the HTTP function section. The `anp_tool.py` defines an asynchronous method `execute(...)`, which is responsible for executing actual HTTP requests and handling identity authentication logic.

For specific code, refer to: https://github.com/agent-network-protocol/anp-examples/blob/main/anp_examples/anp_tool.py

As you can see, with the help of `ANPTool`, the communication process between an AI Agent and a WebAgent is as simple as a regular HTTP call. For agents based on large models, simply adding such a tool with ANP functionality to their tool list and prompting the model on how to use it allows them to autonomously perform cross-agent operations.

For example, a dialogue agent with ANP capabilities, when asked by a user to "help me book a hotel in Shanghai for tomorrow," can: first use ANPTool to find a hotel booking agent -> obtain its description and interface -> complete the booking process and return the result to the user. All this is thanks to the standardized, self-descriptive interfaces provided by WebAgent and the simplicity of the ANP protocol.

## Building a Data Network Exclusively for AI Access

With the launch of the first WebAgent, we see a new form of the future internet: a data service network that is **UI-less and open only to AI**. The construction of this network is based on the three key elements introduced in this article:

- **Agent Discovery**: Through standard discovery protocols and `.well-known` entries, AI can automatically index agent services on the internet without the need for manual directories.
- **Agent Description**: Each WebAgent contains its own functional description and interface specifications, enabling AI to autonomously understand how to call services, forming a highly self-descriptive network.
- **Identity Authentication**: Through a decentralized identity (DID) mechanism, it ensures secure and trustworthy network interactions, supporting cross-platform permission management to ensure healthy network operation.

This "AI Data Network" has some notable features:

- **Designed for AI, UI-less**: Services in the network no longer provide pages or graphical interfaces directly to humans; all interactions occur between agents. This eliminates traditional human-machine interfaces, reduces system complexity, and allows network services to focus entirely on data, providing an efficient data exchange environment for AI.
- **Semi-structured Data**: The data provided by WebAgent is primarily in structured formats (such as JSON, YAML), facilitating rapid parsing and processing by AI agents; it also uses natural language expressions locally to carry personalized descriptive information, helping agents better understand service content or express personalized features.
- **Self-descriptive Capability**: WebAgent comes with standardized description files that detail the services provided, interface definitions, and calling methods. When discovering services, AI agents can autonomously understand the specific functions and interaction methods of the services without human intervention or additional interface documentation.
- **Secure and Reliable**: Considering that WebAgent is aimed at automated AI visitors, open interfaces may face risks of malicious abuse or excessive calls (such as the recent criticism of large model companies' rampant web data crawling). Therefore, WebAgent is equipped with identity verification and permission management mechanisms based on decentralized identity (DID) to effectively prevent data misuse and ensure interface security. By tracking identities and authorizing access, a trustworthy agent network environment is established.

It is imaginable that in the near future, data and services from various industries may be open to AI in the form of WebAgents: weather, news, knowledge bases, trading platforms, merchants... AI will become the primary "user," directly completing tasks that we currently accomplish through apps or web pages via network interfaces. Human users will collaborate with AI, allowing AI to call these WebAgents to achieve complex goals.
