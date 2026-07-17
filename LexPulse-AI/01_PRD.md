# LexPulse AI
# Product Requirements Document (PRD)

Version: 2.0


# 1. Product Overview


## 1.1 Product Name

LexPulse AI


## 1.2 Vision

LexPulse AI is an AI-powered Vietnamese legal intelligence assistant that helps users understand, verify, and explore legal information through Retrieval-Augmented Generation (RAG), Knowledge Graph reasoning, and evidence-based AI responses.

The core principle of LexPulse AI is:

> Every legal answer must be grounded in verified legal evidence.


Unlike general-purpose AI assistants, LexPulse AI prioritizes:

- Citation accuracy
- Transparent reasoning
- Legal source traceability
- User understanding


---

# 2. Problem Statement


Vietnamese legal information is difficult to access and interpret because:

- Legal documents are lengthy and complex
- Regulations are frequently amended
- Related legal provisions are distributed across multiple documents
- Users lack tools to verify legal information quickly


Current AI systems face several limitations:

- Hallucinated legal references
- Incorrect article or clause citations
- Lack of evidence explanation
- Low transparency in reasoning


LexPulse AI addresses these issues by combining:

- Legal document retrieval
- Semantic search
- Knowledge graph relationships
- Citation validation


---

# 3. MVP Scope


## 3.1 Supported Legal Domains


The MVP intentionally focuses on limited domains to ensure accuracy and evaluation feasibility.


## Primary Domain:

### Traffic Law

Including:

- Traffic violations
- Administrative penalties
- Driver obligations
- Road safety regulations


## Secondary Domain:

### Labor Law

Including:

- Employment contracts
- Employee rights
- Employer obligations


The system does NOT attempt to cover all Vietnamese legal domains during MVP.


Future expansion may include:

- Tax law
- Business law
- Civil law


---

# 4. Out of Scope


The MVP does not include:


## Enterprise Authentication

The system does not support:

- Single Sign-On (SSO)
- Enterprise Identity Provider integration
- Organization-level access management


## Multi-Agent Workflow

The MVP uses a single AI orchestration pipeline.


## Legal Decision Automation

The system does not:

- Replace lawyers
- Provide official legal judgments
- Make legally binding decisions


---

# 5. User Roles


The MVP uses a simplified role model.


## Guest User


Can:

- Ask legal questions
- Verify legal claims
- Explore public Knowledge Graph


No authentication is required for demonstration features.


---

## Registered User


Can:

- Save conversation history
- Upload personal documents
- Manage personal workspace


---

## Administrator


Can:

- Manage datasets
- Trigger document indexing
- Monitor system status


The MVP does not implement enterprise RBAC.


---

# 6. Core Product Features


# FR-01: AI Legal Chat


Users can ask questions related to supported legal domains.


The system provides:


## Answer

A natural language explanation.


## Legal Evidence

Including:

- Document name
- Article
- Clause
- Point
- Retrieved text


## Confidence Score

The confidence score must be calculated from:

- Retrieval relevance
- Evidence coverage
- Citation validation


The system must NOT rely only on LLM self-confidence.


---

# FR-02: Legal Claim Verification


Users can submit legal statements.

Example:

"Driving without a helmet results in a fine."


The system returns:


## Verdict Categories


| Verdict | Description |
|-|-|
| Correct | Supported by current legal evidence |
| Incorrect | Contradicted by evidence |
| Misleading | Partially correct but incomplete |
| Need Context | Depends on conditions |
| Unknown | No sufficient evidence |
| Outdated | Regulation changed or partially replaced |


---

# FR-03: Explainable AI Response


Explainability requires:


## Evidence Traceability

The system shows:

- Which document was used
- Which text chunk supported the answer
- Which legal entities were involved


## Knowledge Graph Reasoning Explanation

When graph expansion is used, the system explains:

Example:

"The system retrieved Article 12 because it is connected through the AMENDS relationship with the queried regulation."


---

# FR-04: Legal Document Processing


The system supports:


- Document upload
- Text extraction
- Legal structure parsing
- Chunk creation
- Embedding generation
- Knowledge graph extraction


---

# 7. Data Governance


## Data Sources


Legal documents are collected from:

- Public government legal databases
- Officially published legal documents


The system stores provenance information:


Each document contains:

- Source URL
- Publisher
- Publication date
- Effective date
- Version information


---

# 8. Success Metrics


## Retrieval Accuracy


Target:

≥85%


Measurement:


Using:

- Human-labeled evaluation dataset
- Retrieval relevance scoring


---

## Citation Grounding Accuracy


Target:

≥95%


Measurement:


A citation is considered valid when:


1. Referenced document exists

2. Article/Clause exists

3. Retrieved evidence supports the generated answer


The system does NOT claim perfect citation accuracy.


---

# 9. Non-Functional Requirements


## Accessibility


The system supports:


### Vietnamese Text Compatibility

Requirements:

- UTF-8 encoding
- Vietnamese diacritics
- Common Vietnamese input methods


---

## Performance


Target:


| Operation | Requirement |
|-|-|
| Simple question | <8 seconds |
| Complex reasoning | <20 seconds |
| UI initial loading | <2 seconds |


---

# 10. Security Principles


## Prompt Injection Protection


The system applies:


- Input sanitization
- Retrieved context separation
- System prompt protection
- Output citation verification


---

# 11. Product Principles


## Evidence Before Confidence

The system should prefer:

Verified evidence over fluent generation.


## Never Fabricate Legal References


If evidence is insufficient:


"The system cannot find sufficient legal evidence to provide a conclusion."


---

# 12. MVP Success Criteria


The MVP is considered successful when:


✓ Users can ask legal questions

✓ AI answers contain verifiable citations

✓ Legal claims can be verified

✓ Knowledge Graph relationships can be explored

✓ Responses provide transparent reasoning


---

# Document Information


Version:

2.0


Updated:

2026
