5. Implementation & Execution Specification — Revised
5.1 Purpose

This document defines the implementation strategy and development execution plan for LexPulse AI MVP.

The objective is to ensure that development focuses on:

A working demonstration
Reliable AI responses
Evidence-grounded legal reasoning
Clear user experience

The implementation plan avoids unnecessary complexity and prioritizes high-risk components early.

5.2 Development Principles
Principle 1: Validate Risk Before Building

The team must identify technically uncertain components before implementing the complete system.

The highest-risk areas are:

Vietnamese legal document parsing
Legal entity extraction
Knowledge Graph quality
Citation validation

Therefore, the MVP begins with a risk validation phase.

Principle 2: Demo First, Architecture Second

The MVP prioritizes:

End-to-end working flow
Reliable legal answers
Citation transparency
Graph visualization
UI improvements
Code optimization
Principle 3: Avoid Premature Engineering

The team should not implement:

Microservices
Complex authentication
Enterprise infrastructure
Advanced AI orchestration

unless required by MVP functionality.

5.3 Development Phases
Phase 0: Risk Spike & Dataset Validation

Duration:

Initial development stage

Purpose:

Validate the hardest technical assumptions before full implementation.

Tasks
Legal Dataset Preparation

Collect:

Traffic Law documents
Labor Law documents

Minimum dataset:

10-20 legal documents
100+ evaluation questions
Document Parsing Experiment

Test:

PDF extraction
Article detection
Clause detection
Legal hierarchy parsing
Knowledge Graph Experiment

Validate:

Entity extraction
Relationship extraction
Confidence scoring

Example:

Article 12

       |

    HAS_PENALTY

       |

Traffic Violation
RAG Baseline Test

Build a minimal pipeline:

Question

↓

Embedding Search

↓

Retrieve Chunk

↓

LLM Answer

↓

Citation Check
Phase 0 Success Criteria

Continue development only if:

✓ Legal documents can be extracted successfully

✓ Retrieval returns relevant evidence

✓ Article references can be detected

✓ Basic citation validation works

Phase 1: Project Foundation
Objective

Create stable development environment.

Tasks:

Backend:

FastAPI setup
Database connection
API structure

Frontend:

React setup
Routing
UI framework

Infrastructure:

Environment configuration
Deployment setup
Phase 2: Database Implementation
Objective

Implement core data storage.

Tasks:

Create models for:

Users
Documents
Document Versions
Chunks
Messages
Citations
Processing Jobs

Implement:

Database migrations
Validation rules
Unique constraints
Phase 3: Authentication & User System
Objective

Implement basic access control.

Tasks:

Guest:

Public exploration

User:

Account management
History storage

Admin:

Dataset management

Enterprise authentication is not included.

Phase 4: Document Processing Pipeline
Objective

Build legal document intelligence pipeline.

Pipeline:

Upload

↓

Validation

↓

Extraction

↓

Legal Parsing

↓

Chunking

↓

Embedding

↓

Storage

Tasks:

PDF/DOCX processing
Legal hierarchy extraction
Chunk generation
Metadata storage
Phase 5: Knowledge Graph Construction
Objective

Create explainable legal relationships.

Tasks:

Entity extraction:

Law
Article
Clause
Penalty
Obligation
Right

Relationship extraction:

BELONGS_TO
AMENDS
SUPERSEDES
REFERENCES
HAS_PENALTY

Apply:

Confidence scoring
Validation gate
Phase 6: Retrieval System
Objective

Build reliable legal retrieval.

Tasks:

Implement:

Vector Search

Using:

Qdrant

Keyword Search

Using:

BM25-based retrieval

Hybrid Ranking

Combine:

Semantic similarity
Keyword relevance
Legal structure relevance
Phase 7: AI Chat System
Objective

Provide evidence-grounded answers.

Tasks:

Implement:

Intent detection
Fast path routing
Complex reasoning path
Context builder
Prompt builder
Citation validation
Phase 8: Claim Verification System
Objective

Verify legal statements.

Tasks:

Implement:

Input:

Legal claim

Output:

Verdict
Explanation
Evidence
Confidence
Phase 9: Frontend Experience
Objective

Build user-facing features.

Pages:

Chat
Verify
Knowledge Graph
Document Upload
Dashboard

Implement:

Evidence cards
Citation display
Graph visualization
Processing status
Phase 10: Integration & Demo Preparation
Objective

Create complete demonstration flow.

Demo scenario:

Open Website

↓

Ask Legal Question

↓

Show Evidence

↓

Verify Claim

↓

Explore Graph

↓

Upload Document

↓

Show Processing
Phase 11: Testing & Evaluation
Objective

Validate system reliability.

Testing includes:

API Testing

Check:

Endpoint behavior
Authentication
Error handling
AI Evaluation

Using evaluation dataset:

Measure:

Retrieval accuracy
Citation grounding accuracy
Response correctness
UI Testing

Check:

User flows
Error states
Responsive behavior
5.4 Evaluation Dataset Requirement

The MVP must create an evaluation dataset before final testing.

Dataset includes:

Questions

Examples:

"Đi xe máy không đội mũ bảo hiểm bị phạt bao nhiêu?"

Expected Evidence

Contains:

Document
Article
Clause
Expected Answer Criteria

Used for:

Retrieval evaluation
Citation evaluation
5.5 Priority Rules When Time Is Limited

If development time becomes limited:

The team follows this priority:

Priority 1

Working end-to-end demo

Priority 2

Reliable legal retrieval

Priority 3

Citation validation

Priority 4

Knowledge Graph visualization

Priority 5

UI improvement

Priority 6

Code quality

Priority 7

Future scalability

5.6 Definition of Done

A feature is considered completed when:

✓ Works in real demo scenario

✓ Has basic error handling

✓ Produces reliable output

✓ Does not violate evidence-grounding requirements

5.7 Deployment Strategy

MVP deployment:

Backend:

FastAPI server

Frontend:

React application

Database:

SQLite

Vector storage:

Qdrant

Graph:

NetworkX

The architecture is designed for future migration but optimized for MVP delivery.

5.8 Known MVP Limitations

The MVP accepts:

Limited legal domains
Single-instance deployment
Limited dataset size
Basic graph extraction

These limitations are intentional to maximize reliability.
