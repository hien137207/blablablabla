# API SPECIFICATION

Version: 1.0

Project: LexPulse AI

Purpose:
Define all backend REST APIs for the LexPulse AI MVP.

Base URL

/api/v1

Content-Type

application/json

Authentication

JWT Bearer Token

---

# RESPONSE FORMAT

Every API must return the same structure.

Success

{
  "success": true,
  "message": "Success",
  "data": {}
}

Error

{
  "success": false,
  "message": "Error message",
  "error_code": "ERROR_CODE"
}

---

# AUTHENTICATION

## POST /auth/register

Create new account.

Request

{
  "name":"Nguyen Van A",
  "email":"abc@gmail.com",
  "password":"123456"
}

Response

{
  "user":{
      "id":"uuid",
      "email":"abc@gmail.com"
  }
}

---

## POST /auth/login

Request

{
  "email":"",
  "password":""
}

Response

{
  "access_token":"",
  "refresh_token":"",
  "expires_in":3600
}

---

## POST /auth/logout

Invalidate current token.

---

## GET /auth/me

Return current user profile.

---

# DOCUMENT MODULE

## POST /documents/upload

Upload PDF or DOCX.

Multipart Form Data

file

document_type

language

Response

{
 "document_id":"uuid",
 "status":"uploaded"
}

---

## GET /documents

List all documents.

Query

page

limit

search

type

issuer

---

## GET /documents/{id}

Return document metadata.

---

## DELETE /documents/{id}

Delete document.

---

## POST /documents/{id}/index

Generate chunks

Generate embeddings

Update graph

Response

{
 "status":"indexed"
}

---

# AI CHAT

## POST /chat

Main AI endpoint.

Request

{
 "question":"Theo luật mới doanh nghiệp FDI được hỗ trợ gì?"
}

Pipeline

Intent Detection

↓

Hybrid Search

↓

Knowledge Graph Expansion

↓

Reranking

↓

LLM

↓

Citation Validation

↓

Answer

---

Response

{
 "answer":"...",
 "confidence":0.95,
 "citations":[...],
 "related_documents":[...],
 "processing_time":"2.3s"
}

---

## GET /chat/history

Conversation history.

---

## DELETE /chat/history/{id}

Delete session.

---

# KNOWLEDGE GRAPH

## GET /graph

Return graph.

Query

keyword

node_type

document

---

Response

{
 "nodes":[...],
 "edges":[...]
}

---

## GET /graph/node/{id}

Return node detail.

Includes

Metadata

Relations

Source

Connected Nodes

---

## GET /graph/search

Semantic node search.

---

# TIMELINE

## GET /timeline

Return legal amendment timeline.

Query

document_id

---

Response

{
 "timeline":[]
}

---

## GET /timeline/compare

Compare two versions.

Query

old_document

new_document

Response

{
 "removed":[...],
 "added":[...],
 "modified":[...]
}

---

# CLAIM VERIFICATION

## POST /verify

Verify public statement.

Request

{
 "text":"Người dưới 18 tuổi không được mở tài khoản ngân hàng."
}

---

Pipeline

Claim Extraction

↓

Retriever

↓

Knowledge Graph

↓

LLM

↓

Citation

↓

Verdict

---

Response

{
 "status":"Misleading",
 "explanation":"...",
 "citations":[...],
 "confidence":0.93
}

---

# DASHBOARD

## GET /dashboard

Return overview.

Includes

Total Documents

Total Nodes

Total Claims

Trending Topics

Latest Regulations

Top Discussions

Communication Risk

---

## GET /dashboard/analytics

Return charts.

Query

date_from

date_to

topic

---

# SEARCH

## GET /search

Hybrid Search.

Query

keyword

semantic

document_type

topic

---

Response

Documents

Graph Nodes

Relevant Clauses

Citations

---

# ADMIN

## GET /admin/statistics

System statistics.

---

## POST /admin/reindex

Re-index all embeddings.

---

## POST /admin/rebuild-graph

Rebuild Knowledge Graph.

---

## GET /admin/logs

Return logs.

---

# HEALTH

## GET /health

Response

{
 "status":"healthy"
}

---

# ERROR CODES

AUTH_001

Unauthorized

AUTH_002

Invalid Token

DOC_001

Document Not Found

DOC_002

Upload Failed

DOC_003

Index Failed

CHAT_001

Question Empty

CHAT_002

No Legal Evidence Found

GRAPH_001

Node Not Found

VERIFY_001

Cannot Verify Claim

SYSTEM_001

Unexpected Error

---

# STATUS CODES

200

OK

201

Created

400

Bad Request

401

Unauthorized

403

Forbidden

404

Not Found

422

Validation Error

500

Internal Server Error

---

# SECURITY

JWT Authentication

Role-Based Access Control

Rate Limiting

Request Validation

File Type Validation

Prompt Injection Protection

SQL Injection Protection

CORS

HTTPS Only

---

# PERFORMANCE TARGETS

Chat

<5 seconds

Claim Verification

<15 seconds

Knowledge Graph

<2 seconds

Search

<3 seconds

Upload

<10 seconds

Dashboard

<2 seconds

---

# API VERSIONING

Current

/api/v1

Future

/api/v2

---

# OPENAPI

Backend must automatically generate

Swagger UI

/docs

and

ReDoc

/redoc

using FastAPI.

---

# END OF API SPECIFICATION
