# Agent Identity, Authorization, and Encryption

Agent identity, authorization, and encrypted communication are the core of agent security and the foundation for efficient and secure collaboration between agents.

Today I will attempt to comprehensively articulate my understanding of these three issues.

## Agent Identity

### Explanation of Agent Identity

The first question is: when we discuss agent identity, whose identity are we actually talking about? Do agents have identities?

I believe that in general interaction scenarios, agents as software do not have identities themselves. They are merely authorized by humans to use human identities and help humans complete tasks.

Therefore, when we discuss agent identity issues, we are essentially talking about how to enable agents to safely and efficiently represent humans in interacting with other agents to help humans complete tasks.

### What is Most Urgent for Agent Identity Compared to Traditional Identity Solutions

We already have many identity solutions, such as OIDC, DID, and SAML. Which solution is most suitable for agents?

This requires answering a question: for agent identity authentication, what is the most important and urgent requirement?

I believe it is identity interoperability.

Identity interoperability refers to the ability of one platform's identity to be recognized and trusted by another platform, enabling cross-platform mutual authentication and usage. This is very similar to email: if you have an email account, you can communicate with all email users across the entire network.

Why is interoperability extremely important for agents?

Because I believe the current internet consists of isolated islands, where each platform has its own identity system, users, and data. This greatly hinders agents from obtaining complete context and prevents agents from helping people execute tasks, making it impossible for us to have intelligent agents that are smart, understand us, and help us accomplish many things.

Therefore, we believe that only an open internet where all agents are interconnected can unleash AI's capabilities to a greater extent, allowing us to build powerful agent networks.

The first step toward interconnectivity, especially for cross-platform agent interconnectivity, is enabling mutual cross-platform identity authentication.

### The Most Suitable Identity Solution for Agents

Among all known solutions, DID has the best interoperability. Therefore, I have always believed that DID is the most suitable identity authentication solution for agents. Of course, DID is not without problems, such as limited application scope and lack of standard authorization schemes.

Fortunately, most agents are newly built software, so we can completely adopt new solutions. Although the W3C ZCAP-LD project did not become a recommended standard, it provides a solution for fine-grained authorization using DID, which deserves our attention.

However, other solutions are also considering how to improve identity verification interoperability, and there may be more options in the future.

## Agent Authorization

Agent authorization is related to but different from agent identity. They are related because authorization often depends on identity authentication, but they are different because they solve different problems - one addresses "who you are" and the other addresses "what you can do."

Let's first look at several possible authorization models in the future:
- Agents reading data from existing internet applications
- Different agents owning different user data, with users authorizing cross-agent data access
- Unified user data storage, authorizing different agents to access different data
- Users authorizing agents to represent them in interactions with other users'/enterprises' agents

### Agents Reading Data from Existing Internet Applications

Agents reading data from existing internet applications is an important way for agents to obtain complete context. For example, through my agent, I access Google search results or GitHub code. In this case, my agent needs authorization from Google or GitHub. This process generally uses OAuth, which is currently the most widely used technology on the internet.

![Agents Reading Data from Existing Internet Applications](/blogs/images/agent-authorization/agent-connect-existing-app.png)

### Cross-Agent Data Access Authorization

In the future, an entity (person or organization) may own multiple agents, with users having independent identity IDs in each agent, and each agent maintaining different user data. To enable one agent to obtain more complete user context, users can authorize this agent to access user data from other agents.

![Cross-Agent Data Access Authorization](/blogs/images/agent-authorization/multi-agent-auth.png)

As shown in the figure, cross-agent data access involves two steps:
- The user authorizes agent C to access partial data permissions in agent B. For example, this can be achieved by the user authorizing their identity ID in agent C.
- Agent C uses the user's authorization to access user data in agent B. Agent B verifies the authorization and returns the data.

### Unified Data Storage Authorization

This is my favorite model: in the future, human data can be stored uniformly and securely in one place, with humans having absolute sovereignty over their data. Agents do not own data permissions but are authorized by users to access (read or write) portions of user data. Users can revoke agent access to data at any time, allowing users to freely choose the agents they use.

![Unified Data Storage Authorization](/blogs/images/agent-authorization/one-data-center.png)

In this model, users have independent identity IDs in agents A, B, and C, but user data is stored uniformly in the data center. Users can authorize agents A, B, and C to access portions of data in the data center.

This model could go further: users could also have one or more accounts under their absolute control, then authorize agents to use these accounts to access user data in the data center.

### Cross-Agent Interaction Authorization

This model describes users authorizing agents to represent them in interactions with other users'/enterprises' agents.

![Cross-Agent Interaction Authorization](/blogs/images/agent-authorization/agent-interact.png)

For example, Alice wants her agent to help her book a hotel. Alice's agent needs to use Alice's identity ID to represent Alice in accessing the hotel's agent and booking the hotel using Alice's identity ID.

This involves two different types of authorization:
- General authorization: Alice authorizes the agent to use her identity ID to represent her in accessing general information from the hotel's agent, such as rooms and prices. Access to this type of information doesn't require manual authorization from Alice each time; one-time authorization suffices. Otherwise, the interaction process would be too cumbersome.
- Special authorization: Alice authorizes the agent to use her identity ID to represent her in performing important operations, such as booking hotels or paying for orders. This type of authorization is very important and requires manual authorization from Alice each time. Otherwise, there would be security risks.

### Agent Authorization Solutions

If interoperability with existing systems is required, then use the authorization schemes supported by existing systems, such as OAuth if the existing system only supports OAuth.

However, for newly built agents, we should explore authorization schemes more suitable for agents.

In the agent identity section above, I mentioned that I believe DID is the most suitable identity solution for agents, but DID-based authorization schemes are not yet well-developed. First, W3C VC (Verifiable Credentials), which complements W3C DID, can be used for some authorization scenarios, particularly for expressing attributes, permissions, or qualifications, such as "a user is an employee of an organization" or "a user is of legal age."

The VC solution is somewhat complex when expressing permissions like "30-minute read access to a specific resource," and the costs of issuance, verification, and revocation may be relatively high. W3C ZCAP-LD is an interesting technology for solving this problem, though it is currently still in community draft status.

IETF's GNAP (Grant Negotiation and Authorization Protocol), proposed by the IETF GNAP working group, aims to be the successor to OAuth 2.0, addressing OAuth 2.0's shortcomings in flexibility, security, and extensibility, enabling authorization protocols to adapt to emerging scenarios like AI Agents, IoT, and decentralized identity.

GNAP also supports DID and is a solution worth following.

## End-to-End Encryption

If two agents communicate through messages and use a third-party service for message relay, the communication may not be secure, as messages could be intercepted or even decrypted by the third party.

This is when end-to-end encryption technology is needed, allowing third-party services to conveniently relay messages while being unable to decrypt their content.

If these two agents communicate directly - for example, two agents belonging to different platforms where the platforms have applied for public network endpoints for them - they can connect directly and use traditional HTTPS or WSS to ensure message security without needing end-to-end encryption.
