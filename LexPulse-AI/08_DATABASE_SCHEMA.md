# DATABASE SCHEMA SPECIFICATION

Version: 1.0

Project: LexPulse AI

Purpose:
This document defines the database schema for the LexPulse AI MVP.

---

# DATABASE OVERVIEW

Database Engine (MVP)

SQLite

Future

PostgreSQL

---

# ENTITY RELATIONSHIP OVERVIEW

Users
    │
    ├──────────────┐
    │              │
    ▼              ▼
Chat Sessions   Uploaded Documents
                      │
                      ▼
                 Document Chunks
                      │
        ┌─────────────┴───────────────┐
        ▼                             ▼
 Embeddings                     Graph Nodes
                                        │
                                        ▼
                                   Graph Edges
                                        │
                                        ▼
                               Knowledge Graph

Social Posts
      │
      ▼
Claims
      │
      ▼
Legal Citations

---

# TABLE 1

Users

Purpose

Store user accounts.

Fields

id (UUID)

name

email

password_hash

role

avatar_url

created_at

updated_at

---

Roles

Citizen

Business

Government

Lawyer

Admin

---

# TABLE 2

Documents

Purpose

Store uploaded legal documents.

Fields

id

title

document_type

issuer

effective_date

expiration_date

status

file_name

file_path

language

uploaded_by

created_at

updated_at

---

Document Types

Law

Decree

Circular

Decision

Directive

Resolution

Other

---

Status

Draft

Indexed

Archived

Deleted

---

# TABLE 3

Document Chunks

Purpose

Store chunked document sections.

Fields

id

document_id

article_number

clause_number

point_number

text

page

chunk_index

embedding_id

created_at

---

Example

Law

↓

Article 12

↓

Clause 3

↓

Point b

↓

Chunk

---

# TABLE 4

Embeddings

Purpose

Store vector metadata.

Fields

id

chunk_id

embedding_model

vector_id

dimension

created_at

---

Vector Database

Qdrant

---

# TABLE 5

Knowledge Graph Nodes

Purpose

Represent every legal entity.

Fields

id

node_type

label

description

document_id

metadata_json

created_at

---

Node Types

Law

Article

Clause

Point

Organization

Topic

Penalty

Deadline

Obligation

Right

Prohibited Act

Citizen

Business

---

# TABLE 6

Knowledge Graph Edges

Purpose

Represent relationships.

Fields

id

source_node

target_node

relation

confidence

created_at

---

Relations

BELONGS_TO

AMENDS

SUPERSEDES

REFERENCES

RELATED_TO

HAS_PENALTY

HAS_DEADLINE

HAS_RIGHT

HAS_OBLIGATION

CONFLICTS_WITH

---

# TABLE 7

Topics

Purpose

Store extracted legal topics.

Fields

id

name

description

category

created_at

---

Example

Traffic

Tax

Banking

Labor

Investment

Education

Health

Land

---

# TABLE 8

Social Posts

Purpose

Store public discussions.

Fields

id

platform

author

content

url

posted_at

created_at

---

Platforms

Facebook

Threads

TikTok

YouTube

Forum

News

---

# TABLE 9

Claims

Purpose

Store extracted legal claims.

Fields

id

post_id

claim_text

status

confidence

created_at

---

Status

Correct

Incorrect

Misleading

Need Context

Unknown

---

# TABLE 10

Citations

Purpose

Store legal evidence.

Fields

id

claim_id

document_id

article

clause

point

citation_text

source_url

created_at

---

# TABLE 11

Chat Sessions

Purpose

Conversation history.

Fields

id

user_id

title

created_at

updated_at

---

# TABLE 12

Messages

Purpose

Store AI conversations.

Fields

id

session_id

role

message

citation_ids

created_at

---

Roles

User

Assistant

System

---

# TABLE 13

Analytics

Purpose

Dashboard metrics.

Fields

id

metric_name

metric_value

date

created_at

---

Example

Most Asked Law

Trending Topic

Most Verified Claim

Most Viewed Regulation

---

# TABLE 14

System Logs

Purpose

System monitoring.

Fields

id

level

module

message

created_at

---

Levels

INFO

WARNING

ERROR

CRITICAL

---

# DATABASE RELATIONSHIPS

Users

1

↓

N

Chat Sessions

↓

Messages

----------------------------

Documents

1

↓

N

Chunks

↓

Embeddings

----------------------------

Documents

1

↓

N

Knowledge Nodes

↓

Knowledge Edges

----------------------------

Social Posts

1

↓

N

Claims

↓

Citations

↓

Documents

---

# INDEXES

Documents.title

Documents.document_type

Chunks.document_id

Chunks.article_number

Nodes.node_type

Nodes.label

Claims.status

Messages.session_id

Analytics.metric_name

---

# CASCADE RULES

Delete Document

↓

Delete Chunks

↓

Delete Embeddings

↓

Delete Graph Nodes

↓

Delete Graph Edges

---

Delete User

↓

Delete Sessions

↓

Delete Messages

---

# STORAGE STRATEGY

SQLite

↓

Metadata

Qdrant

↓

Vectors

NetworkX

↓

Knowledge Graph

Filesystem

↓

Original PDF

---

# FUTURE MIGRATION

SQLite

↓

PostgreSQL

NetworkX

↓

Neo4j

Filesystem

↓

AWS S3

Single Server

↓

Microservices

---

# DESIGN PRINCIPLES

Normalize data where practical.

Avoid duplicate storage.

Keep graph relationships lightweight.

Separate metadata from embeddings.

Never store vectors directly inside SQLite.

Use UUIDs for all primary keys.

Support future migration without changing the schema.

---

# MVP DATABASE LIMITS

Documents

≤ 500

Chunks

≤ 30,000

Graph Nodes

≤ 50,000

Graph Edges

≤ 100,000

Chat Sessions

Unlimited

Messages

Unlimited

---

# END OF DATABASE SPECIFICATION
