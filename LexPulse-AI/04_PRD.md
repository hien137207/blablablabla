# PART 4 — Technical Architecture Specification

---

# 26. Technical Vision

LexPulse AI được thiết kế theo kiến trúc AI-native, trong đó toàn bộ hệ thống xoay quanh ba thành phần cốt lõi:

1. Legal Knowledge Graph
2. Advanced Retrieval-Augmented Generation (RAG)
3. Public Discourse Analytics

Hệ thống phải ưu tiên:

- Tính mô-đun (Modularity)
- Khả năng mở rộng (Scalability)
- Dễ thay thế mô hình AI
- Dễ thay thế Vector Database
- Dễ triển khai lên Cloud

Mọi thành phần phải có thể hoạt động độc lập thông qua API.

---

# 27. High-Level System Architecture

                      User
                        │
                        ▼
              Next.js Frontend
                        │
                REST API / WebSocket
                        │
                        ▼
                FastAPI Backend
                        │
 ┌────────────┬──────────────┬─────────────┬─────────────┐
 │            │              │             │
 ▼            ▼              ▼             ▼
Auth      AI Service      Admin      Dashboard
 │            │
 │            ▼
 │      AI Orchestrator
 │            │
 ├────────────┼─────────────────────────────┐
 │            │                             │
 ▼            ▼                             ▼
Retriever   Knowledge Graph           Social Analyzer
 │            │                             │
 ▼            ▼                             ▼
Qdrant    NetworkX / Neo4j          PostgreSQL
 │
 ▼
Embedding Model
 │
 ▼
LLM (GPT / Claude / Gemini)

---

# 28. Technology Stack

## Frontend

Framework

Next.js 15

Language

TypeScript

UI Library

shadcn/ui

Styling

TailwindCSS

State Management

Zustand

Charts

Recharts

Knowledge Graph

React Flow

Authentication

Clerk hoặc Auth.js

---

## Backend

Framework

FastAPI

Language

Python 3.12

API

REST

Async

Uvicorn

Dependency Injection

FastAPI Depends

---

## AI Layer

Framework

LangChain

LLM

OpenAI GPT-4.1

Claude

Gemini

(Thông qua abstraction layer)

Embeddings

bge-m3

hoặc

multilingual-e5-large

Re-ranker

bge-reranker

---

## Knowledge Graph

MVP

NetworkX

Production

Neo4j

---

## Vector Database

Qdrant

---

## Relational Database

PostgreSQL

MVP có thể dùng SQLite.

---

## Cache

Redis

---

## Storage

Local

Sau này

AWS S3

---

## Deployment

Docker

Docker Compose

GitHub Actions

Render

Vercel

Railway

---

# 29. Folder Structure

root/

frontend/

backend/

docs/

scripts/

docker/

dataset/

tests/

README.md

---

## frontend/

app/

components/

hooks/

lib/

services/

store/

types/

public/

---

## backend/

app/

api/

services/

core/

models/

schemas/

rag/

graph/

embeddings/

database/

utils/

middleware/

tests/

main.py

---

# 30. Database Design

Users

Documents

Chunks

Embeddings

Graph Nodes

Graph Edges

Social Posts

Claims

Topics

Citations

Logs

Analytics

---

# 31. Database Schema

Users

id

email

password_hash

role

created_at

updated_at

---

Documents

id

title

type

effective_date

issuer

file_path

status

---

Chunks

id

document_id

article

clause

point

text

embedding_id

---

Embeddings

id

chunk_id

vector_id

model

---

Claims

id

social_post_id

claim

status

citation_id

---

Graph Nodes

id

label

type

metadata

---

Graph Edges

source

target

relation

---

# 32. API Architecture

Frontend

↓

FastAPI

↓

Business Layer

↓

Repository Layer

↓

Database

Không được để Frontend truy cập Database trực tiếp.

---

# 33. API Design

GET

/api/chat

POST

/api/chat

POST

/api/upload

GET

/api/document

GET

/api/graph

GET

/api/dashboard

POST

/api/verify

GET

/api/timeline

POST

/api/admin/reindex

POST

/api/admin/rebuild-graph

---

# 34. Authentication Flow

User

↓

Login

↓

JWT

↓

Refresh Token

↓

Protected Route

↓

API

---

# 35. AI Pipeline

User Question

↓

Intent Detection

↓

Hybrid Search

↓

Graph Expansion

↓

Re-ranking

↓

Prompt Building

↓

LLM

↓

Citation Validation

↓

Response

---

# 36. Document Processing Pipeline

PDF

↓

OCR

↓

Cleaning

↓

Metadata Extraction

↓

Chunking

↓

Embedding

↓

Graph Extraction

↓

Store

↓

Index Complete

---

# 37. Social Processing Pipeline

Dataset

↓

Cleaning

↓

Topic Modeling

↓

NER

↓

Claim Extraction

↓

Graph Linking

↓

Risk Scoring

↓

Dashboard

---

# 38. RAG Architecture

User

↓

Retriever

↓

Vector Search

+

BM25

+

Graph Traversal

↓

Merge Results

↓

Re-rank

↓

Prompt

↓

LLM

↓

Citation

↓

Answer

---

# 39. Knowledge Graph Architecture

Node

Law

Decree

Circular

Article

Clause

Point

Topic

Claim

Organization

Person

---

Edges

REFERENCES

AMENDS

SUPERSEDES

BELONGS_TO

RELATED_TO

HAS_TOPIC

HAS_CLAIM

CONFLICTS_WITH

---

# 40. Security

RBAC

JWT

HTTPS

Input Validation

Prompt Injection Protection

Rate Limit

SQL Injection Protection

CORS

---

# 41. Logging

API Logs

AI Logs

Search Logs

Retriever Logs

User Logs

System Logs

---

# 42. Deployment

Frontend

Vercel

Backend

Railway

Database

Supabase PostgreSQL

Vector DB

Qdrant Cloud

Knowledge Graph

Local JSON

(MVP)

---

# 43. GitHub Structure

LexPulse-AI/

docs/

frontend/

backend/

dataset/

docker/

scripts/

.github/

README.md

LICENSE

---

# 44. Coding Standards

PEP8

Black

ESLint

Prettier

SOLID

Clean Architecture

Repository Pattern

Service Pattern

---

# 45. Performance Targets

Simple Question

<5 seconds

Complex Question

<30 seconds

Upload

<10 seconds

Graph

<2 seconds

Search

<3 seconds

Dashboard

<2 seconds

---

# 46. Technical Constraints

MVP chỉ sử dụng:

- Dataset mẫu
- Không crawl realtime
- Không dùng Neo4j Production
- Không yêu cầu GPU Server
- Chạy được trên laptop 16GB RAM

---

# 47. MVP Architecture

Frontend

↓

Backend

↓

RAG

↓

Qdrant

↓

SQLite

↓

NetworkX

↓

LLM API

↓

Dashboard

↓

GitHub

Đây là kiến trúc bắt buộc cho Hackathon.

Không thêm microservices.

Không thêm Kubernetes.

Không thêm Kafka.

Ưu tiên đơn giản, ổn định và dễ demo.
