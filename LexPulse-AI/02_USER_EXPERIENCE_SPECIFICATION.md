2. User Experience (UX) Specification — Revised
2.1 UX Goals

The UX design of LexPulse AI focuses on creating a trustworthy, transparent, and efficient legal AI experience.

The main UX objectives are:

Allow users to access legal information quickly
Make AI reasoning understandable
Clearly show legal evidence behind every answer
Reduce user uncertainty when interacting with AI-generated legal information

The system must help users answer three questions:

What is the legal answer?
Which legal evidence supports this answer?
Why did the AI reach this conclusion?
2.2 User Access Model

The MVP uses a simplified access model to prioritize usability and demo effectiveness.

Guest User

Guest users can access:

AI Legal Chat
Legal Claim Verification
Knowledge Graph Exploration

Authentication is NOT required for these features.

Reason:

The MVP demonstration requires users to immediately experience the core value of LexPulse AI without login barriers.

Authenticated User

Authenticated users receive additional capabilities:

Upload legal documents
Save conversation history
Access personal workspace
Manage previous interactions
Administrator

Administrators can:

Manage legal datasets
Upload official legal documents
Trigger document indexing
Monitor processing status
Rebuild Knowledge Graph

The MVP does not implement enterprise-level authentication or organization-based RBAC.

2.3 Main User Journeys
Journey 1: Legal Question Answering
Goal

Users ask legal questions and receive evidence-supported answers.

User Flow
Open Website

↓

AI Chat

↓

Enter Legal Question

↓

Intent Detection

↓

Retrieve Legal Evidence

↓

Generate Response

↓

Citation Validation

↓

Display Answer
User Interface Output

Each answer contains:

1. Direct Answer

A concise explanation understandable to normal users.

2. Legal Basis

Example:

Law: Road Traffic Law
Article: 12
Clause: 3
3. Evidence

The system displays:

Source document
Retrieved text chunk
Relevant legal section
4. Confidence Score

The confidence score must be accompanied by explanation.

Example:

Confidence: 91%

Reason:
- Strong document relevance
- Valid citation
- Supporting evidence found

The confidence score must not appear as an unexplained AI-generated number.

2.4 Legal Claim Verification Journey
Goal

Allow users to verify whether a legal statement is accurate.

User Flow
Open Verification Page

↓

Input Legal Claim

↓

Retrieve Relevant Regulations

↓

Analyze Claim

↓

Generate Verdict

↓

Display Evidence
Verdict Categories

The system supports six verdict types:

Verdict	Description
Correct	Statement is supported by current legal evidence
Incorrect	Statement conflicts with legal evidence
Misleading	Statement contains partial truth but lacks important context
Need Context	Correctness depends on specific conditions
Unknown	No sufficient evidence found
Outdated	Regulation existed previously but has been amended or replaced partially
2.5 Knowledge Graph Exploration Journey
Goal

Help users understand relationships between legal concepts and regulations.

User Flow
Open Knowledge Graph

↓

Select Legal Entity

↓

Display Connected Nodes

↓

Explore Relationships

↓

View Source Documents

Each graph node must display:

Entity name
Entity type
Source document
Related legal references

Example:

Traffic Regulation

        |
        |
    AMENDS

        ↓

Previous Regulation

        |
        |
 HAS_PENALTY

        ↓

Administrative Penalty
2.6 Document Upload Journey
Goal

Allow authenticated users/admins to add new legal documents.

User Flow
Upload Document

↓

File Validation

↓

Processing Dashboard

↓

Text Extraction

↓

Legal Structure Parsing

↓

Chunk Generation

↓

Embedding Creation

↓

Knowledge Graph Extraction

↓

Validation

↓

Completed
2.7 Document Processing Experience

The UI must expose processing progress instead of showing only final status.

Processing States
Status	Description
Uploaded	Document received successfully
Validating	Checking file format and safety
Extracting	Extracting text content
Parsing	Detecting legal structure
Chunking	Creating searchable chunks
Embedding	Generating vector representations
Graph Extraction	Building legal relationships
Validation	Checking extraction quality
Completed	Available for retrieval
Failed	Processing error occurred
2.8 Demo Dataset Experience

To support both reliability and demonstration of document processing, LexPulse AI uses two datasets.

Base Dataset

Purpose:

Provide stable demo functionality.

Contains:

Pre-indexed legal documents
Existing Knowledge Graph
Evaluation examples

Used for:

Chat demonstration
Verification demonstration
Graph exploration
Live Upload Dataset

Purpose:

Demonstrate the document intelligence pipeline.

Flow:

Upload New Document

↓

Show Processing Progress

↓

Index Document

↓

Available For Future Queries

This avoids conflict between:

Immediate demo usability
Real-time document processing demonstration
2.9 Chat Interface Design

The Chat interface includes:

Conversation Panel

Displays:

User questions
AI responses
Citations
Evidence Panel

Displays:

Legal source
Article
Clause
Supporting text
Reasoning Panel

Displays:

Why specific evidence was selected.

Example:

"The system selected Article 12 because it contains the same legal obligation mentioned in the user's question."

2.10 Long Response Experience

Complex legal questions may require longer processing time.

The UI must provide progressive feedback:

Example:

Understanding question...

Searching legal documents...

Analyzing related regulations...

Checking citations...

Preparing answer...

The system should use:

Streaming responses
Progressive loading
Processing indicators

to improve perceived performance.

2.11 Error and Edge Case Experience
Case 1: No Evidence Found

Display:

"Không tìm thấy căn cứ pháp lý phù hợp."

Provide suggestions:

Rewrite question
Specify legal context
Case 2: Citation Validation Failure

If the generated response cannot pass citation verification:

Display:

"Không thể xác minh đầy đủ căn cứ pháp lý cho câu trả lời này."

The system must not present unsupported legal conclusions.

Case 3: Outdated or Partially Applicable Regulation

When regulations have changed:

Display:

"This regulation has been amended. Some provisions may no longer apply."

The UI should show:

Previous regulation
New regulation
Effective date
Relationship between versions
Case 4: Empty Knowledge Graph

When no graph data exists:

Display:

"No legal relationships are available yet."

Available actions:

Load demo dataset
Upload legal documents
2.12 Performance Experience

Performance must distinguish between:

Backend Processing Time

Measured by:

Retrieval duration
Graph traversal duration
LLM generation duration
Citation validation duration
User Perceived Response Time

Measured by:

Time until first UI feedback
Streaming response start
Completion time

The UX should optimize perceived waiting time through progressive disclosure.

2.13 Accessibility Requirements

The system must support:

Vietnamese Language Compatibility

Requirements:

UTF-8 encoding
Vietnamese diacritics
Vietnamese input methods
Responsive Design

Supported platforms:

Desktop
Tablet
2.14 UX Success Criteria

A first-time user should be able to:

Open LexPulse AI
Ask a legal question
Understand the answer
Verify supporting evidence
Explore related regulations

within:

Less than 3 minutes.
