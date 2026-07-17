# COMPONENT ARCHITECTURE

Version: 1.0

Project: LexPulse AI

Purpose:
Define the complete frontend component hierarchy, application state management, data flow, reusable components, and development conventions.

---

# 1. ARCHITECTURE PHILOSOPHY

The frontend must follow Component-Driven Development.

Goals

- Highly reusable
- Small components
- Clear responsibility
- Easy maintenance
- Enterprise quality

Never create large components (>300 lines).

Prefer composition over inheritance.

---

# 2. APPLICATION STRUCTURE

Frontend

│

├── App Router

├── Layout

├── Pages

├── Components

├── Features

├── Hooks

├── Services

├── Stores

├── Types

├── Utils

└── Assets

---

# 3. FOLDER STRUCTURE

frontend/

app/

components/

features/

hooks/

services/

store/

types/

utils/

styles/

public/

---

## app/

Responsible for routing.

Example

app/

layout.tsx

page.tsx

dashboard/

chat/

graph/

timeline/

verify/

documents/

analytics/

admin/

settings/

---

## components/

Reusable UI only.

components/

ui/

layout/

charts/

graph/

forms/

feedback/

cards/

tables/

navigation/

---

## features/

Business logic.

features/

chat/

graph/

timeline/

verify/

documents/

analytics/

dashboard/

---

## services/

API communication.

services/

auth.ts

chat.ts

documents.ts

graph.ts

timeline.ts

verify.ts

dashboard.ts

---

## store/

Global State

store/

authStore.ts

chatStore.ts

graphStore.ts

documentStore.ts

dashboardStore.ts

uiStore.ts

---

# 4. PAGE HIERARCHY

App

↓

Layout

↓

Sidebar

↓

Header

↓

Content

↓

Feature Page

↓

Widgets

↓

Reusable Components

---

# 5. PAGE COMPONENT TREE

Landing

↓

Hero

↓

Feature Cards

↓

Technology Section

↓

Footer

---

Dashboard

↓

Statistics Cards

↓

Recent Documents

↓

Trending Topics

↓

Knowledge Graph Preview

↓

Timeline Preview

↓

Analytics Charts

↓

Quick Actions

---

AI Chat

↓

Chat Sidebar

↓

Conversation

↓

Message Bubble

↓

Citation Card

↓

Input Box

↓

Suggestion List

---

Knowledge Graph

↓

Toolbar

↓

Search

↓

Graph Canvas

↓

Node Details

↓

Relationship List

---

Timeline

↓

Timeline Header

↓

Version Selector

↓

Timeline Graph

↓

Change Detail

---

Verify

↓

Input Card

↓

Claim Result

↓

Citation List

↓

Confidence Indicator

---

Documents

↓

Toolbar

↓

Search

↓

Filter

↓

Table

↓

Pagination

↓

Upload Modal

---

Analytics

↓

Charts

↓

Topic List

↓

Risk Heatmap

↓

Trend Cards

---

Admin

↓

System Cards

↓

User Table

↓

Logs

↓

Actions

---

# 6. COMPONENT LIBRARY

Buttons

PrimaryButton

SecondaryButton

DangerButton

IconButton

Cards

StatisticCard

DocumentCard

CitationCard

TopicCard

RiskCard

NodeCard

Tables

DocumentTable

ClaimTable

TopicTable

UserTable

Forms

SearchInput

Textarea

Dropdown

UploadInput

Checkbox

Switch

Dialogs

UploadDialog

DeleteDialog

ErrorDialog

SuccessDialog

Loading

Spinner

Skeleton

ProgressBar

Toast

EmptyState

ErrorState

---

# 7. CHAT COMPONENTS

ChatLayout

ChatSidebar

Conversation

Message

CitationList

CitationCard

SuggestedQuestions

InputBox

StreamingIndicator

ConfidenceBadge

---

# 8. KNOWLEDGE GRAPH COMPONENTS

GraphCanvas

NodeCard

Edge

Toolbar

SearchBar

NodeDetails

MiniMap

ZoomControls

Legend

FilterPanel

---

# 9. DASHBOARD COMPONENTS

StatisticsGrid

TrendChart

PieChartCard

Heatmap

TopicCard

RecentDocuments

QuickActions

---

# 10. DOCUMENT COMPONENTS

UploadButton

UploadProgress

DocumentTable

FilterBar

PreviewPanel

MetadataCard

StatusBadge

---

# 11. VERIFY COMPONENTS

ClaimInput

VerifyButton

ResultCard

EvidenceList

CitationCard

ConfidenceScore

---

# 12. GLOBAL LAYOUT COMPONENTS

AppLayout

Header

Sidebar

Breadcrumb

Footer

NotificationCenter

UserMenu

ThemeSwitcher

---

# 13. STATE MANAGEMENT

Use Zustand.

Global State

Authentication

Current User

Current Chat

Selected Document

Selected Graph Node

Theme

Sidebar

Notifications

---

# 14. LOCAL STATE

Use React State.

Examples

Modal Open

Dropdown

Tabs

Pagination

Input

---

# 15. DATA FLOW

User

↓

React Component

↓

Store

↓

API Service

↓

FastAPI

↓

Database

↓

Response

↓

Store

↓

UI

---

# 16. API LAYER

Never call fetch directly inside components.

Always

Component

↓

Service

↓

API

↓

Backend

---

Example

ChatPage

↓

chatService

↓

POST /chat

↓

Backend

↓

Response

↓

UI

---

# 17. COMPONENT RULES

Each component should:

Have one responsibility

Receive typed props

Avoid business logic

Be reusable

Contain fewer than 300 lines

---

# 18. NAMING CONVENTION

PascalCase

Component

camelCase

Function

UPPER_CASE

Constants

kebab-case

Folders

---

# 19. PERFORMANCE

Lazy load pages

Memoize expensive components

Virtualize large tables

Debounce search

Cache graph data

---

# 20. ERROR BOUNDARIES

Every feature page must include

Loading State

Empty State

Error State

Retry Button

---

# 21. ACCESSIBILITY

Keyboard navigation

Focus management

ARIA labels

Screen reader support

Accessible colors

---

# 22. RESPONSIVE BREAKPOINTS

Mobile

<640px

Tablet

640–1024px

Desktop

>1024px

Sidebar

Desktop → Fixed

Tablet → Collapsible

Mobile → Drawer

---

# 23. THEME

Default

Light

Future

Dark

---

# 24. CODE QUALITY

Every component

Typed

Documented

Reusable

Small

Readable

Testable

No duplicated code

---

# 25. COMPONENT DEPENDENCY RULE

Pages

↓

Features

↓

Components

↓

UI

Never reverse the dependency.

UI components must never import feature logic.

---

# 26. FUTURE EXTENSIBILITY

The architecture must allow adding:

- Multi-agent workflow
- Additional LLM providers
- More dashboards
- More document types
- Multiple languages
- Government APIs
- Real-time notifications

without restructuring the project.

---

# END OF COMPONENT ARCHITECTURE
