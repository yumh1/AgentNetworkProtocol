# ANP Agent Description Protocol Specification

## Abstract

This specification defines the Agent Description Protocol (ADP), a standardized protocol for describing intelligent agents. It defines how an agent publishes its public information and supported interfaces. Other agents can obtain this agent's description and then engage in information exchange and collaboration with it.

This specification defines the information interaction patterns between two agents based on the ANP protocol.

The core content of the specification includes:
1. Using JSON as the base data format, supporting linked data and semantic web features
2. Defining core vocabularies for agent basic information, products, services, interfaces, etc.
3. Adopting the did:wba method as a unified security mechanism to enable cross-platform identity authentication. The identity authentication method is also extensible and can support other methods in the future
4. Supporting interoperability with existing standard protocols (such as OpenAPI, JSON-RPC)

This specification aims to improve interoperability and communication efficiency between agents, providing foundational support for building agent networks.

Information interaction pattern design, compatibility design.

## Overview

An Agent Description (AD) document is the entry point to access an agent, similar to a website's homepage. Other agents can obtain information about the agent's name, entity ownership, functionality, products, services, interaction APIs or protocols based on this AD document. With this information, data communication and collaboration between agents can be achieved.

This specification mainly addresses two issues: first, defining the information interaction patterns between two agents, and second, defining the format of agent description documents.

### Information Interaction Pattern

ANP adopts an information interaction pattern similar to "web crawling", where agents use URLs to connect the data they provide externally (files, APIs, etc.) and their descriptions into a network. Other agents can act like crawlers, selecting appropriate data to read locally based on the data description information, and making decisions and processing locally. If it's an API file, they can also call the API to interact with the agent.

![anp-information-interact](/images/anp-information-interact.png)

The "web crawling" information interaction pattern has the following advantages:
- Similar to existing internet architecture, facilitating search engines to index public agent information and create an efficient agent data network
- Pulling remote data locally for processing as model context helps avoid user privacy leaks. Task delegation interaction patterns would leak user privacy during tasks.
- Natural hierarchical structure, facilitating agent interaction with large numbers of other agents.

### Core Concepts

Information and Interface are the core concepts of the ANP agent description specification.

Information is the data that agents provide externally, including text files, images, videos, audio, etc.

Interface is the interface that agents provide externally. Interfaces are divided into two types:
- One type is natural language interfaces, which allow agents to provide more personalized services through natural language;
- Another type is structured interfaces, which allow agents to provide more efficient and standardized services.

Although natural language interfaces can meet most scenarios using model capabilities, structured interfaces can improve communication efficiency between agents in many scenarios. Therefore, we currently support both structured interfaces and natural language interfaces, achieving a balance between efficiency and personalization. If structured interfaces are available, models should prioritize structured interfaces. If structured interfaces cannot meet user needs, natural language interfaces can be used.

It is recommended that all agents support natural language interfaces.

## Agent Description Document Format

An agent description document is the external entry point for an agent.

Benefiting from improved AI capabilities, agent description documents can be entirely described in natural language, and other agents can basically understand the information they express. However, since agents use different models with varying capabilities, to ensure that most models can have unified and accurate understanding of data, we still recommend that agent description documents use structured descriptions. In the future, to enhance personalized expression capabilities, documents can extensively use natural language internally.

### ANP-Compliant Agent Description

For agent description formats, we recommend using JSON format. We have defined an ANP-compliant agent description document format based on standard JSON.

#### Agent Description Document

The following is an example of an agent description document:

