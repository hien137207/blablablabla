9. API Specification — Revised
9.1 Purpose

This document defines the API contract for LexPulse AI MVP.

The API provides communication between:

React Frontend
FastAPI Backend
AI Pipeline
Database Services

The design prioritizes:

Clear contracts
Security
Error handling
Explainability
9.2 API Design Principles
Principle 1: Consistent Response Format

All APIs return:

{
  "success": true,
  "data": {},
  "message": null,
  "error": null
}
Principle 2: Evidence Transparency

Legal AI responses must include:

Evidence source
Citation reference
Confidence score
Principle 3: Safe Failure

When evidence is insufficient:

The API must return uncertainty instead of unsupported answers.

9.3 Authentication
Authentication Method

MVP uses:

JWT authentication

Token contains:

{
 "user_id": "uuid",
 "role": "user",
 "expires_at": "timestamp"
}
Token Expiration

Access tokens expire after:

Configurable duration

Refresh tokens may be introduced in future versions.

9.4 Common HTTP Status Codes
Code	Meaning
200	Successful request
201	Created
400	Invalid input
401	Unauthorized
403	Forbidden
404	Not found
409	Conflict
429	Rate limit exceeded
500	Server error
9.5 Rate Limiting

The MVP applies basic protection.

Limits:

Public Endpoints

Examples:

Chat
Verify

Limit:

60 requests/minute/IP

Authenticated Users

Limit:

120 requests/minute/user

Admin Operations

Limit:

10 requests/minute/admin

9.6 File Upload Restrictions

Supported:

PDF
DOCX
TXT

Maximum file size:

50MB

Validation:

MIME type checking
File extension checking
Content validation
9.7 Authentication APIs
POST /auth/register

Create account.

Request:

{
 "email":"user@example.com",
 "password":"password"
}

Response:

{
 "success":true,
 "data":{
   "user_id":"uuid"
 }
}
POST /auth/login

Login user.

Response:

{
 "success":true,
 "data":{
   "access_token":"jwt",
   "expires_in":3600
 }
}
9.8 Chat APIs
POST /chat

Purpose:

Ask legal questions.

Request:

{
 "session_id":"uuid",
 "question":"Không đội mũ bảo hiểm bị phạt bao nhiêu?"
}

Response:

{
 "success":true,
 "data":{
   "answer":"...",
   "confidence":0.91,
   "citations":[
     {
      "document":"...",
      "article":"12",
      "chunk_id":"uuid"
     }
   ]
 }
}
Chat Processing Flow
Question

↓

Intent Detection

↓

Retrieval

↓

Generation

↓

Citation Validation

↓

Response
GET /chat/history

Get user conversation history.

Query:

?page=1
&limit=20

Response:

{
 "success":true,
 "data":{
   "items":[],
   "pagination":{
     "page":1,
     "limit":20,
     "total":100
   }
 }
}
9.9 Document APIs
POST /documents/upload

Upload legal document.

Authorization:

Registered User/Admin

Request:

Multipart form:

file=document.pdf

Response:

{
 "success":true,
 "data":{
   "document_id":"uuid",
   "status":"uploaded"
 }
}
POST /documents/{id}/index

Start indexing.

Response:

{
 "success":true,
 "data":{
   "job_id":"uuid",
   "status":"processing"
 }
}
GET /documents/{id}/status

Check processing progress.

Response:

{
 "success":true,
 "data":{
  "status":"embedding",
  "progress":60
 }
}
9.10 Document Listing
GET /documents

Query:

?page=1
&limit=20

Response:

{
 "success":true,
 "data":{
  "items":[],
  "pagination":{
    "page":1,
    "limit":20,
    "total":500
  }
 }
}
9.11 Verification APIs
POST /verify

Purpose:

Verify legal claims.

Request:

{
 "text":"Vượt đèn đỏ bị phạt 5 triệu đồng",
 "platform":"Facebook",
 "author":"Example User",
 "url":"https://example.com"
}

Response:

{
 "success":true,
 "data":{
   "verdict":"Misleading",
   "explanation":"...",
   "confidence":0.84,
   "citations":[]
 }
}
Verdict Types

Supported:

Correct
Incorrect
Misleading
Need Context
Unknown
Outdated
9.12 Knowledge Graph APIs
GET /graph/nodes

Get graph nodes.

Query:

?page=1
&limit=50

Response:

{
 "success":true,
 "data":{
  "items":[]
 }
}
GET /graph/{node_id}

Get graph relationship details.

Response:

{
 "success":true,
 "data":{
  "node":{},
  "connections":[]
 }
}
9.13 Admin APIs

Admin authorization required.

POST /admin/reindex

Purpose:

Rebuild document indexes.

Required role:

Admin

Response:

{
 "success":true,
 "data":{
  "job_id":"uuid"
 }
}
POST /admin/rebuild-graph

Purpose:

Rebuild Knowledge Graph.

Required role:

Admin

Response:

{
 "success":true,
 "data":{
  "job_id":"uuid"
 }
}
9.14 Error Response Format

All errors follow:

{
 "success":false,
 "data":null,
 "message":"Invalid request",
 "error":{
   "code":"INVALID_FILE"
 }
}
9.15 API Security Requirements
CORS

Allow only configured frontend origins.

Example:

Development:

localhost

Production:

official frontend domain
Authentication Expiry

Expired tokens must return:

HTTP 401

Authorization

Protected endpoints must check:

User identity
Role permission

Examples:

Upload:

User/Admin

Admin operations:

Admin only

9.16 Async Processing Design

Long-running operations use asynchronous jobs.

Examples:

Document indexing
Graph rebuilding

Flow:

Request

↓

Create Job

↓

Return job_id

↓

Frontend Polls Status

↓

Complete

Future versions may support:

WebSocket
Server-Sent Events
9.17 API Limitations

The MVP does not include:

Public API access
Third-party integrations
Enterprise authentication
Webhooks

End of Revised Section 9
