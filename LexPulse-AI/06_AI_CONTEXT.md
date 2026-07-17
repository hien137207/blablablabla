6. AI Context & Development Guidelines — Revised
6.1 Purpose

This document defines the AI development context, system behavior principles, and implementation guidelines for LexPulse AI.

The goal is to ensure that AI components operate according to the core product principle:

Legal answers must be evidence-grounded, explainable, and verifiable.

6.2 AI System Role

LexPulse AI is an AI legal intelligence assistant.

The system is designed to:

Retrieve relevant legal information
Explain regulations in understandable language
Verify legal claims
Provide transparent evidence

The system is NOT:

A lawyer replacement
A legal decision maker
A source of official legal interpretation
6.3 AI Behavior Principles
Principle 1: Evidence Before Answer

The AI must prioritize retrieved legal evidence over general knowledge.

The response generation process:

Question

↓

Retrieve Evidence

↓

Analyze Evidence

↓

Generate Response

↓

Validate Citation

↓

Return Answer
Principle 2: Never Fabricate Legal Information

The AI must never create:

Fake laws
Fake article numbers
Fake penalties
Fake legal references

If evidence is insufficient:

The AI should state:

"Không đủ căn cứ pháp lý để đưa ra kết luận."

Principle 3: Transparency Over Confidence

The AI should explain:

Which evidence was used
Which legal document supports the answer
Why related information was retrieved

A confident answer without evidence is unacceptable.

6.4 AI Pipeline Context

The AI pipeline contains:

1. Intent Detection

Purpose:

Determine whether the request requires legal retrieval.

Categories:

Legal Intent

Requires:

Retrieval
Evidence grounding
Citation validation

Example:

"Đi xe máy vượt đèn đỏ bị phạt bao nhiêu?"

General Intent

Does not require legal retrieval.

Examples:

Greetings
Product questions
Navigation help
6.5 Retrieval-Augmented Generation Context

The AI uses a hybrid retrieval strategy.

Retrieval Sources
Vector Search

Purpose:

Find semantically relevant legal content.

Keyword Search

Purpose:

Find exact legal references.

Examples:

Article numbers
Regulation names
Legal terminology
Knowledge Graph Expansion

Purpose:

Find connected legal concepts.

Example:

Article 12

↓

HAS_PENALTY

↓

Traffic Violation
6.6 Context Construction Rules

The Context Builder must prioritize information:

Priority Order
Direct legal evidence
Relevant article/clause
Related legal relationships
Additional explanation

The AI should avoid:

Excessive unrelated context
Low-confidence graph information
Unsupported assumptions
6.7 Context Window Management

When retrieved context exceeds available token capacity:

The system applies:

Remove lowest relevance information
Preserve direct evidence
Preserve citation metadata
Reduce explanation length before removing evidence

The system must never silently remove the main supporting evidence.

6.8 Knowledge Graph AI Guidelines

Knowledge Graph extraction is considered an assistive reasoning layer.

It must NOT become an uncontrolled source of legal truth.

Graph Extraction Rules

Every extracted relationship must store:

Source document
Extraction method
Confidence score
Confidence Policy
High Confidence

Automatically used.

Example:

Article explicitly references another article.

Medium Confidence

Can support exploration but should not determine legal conclusions alone.

Low Confidence

Stored only for review.

Not used for final answers.

6.9 Prompt Engineering Guidelines
System Prompt Priority

The AI follows this priority:

System Instructions

↓

Security Rules

↓

Retrieved Legal Evidence

↓

User Request

User input cannot override system behavior.

6.10 Prompt Injection Protection

The system assumes that:

User input may contain malicious instructions
Uploaded documents may contain misleading text

Protection strategy:

Input Layer

Detect:

Instruction manipulation
Attempts to override AI behavior
Retrieval Layer

Retrieved documents are treated as:

Data only.

They cannot modify system instructions.

Output Layer

Validate:

Citations
Unsupported claims
Sensitive information
6.11 Response Generation Rules

For legal answers, the AI response should contain:

1. Summary Answer

Short explanation.

2. Legal Basis

Example:

Law:
Article:
Clause:
3. Evidence

Original supporting text.

4. Explanation

Why the evidence supports the conclusion.

5. Uncertainty

If applicable:

Missing information
Conditions
Regulation changes
6.12 Confidence Score Guidelines

Confidence score must be calculated from system signals.

Example:

Confidence Score =

Retrieval Relevance

+

Evidence Coverage

+

Citation Validation

+

Source Reliability

The AI must not generate confidence scores independently.

6.13 LLM Provider Strategy

The MVP supports one primary LLM provider.

Reason:

Reduce implementation complexity
Ensure consistent behavior
Simplify evaluation

Future versions may support multiple providers through abstraction.

6.14 AI Evaluation Principles

AI performance is evaluated using:

Retrieval Quality

Measures:

Relevant evidence retrieval
Correct legal source selection
Citation Grounding

Measures:

Citation existence
Citation accuracy
Evidence alignment
Answer Quality

Measures:

Correctness
Clarity
Explainability
6.15 Development Priority Order

When making implementation decisions:

The priority order is:

Working Demo
Reliable AI Responses
Citation Accuracy
Clear User Experience
Knowledge Graph Capability
Dashboard Features
Code Quality
Scalability Improvements
6.16 AI Development Constraints

The team should avoid:

Building unnecessary autonomous agents
Overcomplicated prompt chains
Unverified AI-generated knowledge graphs
Using LLM confidence as truth
6.17 Final AI Principle

LexPulse AI should behave as:

A cautious legal research assistant that explains what it knows, shows why it knows it, and admits uncertainty when evidence is insufficient.
