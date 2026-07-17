# PART 4 — SYSTEM ARCHITECTURE SPECIFICATION

Version: 2.0

Project: LexPulse AI

Purpose:
This document defines the overall technical architecture, system components, data flow, AI pipeline, deployment strategy, and design principles of LexPulse AI.

The architecture must prioritize simplicity, scalability, maintainability, and rapid implementation within a 35-hour hackathon.

---

# 1. SYSTEM OVERVIEW

LexPulse AI is an AI-powered Legal Intelligence Platform.

The system combines:

• Advanced Retrieval-Augmented Generation (RAG)

• Knowledge Graph

• Semantic Search

• Legal Citation Engine

• Legal Amendment Tracking

• AI Question Answering

• Social Claim Verification

The Knowledge Graph is the center of the system.

The LLM is used only for reasoning and explanation.

---

# 2. HIGH LEVEL ARCHITECTURE

                    User
                      │
                      ▼
          Next.js Frontend (React)
                      │
                      ▼
             FastAPI Backend
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
AI Orchestrator                Authentication
      │
      ▼
Retriever Engine
      │
 ┌────┴────┐
 ▼         ▼
Vector DB  Knowledge Graph
(Qdrant)   (NetworkX)
      │         │
      └────┬────┘
           ▼
     Context Builder
           ▼
      Prompt Builder
           ▼
        LLM API
(OpenAI / Claude / Gemini)
           ▼
 Answer + Citations
           ▼
      Frontend

---

# 3. ARCHITECTURE PRINCIPLES

The architecture must follow:

Clean Architecture

Service-Oriented Design

Component-Based Frontend

REST API

Loose Coupling

High Cohesion

Stateless Backend

Reusable Components

Modular AI Pipeline

---

# 4. FRONTEND ARCHITECTURE

Technology

Next.js

React

TypeScript

TailwindCSS

shadcn/ui

React Flow

Recharts

Responsibilities

• User Interface

• Dashboard

• AI Chat

• Knowledge Graph

• Timeline

• Claim Verification

• Authentication

• File Upload

The frontend never communicates directly with the database.

Every request goes through the backend API.

---

# 5. BACKEND ARCHITECTURE

Technology

FastAPI

Python

Pydantic

SQLAlchemy

Responsibilities

• Authentication

• API Gateway

• AI Orchestration

• Document Processing

• Embedding Generation

• Retrieval

• Knowledge Graph

• Logging

• Error Handling

The backend is responsible for every business rule.

---

# 6. DATABASE ARCHITECTURE

SQLite

Stores

Users

Documents

Chunks

Metadata

Claims

Chat History

Logs

Qdrant

Stores

Embeddings

NetworkX

Stores

Knowledge Graph

Filesystem

Stores

Uploaded PDF

---

# 7. DOCUMENT PROCESSING PIPELINE

User Upload

↓

Validate File

↓

Extract Text

↓

Clean Text

↓

Split into:

Document

↓

Article

↓

Clause

↓

Point

↓

Generate Metadata

↓

Chunk Text

↓

Embedding

↓

Store Metadata

↓

Store Embedding

↓

Create Graph Nodes

↓

Create Relationships

↓

Ready for Search

---

# 8. KNOWLEDGE GRAPH PIPELINE

Legal Document

↓

Entity Extraction

↓

Relationship Extraction

↓

Node Creation

↓

Edge Creation

↓

Graph Storage

↓

Interactive Visualization

Node Examples

Law

Article

Clause

Point

Penalty

Deadline

Organization

Topic

Relations

AMENDS

SUPERSEDES

REFERENCES

HAS_RIGHT

HAS_OBLIGATION

CONFLICTS_WITH

BELONGS_TO

---

# 9. ADVANCED RAG PIPELINE

User Question

↓

Intent Detection

↓

Hybrid Search

↓

Vector Search

+

BM25

↓

Knowledge Graph Expansion

↓

Reranking

↓

Context Builder

↓

Prompt Builder

↓

LLM

↓

Citation Validation

↓

Response

The LLM must never answer before retrieval.

---

# 10. CLAIM VERIFICATION PIPELINE

Input Statement

↓

Claim Extraction

↓

Keyword Detection

↓

Semantic Retrieval

↓

Knowledge Graph Matching

↓

Legal Evidence Retrieval

↓

LLM Reasoning

↓

Verdict

↓

Citation

Possible Verdicts

Correct

Incorrect

Misleading

Need Context

Unknown

---

# 11. SEARCH ARCHITECTURE

The search engine combines three techniques.

BM25

Fast keyword matching.

Vector Search

Semantic understanding.

Knowledge Graph Traversal

Relationship discovery.

The three results are merged and reranked before sending to the LLM.

---

# 12. AI ORCHESTRATOR

Responsibilities

Receive request

↓

Select workflow

↓

Retrieve evidence

↓

Expand context

↓

Call LLM

↓

Validate citations

↓

Return response

The Orchestrator controls every AI workflow.

---

# 13. API ARCHITECTURE

Frontend

↓

REST API

↓

FastAPI

↓

Service Layer

↓

Repository Layer

↓

Database

Business logic must never exist inside API routes.

---

# 14. SECURITY ARCHITECTURE

JWT Authentication

Role-Based Access

Environment Variables

Input Validation

Prompt Injection Protection

SQL Injection Protection

Rate Limiting

HTTPS Ready

Secure File Upload

---

# 15. PERFORMANCE TARGETS

Simple Question

≤ 5 seconds

Complex Question

≤ 30 seconds

Upload

≤ 10 seconds

Graph Rendering

≤ 2 seconds

Dashboard

≤ 2 seconds

Search

≤ 3 seconds

---

# 16. DEPLOYMENT ARCHITECTURE

Frontend

↓

Vercel

Backend

↓

Railway

Database

↓

SQLite

Vector Database

↓

Qdrant Cloud

Repository

↓

GitHub

The MVP must be deployable with minimal configuration.

---

# 17. SCALABILITY ROADMAP

Hackathon

SQLite

↓

Pilot

PostgreSQL

↓

Enterprise

Neo4j

↓

Government Scale

Distributed Microservices

The architecture should allow migration without changing business logic.

---

# 18. TECHNOLOGY DECISIONS

Frontend

Next.js

Reason

Fast development and excellent React ecosystem.

Backend

FastAPI

Reason

High performance, automatic API documentation, and strong AI ecosystem.

Vector Database

Qdrant

Reason

Lightweight, free tier available, and optimized for semantic search.

Knowledge Graph

NetworkX

Reason

Simple for MVP and easy to migrate to Neo4j.

LLM

Claude / GPT / Gemini

Reason

Excellent reasoning capability with API support.

Embeddings

bge-m3 or multilingual-e5

Reason

Strong multilingual retrieval performance, including Vietnamese.

---

# 19. NON-FUNCTIONAL REQUIREMENTS

Availability

>99%

Maintainability

High

Scalability

High

Reliability

High

Security

Medium (Hackathon MVP)

Performance

Optimized for demo environment.

---

# 20. ARCHITECTURE SUCCESS CRITERIA

The architecture is considered successful if:

✓ Frontend and backend communicate correctly.

✓ Documents are uploaded and indexed.

✓ Knowledge Graph is generated.

✓ Hybrid RAG retrieves relevant evidence.

✓ AI responses include legal citations.

✓ Claim verification produces explainable results.

✓ The dashboard reflects live project data.

✓ Every module can be demonstrated independently.

---

END OF SYSTEM ARCHITECTURE SPECIFICATION
