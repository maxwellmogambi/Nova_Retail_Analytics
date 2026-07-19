# Retail Intelligence Platform (RIP)

## Project Constitution (v1.0)

### Purpose

Build a production-style end-to-end Retail Intelligence Platform that
demonstrates both **technical excellence** and **business impact**. The
project should resemble the work of a Data Engineer / Analytics Engineer
in a real organization rather than a standalone analytics exercise.

## Business Context

A growing retail company has data spread across operational systems and
lacks a trusted analytics platform. The objective is to centralize data,
automate ingestion and transformation, enforce data quality, and provide
trusted KPIs for decision makers.

## Objectives

### Engineering

-   Historical backfill and incremental ingestion
-   Layered architecture (Bronze → Silver → Gold)
-   Airflow orchestration
-   DuckDB warehouse
-   dbt transformations
-   Automated testing
-   Documentation
-   Dockerized development

### Business

Provide trusted analytics for: - Executive KPIs - Sales - Customers -
Products - Operations - Geographic performance

## Guiding Principles

-   Profile data before modeling.
-   Define grain before writing SQL.
-   Preserve grain throughout transformations.
-   Build reusable intermediate models.
-   Maintain authoritative lineage.
-   Facts capture events; dimensions describe entities.
-   Validate assumptions with exploration.
-   Add tests and documentation immediately.
-   Reassess architecture before continuing.
-   Favor maintainability over cleverness.

## Development Workflow

1.  Understand business problem
2.  Profile source data
3.  Identify entities and events
4.  Define grain
5.  Design dimensional model
6.  Review architecture
7.  Implement incrementally
8.  Validate data and metrics
9.  Add tests and documentation
10. Reassess architecture

## Scope (v1)

### In Scope

-   Historical dataset (recommended: Olist)
-   Lightweight API for incremental ingestion
-   Python ingestion
-   Bronze/Silver/Gold architecture
-   DuckDB
-   dbt
-   Airflow (Astro)
-   Power BI
-   Docker
-   GitHub Actions (later)

### Out of Scope

-   Kafka / Streaming
-   Spark
-   Kubernetes
-   Cloud deployment
-   ML pipelines

## High-Level Architecture

``` text
Historical Dataset + Lightweight API
                │
                ▼
        Python Ingestion
                │
                ▼
      Bronze (Raw Parquet/CSV)
                │
                ▼
      Silver (Clean & Standardized)
                │
                ▼
         DuckDB Warehouse
                │
                ▼
     dbt (Stage → Int → Dim/Fact)
                │
                ▼
        Gold Analytics Layer
                │
                ▼
        Power BI Dashboards
```

## Repository Structure

``` text
retail-intelligence-platform/
│
├── ingestion/
├── airflow/
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── warehouse/
│
├── dbt/          <-- your existing project
│
├── dashboards/
├── docs/
├── tests/
├── docker/
└── scripts/
├── .github/
└── README.md
```

## Roadmap

-   Phase 0: Planning (complete)
-   Phase 1: Data Discovery
-   Phase 2: Ingestion
-   Phase 3: Standardization
-   Phase 4: Analytics Engineering
-   Phase 5: Orchestration
-   Phase 6: Business Intelligence
-   Phase 7: Production Readiness

## Definition of Success

-   Reliable historical and incremental pipelines
-   Modular dbt project
-   Automated tests
-   Documented architecture
-   Executive dashboards with reconciled KPIs
-   Production-oriented engineering practices

## Instructions for a New Chat

Assume this constitution is the project's single source of truth.

Do **not** restart brainstorming unless a major architectural issue is
discovered.

Act as a Principal Data Engineer / Principal Analytics Engineer
mentoring me through a production-style implementation.

Challenge architectural decisions where appropriate and optimize for
maintainability, correctness, and business value rather than shortcuts.
