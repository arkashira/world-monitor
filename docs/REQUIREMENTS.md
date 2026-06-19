# REQUIREMENTS.md

## Overview
The `world-monitor` system is a comprehensive, real-time monitoring platform designed to provide developers and end users with actionable insights into global digital signals, infrastructure health, and emergent market or technical trends. Built as part of the axentx autonomous AI-workforce pipeline, this product must avoid duplication with existing portfolio items (e.g., IPC tools like iceoryx2) and instead extend capabilities toward observable signal aggregation, analysis, and user-driven alerting.

All requirements are grounded in axentx’s verified tech stack (vLLM, SGLang), data assets (auto, instr-resp, messages, query-resp), and the shared BRAIN (pgvector) for context retention and self-improvement.

---

## Functional Requirements

**FR-1: Global Signal Ingestion Pipeline**  
The system shall ingest real-time digital signals from public sources including but not limited to:
- GitHub commit and issue activity (via GitHub Events API)
- Public Lemmy/Reddit posts in developer-focused communities
- Open-source package registry updates (npm, PyPI)
- Public CI/CD status feeds (e.g., uptime reports, build logs)
Signals shall be normalized into structured events and stored in the central pgvector BRAIN with metadata (source, timestamp, topic tags).

**FR-2: Topic-Based Event Filtering**  
Users shall be able to subscribe to topics of interest (e.g., “Rust,” “AI agents,” “distributed systems”) using natural language or predefined tags. The system shall use SGLang to parse and map user queries into vector embeddings and match against ingested events in pgvector.

**FR-3: Real-Time Alerting**  
The system shall generate real-time alerts when high-signal events occur (e.g., spike in mentions, critical vulnerability disclosure). Alerts shall be delivered via:
- Email
- Webhook
- In-app notification (web UI)
Alert thresholds shall be user-configurable (e.g., volume, sentiment, source credibility).

**FR-4: Developer Dashboard**  
A web-based dashboard shall display:
- Live event stream
- Trending topics (top 10 by engagement/growth)
- Historical signal volume (time-series charts)
- User subscription status and alert history
The UI shall be responsive and accessible via modern browsers.

**FR-5: Signal Validation Layer**  
Before surfacing events to users, the system shall validate signal relevance and novelty using the axentx BRAIN:
- Compare against existing portfolio (e.g., no duplication with iceoryx2-related IPC monitoring)
- Cross-reference with training-pairs and messages datasets to assess community engagement
- Flag signals that correlate with revenue-validated pain points (from query-resp dataset)

**FR-6: API Access**  
A RESTful API shall expose core functionality:
- GET /events?topic=rust&limit=50
- POST /subscribe { topic: "vector-db", method: "webhook", endpoint: "..." }
- GET /trends?window=24h
API shall require authentication via API key and rate limiting (100 req/min per key).

**FR-7: Autonomous Signal Scoring**  
Each ingested event shall be scored for:
- Velocity (rate of mention increase)
- Source authority (GitHub org tier, community mod status)
- Semantic uniqueness (via embedding distance in pgvector)
Scores shall be recalculated hourly and used to prioritize alerts and dashboard content.

---

## Non-Functional Requirements

**Performance**  
- Ingestion pipeline shall process ≥100K events/hour with <10s end-to-end latency
- Dashboard shall load initial view in <1.5s (median)
- API 95th percentile response time <800ms

**Reliability**  
- System shall maintain 99.9% uptime (monthly)
- All data pipelines shall include retry logic and dead-letter queue for failed events
- Stateful components (e.g., subscriptions) shall be backed by durable storage (PostgreSQL)

**Security**  
- All user data and API keys shall be encrypted at rest (AES-256) and in transit (TLS 1.3+)
- API keys shall be hashed before storage
- Input validation shall be enforced on all endpoints to prevent injection attacks
- Authentication shall follow zero-trust model; no default credentials

**Scalability**  
- System shall scale horizontally using Kubernetes
- Ingestion workers shall be auto-scaled based on queue depth (using vLLM-style async batching where applicable)

**Maintainability**  
- All services shall emit structured logs (JSON) with trace IDs
- Codebase shall follow monorepo structure under `arkashira/surrogate-1-harvest` with clear module boundaries
- Automated tests (unit, integration) shall cover ≥85% of critical path code

**Extensibility**  
- Plugin architecture shall allow new signal sources to be added without downtime
- Alert delivery methods shall be modular (new channels pluggable via interface)

---

## Constraints

- Must use `pgvector` as the central knowledge BRAIN for all embeddings and context storage
- Must leverage `sgl-project/sglang` for structured generation tasks (e.g., topic extraction, intent parsing)
- Must not duplicate functionality in existing axentx products (e.g., IPC monitoring via iceoryx2)
- All new datasets introduced must comply with apache-2.0, mit, or cdla licenses
- Deployment must be compatible with axentx’s existing CI/CD pipeline in `arkashira/surrogate-1-harvest`

---

## Assumptions

- Public APIs (GitHub, Lemmy, etc.) remain stable and accessible
- The axentx BRAIN (pgvector) is continuously updated with outcome feedback from prior products
- Training-pairs and messages datasets contain sufficient signal to train topic classifiers and relevance models
- Users have technical proficiency (developers, product managers) — UX may assume intermediate technical literacy
- Revenue validation occurs upstream via axentx’s BD/HR scouting and PRD validation pipeline; world-monitor surfaces only pre-validated pain areas