```json
{
  "protocolType": "ANP",
  "protocolVersion": "1.0.0",
  "type": "AgentDescription",
  "url": "https://grand-hotel.com/agents/hotel-assistant",
  "name": "Grand Hotel Assistant",
  "did": "did:wba:grand-hotel.com:service:hotel-assistant",
  "owner": {
    "type": "Organization",
    "name": "Grand Hotel Management Group",
    "url": "https://grand-hotel.com"
  },
  "description": "Grand Hotel Assistant is an intelligent hospitality agent providing comprehensive hotel services including room booking, concierge services, guest assistance, and real-time communication capabilities.",
  "created": "2024-12-31T12:00:00Z",
  "securityDefinitions": {
    "didwba_sc": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "security": "didwba_sc",
  "Infomations": [
    {
      "type": "Product",
      "description": "Luxury hotel rooms with premium amenities and personalized services.",
      "url": "https://grand-hotel.com/products/luxury-rooms.json"
    },
    {
      "type": "Product", 
      "description": "Comprehensive concierge and guest services including dining, spa, and local attractions.",
      "url": "https://grand-hotel.com/products/concierge-services.json"
    },
    {
      "type": "Information",
      "description": "Complete hotel information including facilities, amenities, location, and policies.",
      "url": "https://grand-hotel.com/info/hotel-basic-info.json"
    },
    {
      "type": "VideoObject",
      "description": "Hotel virtual tour showcasing rooms, facilities, dining areas, and recreational amenities.",
      "url": "https://grand-hotel.com/media/hotel-tour-video.mp4"
    }
  ],
  "interfaces": [
    {
      "type": "NaturalLanguageInterface",
      "protocol": "YAML",
      "version": "1.2.2",
      "url": "https://grand-hotel.com/api/nl-interface.yaml",
      "description": "Natural language interface for conversational hotel services and guest assistance."
    },
    {
      "type": "StructuredInterface",
      "protocol": "YAML",
      "humanAuthorization": true,
      "version": "1.1",
      "url": "https://grand-hotel.com/api/booking-interface.yaml",
      "description": "Structured interface for hotel room booking and reservation management."
    },
    {
      "type": "StructuredInterface",
      "protocol": "JSON-RPC 2.0",
      "url": "https://grand-hotel.com/api/services-interface.json",
      "description": "JSON-RPC 2.0 interface for accessing hotel services and amenities."
    },
    {
      "type": "StructuredInterface",
      "protocol": "MCP",
      "version": "1.0",
      "url": "https://grand-hotel.com/api/mcp-interface.json",
      "description": "MCP-compatible interface for seamless integration with MCP-based systems."
    },
    {
      "type": "StructuredInterface",
      "protocol": "WebRTC",
      "version": "1.0",
      "url": "https://grand-hotel.com/api/webrtc-interface.yaml",
      "description": "WebRTC interface for real-time video communication and streaming services."
    }
  ],
  "proof": {
    "type": "EcdsaSecp256r1Signature2019",
    "created": "2024-12-31T15:00:00Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:wba:grand-hotel.com:service:hotel-assistant#keys-1",
    "challenge": "1235abcd6789",
    "proofValue": "z58DAdFfa9SkqZMVPxAQpic7ndSayn1PzZs6ZjWp1CktyGesjuTSwRdoWhAfGFCF5bppETSTojQCrfFPP2oumHKtz"
  }
}
```

##### Hotel Agent Description Document Field Descriptions

| Field Name | Type | Required | Description |
|-----------|------|----------|-------------|
| protocolType | string | Required | Protocol type identifier, fixed value "ANP" |
| protocolVersion | string | Required | ANP protocol version number, currently "1.0.0" |
| type | string | Required | Document type identifier, "AgentDescription" for agent description documents |
| url | string | Optional | Agent's network access address for identifying agent location |
| name | string | Required | Human-readable name of the agent, such as "Grand Hotel Assistant" |
| did | string | Optional | Decentralized identifier of the agent for identity verification |
| owner | object | Optional | Agent owner information, including organization name and URL |
| description | string | Optional | Detailed functional description and service explanation of the agent |
| created | string | Optional | Creation time of the agent description document, ISO 8601 format |
| securityDefinitions | object | Required | Security mechanism definitions, including authentication methods and parameter locations |
| security | string | Required | Enabled security configuration name, referencing definitions in securityDefinitions |
| Infomations | array | Optional | List of information resources provided by the agent, including products, services, media files, etc. |
| interfaces | array | Optional | List of interaction interfaces supported by the agent, including various protocols and APIs |
| proof | object | Optional | Digital signature and integrity verification information to prevent document tampering |

##### Information Object Field Descriptions

| Field Name | Type | Description |
|-----------|------|-------------|
| type | string | Information type, such as "Product", "Information", "VideoObject", etc. |
| description | string | Detailed description of the information content |
| url | string | Access address of the information resource |

##### Interface Object Field Descriptions

