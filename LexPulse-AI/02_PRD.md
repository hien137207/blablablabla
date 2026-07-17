# PART 2 — Users, Business Workflow & Product Experience

---

# 10. Target Users

LexPulse AI được thiết kế cho nhiều nhóm người dùng khác nhau.

Mỗi nhóm có mục tiêu, nhu cầu và quyền truy cập riêng.

---

## User Group 1 — Citizens

### Description

Người dân muốn nhanh chóng hiểu quy định pháp luật bằng ngôn ngữ đơn giản.

### Goals

- Hiểu luật mới.
- Kiểm tra thông tin trên mạng xã hội.
- Đặt câu hỏi bằng tiếng Việt tự nhiên.
- Xem nguồn trích dẫn chính xác.

### Permissions

- Chat với AI
- Xem citation
- Xem Knowledge Graph
- Xem Timeline

---

## User Group 2 — Businesses

### Description

Doanh nghiệp muốn đánh giá tác động của luật đối với hoạt động kinh doanh.

### Goals

- Kiểm tra nghĩa vụ pháp lý.
- Phân tích thay đổi của luật.
- Kiểm tra deadline.
- Kiểm tra mức xử phạt.
- Theo dõi văn bản mới.

### Permissions

- Chat
- Dashboard
- Document Upload
- Knowledge Graph
- Timeline
- Report Export

---

## User Group 3 — Government Officers

### Description

Theo dõi xu hướng thảo luận và hiệu quả truyền thông chính sách.

### Goals

- Xác định điều luật đang được quan tâm.
- Theo dõi mức độ hiểu sai.
- Phát hiện misinformation.
- Theo dõi communication risk.

### Permissions

- Dashboard
- Trend Analytics
- Social Analytics
- Knowledge Graph
- Reports

---

## User Group 4 — Legal Professionals

### Description

Luật sư, chuyên viên pháp chế và chuyên gia compliance.

### Goals

- Tìm điều luật.
- Kiểm tra sửa đổi.
- So sánh phiên bản.
- Xem quan hệ giữa các văn bản.

### Permissions

- Advanced Search
- Knowledge Graph
- Timeline
- Citation
- Version Comparison

---

# 11. User Personas

---

## Persona A

Name

Nguyễn Minh

Age

28

Occupation

Startup Founder

Pain Points

- Không có thời gian đọc luật.
- Không biết thông tin trên Facebook đúng hay sai.
- Muốn biết doanh nghiệp phải làm gì.

Expected Result

AI trả lời dễ hiểu, có nguồn.

---

## Persona B

Name

Lan Anh

Age

38

Occupation

Legal Officer

Pain Points

- Nhiều văn bản sửa đổi.
- Khó kiểm tra phiên bản.
- Khó theo dõi hiệu lực.

Expected Result

Timeline + Citation + Version Comparison.

---

## Persona C

Name

Quang

Age

45

Occupation

Government Communication Officer

Pain Points

- Không biết dân đang hiểu sai gì.
- Không biết chủ đề nào đang hot.

Expected Result

Dashboard + Trend + Risk Alert.

---

# 12. User Journey

## Journey 1 — Ask Legal Question

User

↓

Trang chủ

↓

Nhập câu hỏi

↓

AI hiểu ý định

↓

Hybrid Search

↓

Knowledge Graph

↓

LLM

↓

Citation

↓

Hiển thị câu trả lời

↓

Đề xuất điều luật liên quan

---

## Journey 2 — Verify Social Media Claim

User

↓

Paste bài Facebook

↓

Claim Extraction

↓

Knowledge Graph

↓

Legal Verification

↓

AI phân tích

↓

Correct / Incorrect / Misleading

↓

Citation

↓

Giải thích

---

## Journey 3 — Upload New Regulation

Admin

↓

Upload PDF

↓

OCR

↓

Chunking

↓

Metadata Extraction

↓

Knowledge Graph Update

↓

Embedding

