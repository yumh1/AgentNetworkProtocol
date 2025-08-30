# Agent Identity, Authorization, and Encryption

Agent identity, authorization, and encrypted communication are the core of agent security and the foundation for efficient and secure collaboration between two agents.

Today, I attempt to provide a comprehensive explanation of my understanding of these three issues.

## Agent Identity

### Explanation of Agent Identity

The first question is: when we discuss agent identity, whose identity are we actually talking about? Do agents have identity?

I believe that in general interaction scenarios, an agent, as a piece of software, does not have an identity of its own. It is merely authorized by a person to use that person's identity to help them complete tasks.

Therefore, when we discuss agent identity issues, we are essentially addressing how to enable agents to safely and efficiently represent people in interactions with other agents to help people complete tasks.

### What is Most Urgent for Agent Identity Compared to Traditional Identity Solutions

We already have many identity solutions, such as OIDC, DID, and SAML. Which solution is more suitable for agents?

This requires answering a question: what is the most important and urgent aspect of agent identity authentication?

I believe it is identity interoperability.

Identity interoperability refers to the ability of one platform's identity to be recognized and trusted by another platform, thereby enabling cross-platform mutual authentication and usage. This is very similar to email: if you have an email account, you can communicate with all email users across the entire network.

Why is interoperability extremely important for agents?

Because I believe the current internet consists of isolated islands, where each platform has its own identity system, its own users, and its own data. This greatly hinders agents from obtaining complete context and prevents agents from helping people execute tasks, making it impossible for us to have intelligent agents that are smart, understand you, and help you with many things.

Therefore, we believe that only an internet where all agents are interconnected and open can release AI capabilities to a greater extent, allowing us to build powerful agent networks.

The first step toward interconnectivity, especially for agents from different platforms, is enabling cross-platform identity authentication between them.

### The Most Suitable Identity Solution for Agents

Among all currently known solutions, DID has the best interoperability. Therefore, I have always believed that DID is the most suitable identity authentication solution for agents. Of course, DID is not without problems, such as limited application scope and lack of standard authorization solutions.

Fortunately, most agents are newly built software, so we can completely adopt new solutions. Although the W3C ZCAP-LD project did not become a recommended standard, it provides a solution for fine-grained authorization using DID, which deserves our attention.

However, other solutions are also considering how to improve identity verification interoperability, and there may be more choices in the future.

## Agent Authorization

Agent authorization and agent identity are related yet different issues. They are related because authorization often depends on identity authentication, but they are different because they solve different problems: one addresses who you are, and the other addresses what you can do.

Let's first look at several possible authorization modes in the future:
- Agents reading data from existing internet applications
- Different agents owning different user data, with users being able to authorize cross-agent data access
- Unified user data storage, authorizing different agents to access different data
- Users authorizing agents to represent them in interactions with other users'/enterprises' agents

### Agents Reading Data from Existing Internet Applications

Agents reading data from existing internet applications is an important way for agents to obtain complete context. For example, through my agent, I access Google questions and GitHub code. In this case, my agent needs to obtain authorization from Google or GitHub. This process generally uses OAuth, which is currently the most widely used technology on the internet.

![Agent Reading Data from Existing Internet Applications](/blogs/images/agent-authorization/agent-connect-existing-app.png)

### Cross-Agent Data Access Authorization

In the future, an entity (person or organization) may own multiple agents, with users having independent identity IDs in each agent, and each agent maintaining different user data. To allow one agent to obtain more complete user context, users can authorize this agent to access user data on other agents.

![Cross-Agent Data Access Authorization](/blogs/images/agent-authorization/multi-agent-auth.png)

As shown in the figure, cross-agent data access involves two steps:
- In agent B, the user authorizes agent C to access some data permissions in B. For example, this can be achieved by the user authorizing their identity ID in agent C.
- Agent C uses the user's authorization to access user data in agent B. After agent B verifies the authorization, it returns the data.

### Unified Data Storage Authorization

This is my favorite mode: in the future, people's data can be stored uniformly and securely in one place, with people having absolute sovereignty over their data. Agents do not own data permissions but are authorized by users to access (read or write) part of the user's data. Users can revoke agents' access to data at any time, allowing users to freely choose the agents they use.

![Unified Data Storage Authorization](/blogs/images/agent-authorization/one-data-center.png)

In this mode, users have independent identity IDs in agents A, B, and C, but user data is stored uniformly in the data center. Users can authorize agents A, B, and C to access part of the data in the data center.

This mode could be taken further, where users also own one or more accounts that they absolutely control, then authorize agents to use these accounts to access user data in the data center.

### Cross-Agent Interaction Authorization

This mode describes users authorizing agents to represent them in interactions with other users'/enterprises' agents.

![Cross-Agent Interaction Authorization](/blogs/images/agent-authorization/agent-interact.png)

For example, if Alice wants her agent to help her book a hotel, Alice's agent needs to use Alice's identity ID to represent Alice in accessing the hotel's agent and use Alice's identity ID to book the hotel.

This involves two different types of authorization:
- General authorization: Alice authorizes the agent to use her identity ID to represent her in accessing general information from the hotel's agent, such as rooms and prices. Access to this type of information does not require Alice's manual authorization each time; one-time authorization is sufficient. Otherwise, the interaction process would be too cumbersome.
- Special authorization: Alice authorizes the agent to use her identity ID to represent her in performing important operations, such as booking hotels and paying for orders. This type of authorization is very important and requires Alice's manual authorization each time. Otherwise, there would be security risks.

### Agent Authorization Solutions

If interoperability with existing systems is required, then use the authorization solutions supported by existing systems, such as OAuth if the existing system only supports OAuth.

However, for newly built agents, we should explore authorization solutions more suitable for agents.

In the agent identity section above, we mentioned that I believe DID is the most suitable identity solution for agents, but DID-based authorization solutions are not yet well-developed. First, W3C VC (Verifiable Credentials), which comes with W3C DID, can be used for some authorization scenarios, particularly for expressing attributes, permissions, or qualifications, such as "a user is an employee of an organization" or "a user is of legal age."

The VC solution is somewhat complex when expressing something like "30-minute read access to a specific resource," and the cost of issuance, verification, and revocation may be relatively high. W3C ZCAP-LD is an interesting technology for solving this problem, but it is currently still in community draft status.

IETF's GNAP (Grant Negotiation and Authorization Protocol) is proposed by the IETF GNAP working group and aims to be the successor to OAuth 2.0, addressing OAuth 2.0's shortcomings in flexibility, security, and extensibility, enabling authorization protocols to adapt to emerging scenarios such as AI Agents, IoT, and decentralized identity.

GNAP also supports DID and is a solution worth attention.

## End-to-End Encryption

If two agents communicate through messages and use a third-party service for message relay, this communication may not be secure, as messages could be intercepted or even decrypted by the third party.

In this case, end-to-end encryption technology is needed to allow third-party services to conveniently relay messages while being unable to decrypt their content.

If these two agents communicate directly, for example, two agents belonging to different platforms where each platform has applied for a public network endpoint for them, they can connect directly and use traditional HTTPS or WSS to ensure message security without needing end-to-end encryption.
