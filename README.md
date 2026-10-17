# ⚡ ApiVerse

> **A Production-Grade Roadmap to Modern API Engineering & Machine Learning Model Serving with FastAPI**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![ASGI / Uvicorn](<https://img.shields.io/badge/Server-Uvicorn%20ASGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white>)](https://www.uvicorn.org/)
[![OpenAPI 3.1](<https://img.shields.io/badge/Documentation-OpenAPI%203.1-85EA2D?style=for-the-badge&logo=openapiinitiative&logoColor=black>)](https://spec.openapis.org/oas/v3.1.0)

---

## 📌 Executive Overview

**ApiVerse** is a structured, engineering-first laboratory designed to master modern backend architecture, RESTful API design, asynchronous execution, and low-latency Machine Learning model inference using **FastAPI**, **Starlette**, and **Pydantic**.

Moving progressively from first principles (client-server network protocols and ASGI event loops) to deployment-ready ML microservices, this repository documents real-world design patterns, type-safe data pipelines, and production performance optimizations.

---

## 🏛️ System Architecture

FastAPI operates as a high-level asynchronous orchestration layer built on top of **Starlette** (for raw ASGI routing and web server capabilities) and **Pydantic** (for Rust-powered validation and JSON schema serialization).

```mermaid
graph TD
    Client["Client / Frontend / HTTP Request"]
  
    subgraph Host ["ASGI Application Server (Uvicorn)"]
        EventLoop["Asyncio Event Loop (uvloop)"]
        HTTPParser["C-Speed HTTP Parsing (httptools)"]
    end
  
    subgraph Framework ["FastAPI Framework Engine"]
        StarletteCore["Starlette Core Routing & Middleware"]
        DI["Dependency Injection System"]
        PydanticCore["Pydantic v2 Engine (Rust core)"]
      
        subgraph Handlers ["Application Logic & Endpoints"]
            CRUD["CRUD Operations & Business Rules"]
            MLService["ML Inference Engine (Scikit-Learn/Joblib)"]
        end
    end
  
    Docs["Automated OpenAPI 3.1 (Swagger UI / ReDoc)"]
  
    Client -->|HTTP / JSON| Host
    Host --> Framework
    StarletteCore --> DI
    DI --> PydanticCore
    PydanticCore -->|Validated Schema| Handlers
    Handlers -->|Type-Safe Response| Host
    Host -->|HTTP 200/201/422 JSON| Client
    Framework -.->|Introspects Type Hints| Docs

    classDef host fill:#1e293b,stroke:#38bdf8,stroke-width:1px,color:#f8fafc;
    classDef framework fill:#0f172a,stroke:#34d399,stroke-width:1px,color:#f8fafc;
    classDef client fill:#334155,stroke:#94a3b8,stroke-width:1px,color:#f8fafc;
    class Host host;
    class Framework framework;
    class Client client;
```

---

## 🔄 End-to-End Request & Validation Lifecycle

Every request submitted to FastAPI flows through strict parsing, dependency resolution, schema validation, and serialisation:

```mermaid
sequenceDiagram
    autonumber
    actor Client as HTTP Client
    participant Server as Uvicorn (ASGI)
    participant Route as FastAPI Router
    participant Val as Pydantic Engine (Rust)
    participant Logic as Controller / ML Model
  
    Client->>Server: HTTP Request (Method, Path, Query, Payload)
    Server->>Route: Dispatches ASGI Scope
    Route->>Val: Extract & Validate Path, Query & Body Schema
    alt Validation Failure (422)
        Val-->>Client: 422 Unprocessable Entity (Structured Error Detail)
    else Validation Succeeded
        Val->>Logic: Inject Typed Pydantic Objects into Handler
        Logic->>Logic: Run Business Logic or ML Inference
        Logic-->>Route: Return Python Dict / ORM Object / Model
        Route->>Val: Filter through response_model
        Val-->>Server: Serialize to JSON String
        Server-->>Client: HTTP Response (Status Code, JSON Body)
    end
```

---

## 🗺️ Learning Roadmap & Curriculum Structure

This repository tracks the **CampusX FastAPI & Machine Learning Masterclass** curriculum, systematically advancing from fundamental concepts to enterprise-grade model serving:

```mermaid
flowchart LR
    M1["01. API Core & Protocols"] --> M2["02. FastAPI Architecture"]
    M2 --> M3["03. HTTP Methods & REST"]
    M3 --> M4["04. Path & Query Params"]
    M4 --> M5["05. Pydantic v2 Mastery"]
    M5 --> M6["06. POST & Request Bodies"]
    M6 --> M7["07. Full CRUD Lifecycle"]
    M7 --> M8["08. ML Model Serving"]
    M8 --> M9["09. Production Hardening"]

    classDef step fill:#1e1e2e,stroke:#89b4fa,stroke-width:2px,color:#cdd6f4;
    class M1,M2,M3,M4,M5,M6,M7,M8,M9 step;
```

### Module Breakdown

| Module                            | Focus Area                  | Key Technologies & Concepts                                                    |
| :-------------------------------- | :-------------------------- | :----------------------------------------------------------------------------- |
| **01. API Fundamentals**    | Core Network Architecture   | Client-Server Model, HTTP/HTTPS, Statelessness, ASGI vs WSGI                   |
| **02. FastAPI Philosophy**  | Runtime & Server Setup      | Uvicorn, Starlette, Asynchronous Event Loop, Interactive OpenAPI Docs          |
| **03. HTTP Methods**        | RESTful Endpoint Design     | GET, Safe & Idempotent Methods, HTTP Status Codes, Route Decorators            |
| **04. Parameters & Types**  | Input Data Binding          | Path Parameters, Query Parameters, Type Conversion, Default Arguments          |
| **05. Pydantic Deep-Dive**  | Data Validation & Integrity | `BaseModel`, `Field`, Constraints, Rust Validation Core, Nested Models     |
| **06. POST & Request Body** | Payload Handling            | JSON Body Deserialization, Schema Enforcement,`response_model` Filtering     |
| **07. CRUD & Mutations**    | Complete State Operations   | PUT, PATCH, DELETE,`HTTPException`, Error Handling Patterns                  |
| **08. ML Model Serving**    | Model Inference Pipelines   | Serialized Artifacts (`joblib`/`pickle`), Feature Vectors, Prediction APIs |
| **09. API Optimization**    | Production Hardening        | Modular`APIRouter`, Custom Middleware, CORS, Dependency Injection, Profiling |

---

## ⚡ Tech Stack & Specifications

| Technology             | Role                             | Documentation                                  |
| :--------------------- | :------------------------------- | :--------------------------------------------- |
| **FastAPI**      | Async Web Framework              | [FastAPI Docs](https://fastapi.tiangolo.com/)   |
| **Pydantic v2**  | Data Parsing & Rust Validation   | [Pydantic Docs](https://docs.pydantic.dev/)     |
| **Starlette**    | ASGI Web Toolkit                 | [Starlette Docs](https://www.starlette.io/)     |
| **Uvicorn**      | ASGI Web Server                  | [Uvicorn Docs](https://www.uvicorn.org/)        |
| **OpenAPI 3.1**  | Standard API Specification       | [OpenAPI Initiative](https://www.openapis.org/) |
| **Scikit-Learn** | ML Artifact Pipeline Integration | [Scikit-Learn Docs](https://scikit-learn.org/)  |

---

