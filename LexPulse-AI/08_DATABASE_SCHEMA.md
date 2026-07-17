8. Database Schema Specification — Revised
8.1 Purpose

This document defines the database design for LexPulse AI MVP.

The database is responsible for storing:

User information
Legal documents
Document versions
Processing metadata
Conversation history
Citation relationships
Knowledge Graph metadata

The design prioritizes:

Data consistency
Traceability
Explainability
Future migration capability
8.2 Storage Architecture

LexPulse AI uses three storage layers:

SQLite

Purpose:

Persistent application metadata.

Stores:

Users
Documents
Chunks
Messages
Citations
Processing jobs
Qdrant

Purpose:

Vector storage.

Stores:

Document embeddings

SQLite stores only:

Vector ID
Embedding model
Dimension information

The system does NOT store raw vectors in SQLite.

NetworkX

Purpose:

Runtime Knowledge Graph representation.

Stores:

Nodes
Relationships

The MVP uses single-instance deployment.

8.3 Database Design Principles
Principle 1: Persistent Truth

SQLite is the source of truth for stored metadata.

NetworkX is only a runtime graph representation.

Principle 2: Version Awareness

Legal documents change over time.

The database must support:

Current version
Previous version
Amendment relationship
Principle 3: Avoid Uncontrolled JSON Storage

JSON fields are allowed only when the schema is documented.

8.4 Users Table
Users
Field	Type	Constraint	Description
id	UUID	Primary Key	User identifier
email	VARCHAR	Unique, Nullable	User email
password_hash	VARCHAR	Nullable	Authentication data
role	ENUM	Required	guest/user/admin
created_at	TIMESTAMP	Required	Creation time
updated_at	TIMESTAMP	Required	Last update
8.5 Documents Table
Documents
Field	Type	Constraint	Description
id	UUID	Primary Key	Document ID
title	VARCHAR	Required	Document name
source_url	TEXT	Nullable	Original source
publisher	VARCHAR	Nullable	Issuing organization
domain	ENUM	Required	Traffic/Labor
version	VARCHAR	Required	Document version
effective_date	DATE	Nullable	Effective date
status	ENUM	Required	Processing status
uploaded_by	UUID	Foreign Key	User
previous_version_id	UUID	Foreign Key	Previous document version
created_at	TIMESTAMP	Required	Creation time
8.6 Document Version Relationship

A legal document can have multiple versions.

Example:

Labor Law Version 1

        |

     AMENDED_BY

        ↓

Labor Law Version 2

The database supports:

Previous version lookup
Current version comparison
Amendment timeline
8.7 Document Processing Table
Document Processing Jobs

Stores indexing execution history.

Field	Type	Constraint
id	UUID	Primary Key
document_id	UUID	Foreign Key
status	ENUM	Required
progress	INTEGER	0-100
error_message	TEXT	Nullable
started_at	TIMESTAMP	Nullable
completed_at	TIMESTAMP	Nullable
8.8 Document Chunks Table
Chunks

Stores searchable legal text segments.

Field	Type	Constraint
id	UUID	Primary Key
document_id	UUID	Foreign Key
article	VARCHAR	Nullable
clause	VARCHAR	Nullable
point	VARCHAR	Nullable
content	TEXT	Required
chunk_index	INTEGER	Required
created_at	TIMESTAMP	Required
8.9 Embeddings Table
Embeddings

Stores embedding metadata.

Field	Type	Constraint
id	UUID	Primary Key
chunk_id	UUID	Foreign Key
vector_id	VARCHAR	Unique
embedding_model	VARCHAR	Required
dimension	INTEGER	Required
created_at	TIMESTAMP	Required

Actual vectors are stored in Qdrant.

8.10 Knowledge Graph Nodes
Graph Nodes
Field	Type	Constraint
id	UUID	Primary Key
node_type	ENUM	Required
name	VARCHAR	Required
document_id	UUID	Foreign Key
metadata_json	JSON	Optional
confidence	FLOAT	Required
created_at	TIMESTAMP	Required
8.11 Metadata JSON Schema

The metadata_json field must follow controlled structures.

Example:

Article Node
{
 "article_number": "12",
 "legal_domain": "traffic",
 "effective_date": "2026-01-01"
}
Penalty Node
{
 "penalty_type": "administrative",
 "amount": "500000",
 "currency": "VND"
}

Unknown keys should not be added without schema update.

8.12 Knowledge Graph Relationships
Graph Edges
Field	Type
id	UUID
source_node_id	UUID
target_node_id	UUID
relation_type	ENUM
confidence	FLOAT
source_document_id	UUID
created_at	TIMESTAMP
Supported Relation Types

MVP supports:

BELONGS_TO
AMENDS
SUPERSEDES
REFERENCES
RELATED_TO
HAS_PENALTY
HAS_RIGHT
HAS_OBLIGATION
8.13 Messages Table
Messages

Stores user conversations.

Field	Type	Constraint
id	UUID	Primary Key
user_id	UUID	Foreign Key
session_id	UUID	Required
role	ENUM	user/assistant
content	TEXT	Required
confidence	FLOAT	Nullable
created_at	TIMESTAMP	Required
8.14 Message Citations Relationship

Citations are stored through a join table.

Message Citations
Field	Type
id	UUID
message_id	UUID
citation_id	UUID

This avoids storing citation arrays inside messages.

8.15 Citations Table
Citations
Field	Type
id	UUID
document_id	UUID
chunk_id	UUID
article	VARCHAR
clause	VARCHAR
validation_status	ENUM
created_at	TIMESTAMP
8.16 Legal Claims Table
Claims

Stores verification requests.

Field	Type
id	UUID
user_id	UUID
claim_text	TEXT
platform	VARCHAR
author	VARCHAR
url	TEXT
verdict	ENUM
explanation	TEXT
created_at	TIMESTAMP
8.17 Analytics Design

The MVP avoids complex analytics modeling.

Instead of unrestricted EAV:

The system stores predefined events.

Example:

Analytics Events
Field	Type
id	UUID
event_type	VARCHAR
user_id	UUID
document_id	UUID
timestamp	TIMESTAMP

Examples:

question_submitted
document_uploaded
citation_failed
verification_completed

This allows structured querying.

8.18 Database Constraints

Required constraints:

Unique Constraints

Examples:

Users:

email UNIQUE

Documents:

(source_url, version) UNIQUE

Embeddings:

vector_id UNIQUE
Foreign Key Rules

All relationships must define:

Cascade behavior
Delete behavior
Nullability
8.19 Data Retention
User Data

Stored while account exists.

Users may request deletion.

Uploaded Documents

Stored according to ownership rules.

Chat History

Stored only for authenticated users.

8.20 MVP Database Limitations

The MVP supports approximately:

≤500 documents
≤30,000 chunks
≤50,000 graph nodes
≤100,000 graph edges

For larger deployments:

Migration path:

SQLite → PostgreSQL

NetworkX → Neo4j
