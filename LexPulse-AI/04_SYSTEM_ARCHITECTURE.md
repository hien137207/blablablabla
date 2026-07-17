4. System Architecture — Revised
4.1 Architecture Overview

LexPulse AI MVP follows a modular AI application architecture combining:

Retrieval-Augmented Generation (RAG)
Hybrid Search
Knowledge Graph reasoning
Citation validation
Explainable response generation

The architecture is designed around the MVP principle:

Reliability and correctness are prioritized over unnecessary scalability.

4.2 High-Level Architecture
                    User

                     |
                     |

              React Frontend

                     |

                     |

              FastAPI Backend

                     |

      --------------------------------

      |              |              |

  Document      AI Orchestrator   Auth

  Service            |              |

                     |

        ----------------------------

        |            |             |

   Retrieval    Knowledge      Citation

   Pipeline       Graph        Validator


        |

 -------------------------------

 |              |              |

SQLite        Qdrant       NetworkX

Metadata     Vector DB    Graph Memory


        |

        |

       LLM Provider

4.3 Core Architectural Principles
Principle 1: Evidence Before Generation

The LLM must not independently generate legal answers.

The generation pipeline must always follow:

Question

↓

Retrieve Evidence

↓

Analyze Context

↓

Generate Answer

↓

Validate Citation

↓

Return Response
Principle 2: Single Source of Truth

Different components have clear responsibilities.

SQLite

Stores:

User data
Documents metadata
Chunks metadata
Messages
Citations
Processing status
Qdrant

Stores:

Vector embeddings
NetworkX

Stores:

Runtime Knowledge Graph representation

The database remains the persistent source of truth.

Principle 3: MVP Deployment Simplicity

The MVP uses:

Single Backend Instance

Reason:

Hackathon timeline
Reduced synchronization complexity
Easier debugging

The architecture does NOT assume horizontal scaling during MVP.

4.4 Backend Architecture
FastAPI Layer

Responsibilities:

API routing
Authentication
Request validation
Response formatting
AI Orchestrator

The AI Orchestrator manages:

Intent routing
Retrieval strategy
Context preparation
LLM generation
Citation validation
4.5 Request Processing Flow
Legal Question Flow
User Question

↓

Intent Detection

↓

Is Legal Query?

      |

      Yes

      |

Hybrid Retrieval

↓

Knowledge Graph Expansion

↓

Context Ranking

↓

Prompt Construction

↓

LLM Generation

↓

Citation Validation

↓

Final Response

General Conversation Flow

For intents such as:

Greeting
Product explanation
Navigation help

Flow:

User Input

↓

Intent Detection

↓

Direct Response


No legal retrieval is required.

4.6 RAG Pipeline Architecture
Step 1: Intent Routing

The system first determines:

Legal query
General conversation

This prevents unnecessary retrieval.

Step 2: Hybrid Retrieval

The retrieval pipeline combines:

Vector Search

Purpose:

Find semantically similar legal content.

Technology:

Qdrant

Keyword Search

Purpose:

Handle exact legal terms.

Examples:

Article numbers
Regulation names
Legal terminology
Step 3: Knowledge Graph Expansion

The system expands retrieved information through related legal entities.

Example:

Question:

"Phạt lỗi vượt đèn đỏ?"

Retrieved:

Traffic Law Article X

↓

HAS_PENALTY

↓

Administrative Penalty

Only high-confidence graph relationships are used.

4.7 Context Building Strategy

The Context Builder prepares information before sending to the LLM.

Priority order:

Direct legal evidence
Relevant article/clause
Related graph information
Additional explanation

If context exceeds token limits:

The system applies:

Remove low relevance chunks
Keep highest confidence evidence
Preserve citation source

The system must never remove the main supporting evidence silently.

4.8 Reranking Strategy

The MVP uses lightweight reranking.

Pipeline:

Retrieved Candidates

↓

Similarity Score

↓

Keyword Match Score

↓

Legal Structure Match

↓

Final Ranking


A heavy cross-encoder reranker is not required in MVP because of latency constraints.

Future versions may introduce advanced reranking models.

4.9 Knowledge Graph Architecture
Purpose

The Knowledge Graph improves:

Legal relationship discovery
Regulation comparison
Explainable reasoning
4.10 Graph Extraction Pipeline

Graph construction follows:

Legal Document

↓

Legal Structure Parser

↓

Entity Extraction

↓

Relationship Extraction

↓

Confidence Evaluation

↓

Graph Update

4.11 Graph Confidence Gate

LLM-extracted relationships must pass confidence validation.

Each relationship stores:

Source document
Extraction method
Confidence score

Rules:

High Confidence

Automatically added.

Medium Confidence

Added but marked uncertain.

Low Confidence

Stored only for review.

Low-confidence relationships must not influence final legal answers.

4.12 Citation Validation Architecture

Citation validation is a mandatory safety layer.

Flow:

Generated Answer

↓

Extract Citations

↓

Check Document Exists

↓

Check Article Exists

↓

Compare Evidence

↓

Approve / Reject

Validation Failure Handling

If validation fails:

Step 1:

Attempt regeneration once.

Step 2:

If still invalid:

Return:

"Không thể xác minh đầy đủ căn cứ pháp lý."

The system must never display fabricated references.

4.13 Confidence Score Design

Confidence score is calculated from:

Confidence =

Retrieval Quality

+

Evidence Coverage

+

Citation Validation

+

Source Reliability


The score is NOT generated directly by the LLM.

4.14 Performance Design
Target
Query Type	Target
Simple Query	<8 seconds
Complex Query	<20 seconds
Fast Path

For simple legal questions:

Pipeline:

Question

↓

Vector Retrieval

↓

Citation Validation

↓

Answer

Graph expansion and advanced reasoning may be skipped.

Complex Path

For complex questions:

Question

↓

Hybrid Search

↓

Graph Expansion

↓

Context Ranking

↓

LLM Reasoning

↓

Validation

4.15 Database and State Management
SQLite

Used for MVP persistent metadata.

Limitations:

Single-instance deployment
Limited concurrent writes
NetworkX

Used as runtime graph memory.

Important constraint:

The MVP does not support multiple backend instances because NetworkX graph state is stored in memory.

Future migration:

NetworkX

↓

Neo4j
4.16 Security Architecture
Input Security

Includes:

File validation
Prompt injection detection
User input sanitization
Retrieval Security

Retrieved documents are treated as information only.

They cannot modify system behavior.

Output Security

Before returning:

The system validates:

Citation correctness
Unsupported claims
Sensitive information exposure
4.17 Future Scalability Roadmap

The MVP intentionally avoids premature scaling.

Future improvements:

Storage

SQLite → PostgreSQL

Vector Database

Qdrant scaling cluster

Knowledge Graph

NetworkX → Neo4j

File Storage

Local storage → Object Storage

Deployment

Single instance → Distributed services

4.18 Architecture Constraints

The MVP intentionally avoids:

Microservices
Multi-agent systems
Enterprise authentication
Complex distributed infrastructure

The goal is:

A reliable and explainable legal AI prototype within limited development time.
