# Comparative Analysis of Open-Source Agent Communication Protocols: MCP, ANP, Agora, agents.json, LMOS, and AITP

During the development of agent communication protocols, I have collected various existing protocols in the industry and conducted an analysis using OpenAI's deepresearch. The analysis covers aspects such as target problems, key technologies, applicable scenarios, technical architectures, compatibility and extensibility, open-source ecosystems, and future development prospects. While some details may not be entirely precise, this analysis serves as a valuable reference.

Our team initiated the design and development of an open-source agent communication protocol early last year. As one of the earliest teams researching this field, we have clearly observed a significant increase in attention and interest over the past two to three months.

We warmly invite you to follow our open-source project and join our community. Whether you are an individual developer or a company in the AI industry, your participation is highly welcomed. The vitality of agent communication protocols depends on collaborative industry efforts.

Contact us:
- Email: chgaowei@gmail.com  
- GitHub: [https://github.com/agent-network-protocol/AgentNetworkProtocol](https://github.com/agent-network-protocol/AgentNetworkProtocol)
- Discord: [https://discord.gg/sFjBKTY7sB](https://discord.gg/sFjBKTY7sB)  
- Official Website: [https://agent-network-protocol.com/](https://agent-network-protocol.com/)  
- WeChat: flow10240

## MCP (Model Context Protocol)

### Target Problem
Focused on **Large Language Model (LLM) Context Integration**:
- Addresses the difficulty of integrating AI models with external data sources and the fragmentation of context.
- Provides a unified standard enabling LLMs to conveniently and securely access various content repositories, tools, and environments, breaking data silos and avoiding customized integrations for each data source.

### Key Technologies

**Open RPC Framework**:
- Defines standard request/response/notification message formats based on JSON-RPC 2.0.
- Introduces a **capability negotiation** mechanism, allowing clients and servers to dynamically agree on supported protocol features (including fine-grained sub-features), enhancing flexibility and extensibility.
- Currently supports local bidirectional streaming communication (e.g., standard IO pipes, HTTP+SSE streaming output); remote communication features such as identity authentication and service discovery are planned.
- Conceptually serves as a "USB-C interface" for AI applications.

### Applicable Scenarios

**AI Application Integration**:
- Suitable for scenarios requiring embedding LLMs into business systems and rapidly connecting to multiple data sources and tools, such as enterprise knowledge base Q&A, programming assistants integrating with code repositories/IDEs, and office assistants accessing calendars and emails.
- Through MCP, developers can provide LLMs with unified interfaces to databases, cloud documents, development environments, etc.
- Currently primarily used in **local or intranet** environments for agent integration with internal tools; with future remote support, it can extend to cross-service cloud agent integrations.

### Technical Architecture

**Client-Server Architecture**:
- MCP treats the AI model as the client and external data sources as MCP servers.
- Both sides exchange predefined JSON messages, similar to RPC calls.
- The transport layer currently supports **local pipes** (standard input/output streams) and **HTTP persistent connections with SSE** (Server-Sent Events unidirectional streams) for request/response or streaming messages.
- Each transport method has specific message exchange requirements.
- Currently limited to local or intranet communication to ensure simplicity and security (no remote identity issues without external connections).
- Future plans include remote connectivity capabilities involving authentication, authorization, service discovery, and stateless operations.
- Thus, MCP architecture favors **one-to-one** communication between models and resource services, similar to plugin calls, and does not handle multi-agent routing.

### Compatibility and Extensibility

**Easy Integration**:
- MCP employs common technologies like JSON and HTTP, ensuring high transparency and ease of local deployment. Claude and other models already support MCP clients.
- Anthropic has open-sourced the specification and SDK, providing MCP server examples for popular systems (Google Drive, Slack, GitHub, etc.) for straightforward integration.
- Due to its open nature, other large models (including open-source LLMs) can implement MCP, making it cross-model compatible.
- Currently lacking remote invocation capabilities, but future additions of authentication and networking will enable adaptation to microservices and cloud APIs.
- Its **capability negotiation** mechanism allows adding new functional modules without breaking compatibility, enabling existing clients to negotiate and utilize new features, thus ensuring good extensibility.
- Overall, MCP integrates easily with existing systems (especially REST-style services) and can serve as a standard component for LLM plugins.

### Open Source and Ecosystem

**Anthropic Open Standard**:
- MCP specifications and partial SDK implementations are publicly available.
- Anthropic has integrated local MCP server support into the Claude desktop application, demonstrating data integration.
- The initial ecosystem includes early adopters such as Block and Apollo, and developer tool companies like Zed, Replit, Codeium, and Sourcegraph are collaborating to enhance code-related agents using MCP.
- The community maintains MCP specifications on GitHub, and third-party tools (such as open-source MCP visualization management clients) have emerged.
- Released at the end of 2024, the ecosystem is still in its early stages but has attracted significant attention, with strong support and active discussions (e.g., Reddit developer discussions on MCP breakthroughs).
- MCP is released under an open license, encouraging community contributions to transport mechanisms and server implementations.
- With future remote capabilities and broader LLM compatibility, the MCP ecosystem is expected to expand into an "LLM plugin marketplace."

### Future Prospects

**Short-term Lead, Awaiting Expansion**:
- Backed by Anthropic and early adopters, MCP is expected to become one of the de facto standards for LLM tool integration in the near term.
- As remote capabilities are added, MCP may quickly expand its applicability and establish a foothold in enterprise applications.
- Its advantages lie in its **simplicity and practicality**, being developer-friendly and supported by major companies.
- However, in the long run, MCP currently lacks decentralized identity and multi-agent interaction capabilities, which may limit its ability to build large-scale agent networks.
- If Anthropic and the community continue to iterate and add modules such as identity authentication, MCP may evolve into a more general protocol.
- Overall, MCP has a bright future in the field of **LLM context integration**, potentially becoming the "USB interface of the AI era"; however, it will need to collaborate with other protocols to achieve the grand vision of agent interconnectivity.

## ANP (Agent Network Protocol)

### Target Problem
Focused on **Agent Interconnectivity**:
- Solves the problem of communication and collaboration among multiple agents, with the vision of being the "HTTP for agents."
- Tackles the challenges of identity trust and connectivity in agent networks, enabling direct communication across platforms and supporting agents in autonomously forming networks for collaborative work.

### Key Technologies

**Three-layer Architecture + Decentralized Identity**:
- Utilizes the **W3C Decentralized Identifier (DID)** standard to build the identity layer, achieving trustless authentication and end-to-end encrypted communication.
- Designs its own DID method, using cryptography to replace central authorities, balancing decentralization with large-scale deployment.
- Introduces a **meta-protocol layer**, a "protocol of protocols," allowing agents to automatically negotiate communication protocols using natural language and generate application layer protocol code, enabling autonomous interfacing and protocol upgrades.
- Features a complete stack of capabilities including identity authentication, encrypted communication, meta-protocol negotiation, and application layer protocol description.
- Agents can leverage LLMs to autonomously organize networks and negotiate communication schemes, achieving self-organizing network collaboration without human intervention.

### Applicable Scenarios
**Multi-Agent Collaboration**:
- Suitable for building **decentralized agent networks**, such as personal AI assistants directly communicating with third-party service agents, IoT device intelligent agents negotiating actions, or multiple autonomous agents forming alliances to complete complex tasks.
- Particularly suitable for scenarios with high security requirements and lacking a unified trust center (e.g., cross-platform personal data integration) due to its support for identity authentication and encryption.
- Can also be used in research agent communities, allowing agents from different teams to interact according to open protocols.

### Technical Architecture

**Peer-to-Peer Mesh**:
- ANP adopts a **decentralized P2P** approach, allowing agents to establish encrypted communication connections directly.
- Trust is established through DID identity exchange and verification, followed by negotiation of communication protocols and formats.
- The architecture is divided into three layers: the **identity and encryption layer** ensures secure and trustworthy channels; the **meta-protocol layer** handles automatic negotiation of application protocols between agents (or multiple agents); the **application protocol layer** executes specific business data exchanges, with agents selecting or generating the protocol for this layer based on semantic descriptions.
- This architecture allows the agent network to be loosely coupled like a human network: no single point of failure, with agents discovering and connecting to each other.
- Implementation can run on existing web infrastructure (e.g., WebSocket or P2P libraries), with an official AgentConnect implementation providing the framework.
- The network topology supports **multi-hop networking**, allowing agents to dynamically find other agents that meet certain conditions for collaboration, not limited to centralized servers.

### Compatibility and Extensibility

**Open and Comprehensive**:
- ANP is fully open-source (providing specifications and reference implementations), designed to integrate with existing web standards (e.g., based on DID standards, semantic web).
- Supports various agent frameworks, as long as they implement identity authentication and the meta-protocol layer, they can join the ANP network.
- Its **layered structure** is clear, with each layer replaceable or upgradable (e.g., future use of new encryption algorithms, addition of new application layer protocol types).
- Through **semantic capability descriptions**, third parties can define new agent capabilities and recognize and utilize them during negotiation.
- In terms of compatibility, ANP's protocol documents and code are available in both Chinese and English, lowering the integration threshold.
- Due to its decentralized design, it does not rely on specific platforms, allowing internet participants to implement their own ANP agents.
- Theoretically, it can also bridge existing protocols: existing services that implement agent proxies and support DID authentication can communicate with ANP proxies.
- Therefore, ANP can smoothly expand into a large network, with the bottleneck being industry adoption rates.

### Open Source and Ecosystem
**Pioneering Domestic Open Source**:
- ANP is developed and open-sourced by a Chinese team (including Chang Gaowei), with specifications and code publicly available on GitHub.
- As one of the earliest proposed agent communication protocols, it has attracted attention in the domestic AI development community, being called the industry's first true agent communication protocol.
- The current ecosystem includes an AgentConnect implementation framework and a supporting DID method specification.
- The community mainly communicates domestically, with multiple analysis tutorials on platforms like CSDN.
- However, its global recognition is relatively limited, requiring more international developers to participate.
- ANP keeps pace with the cutting edge (its meta-protocol concept aligns with Oxford's Agora), and if it can gather a community to improve standards and provide multi-language SDKs, it may become an important part of the Agentic Web.
- Its open-source license is friendly, welcoming commercial and personal use.
- Domestically, ANP is expected to form an ecosystem with local large models/applications; internationally, it needs promotion to attract developers to join the ecosystem and achieve truly global agent network interconnectivity.

### Future Prospects

**Technically Comprehensive, Ecosystem Needed**:
- ANP is ahead in concept, solving identity trust and automatic negotiation challenges in advance, with **high technical maturity** (achieving end-to-end network communication).
- This gives it an edge in the future open agent network competition.
- If widely adopted, ANP has the potential to become the underlying communication framework for the Agentic Web.
- However, currently, ANP is mainly driven by a domestic team, with relatively weak international influence, making **ecosystem scale** a concern.
- The future advantage depends on: first, whether it can attract more developers and organizations to join and improve the ecosystem; second, whether major companies will support the DID route.
- If decentralized agent networks become a trend (e.g., the web moving towards decentralized identity), ANP will shine.
- Conversely, if giants prefer proprietary protocols, ANP may become a niche standard.
- Considering that the MCP team is also aware of the importance of open identity, ANP's leading design is likely to be referenced or integrated, maintaining its leading position.

## Agora (Oxford University Meta-Protocol)

### Target Problem
Focused on the **Three Dilemmas of LLM Agent Networks**:
- Attempts to achieve high **versatility, efficiency, and portability** in communication simultaneously.
- Proposes using the capabilities of large models to adapt to different scenarios, constructing a scalable "world-class LLM agent network" to address the current isolation and difficulty of intercommunication among models.

### Key Technologies
**LLM-Driven Meta-Protocol**:
- The core innovation is the **Protocol Document (PD)** mechanism, describing communication protocols in plain text.
- Agents can use protocol descriptions as transferable objects, uniquely identified by hash values without central registration.
- Leveraging the three major capabilities of LLMs: natural language understanding and generation, code writing following instructions, and autonomous negotiation in complex contexts, Agora allows agents to adopt different communication formats for different scenarios.
- Common high-frequency interactions are handled using existing efficient protocols/routines to improve efficiency; for uncommon or non-standard protocol scenarios, agents negotiate new protocol schemes using structured data or natural language, dynamically generating and executing corresponding routines with LLMs.
- This adaptive layering achieves a balance of **high versatility** (almost any content can be exchanged), **high efficiency** (optimized common paths), and **high portability** (LLMs handle negotiation and implementation without human intervention).

### Applicable Scenarios

**Cutting-Edge Research and High-Complexity Tasks**:
- Agora is currently validated mainly in academic experimental scenarios.
- Suitable for multi-agent environments requiring **highly flexible protocols**, such as research-oriented multi-agent systems, allowing agents to evolve communication methods autonomously.
- For example, agents dynamically negotiate the optimal communication method to improve collaboration efficiency for different task requirements or create communication protocols on the fly to solve new problems in unknown environments.
- This is valuable in **AGI research** and large-scale agent simulations.
- In the short term, Agora is more for **proof of concept**, such as experimenting with whether LLMs can automatically generate protocols to solve specific tasks (the paper demonstrates two scenario experiments).
- If matured in the future, it can be applied to agent networks with high scale and heterogeneity, as it does not require pre-standardizing all interactions.

### Technical Architecture

**Adaptive Layered Protocol Stack**:
- Agora is not a fixed network topology protocol but provides agents with a strategy to switch communication methods at different abstraction layers.
- It can be understood as implementing a **"protocol router"** within the agent: when Agent A communicates with B, it first checks if there is an applicable efficient established protocol (PD known and implemented by both parties), and if so, directly adopts it (e.g., standard API calls or custom binary protocols).
- If not, it falls back to **structured data exchange**, such as JSON-based round trips, with necessary parsing and construction routines dynamically written by LLMs.
- If further complexity or negotiation issues arise, it degrades to **natural language communication**: the two agents directly describe needs and data in human language generated by LLMs, with the counterpart LLM parsing and executing.
- This architecture essentially **dynamically selects** communication protocols at the application layer, while the underlying layer still requires basic connectivity (assumed to transmit text streams through existing networks/sockets).
- Agora treats the protocol itself as negotiable content, reaching consensus by exchanging protocol documents (PD) before specific data exchange.
- Therefore, the topology is essentially **peer-to-peer communication** (any agent can converse), running on existing networks, but with highly flexible communication content layers.
- Agora is called a "zero-layer protocol," meaning it coordinates various specific protocols at the meta-layer, providing a foundation for high-level collaboration between LLMs.

### Compatibility and Extensibility

**Proof of Concept Stage**:
- Agora originates from academic papers and currently lacks mature industrial implementations, with portability theoretically compatible with various protocol descriptions (most existing RFCs can be used as PDs).
- Therefore, if implemented, it can directly utilize a large number of existing protocol standards, with agents only needing to obtain the corresponding PD text and have the capability to execute/parse.
- Extensibility is almost unlimited: any new protocol can be included in the system as long as it is described in text, with LLMs responsible for understanding and deploying.
- However, this also requires strong LLM capabilities to correctly generate and parse protocol code.
- Current compatibility mainly depends on agents having sufficient knowledge and tool libraries to execute LLM-generated protocols (e.g., if Python code is generated for communication, the agent environment must be able to run it).
- Agora avoids centralized protocol ID registration, using hash identifiers to reduce global coordination needs.
- As agent interactions increase, a protocol document sharing library (decentralized distribution) may form.
- Overall, Agora is designed to accommodate all communication paradigms, but before unified implementation, different teams' experiments may be fragmented.
- The current ecosystem is mainly **research community** focused, with its open-source status depending on the paper authors' team; if open-source code is later implemented and uploaded to GitHub, it will officially start the developer ecosystem.
- In the long run, once LLMs are fully capable of automatic protocol generation, this architecture can adaptively expand to any new device and communication need.

### Open Source and Ecosystem

**Academic Leadership**:
- Agora originates from an Oxford University team paper (submitted in October 2024), with the current ecosystem mainly consisting of academic discussions and evaluations.
- The Machine Learning community has responded well to its definition of the "three dilemmas" and solutions, with some discussions on Reddit focusing on its innovation.
- However, there is no open-source framework implementing Agora's ideas yet—possibly due to its reliance on newer LLM capabilities.
- Without code, the ecosystem remains theoretical.
- Some researchers may experiment based on the paper, using GPT-4 and other models to verify partial functionality.
- This belongs to **cutting-edge exploration**, with no commercial applications joining the ecosystem in the short term.
- However, its concept may influence other projects: for example, ANP's meta-protocol part reflects similar ideas, which can be considered an ecosystem response.
- If Agora proves effective, future agent frameworks may incorporate its ideas, adding LLM's flexible protocol adaptation as a feature without necessarily fully adopting the Agora architecture.
- As an open paper, its concept is available to anyone without restrictions.
- If the authors or open-source community later implement reference code and upload it to GitHub, it will formally start the developer ecosystem.
- Currently, it mainly builds an "ecosystem" at the level of **paper citations and academic discussions**.

### Future Prospects

**Grand Vision, Challenging Path**:
- Agora represents a highly forward-looking direction—allowing AI to autonomously define communication methods, thus breaking human-imposed protocol limitations.
- In the **distant future**, if agents reach higher intelligence levels, Agora's adaptive communication may become the default: agents do not need human-defined rules, autonomously creating optimal interaction protocols for task collaboration, truly achieving self-organizing machine society.
- Therefore, Agora's concept has profound significance for the AGI era, seen as a prototype of future high-level protocols.
- However, its short-term prospects are limited: constrained by current LLM capabilities and reliability, Agora's solution is difficult to implement in real-world environments.
- It may first be applied in research simulations, providing references for subsequent protocols (ANP's design already reflects similar idea integration).
- If LLM technology and automatic code execution technology make breakthroughs in the next few years, Agora may move from paper to implementation, possibly under a new name and standard.
- It is foreseeable that major companies are also paying attention to this idea and may secretly experiment in their agent systems.
- At the standard level, if Agora proves successful in the future, it may inspire the formulation of **new generation protocol standards**, incorporating the "three dilemmas" concept into protocol design.
- In summary, Agora is more like a **key concept in the future game**, with its advantages gradually manifesting in long-term competition: when scenarios that traditional protocols cannot cover arise, it provides a solution.
- So, although it is not the main player in the arena right now, in the long run, the paradigm created by Agora may profoundly influence later players and even ultimately win out as the foundation of agent communication.

## agents.json

### Target Problem
Focused on **Agent Accessibility for Websites/Services**:
- Provides an open standard for websites to declare how they can be discovered and interacted with by autonomous agents.
- Solves the current problem of AI agents needing to crawl human interfaces and lacking machine-readable interfaces, by allowing sites to explicitly provide agent-friendly interface locations, permission requirements, and interaction rules through the `agents.json` file.
- Also introduces an agent identity verification mechanism to reduce risks from unknown automation.

### Key Technologies

**Web Declarative Standard**:
- Inspired by `robots.txt`/`sitemap.xml`, defines **agent interfaces** in a machine-readable JSON file.
- Includes site information, available API endpoints and their input/output modes, authentication methods (e.g., OAuth2), required permission scopes, usage policies (rate limits, terms of service), etc.
- Available for agent automatic discovery through a conventional path (e.g., `/.well-known/agents.json`).
- Supports version fields and custom extensions to ensure evolutionary compatibility.
- Can also link to **agent identity** verification mechanisms, allowing sites to require agents to declare their identity and permissions.
- Overall provides structured **capability declarations**, reducing ambiguity and friction in parsing web pages.

### Applicable Scenarios

**Agentic Web**:
- Applied to **websites/open APIs** that wish to open services to AI agents.
- Any online service (e-commerce, travel booking, government data interfaces, etc.) can declare machine interfaces through `agents.json`, allowing agents like AutoGPT to directly discover functional endpoints and call them, rather than simulating human clicks on web pages.
- Also applicable to **enterprise internal API directories**: companies can list departmental service interfaces through `agents.json`, facilitating automatic discovery and integration by internal AI agents.
- In summary, `agents.json` is a web-level protocol suitable for a wide range of industries, as long as a website wishes to be efficiently accessed by AI.

### Technical Architecture

**Declaration + Standard Interface**:
- `agents.json` itself does not define communication channels but integrates into the existing web architecture.
- Typically, agents first **GET the `/.well-known/agents.json`** file via HTTP (possibly in the site root directory or well-known path).
- The file content describes available API endpoints (often HTTP RESTful interfaces, GraphQL, or WebSocket endpoints) and how to call them, so the actual communication mode depends on the interfaces listed in the file.
- For example, the file may indicate that the agent should call a URL to submit an order via POST or subscribe to messages via a WebSocket.
- Therefore, `agents.json` serves as a **metadata layer**, with the upper layer's actual communication possibly using RPC, REST, or message queues.
- It can also reference **open API documents** or schemas, allowing agents to construct requests according to the given data format.
- The entire architecture is highly compatible with the web: find the site through DNS -> get `agents.json` -> interact according to the defined interface standards.
- Thus, communication can be **client-server** (agent as client calling service APIs) or potentially extend P2P elements in the future (e.g., `agents.json` pointing to decentralized service addresses).

### Compatibility and Extensibility
**Web-Friendly**:
- `agents.json` is a lightweight extension to websites, using a standard HTTP file format, making it **extremely easy to integrate**: site developers only need to write the JSON declaration (partially generated from their own OpenAPI documents) and host it at a fixed URL.
- For client agents, parsing JSON is much simpler than parsing HTML, and many existing HTTP libraries can handle retrieval.
- **Compatible with existing identity systems**: can reference existing OAuth2 authentication processes on the site.
- **No dependency on tools and frameworks**: any language agent can read JSON and call HTTP interfaces according to the descriptions, using existing network protocols—no special runtime library required.
- Highly extensible, the standard allows for custom fields/namespaces to experiment with new features, while including version fields to prevent parsing errors by older agents.
- As it is still in the proposal stage, community support is needed to reach a consensus or establish a W3C standard.
- Once standardized, its ecological potential is immense: browser vendors, crawlers, and agent frameworks could support automatic discovery of agents.json to enhance automation.

### Open Source and Ecosystem
**Draft Proposal Stage**:
- Currently, agents.json is merely a conceptual proposal.
- Ideas have been collectively proposed by the community (Reddit discussions and the AgentProtocol community) but have not been formally finalized.
- There is no official organizational endorsement yet, but it may be discussed in W3C or the Open Web Alliance.
- Nevertheless, its simple and feasible concept has already attracted some developers' attention.
- Similar ideas have also appeared in some media articles, sparking discussions on agent crawler friendliness.
- Due to low implementation costs, some cutting-edge websites might experiment with releasing agents.json.
- If grassroots practices form, standard organizations might facilitate the establishment of norms.
- The current ecosystem is mainly focused on advocacy and discussion, with potential example repositories or JSON schema drafts available on GitHub.
- Unlike MCP, which requires bilateral implementation, agents.json relies more on **site support**: only with widespread site adoption can the agent ecosystem truly thrive.
- If major content providers (search engines, social platforms) adopt it first, it will significantly boost the ecosystem.
- Open-source agent projects (like AutoGPT) starting to automatically search for agents.json could also pressure sites to follow suit.
- Overall, its ecosystem development depends on **bidirectional** support: site willingness and agent tool support.

### Future Prospects
**Potential Web Standard Complement**:
- The concept of agents.json is simple yet significant, aligning with the web's evolution from "human-oriented" to "agent-oriented."
- In the future, if **large model agents become widespread**, sites will have to consider machine visitors, and an agent protocol similar to robots.txt is likely to emerge.
- Agents.json perfectly fills this gap, with advantages in **compatibility with existing networks** and low deployment costs, making it easy to become an industry consensus.
- It is anticipated that in the near future, with community promotion, W3C might propose an official standard with browser/search engine support, establishing the position of agents.json.
- It will not replace other communication protocols but will exist widely as a **complementary standard**: for example, agents using MCP or AITP can check agents.json to determine the calling method before accessing web services.
- In the long run, agents.json is almost certain to integrate into the agent ecosystem, with its prospects depending on the speed of adoption and detail formulation. It can be said that it has a **high chance of success** in the future, likely becoming a standard configuration file for "agent-friendly websites."

## LMOS (Language Model Operating System)

### Target Problem
Aimed at **Multi-Agent System Infrastructure**:
- Committed to creating an open multi-agent platform and ecosystem, reducing development and deployment complexity.
- Addresses issues of incompatibility, expansion difficulties, and complex scheduling management among various agent platforms.
- Provides a unified environment akin to an operating system, enabling heterogeneous agents to easily discover each other's capabilities and efficiently communicate and collaborate on tasks.
### Key Technologies
**Open Multi-Agent Architecture**:
- Provides an **Agent Description Format** to standardize the description of agent/tool capabilities and metadata, ensuring cross-platform interoperability through semantic abstraction.
- Implements a **Discovery Mechanism**: local discovery via mDNS broadcast and cross-network discovery through a **central registry**.
- Offers an **Agent Registry** serving as a directory service, supporting capability metadata-based searches to match suitable agents.
- The communication protocol is flexible and pluggable, not enforcing a single transport method, allowing agents to choose the best option such as HTTP, message queues (MQTT/AMQP), or P2P based on their needs.
- Supports **Agent Group Management**, enabling collaborative operations within trusted groups.
- Also provides the **Agent ReaCtor** framework to abstract LLM, memory, and tool interfaces, acting as a virtual "operating system" kernel for agents.
- Intelligent task scheduling is achieved through NLU-driven routing and task allocation to the most suitable agents.

### Applicable Scenarios
**Enterprise-Level Multi-Agent Systems**:
- LMOS is suitable for scenarios requiring the **deployment and management of large-scale intelligent agents**, such as numerous conversational agents in call centers, clusters of customer service assistants, or the collaboration of agents with different expertise in large automated workflows.
- Particularly effective in multi-channel (web, mobile, voice IVR) agent services requiring elastic scaling, where LMOS's cloud-native architecture can be advantageous.
- Also applicable for **R&D testing** of multi-agent ecosystems, experimenting with the collaboration of different agent frameworks on a unified platform.
- Emphasizing vendor lock-in avoidance, enterprises or research institutions can integrate existing agents like LangChain and LlamaIndex into LMOS for unified management.

### Technical Architecture
**Cloud Cluster + Bus**:
- The LMOS architecture includes a **control plane** and **runtime**.
- The control plane comprises a central **Agent Registry Service** and **Scheduler Router**.
- Each agent (which can be implemented by different frameworks) registers its capability description and communication address with the registry upon startup.
- The Router matches the task content parsed from natural language to the appropriate agent, performing **RPC calls or message delivery**.
- LMOS supports **WebSocket subprotocols** for agent communication (indicating that its documentation includes WebSocket subprotocol specifications) and HTTP interfaces.
- Within the cluster, agent communication may occur through a publish/subscribe message bus or direct network calls, with LMOS handling protocol conversion and ensuring reliable delivery.
- The topology is mostly **star-shaped**: the central Router receives user requests or agent messages, then routes them to the target agent or broadcasts to the group.
- For local networks, mDNS allows agents to discover and connect directly for simple communication; across subnets, the registry center acts as an intermediary.
- LMOS runtime is based on Kubernetes, with agent instances horizontally scaling as containers.
- It provides **lifecycle management** (e.g., rolling upgrades, canary releases) to ensure system stability.
- The overall communication model supports both **request-response** (Router->Agent->Router) and **event-driven** (agent pushes messages via Router to subscribers).

### Compatibility and Extensibility
**Cross-Framework Interoperability**:
- LMOS is designed with open standards, supporting the integration of agents from different languages and frameworks.
- Officially adapted frameworks like LangChain, Langchain4j, and LlamaIndex can seamlessly run as LMOS agents.
- Utilizing common cloud technologies like Kubernetes, it is friendly to operations teams.
- The **modular** design offers rich extension points: developers can extend new tool interfaces, scheduling strategies, or custom protocol support.
- For example, a custom message queue system can replace the default communication, or custom monitoring can be added.
- LMOS's **observability** and **security/privacy** modules ensure compliance with enterprise requirements.
- Through standard description formats and registration APIs, it can exchange agent metadata with external existing systems, even interfacing with other agent platforms (theoretically, different LMOS deployments can also interoperate).
- The only barrier is LMOS's relatively comprehensive and large system, requiring some architectural adjustments for introduction, but in the long run, it avoids vendor lock-in and is conducive to expansion.
- Its **scalability** is designed to add hundreds or thousands of agent nodes as the business grows without changing the architecture.

### Open Source and Ecosystem
**Eclipse Foundation Incubation**:
- As an Eclipse open-source project, LMOS has enterprise credibility.
- Currently in the incubation stage, core code and documentation are open on the Eclipse platform.
- Supported by enterprises and community developers, the Eclipse official site provides detailed documentation and vision statements, indicating its ambition.
- Ecologically, LMOS focuses on integrating existing open-source agent frameworks, effectively incorporating other projects' achievements into its ecosystem (e.g., ARC framework, various LLM adaptations).
- Therefore, it acts more like an **ecosystem integrator**.
- There are no large-scale application cases publicly available yet, mostly proof-of-concept and pilot projects (possibly within some companies).
- As the multi-agent concept gains traction, the LMOS community may attract more contributors to write adapters and deployment cases.
- Eclipse's endorsement also facilitates adoption by governments and enterprises.
- If an **alliance** forms (e.g., multiple vendors interacting based on LMOS standards), the ecosystem will steadily expand.
- Currently, the official team is actively promoting the LMOS concept, publishing blogs and documentation to attract developers.
- In the long term, its ecosystem's success depends on becoming a de facto standard: if integrated by major AI companies or cloud providers as an agent management layer, LMOS will receive continuous community resource support.

### Future Prospects
**Great Potential but Requires Collaboration**:
- LMOS outlines a comprehensive blueprint for a multi-agent operating system, aligning with future enterprise and cloud needs for large-scale agent management.
- Its **advantage lies in comprehensiveness**: covering a one-stop solution from development framework to deployment and operations, significantly lowering the threshold for large-scale AI agent applications if successful.
- With the support of the Eclipse organization and an open community, LMOS has the opportunity to grow into industry infrastructure.
- However, it also faces challenges: competing protocols (like MCP, AITP) focus on specific aspects and may gain popularity faster; LMOS needs to prove the practicality and performance of its large architecture.
- In the coming years, LMOS may first pilot in vertical fields (e.g., comprehensive adoption within a large enterprise), using successful cases to drive standardization.
- If the industry trends towards **multi-protocol coexistence**, LMOS can also integrate other standards with its flexible adaptability, becoming a "meta-operating system" supporting various protocols.
- Therefore, LMOS's prospects lie in two paths: either becoming the mainstream multi-agent platform standard or serving as an integration framework supporting different protocols.
- Regardless, as agent system complexity increases, it has unique value and a promising future.
- In the short term, its ecosystem maturity needs improvement, and the promotion pace may be slower than specialized protocols.

## AITP (Agent Interaction & Transaction Protocol)

### Target Problem
Focused on **secure interaction and transactions between agents**:
- Addresses the issue of AI agents communicating and transacting across **trust boundaries**.
- Provides a standard that allows agents from different organizations/individuals to communicate autonomously, reach agreements, and conduct value exchanges (such as payments) securely, supporting interactions and transactions between agents and between humans and agents in the "Agent Internet".
- Replaces fragmented interfaces with a unified protocol, enabling agents to interact with any service as freely as browsers access websites.

### Key Technologies
**Threaded Sessions + Extensible Capabilities**:
- Utilizes an interaction model similar to chat threads (referencing OpenAI's Assistant Threads API) for structured message exchange within **conversation contexts**.
- Defines the **Thread** abstraction and multiple transport methods (such as HTTP, WebSocket) to establish persistent communication sessions.
- Extends through **capability modules** to achieve structured interaction types: such as payment requests (AITP-01), decision negotiations (AITP-02), data queries (AITP-03), on-chain identity/wallet verification (AITP-04/05), etc.
- These capabilities are embedded in conversations using standard message formats, allowing agents to exchange not only text but also complex data like form UIs and payment credentials.
- Emphasizes message signing and verification across trust boundaries to ensure trustworthy interactions between different entity agents.
- The entire protocol supports **transactional operations** (including cryptocurrency or fiat payments), enabling agents to directly perform economic activities.

### Applicable Scenarios
**Ubiquitous Agent Interaction**:
- Suitable for building the "Agent Internet" where AI agents from different organizations or individuals need to **communicate and transact directly**.
- For example, personal digital assistants communicating directly with bank/airline agents to handle business and execute payments automatically; or multiple companies' AI agents negotiating and placing orders in a supply chain.
- These scenarios require standardized conversation interfaces and **transaction protocols**. AITP provides structured conversations and payment capabilities, suitable for **online service markets, agent microservices, cross-domain agent collaboration**, and other applications.
- Agents in blockchain ecosystems like NEAR are also target users, leveraging AITP to bridge on-chain and off-chain interactions, achieving **value exchange** (such as token payments) driven agent services.

### Technical Architecture
**Session-Driven Interaction**:
- AITP treats **each conversation as a thread**, initiated by one agent to open a session with another agent or user.
- Threads have unique IDs and can be carried over different transport channels, such as HTTP long polling, WebSocket, or mailbox-style relays.
- Within threads, communication uses a **message body + metadata** format, compatible with regular chat message structures while supporting specific "capability" messages.
- For instance, when a payment is needed, a message containing a payment request capability is sent, and the receiving agent processes the payment through its wallet module.
- AITP's defined capability messages are akin to extended RPCs—completing transactions within the conversation context.
- Thus, the architecture is **peer-to-peer session-based communication** between agents, combining conversation context with remote procedure call characteristics.
- Any agent can act as both a server and a client within a thread (similar to user-to-user chat); meanwhile, standardized functional modules ensure certain message types have defined processing flows (e.g., the payment capability corresponds to a clear multi-step interaction protocol).
- Identity verification relies on existing account systems (such as NEAR blockchain accounts or conventional OAuth), exchanging credentials before or during session establishment.
- In summary, AITP's architecture allows agent communication to resemble a combination of instant messaging and transaction protocols, achieving **loosely coupled multi-entity conversations** while enabling structured transaction modes when needed.

### Compatibility and Extensibility
**Open Standards + Multi-Ecosystem**:
- AITP is open as an RFC, with core specifications and reference implementation code available on GitHub.
- The protocol is not heavily dependent on specific agent development frameworks; as long as the Threads API and capability interfaces are followed, existing conversational AIs (such as agents based on OpenAI's ChatCompletion) can integrate with minimal modifications, as AITP is designed to be **largely compatible** with OpenAI's conversation format.
- Its **capability system** is extensible: new capability modules can be added by defining message types without affecting existing modules.
- Especially for transaction-related capabilities, it is designed to be compatible with mainstream crypto wallets and traditional payments (NEAR Wallet/EVM Wallet), facilitating the addition of more payment methods.
- Promoted by NEAR, AITP is likely to be first applied within the NEAR community and integrated with blockchain infrastructure (such as smart contract verification of agent behavior).
- However, the protocol itself is blockchain-agnostic and can be adopted by traditional web service agents.
- This design allows AITP to expand across both crypto and web domains.
- To achieve widespread adoption, more platforms need to support it, such as integration with mainstream AI assistants or browser agents.
- Currently, NEAR AI Hub and others are integrating AITP, and community feedback will determine the ecosystem's direction.

### Open Source and Ecosystem
**NEAR-Led Promotion**:
- AITP is initiated by the NEAR Foundation, with core authors including NEAR co-founders, thus inherently possessing blockchain community resources.
- The RFC was released in February 2025, with the aitp.dev site open for documentation and discussion.
- NEAR AI Hub is integrating AITP, and NEAR ecosystem agents (such as decentralized customer service) will prioritize its implementation.
- NEAR also invites external collaboration, expressing willingness to co-develop standards with other agent developers.
- The AI and blockchain communities are paying attention: crypto media has reported "AITP new standard born".
- Due to its transaction capabilities, it may attract fintech AI applications.
- Open source-wise, AITP code is released under MIT or similar licenses, encouraging community contributions of new capability modules.
- NEAR's AI team regularly hosts discussions (Office Hours) to promote the ecosystem.
- The potential risk is whether AITP can extend beyond the NEAR community and be accepted by the broader AI community; however, its statement does not bind it to the NEAR chain.
- Therefore, the ecosystem has the opportunity to expand to Web2 enterprises.
- If it can form alliances with OpenAI, Anthropic, etc. (e.g., an open agent standards alliance), the AITP ecosystem will grow rapidly.

### Future Prospects
**A Strong Candidate for Building the Agent Internet**:
- AITP is highly anticipated due to its direct focus on **agent economic activities**.
- It unifies communication and transactions, meeting the critical needs of future autonomous agent transactions and collaboration, distinguishing it from other protocols.
- As more business activities are executed by AI agents, if AITP is widely accepted, it could become a **new protocol layer for internet applications** (similar to HTTP for browsing).
- NEAR's support provides a launch acceleration, but long-term success requires more neutral participants.
- Optimistically, AITP, due to its novel concept and timely release (coinciding with the agent boom), will quickly form a developer community and establish a standard advantage in cross-agent transactions.
- Once demonstration scenarios (such as cross-agent processes for automatic ticket booking) are successfully implemented and superior to traditional scraping solutions, the industry will follow suit.
- Additionally, AITP does not necessarily compete with MCP/ANP; it focuses on the interaction and transaction layer and can combine with other agent communication protocols.
- Therefore, the future may see a **protocol fusion** scenario: MCP for tool integration, ANP for identity and P2P, AITP for standard interactions and payments, each leveraging their strengths.
- In conclusion, AITP has the potential to create an "Agent Interconnected Economy" ecosystem, securing a place in the future protocol landscape, especially with **significant advantages in commercial scenarios**.

## Summary

In summary, each protocol has its focus:

- **MCP** is positioned as a **tool interface for LLMs**, with rapid implementation and backed by major companies.
- **ANP** aims at a **decentralized agent network**, leading in technology but requiring ecosystem support.
- **agents.json** is an **auxiliary standard** for the web environment, likely to become widely popular and complement other protocols.
- **LMOS** offers a **full-stack platform**, suitable for large-scale deployment with long-term potential.
- **AITP** focuses on **secure interactions and economic transactions**, potentially leading agent commercial interconnectivity.
- **Agora** represents the direction of **future adaptive communication**, with far-reaching impact.

The future protocol landscape may not be dominated by a single protocol but rather a complementary fusion:

- For example, using AITP to define interaction formats, ANP for identity trust, and MCP/agents.json for specific data source integration.

In the foreseeable future, **MCP** may lead in tool integration due to its direct problem-solving and initial ecosystem scale; however, looking further ahead, **open protocols with identity authentication and transaction capabilities** (such as ANP, AITP) align more with the "Agent Internet" vision and are likely to play a larger role in building a global intelligent agent network.
