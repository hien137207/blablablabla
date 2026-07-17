# LexPulse AI
# Product Requirements Document (PRD) v2.0

## 1. Product Overview

### 1.1 Product Name

LexPulse AI

### 1.2 Vision

LexPulse AI is an AI-powered Vietnamese legal intelligence assistant designed to help users understand, verify, and explore Vietnamese legal information through Retrieval-Augmented Generation (RAG), Knowledge Graph reasoning, and citation-grounded responses.

The system prioritizes:

- Legal accuracy
- Evidence-based answers
- Transparent reasoning
- Accessible legal knowledge

---

# 2. Problem Statement

Vietnamese legal documents are often:

- Long and difficult to interpret
- Distributed across multiple sources
- Frequently amended
- Difficult for ordinary users to verify

Current AI assistants may generate fluent answers but often suffer from:

- Hallucinated legal references
- Incorrect article citations
- Lack of explanation
- Lack of connection between related regulations

LexPulse AI addresses these problems by grounding every legal answer in verified document evidence.

---

# 3. MVP Scope

## 3.1 Included Scope

The MVP focuses on two Vietnamese legal domains:

### Primary Domain

Traffic Law

Examples:

- Road traffic regulations
- Violations
- Administrative penalties
- Driver responsibilities


### Secondary Domain

Labor Law

Examples:

- Employment contracts
- Employee rights
- Employer obligations


## 3.2 Out of Scope

The MVP does NOT include:

- Full Vietnamese legal coverage
- Enterprise authentication
- Multi-agent AI workflow
- Legal advice replacing lawyers
- Automated legal decisions

---

# 4. Target Users

## 4.1 Guest Users

Guest users can:

- Ask legal questions
- Verify legal claims
- Explore Knowledge Graph
- View evidence-based answers


## 4.2 Registered Users

Registered users can additionally:

- Upload legal documents
- Save conversation history
- Manage personal workspace


## 4.3 Administrators

Administrators can:

- Manage datasets
- Trigger document re-indexing
- Monitor system status

---

# 5. Core Features

## FR-01: AI Legal Chat

Users can ask questions related to supported legal domains.

The system must:

- Retrieve relevant legal evidence
- Generate grounded responses
- Display citations
- Provide confidence indicators


---

## FR-02: Citation-Based Answering

Every legal answer must include:

- Source document
- Article number
- Clause/Point reference
- Retrieved text evidence


The system must never generate unsupported legal citations.


---

## FR-03: Legal Claim Verification

Users can submit a legal statement.

Example:

"Driving without helmet is fined 500,000 VND."

System outputs:

- Correct
- Incorrect
- Misleading
- Need Context
- Unknown
- Outdated / Partially Applicable


---

## FR-04: Knowledge Graph Exploration

Users can explore relationships between:

- Laws
- Articles
- Clauses
- Penalties
- Organizations


---

## FR-05: Document Intelligence

Administrators can upload legal documents.

System performs:

- Text extraction
- Structure parsing
- Chunk creation
- Embedding generation
- Knowledge graph extraction


---

# 6. Explainable AI Requirements

Explainability requires:

Every answer must provide:

1. Retrieved evidence chunks
2. Legal source references
3. Reason for related graph expansion

Example:

"The answer references Article 12 because the user question matches vehicle safety obligations."

---

# 7. Success Metrics

## Accuracy

### Retrieval Accuracy

Target:

≥85%

Measured through:

- Human-labeled evaluation dataset
- Retrieval relevance scoring


### Citation Grounding Accuracy

Target:

≥95%

Measured through:

- Citation existence validation
- Chunk matching
- Evidence-answer alignment


---

## Performance

| Operation | Target |
|-|-|
| Simple legal question | <8 seconds |
| Complex reasoning question | <20 seconds |
| Dashboard loading | <2 seconds |
| Document processing | Async progress tracking |


---

# 8. Data Governance

## Legal Dataset

MVP uses publicly available Vietnamese legal documents.

Data sources:

- Government legal databases
- Public regulatory documents


Every indexed document must store:

- Source URL
- Publisher
- Publication date
- Effective date


---

# 9. Security Requirements

The system must protect against:

## Prompt Injection

Protection includes:

- Input sanitization
- System prompt isolation
- Retrieved context labeling
- Output citation validation


## File Upload Security

The system validates:

- File type
- File size
- Content format


---

# 10. MVP Constraints

Technical constraints:

- Team size: 3 members
- Development time: 35 hours
- Single-instance deployment


Architecture priority:

1. Working demo
2. Reliable AI answers
3. Clean UI
4. Knowledge Graph visualization
5. Dashboard
6. Code quality
7. Scalability


---

# 11. Non Goals

LexPulse AI is not:

- A replacement for lawyers
- A legal judgment system
- A government legal authority


---

# 12. Product Principles

## Never fabricate legal references

If evidence is insufficient:

Return:

"Không đủ căn cứ pháp lý để đưa ra kết luận."


## Evidence before confidence

Confidence score must be derived from:

- Retrieval quality
- Citation validation
- Evidence coverage


---

# Document Version

Version: 2.0

Last Updated:
2026-07-17