↓

Vector Database

↓

Available for Chat

---

## Journey 4 — Monitor Public Discussion

Dashboard

↓

Collect Dataset

↓

Topic Detection

↓

Sentiment Analysis

↓

Trend Detection

↓

Knowledge Graph Linking

↓

Communication Risk Score

↓

Visualization

---

# 13. Business Workflow

LexPulse AI hoạt động theo quy trình sau.

STEP 1

Thu thập dữ liệu

Nguồn:

- Laws
- Decrees
- Circulars
- Social Dataset

↓

STEP 2

Document Processing

- OCR
- Cleaning
- Chunking

↓

STEP 3

Information Extraction

AI trích xuất:

- Subject
- Rights
- Obligations
- Penalties
- Deadlines
- References
- Effective Dates

↓

STEP 4

Knowledge Graph Construction

Node

Edge

Relationship

↓

STEP 5

Embedding Generation

↓

Vector Database

↓

STEP 6

Hybrid Search

BM25

+

Vector Search

+

Graph Traversal

↓

STEP 7

LLM Reasoning

↓

Citation

↓

Answer

---

# 14. Core Product Features

Feature 1

Natural Language Legal Chat

Description

Cho phép người dùng hỏi bằng tiếng Việt.

Priority

Critical

---

Feature 2

Knowledge Graph Visualization

Description

Hiển thị mối quan hệ giữa:

Luật

Điều

Khoản

Điểm

Văn bản

Priority

Critical

---

Feature 3

Legal Timeline

Description

Hiển thị lịch sử sửa đổi.

Priority

High

---

Feature 4

Citation Engine

Description

Luôn hiển thị:

- Điều
- Khoản
- Điểm
- Văn bản

Priority

Critical

---

Feature 5

Social Claim Verification

Description

Đối chiếu bài đăng với quy định pháp luật.

Priority

Critical

---

Feature 6

Communication Risk Dashboard

Description

Theo dõi:

- Trending Topics
- Sentiment
- Risk
- Misinformation

Priority

High

---

Feature 7

Advanced Search

Description

Hybrid Search:

- Keyword
- Semantic
- Graph

Priority

High

---

Feature 8

Admin Portal

Description

Upload văn bản.

Quản lý dữ liệu.

Re-index.

Priority

Medium

---

# 15. User Stories

Citizen

"As a citizen,

I want to ask legal questions in natural language

so that I can understand new regulations without reading hundreds of pages."

---

Business

"As a business owner,

I want to know whether a regulation affects my company

so that I can stay compliant."

---

Government

"As a communication officer,

I want to know which regulations are misunderstood the most

so that I can prioritize communication campaigns."

---

Lawyer

"As a legal professional,

I want to compare different versions of regulations

so that I can determine the latest applicable provisions."

---

# 16. User Interface Flow

Landing Page

↓

Chat

↓

Answer

↓

Citation

↓

Knowledge Graph

↓

Timeline

↓

Suggested Questions

---

Dashboard

↓

Trending Topics

↓

Risk Score

↓

Topic Detail

↓

Related Articles

↓

Knowledge Graph

---

Admin

↓

Upload

↓

Processing

↓

Knowledge Graph Update

↓

Embedding

↓

Index Complete

---

# 17. Acceptance Criteria

MVP được coi là hoàn thành nếu:

✓ Người dùng có thể hỏi bằng tiếng Việt.

✓ AI trả lời trong dưới 5 giây đối với câu hỏi đơn giản.

✓ AI luôn hiển thị nguồn trích dẫn.

✓ Knowledge Graph trực quan và có thể tương tác.

✓ Dashboard hiển thị chủ đề thảo luận.

✓ Người dùng có thể kiểm tra một bài đăng mạng xã hội và nhận được đánh giá đúng/sai cùng căn cứ pháp lý.

✓ Demo hoàn chỉnh trong 5–7 phút mà không cần thao tác kỹ thuật phức tạp.
