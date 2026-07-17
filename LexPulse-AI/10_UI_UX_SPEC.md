10. Frontend Component Architecture — Revised
10.1 Purpose

This document defines the frontend architecture for LexPulse AI MVP.

The objective is to create a frontend that is:

Easy to develop
Easy to maintain
Consistent with backend APIs
Suitable for a small development team

The architecture prioritizes delivery speed over excessive abstraction.

10.2 Frontend Technology Stack
Framework

React + TypeScript

Styling

Tailwind CSS

State Management

Lightweight state management.

Recommended:

React Context for simple global states
Zustand only when shared state complexity requires it

The MVP does not require multiple isolated stores by default.

10.3 Frontend Architecture Principles
Principle 1: Feature-Based Organization

The project is organized around user features rather than technical layers.

Structure:

src/

├── app/

├── features/

│   ├── chat/

│   ├── verify/

│   ├── documents/

│   ├── graph/

│   └── dashboard/

│

├── components/

├── services/

├── hooks/

├── types/

└── utils/

10.4 Feature Responsibility
Chat Feature

Responsible for:

Sending questions
Streaming responses
Displaying answers
Showing citations

Components:

ChatPage

├── ChatInput

├── MessageList

├── MessageBubble

├── CitationCard

└── EvidencePanel
Verification Feature

Responsible for:

Claim submission
Verdict display
Evidence explanation

Components:

VerifyPage

├── ClaimInput

├── VerdictCard

├── EvidenceList

└── ConfidenceIndicator
Document Feature

Responsible for:

Upload
Processing status
Document listing

Components:

DocumentPage

├── UploadForm

├── ProcessingStatus

├── DocumentTable

└── Pagination
Knowledge Graph Feature

Responsible for:

Graph visualization
Relationship exploration

Components:

GraphPage

├── GraphCanvas

├── NodeDetail

└── RelationshipList
10.5 Shared Components

Reusable components:

components/

├── Button

├── Modal

├── LoadingState

├── ErrorState

├── EmptyState

├── Pagination

└── Layout
10.6 Error Handling Strategy

The frontend uses multiple error layers.

Global Error Boundary

A root-level React ErrorBoundary handles:

Unexpected rendering errors
Component crashes
Invalid API response rendering

Example:

Application

↓

ErrorBoundary

↓

Pages

↓

Components
Feature-Level Error Handling

Each feature must handle:

Loading state
Empty state
API failure

Example:

Chat:

Loading response
Failed retrieval
No evidence found
10.7 API Integration Layer

The frontend communicates with backend through services.

Structure:

services/

├── authService.ts

├── chatService.ts

├── documentService.ts

├── verifyService.ts

└── graphService.ts

Components should not directly call APIs.

Example:

Bad:

ChatPage → fetch()

Good:

ChatPage

↓

chatService

↓

API
10.8 Type Management Strategy

The frontend must maintain consistency with backend schemas.

Preferred approach:

Generate TypeScript types from FastAPI OpenAPI schema.

Flow:

FastAPI Pydantic Models

↓

OpenAPI Schema

↓

TypeScript Types

↓

Frontend

This prevents:

API mismatch
Incorrect fields
Runtime errors
10.9 State Management
Local State

Used for:

Input fields
Temporary UI states
Modal visibility
Global State

Used only for:

Authentication
Current user
Application settings
Server State

Handled through:

React Query / TanStack Query

Used for:

API caching
Loading states
Refetching
10.10 Chat UI Architecture

The Chat interface supports:

Response Streaming

The UI should display:

Processing state
Retrieval progress
Final response

Example:

Searching legal documents...

↓

Finding evidence...

↓

Generating explanation...
Citation Display

Each legal answer should show:

Document name
Article
Clause
Evidence snippet
10.11 Graph UI Architecture

The graph visualization should prioritize:

Understanding relationships
Evidence exploration

The UI should avoid:

Showing excessive nodes
Unfiltered graph complexity
10.12 Document Processing UI

Upload flow:

Upload File

↓

Validation

↓

Processing

↓

Embedding

↓

Graph Building

↓

Completed

The frontend displays:

Current status
Progress percentage
Errors
10.13 Responsive Design

The MVP supports:

Desktop
Tablet

Mobile optimization is considered secondary.

10.14 Performance Guidelines

The frontend should:

Lazy load large components
Avoid unnecessary rerenders
Paginate large datasets
Limit graph rendering size
10.15 Security Guidelines

Frontend must:

Never store sensitive secrets
Validate user inputs
Handle expired tokens
Prevent unsafe HTML rendering
10.16 Development Rules

The team should follow:

Required

✓ Clear component responsibility

✓ Reusable common components

✓ API abstraction

✓ Error handling

Flexible

The team may simplify:

Folder structure
State management
Component abstraction

when under time pressure.

10.17 MVP Frontend Completion Criteria

Frontend is complete when:

✓ Users can ask legal questions

✓ Citations are visible

✓ Claims can be verified

✓ Documents can be uploaded

✓ Processing progress is displayed

✓ Knowledge Graph can be explored

✓ Errors are handled gracefully

10.18 Future Improvements

Possible improvements:

Advanced design system
Mobile application
Real-time collaboration
Advanced dashboard analytics