| Field Name | Type | Description |
|-----------|------|-------------|
| type | string | Interface type, such as "NaturalLanguageInterface", "StructuredInterface" |
| protocol | string | Protocol used by the interface, such as "YAML", "JSON-RPC 2.0", "MCP", "WebRTC" |
| version | string | Interface version number |
| url | string | Address of the interface definition document |
| description | string | Description of interface functionality and purpose |
| humanAuthorization | boolean | Whether human authorization is required, applicable to sensitive operations like booking payments |

#### Product Description Document

The following is an example of a Product description:

```json
{
  "protocolType": "ANP",
  "protocolVersion": "1.0.0",
  "type": "Product",
  "url": "https://grand-hotel.com/products/deluxe-suite.json",
  "identifier": "deluxe-suite-001",
  "name": "Deluxe Suite",
  "description": "A luxurious suite with separate living room and bedroom, equipped with panoramic floor-to-ceiling windows, premium sound system, and smart home controls. Suitable for business travelers and high-end customers.",
  "security": {
    "didwba": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "brand": {
    "type": "Brand",
    "name": "Grand Hotel"
  },
  "additionalProperty": [
    {
      "type": "PropertyValue",
      "name": "Room Area",
      "value": "80 square meters"
    },
    {
      "type": "PropertyValue", 
      "name": "Bed Type",
      "value": "King Size Bed"
    }
  ],
  "offers": {
    "type": "Offer",
    "price": "1288",
    "priceCurrency": "CNY",
    "availability": "https://schema.org/InStock",
    "priceValidUntil": "2025-12-31"
  },
  "amenityFeature": [
    {
      "type": "LocationFeatureSpecification",
      "name": "Free WiFi",
      "value": true
    },
    {
      "type": "LocationFeatureSpecification", 
      "name": "Air Conditioning",
      "value": true
    }
  ],
  "category": "Hotel Room",
  "sku": "GH-DELUXE-SUITE-001",
  "image": [
    {
      "type": "ImageObject",
      "url": "https://grand-hotel.com/images/deluxe-suite-bedroom.jpg",
      "caption": "Deluxe Suite - Bedroom Area",
      "description": "Spacious bedroom with king-size bed and premium bedding"
    },
    {
      "type": "ImageObject",
      "url": "https://grand-hotel.com/images/deluxe-suite-living.jpg", 
      "caption": "Deluxe Suite - Living Area",
      "description": "Separate living room with sofa, coffee table, and work area"
    },
    {
      "type": "ImageObject",
      "url": "https://grand-hotel.com/images/deluxe-suite-view.jpg",
      "caption": "Deluxe Suite - City View",
      "description": "Panoramic floor-to-ceiling windows offering excellent city views"
    }
  ],
  "audience": {
    "type": "Audience",
    "audienceType": "Business travelers, luxury guests",
    "geographicArea": "Global"
  },
  "manufacturer": {
    "type": "Organization", 
    "name": "Grand Hotel Management Group",
    "url": "https://grand-hotel.com"
  }
}
```

##### Product Description Document Field Descriptions

| Field Name | Type | Required | Description |
|-----------|------|----------|-------------|
| protocolType | string | Required | Protocol type identifier, fixed value "ANP" |
| protocolVersion | string | Required | ANP protocol version number |
| type | string | Required | Object type, "Product" for products |
| url | string | Optional | Network address of product information |
| identifier | string | Optional | Unique identifier of the product |
| name | string | Required | Product name |
| description | string | Required | Detailed product description |
| brand | object | Optional | Product brand information |
| additionalProperty | array | Optional | Additional properties and features of the product |
| offers | object | Optional | Price and availability information of the product |
| amenityFeature | array | Optional | Facilities and functions provided by the product |
| category | string | Optional | Product category |
| sku | string | Optional | Product SKU code |
| image | array | Optional | Product image list |
| audience | object | Optional | Target customer group |
| manufacturer | object | Optional | Product provider information |

#### JSON-RPC 2.0 Interface Description Document

The following is an example of a JSON-RPC 2.0 interface description document:

