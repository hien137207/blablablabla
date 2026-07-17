3. Software Requirements Specification (SRS) — Revised
3.1 Purpose

This Software Requirements Specification defines the functional and non-functional requirements of LexPulse AI MVP.

The purpose of this document is to establish:

System capabilities
User interactions
AI pipeline requirements
Security requirements
Data handling requirements
Performance expectations

The MVP focuses on providing evidence-grounded legal information through Retrieval-Augmented Generation (RAG) and Knowledge Graph reasoning.

3.2 System Scope

LexPulse AI MVP supports:

Legal Question Answering

Users can ask questions related to supported legal domains:

Traffic Law
Labor Law

The system retrieves relevant legal evidence and generates explainable responses.

Legal Claim Verification

Users can submit legal statements.

The system evaluates whether claims are:

Correct
Incorrect
Misleading
Need Context
Unknown
Outdated
Legal Document Intelligence

The system processes legal documents through:

Text extraction
Legal structure parsing
Chunk generation
Embedding creation
Knowledge Graph extraction
Knowledge Graph Exploration

Users can explore relationships between legal entities.

3.3 User Roles

The MVP uses three roles:

Guest

Permissions:

Ask legal questions
Verify claims
Explore public Knowledge Graph

Restrictions:

Cannot upload documents
Cannot access saved history
Registered User

Permissions:

All Guest capabilities
Upload documents
Save conversation history
Manage personal workspace
Administrator

Permissions:

Manage datasets
Manage documents
Trigger indexing
Rebuild Knowledge Graph
Monitor system status
3.4 Functional Requirements
FR-01: User Question Processing

The system shall allow users to submit legal questions.

Input:

Natural language question

Output:

AI-generated explanation
Legal evidence
Citation references
Confidence score
FR-02: Intent Detection and Routing

The system shall classify user input before retrieval.

Supported intents:

Legal Query

Requires:

Retrieval
Evidence grounding
Citation validation

Example:

"Không đội mũ bảo hiểm bị phạt bao nhiêu?"

General Conversation Intent

Does not require legal retrieval.

Examples:

Hello
What can you do?
Explain your features

For these intents, the system may respond without legal evidence.

This exception prevents unnecessary retrieval while maintaining the requirement:

Legal answers must always be supported by evidence.

FR-03: Legal Document Upload

The system shall allow authorized users to upload legal documents.

Supported formats:

PDF
DOCX
TXT

The system must validate:

File type
File size
File safety
FR-04: Document Processing Pipeline

Uploaded documents shall be processed through:

Upload

↓

Validation

↓

Text Extraction

↓

Legal Structure Parsing

↓

Chunk Creation

↓

Embedding Generation

↓

Vector Indexing

↓

Knowledge Graph Extraction

↓

Validation
FR-05: Document Indexing Idempotency

The system shall prevent duplicate indexing.

When the same document is processed multiple times:

The system must:

Detect existing document version
Reuse existing embeddings where possible
Avoid duplicate chunks
Avoid duplicate graph nodes

Each indexing operation must have a unique processing identifier.

FR-06: Evidence-Grounded Response Generation

The system shall never generate unsupported legal conclusions.

For legal queries:

The response pipeline must:

Retrieve evidence
Generate answer using retrieved context
Validate citations
Return answer only if evidence requirements are satisfied

If evidence is insufficient:

The system must respond:

"Không đủ căn cứ pháp lý để đưa ra kết luận."

FR-07: Citation Validation

The system shall validate generated citations.

Validation checks:

Document Existence

Referenced document exists.

Legal Reference Existence

Article, Clause, Point exists.

Evidence Alignment

Retrieved evidence supports generated statement.

Citation Validation Failure Handling

If validation fails:

The system must:

Remove unsupported citation
Retry generation once if possible
Otherwise return uncertainty response

The system must never silently display invalid citations.

FR-08: Legal Version Tracking

The system shall support regulation version comparison.

Each document must contain:

Version identifier
Effective date
Previous version reference
Superseded document reference

The system should support:

Previous regulation view
Current regulation view
Amendment relationship
FR-09: Knowledge Graph Management

The system shall maintain legal relationships.

Supported entities:

Law
Article
Clause
Point
Organization
Penalty
Obligation
Right

Supported relationships:

BELONGS_TO
AMENDS
SUPERSEDES
REFERENCES
HAS_PENALTY
HAS_RIGHT
HAS_OBLIGATION
RELATED_TO
FR-10: Graph Extraction Confidence Control

Knowledge Graph extraction must include confidence evaluation.

For each extracted relationship:

Store:

Extraction source
Extraction method
Confidence score

Low-confidence relationships must not automatically appear as trusted legal facts.

FR-11: Conversation History

Authenticated users may access previous conversations.

Stored information:

User message
AI response
Citations
Timestamp
FR-12: Verification System

The system shall allow users to verify legal claims.

Input:

Claim text

Optional metadata:

Source platform
Author
URL

Output:

Verdict
Explanation
Supporting evidence
FR-13: Administration

Administrators can:

Upload official datasets
Trigger document re-indexing
Rebuild Knowledge Graph
Monitor processing status

Admin operations require role verification.

3.5 Non-Functional Requirements
NFR-01: Performance

The system targets:

Operation	Target
Simple legal query	<8 seconds
Complex reasoning query	<20 seconds
Dashboard loading	<2 seconds

Measurement includes:

Backend processing time
User-perceived response time
NFR-02: Availability

The MVP does not provide production SLA guarantees.

Requirement:

The system must remain stable throughout demonstrations and testing sessions.

Future production versions may introduce formal availability targets.

NFR-03: Security
Prompt Injection Protection

The system shall apply:

Input Layer
User input filtering
Malicious instruction detection
Retrieval Layer
Retrieved documents treated as data, not instructions
Generation Layer
Protected system instructions
Output validation
NFR-04: Data Privacy and Retention

The system must define storage policies.

Uploaded Documents

Stored with:

Owner information
Source information
Processing status
Chat History

Stored only for authenticated users.

Users may delete stored conversations.

Personal Data

If documents contain personal information:

Data usage must be documented
Storage should follow privacy principles
NFR-05: Database Reliability

The MVP uses a single-instance deployment model.

Constraints:

SQLite is used only for MVP scale
Concurrent heavy writes should be limited
Future migration path exists toward PostgreSQL
NFR-06: Encoding and Localization

The system must support:

UTF-8 encoding
Vietnamese Unicode characters
Vietnamese input methods
3.6 Business Rules
Rule 1

Legal answers require verified evidence.

Rule 2

The system must not invent:

Laws
Articles
Clauses
Penalties
Rule 3

Low-confidence Knowledge Graph relationships must not be treated as authoritative.

Rule 4

Document re-indexing must not create duplicate data.

Rule 5

Administrative operations require administrator authorization.

3.7 MVP Constraints

The MVP prioritizes:

Working demonstration
Reliable legal answers
Evidence transparency
Knowledge Graph visualization

The MVP does not prioritize:

Enterprise scalability
Complex authentication
Multi-agent architecture
