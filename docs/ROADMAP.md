# Roadmap

## Vision

**world‑monitor** is Axentx’s next‑generation, end‑to‑end world monitoring platform.  
It aggregates real‑time geopolitical, economic, environmental, and social data, presents it through a developer‑friendly API and a polished UI, and empowers users to build custom dashboards, alerts, and analytics pipelines.

The roadmap below follows the Axentx pipeline:  
* **MVP** – Must‑have features for launch.  
* **v1** – Core product expansion.  
* **v2** – Advanced analytics & developer ecosystem.

All milestones are time‑boxed, shippable, and tied to measurable KPIs (e.g., data coverage, API latency, user adoption).

---

## MVP (Launch – Q3 2026)

| Sprint | Deliverable | Owner | KPI | Notes |
|--------|-------------|-------|-----|-------|
| **Sprint 1** (Week 1‑2) | • Core data ingestion pipeline (geopolitical + economic feeds) <br>• Basic data schema & storage (PostgreSQL + TimescaleDB) | Data Engineering | 95 % data ingestion success | Uses existing open‑source scrapers; no external API costs |
| **Sprint 2** (Week 3‑4) | • RESTful API (FastAPI) exposing latest data points <br>• API auth (JWT) | Backend | 99.9 % uptime, <200 ms latency | API rate‑limit 100 req/s |
| **Sprint 3** (Week 5‑6) | • Front‑end dashboard (React) with world map, key metrics, and drill‑down <br>• Responsive design | Frontend | 80 % of target users can view dashboard in <5 s | Uses Mapbox GL |
| **Sprint 4** (Week 7‑8) | • Basic alerting system (email/SMS via Twilio) <br>• User onboarding & account creation | Full Stack | 70 % of trial users set up at least one alert | Twilio sandbox for MVP |
| **Sprint 5** (Week 9‑10) | • Documentation (API reference, quickstart) <br>• CI/CD pipeline (GitHub Actions) | DevOps | 100 % of commits pass tests | Uses GitHub Actions + Docker |
| **Sprint 6** (Week 11‑12) | • Beta launch & feedback loop (NPS ≥ 70) | PM | 200 beta users | Collect usage analytics via Segment |

**MVP‑Critical**: Data ingestion, API, dashboard, alerting, documentation, CI/CD.  
**Outcome**: First paid customers, validated willingness‑to‑pay, and a solid foundation for future features.

---

## v1 – Core Expansion (Q4 2026 – Q1 2027)

| Theme | Milestone | Owner | KPI |
|-------|-----------|-------|-----|
| **Data Coverage** | • Add environmental (air quality, climate) & social (demographics, health) feeds | Data Engineering | 90 % of target regions covered |
| **Developer Experience** | • SDKs (Python, JavaScript) <br>• GraphQL endpoint | Backend | 50 % of API calls via SDK |
| **Analytics** | • Historical trend charts <br>• Export CSV/JSON | Frontend | 60 % of users export data |
| **Security & Compliance** | • GDPR‑compliant data handling <br>• Role‑based access control | Security | Zero data breaches, 99.9 % compliance audit |
| **Performance** | • Cache layer (Redis) <br>• API throttling | DevOps | <150 ms average latency |
| **Community** | • Public API portal <br>• Sample projects | PM | 30 % of new sign‑ups use sample projects |

**Key Deliverables**: Expanded data sources, richer analytics, improved developer tooling, and stronger security posture.

---

## v2 – Advanced Ecosystem (Q2 2027 – Q4 2027)

| Theme | Milestone | Owner | KPI |
|-------|-----------|-------|-----|
| **Predictive Analytics** | • ML models for trend forecasting (using vLLM for inference) | ML Engineering | MAE < 5 % on key indicators |
| **Custom Pipelines** | • Drag‑and‑drop workflow builder <br>• Integration with external services (Zapier, Integromat) | Frontend | 40 % of users create custom pipelines |
| **Marketplace** | • Plugin architecture for third‑party data & visualizations | Product | 10 plugins published |
| **Scalability** | • Kubernetes deployment <br>• Auto‑scaling based on traffic | DevOps | 99.99 % availability under peak load |
| **Monetization** | • Tiered pricing (free, pro, enterprise) <br>• Usage‑based billing | Finance | 30 % conversion from free to paid |
| **Governance** | • Data lineage & audit logs <br>• Data quality dashboards | Data Engineering | 95 % data quality score |

**Outcome**: A fully‑featured, developer‑centric platform that supports predictive insights, custom workflows, and a growing ecosystem of plugins, driving higher ARR and user retention.

---

## Success Metrics (Across All Phases)

| Metric | Target | Frequency |
|--------|--------|-----------|
| Monthly Active Users (MAU) | 5 k (MVP) → 50 k (v1) → 200 k (v2) | Monthly |
| API Latency | <200 ms (MVP) → <150 ms (v1) → <100 ms (v2) | Real‑time |
| NPS | ≥70 (MVP) | Quarterly |
| Revenue | $0 (MVP) → $200 k ARR (v1) → $1 M ARR (v2) | Quarterly |

---

## Dependencies & Risks

| Risk | Mitigation |
|------|------------|
| Data source reliability | Build fallback scrapers, maintain multiple feeds |
| API abuse | Rate limiting, API keys, monitoring |
| Regulatory changes | Continuous compliance review, GDPR module |
| Talent turnover | Knowledge base in pgvector, cross‑team training |

---

## Release Cadence

* **MVP** – 3 months (12 sprints)  
* **v1** – 4 months (8 sprints)  
* **v2** – 6 months (12 sprints)

All releases will follow the Axentx QA & review gates before production deployment.

---