```json
{
  "protocolType": "ANP",
  "protocolVersion": "1.0.0",
  "type": "JSON-RPC 2.0",
  "url": "https://grand-hotel.com/api/jsonrpc-interface.json",
  "security": {
    "didwba": {
      "scheme": "didwba",
      "in": "header",
      "name": "Authorization"
    }
  },
  "transport": {
    "protocol": "HTTPS",
    "host": "grand-hotel.com",
    "path": "/api/v1/jsonrpc",
    "method": "POST",
    "port": 443,
    "contentType": "application/json"
  },
  "info": {
    "title": "Grand Hotel Services API",
    "version": "1.0.0",
    "description": "JSON-RPC 2.0 API for hotel services including room management, booking, and guest services"
  },
  "methods": [
    {
      "name": "searchRooms",
      "description": "Search available hotel rooms based on criteria",
      "params": {
        "type": "object",
        "properties": {
          "checkIn": {
            "type": "string",
            "format": "date",
            "description": "Check-in date in YYYY-MM-DD format"
          },
          "checkOut": {
            "type": "string", 
            "format": "date",
            "description": "Check-out date in YYYY-MM-DD format"
          },
          "guests": {
            "type": "integer",
            "minimum": 1,
            "maximum": 8,
            "description": "Number of guests"
          },
          "roomType": {
            "type": "string",
            "enum": ["standard", "deluxe", "suite", "presidential"],
            "description": "Preferred room type"
          }
        },
        "required": ["checkIn", "checkOut", "guests"]
      },
      "result": {
        "type": "object",
        "properties": {
          "rooms": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/Room"
            }
          },
          "total": {
            "type": "integer",
            "description": "Total number of available rooms"
          }
        }
      }
    },
    {
      "name": "makeReservation",
      "description": "Create a new hotel reservation",
      "params": {
        "type": "object",
        "properties": {
          "roomId": {
            "type": "string",
            "description": "Unique room identifier"
          },
          "guestInfo": {
            "$ref": "#/definitions/GuestInfo"
          },
          "checkIn": {
            "type": "string",
            "format": "date"
          },
          "checkOut": {
            "type": "string",
            "format": "date"
          },
          "specialRequests": {
            "type": "string",
            "description": "Special requests or preferences"
          }
        },
        "required": ["roomId", "guestInfo", "checkIn", "checkOut"]
      },
      "result": {
        "type": "object",
        "properties": {
          "reservationId": {
            "type": "string",
            "description": "Unique reservation identifier"
          },
          "confirmationNumber": {
            "type": "string",
            "description": "Booking confirmation number"
          },
          "totalAmount": {
            "type": "number",
            "description": "Total reservation amount"
          }
        }
      }
    }
  ],
  "definitions": {
    "Room": {
      "type": "object",
      "properties": {
        "id": {"type": "string"},
        "type": {"type": "string"},
        "price": {"type": "number"},
        "amenities": {"type": "array", "items": {"type": "string"}},
        "availability": {"type": "boolean"}
      }
    },
    "GuestInfo": {
      "type": "object",
      "properties": {
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"}
      },
      "required": ["firstName", "lastName", "email"]
    }
  }
}
```

##### JSON-RPC 2.0 Interface Document Field Descriptions

| Field Name | Type | Required | Description |
|-----------|------|----------|-------------|
| jsonrpc | string | Required | JSON-RPC protocol version, fixed value "2.0" |
| security | object | Required | Security mechanism definition, including authentication methods and parameter configuration |
| transport | object | Required | Transport layer configuration, including protocol, endpoint, method, etc. |
| info | object | Required | API basic information, including title, version, description |
| methods | array | Required | List of callable methods |
| definitions | object | Optional | Data structure definitions for reuse |

##### Transport Object Field Descriptions

| Field Name | Type | Description |
|-----------|------|-------------|
| protocol | string | Transport protocol, such as "HTTPS", "HTTP" |
| host | string | Server hostname |
| basePath | string | API base path |
| endpoint | string | Specific API endpoint path |
| port | integer | Port number, HTTPS default 443, HTTP default 80 |
| method | string | HTTP request method, JSON-RPC typically uses "POST" |
| contentType | string | Content type, typically "application/json" |
| fullUrl | string | Complete API access address |

##### Method Object Field Descriptions

| Field Name | Type | Description |
|-----------|------|-------------|
| name | string | Method name for RPC calls |
| description | string | Method functionality description |
| params | object | JSON Schema definition of input parameters |
| result | object | JSON Schema definition of return results |

#### MCP Server Interface Document Description

To be completed

### JSON-LD Format

### Security Mechanism

The Agent Description Protocol currently uses the did:wba method as its security mechanism. The did:wba method is a web-based Decentralized Identifier (DID) specification designed to meet the needs of cross-platform identity authentication and agent communication.

Other identity authentication schemes can be extended as needed in the future.

