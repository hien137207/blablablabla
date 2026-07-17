# PART 3 — Functional Requirements, AI Requirements & System Specifications

---

# 18. Functional Requirements

## Module A — Authentication

### FR-001

Hệ thống phải hỗ trợ đăng nhập bằng Email và Google OAuth.

Priority: High

---

### FR-002

Hệ thống phải phân quyền theo Role-Based Access Control (RBAC).

Roles:

- Guest
- Citizen
- Business
- Government Officer
- Legal Professional
- Administrator

Priority: High

---

### FR-003

Mỗi người dùng chỉ được truy cập các chức năng tương ứng với quyền của mình.

---

# Module B — AI Legal Chat

### FR-010

Người dùng có thể nhập câu hỏi bằng tiếng Việt tự nhiên.

Ví dụ:

"Từ ngày 1/7/2026 người dưới 18 tuổi có được mở tài khoản ngân hàng không?"

---

### FR-011

AI phải xác định Intent của câu hỏi.

Ví dụ:

- Search Regulation
- Explain Law
- Compare Regulations
- Verify Claim
- Summarize
- Find Penalty

---

### FR-012

AI phải sử dụng Retrieval-Augmented Generation (RAG).

Không được trả lời bằng kiến thức nội bộ của LLM nếu không có nguồn.

---

### FR-013

Mỗi câu trả lời phải hiển thị:

- Điều
- Khoản
- Điểm
- Văn bản
- Link nguồn

---

### FR-014

Người dùng có thể nhấn vào Citation để mở văn bản gốc.

---

### FR-015

AI phải trả lời bằng ngôn ngữ đơn giản.

Không sử dụng quá nhiều thuật ngữ pháp lý.

---

# Module C — Legal Document Processing

### FR-020

Admin có thể Upload:

- PDF
- DOCX
- TXT

---

### FR-021

Sau khi upload hệ thống tự động:

OCR (nếu cần)

↓

Clean Text

↓

Metadata Extraction

↓

Chunking

↓

Embedding

↓

Knowledge Graph Update

↓

Vector Database

---

### FR-022

Metadata cần trích xuất:

- Title
- Document Type
- Effective Date
- Issuing Authority
- Expiration Date
- References

---

### FR-023

Chunk phải được tạo theo:

Điều

↓

Khoản

↓

Điểm

không cắt giữa câu.

---

# Module D — Knowledge Graph

### FR-030

Hệ thống phải tự động xây dựng Knowledge Graph.

---

### FR-031

Node Types

- Law
- Decree
- Circular
- Article
- Clause
- Point
- Organization
- Person
- Topic

---

### FR-032

Relationship Types

REFERENCES

AMENDS

REPLACES

BELONGS_TO

RELATED_TO

SUPERSEDES

CONFLICTS_WITH

CITES

---

### FR-033

Knowledge Graph phải hỗ trợ Interactive Visualization.

---

### FR-034

Click vào Node.

↓

Hiển thị Metadata.

↓

Điều luật.

↓

Citation.

---

# Module E — Timeline

### FR-040

Hiển thị lịch sử sửa đổi.

Ví dụ

Luật A

↓

Nghị định B

↓

Thông tư C

↓

Thông tư D

---

### FR-041

Cho phép Compare Version.

---

### FR-042

Highlight phần thay đổi.

---

# Module F — Social Media Analysis

### FR-050

Upload Dataset mạng xã hội.

CSV

JSON

---

### FR-051

AI tự động:

Topic Detection

↓

Sentiment

↓

Entity Extraction

↓

Claim Detection

---

### FR-052

Liên kết Claim tới Điều luật tương ứng.

---

### FR-053

Đánh giá:

Correct

Incorrect

Misleading

Need Context

---

### FR-054

Hiển thị Citation.

---

# Module G — Dashboard

### FR-060

Dashboard hiển thị:

Trending Topics

↓

Top Regulations

↓

Misinformation

↓

Communication Risk

↓

Latest Updates

---

### FR-061

Dashboard phải có biểu đồ.

---

### FR-062

Cho phép Filter.

Theo:

Ngày

Loại văn bản

Topic

Risk

---

# Module H — Search

### FR-070

Search hỗ trợ:

Keyword

Semantic

Knowledge Graph

Hybrid Search

---

### FR-071

Search phải hỗ trợ:

Autocomplete

Recent Search

Suggested Question

---

# Module I — Administration

### FR-080

Admin Dashboard

Quản lý:

Documents

Knowledge Graph

Users

Embeddings

Vector Database

Logs

---

### FR-081

Admin có thể Re-index.

---

### FR-082

Admin có thể Rebuild Knowledge Graph.

---

# 19. AI Requirements

## AI-001

LLM chỉ được phép trả lời nếu Retriever trả về tài liệu liên quan.

---

## AI-002

Nếu Retriever không tìm thấy.

AI phải trả lời:

"Tôi chưa tìm thấy căn cứ pháp lý phù hợp."

Không được tự bịa.

---

## AI-003

Citation là bắt buộc.

---

## AI-004

AI phải trả lời bằng tiếng Việt.

---

## AI-005

AI phải ưu tiên:

Tóm tắt

↓

Giải thích

↓

Điều luật

↓

Nguồn

---

## AI-006

Không được đưa ra tư vấn pháp lý cuối cùng.

Luôn thêm Disclaimer.

---

# 20. RAG Requirements

Pipeline

User

↓

Intent Detection

↓

Hybrid Retrieval

↓

Vector Search

+

BM25

+

Graph Traversal

↓

Context Ranking

↓

LLM

↓

Citation

↓

Answer

---

Chunk Size

400–800 tokens.

---

Chunk Overlap

100 tokens.

---

Embedding Model

multilingual-e5-large

hoặc

bge-m3

---

Vector Database

Qdrant

---

Top K

5

---

Re-ranking

Cross Encoder.

---

# 21. Knowledge Graph Requirements

Knowledge Graph phải:

✓ Interactive

✓ Searchable

✓ Zoom

✓ Pan

✓ Expand

✓ Collapse

✓ Filter

✓ Highlight Citation

---

Node phải có:

ID

Title

Document

Article

Clause

Point

Effective Date

Metadata

Embedding ID

---

# 22. Dashboard Requirements

Dashboard gồm:

Overview

Legal Updates

Trending Topics

Knowledge Graph

Timeline

Claim Verification

Communication Risk

Analytics

Admin

---

Dashboard phải Responsive.

---

# 23. Performance Requirements

Simple Question

<5 giây

---

Complex Question

<30 giây

---

Upload

<10 giây

---

Knowledge Graph

<2 giây

---

Dashboard

<3 giây

---

# 24. Non Functional Requirements

Availability

99%

---

Responsive

Desktop

Tablet

Mobile

---

Accessibility

WCAG AA

---

Security

HTTPS

JWT

RBAC

Input Validation

---

Scalability

Có thể mở rộng lên:

100.000+

Legal Documents

---

Maintainability

Modular Architecture

Clean Code

SOLID Principles

---

Observability

Logging

Error Tracking

Health Check

---

# 25. Acceptance Criteria

MVP được coi là hoàn thành nếu:

✓ AI Chat hoạt động.

✓ Citation chính xác.

✓ Upload thành công.

✓ Knowledge Graph hoạt động.

✓ Dashboard hoạt động.

✓ Timeline hoạt động.

✓ Claim Verification hoạt động.

✓ Toàn bộ demo hoàn thành trong 5–7 phút.

✓ Không xuất hiện lỗi nghiêm trọng trong demo.
