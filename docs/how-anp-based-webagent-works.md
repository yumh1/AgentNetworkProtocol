# How ANP-based WebAgent Works: Weather Agent as an Example

## Overview

WebAgent is a network agent specifically designed for AI access, allowing other agents to directly obtain information and services through standardized protocols. This document uses the Weather WebAgent as an example to explain in detail the operating mechanism and usage methods of WebAgent.

## 1. WebAgent Discovery Mechanism

Agents can discover WebAgents through two methods:

### 1.1 Active Discovery (via Domain)

When you know the domain of a WebAgent, you can obtain a list of agents by accessing a standardized path:

```
https://<domain>/.well-known/agent-descriptions
```

**Example**: Accessing `https://agent-weather.xyz/.well-known/agent-descriptions` will return the following JSON-LD format data:

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
      "name": "Weather Agent",
      "@id": "https://agent-weather.xyz/ad.json"
    }
  ]
}
```

Through this response, an agent can learn about the list of WebAgents under the domain and their description file addresses.

In this case, https://agent-weather.xyz/ad.json is the address of the Weather Agent's description file.

### 1.2 Passive Discovery (via Search Services)

WebAgents can register themselves with agent search services, allowing other agents to find them through keyword searches. For example, searching for the keyword "weather" might return information about the Weather WebAgent.

## 2. WebAgent Description File Parsing

After discovering a WebAgent, the next step is to retrieve and parse its description file (Agent Description).

**Example**: The Weather Agent's description file `https://agent-weather.xyz/ad.json` contains:

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

**Key fields in the description file**:

- `name`, `description`: Name and functional description of the WebAgent
- `owner`: Information about the WebAgent owner
- `securityDefinitions`: Definition of authentication methods
- `security`: Name of the verification scheme used
- `interfaces`: List of provided interfaces, including:
  - Structured interfaces: For weather queries, booking services, etc.
  - Natural language interface: For interaction through natural language

Through this description, agents can learn about the WebAgent's name, functions, interface types, interface addresses, authentication methods, and more. By calling these interfaces, agents can access weather information, booking services, subscription status queries, and other functionalities.

## 3. Identity Authentication Mechanism

Accessing a WebAgent requires identity verification to ensure requests come from trusted agents.

### 3.1 DID Authentication Process

The Weather WebAgent uses the `did:wba` method for authentication:

1. **Obtain DID**: Each agent needs its own DID, such as `did:wba:example.com:agent:weather123`
2. **Prepare DID Document**: A DID document containing public keys must be published at a specific path on the domain
3. **Sign Request**: The caller uses its private key to generate a signature for the request content
4. **Send Request**: Add the signature to the `Authorization` header when sending the request
5. **Verification Process**: The WebAgent verifies the validity of the signature and decides whether to authorize access

### 3.2 Test DID

To facilitate developer testing, ANP provides a public test DID:

- DID: `did:wba:agent-did.com:test:public`
- Location: [ANP Example Code Repository](https://github.com/agent-network-protocol/anp-examples/tree/main/use_did_test_public)
- Purpose: For testing only, not for sensitive operations

## 4. Interacting with WebAgent

### 4.1 Access Process

The standard process for using the Weather WebAgent:

1. **Get Description File**: Access `https://agent-weather.xyz/ad.json`
2. **Parse Interface Information**: Obtain available API interfaces from the `interfaces` field
3. **Get Interface Definition**: Download OpenAPI definition files like `weather-info.yaml`
4. **Build Request**: Create requests in the correct format according to the API definition
5. **Add Authentication**: Add DID signature authentication information in the request header
6. **Send Request**: Send HTTP request to the WebAgent
7. **Process Response**: Parse the returned structured data (JSON/YAML)

### 4.2 Code Example

Example code using ANP tools to interact with the Weather WebAgent:

```python
# The following code demonstrates how to use ANPTool to access the Weather WebAgent

async def query_weather(city):
    # Step 1: Get the agent description file
    ad_url = "https://agent-weather.xyz/ad.json"
    ad_response = await anp_tool.execute(url=ad_url)
    
    # Step 2: Parse interface information
    weather_api_url = None
    for interface in ad_response["ad:interfaces"]:
        if "weather" in interface["description"]:
            weather_api_url = interface["url"]
            break
    
    # Step 3: Get API definition
    api_def = await anp_tool.execute(url=weather_api_url)
    
    # Steps 4-6: Build and send request
    # Note: Actual URL and parameters should be determined based on the API definition
    weather_endpoint = "https://agent-weather.xyz/api/weather"
    weather_data = await anp_tool.execute(
        url=weather_endpoint,
        method="GET",
        params={"city": city}
    )
    
    # Step 7: Process response
    return weather_data
```

### 4.3 Using the ANP Explorer Tool

ANP Explorer is a convenient tool for interacting with WebAgents:

- Website: https://service.agent-network-protocol.com/anp-explorer/
- Functions:
  1. Query weather information using natural language
  2. Browse and explore WebAgent description documents
- Usage: Enter the URL of an agent description document or directly ask weather-related questions

## 5. WebAgent Technical Features Summary

The Weather WebAgent demonstrates the core advantages of the ANP protocol:

1. **Structured Data**: Directly provides data in JSON/YAML format, no need to parse HTML
2. **Self-Descriptive**: Agents come with complete interface documentation, facilitating automatic discovery and use
3. **Decentralized Authentication**: Uses DID to provide cross-platform authentication, eliminating the need for separate registration in each agent system
4. **Native AI Interface**: Interface mode designed specifically for AI, no need to simulate human operations

## 6. Developing Your Own WebAgent Client

To develop a client that can interact with the Weather WebAgent, you need:

1. Integrate ANP tools, reference: https://github.com/agent-network-protocol/anp-examples
2. Implement DID authentication functionality
3. Write agent discovery and description file parsing logic
4. Build request generators based on interface definitions

With just one prompt and one HTTP function, you can enable an AI agent to interact with WebAgents.

## Reference Resources

- ANP Protocol Specification: https://github.com/agent-network-protocol/AgentNetworkProtocol
- Example Code Repository: https://github.com/agent-network-protocol/anp-examples
- Weather WebAgent: https://agent-weather.xyz/
- ANP Explorer: https://service.agent-network-protocol.com/anp-explorer/
- ANP Official Website: https://agent-network-protocol.com/
- The Birth of the First WebAgent Designed for AI Access: [The Birth of the First WebAgent Designed for AI Access](/blogs/The-Birth-of-the-First-WebAgent-Designed-for-AI-Access.md) 