#### DIDWBASecurityScheme (DID WBA Security Scheme)

Describes metadata for security mechanism configuration based on the did:wba method. The value assigned to the scheme name must be defined in the vocabulary included in the agent description.

For all security schemes, any keys, passwords, or other sensitive information that directly provides access should not be stored in the AD, but should be shared and stored out-of-band through other mechanisms. The purpose of AD is to describe how to access the agent (if the consumer is already authorized), not to grant that authorization.

Security schemes typically require additional authentication parameters, such as digital signatures. The location of this information is indicated by the value associated with name, usually in combination with the value of in. The value associated with in can take one of the following values:

- header: The parameter will be given in the header provided by the protocol, with the header name provided by the value of name. In the did:wba method, authentication information is passed through the Authorization header.
- query: The parameter will be appended to the URI as a query parameter, with the query parameter name provided by name.
- body: The parameter will be provided in the body of the request payload, using the data schema element provided by name.
- cookie: The parameter is stored in a cookie identified by the name value.
- uri: The parameter is embedded in the URI itself, encoded by URI template variables defined in related interactions (defined by the value of name).
- auto: The location is determined or negotiated as part of the protocol. If the in field of SecurityScheme is set to auto value, the name field should not be set.

Table 2: Security scheme level vocabulary terms

| Vocabulary Term | Description | Required | Type |
|----------------|-------------|----------|------|
| type | Object type identifier for adding semantic labels to objects. | Optional | string |
| description | Additional (human-readable) information based on default language. | Optional | string |
| scheme | Security mechanism identifier | Required | string |
| in | Location of authentication parameters. | Required | string |
| name | Name of authentication parameters. | Required | string |

The following is an example of security configuration using the did:wba method:

```json
{
    "securityDefinitions": {
        "didwba_sc": {
            "scheme": "didwba",
            "in": "header",
            "name": "Authorization"
        }
    },
    "security": "didwba_sc"
}
```

Security configuration in AD is required. Security definitions must be activated through the agent-level security member. This configuration is the security mechanism required for interacting with the agent.

When security appears at the top level of the AD document, it means that all resources must use this security mechanism for verification when accessed. When it appears inside a specific resource, it means that the resource can only be accessed when this security mechanism is satisfied. If the security specified at the top level differs from the security specified in the resource, the security specified in the resource takes precedence.

### Human Manual Authorization

If an interface requires human manual authorization when called, such as a purchase interface, the field humanAuthorization can be added to the interface definition. True indicates that interface calls require human manual authorization to access.

### Proof (Integrity Verification)

To prevent AD documents from being maliciously tampered with, impersonated, or reused, we have added verification information Proof to AD documents. The Proof definition can refer to the specification: [https://www.w3.org/TR/vc-data-integrity/#defn-domain](https://www.w3.org/TR/vc-data-integrity/#defn-domain).

Where:
- domain: Defines the domain name where the AD document is stored. Users must verify that the domain name from which the document was obtained matches the domain name defined in the domain after obtaining the document. If they don't match, this document may be fake.
- challenge: Defines challenge information for verification to prevent tampering. When specifying domain, challenge must also be specified.
- verificationMethod: Defines the verification method, currently using the verification method in the did:wba document. More methods can be extended in the future.
- proofValue: Carries digital signature. Generation rules are as follows:
  - Generate the website's AD document without the proofValue field
  - Use [JCS (JSON Canonicalization Scheme)](https://www.rfc-editor.org/rfc/rfc8785) to normalize the above AD document and generate a normalized string.
  - Use SHA-256 algorithm to hash the normalized string and generate a hash value.
  - Use the client's private key to sign the hash value, generate a signature value, and perform URL-safe Base64 encoding.
  - The signature verification process is the reverse of the above process.

## Common Definition Standardization

For specific products or services, such as a cup of coffee or a toy, a subset of schema.org Product properties can be used to define a specific type and clarify the product description method. This way, all agents can use unified definitions when constructing product data, enabling interoperability between different agents.

Similar approaches can be used for interfaces. For example, for product purchase interfaces, we can define a unified purchase interface specification that all agents can use, enabling interoperability between different agents.

## Copyright Notice  
Copyright (c) 2024 GaoWei Chang  
This file is released under the [MIT License](./LICENSE). You are free to use and modify it, but must retain this copyright notice.
