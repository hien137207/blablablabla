# PART 5 — MVP Scope, Development Strategy & Delivery Plan

---

# 48. MVP Definition

Trong thời gian 35 giờ của Hackathon, mục tiêu KHÔNG phải xây dựng một nền tảng pháp lý hoàn chỉnh.

Mục tiêu là xây dựng một MVP có khả năng chứng minh giá trị của kiến trúc AI.

MVP phải đủ để giám khảo thấy rằng hệ thống có thể mở rộng thành một sản phẩm thực tế.

MVP phải tập trung vào:

- Legal Knowledge Graph
- AI Legal Chat
- Claim Verification
- Dashboard
- Citation
- Timeline

Không cố gắng xử lý hàng triệu văn bản.

---

# 49. MVP Features

## Must Have (P0)

✓ Upload Legal Documents

✓ Parse Document

✓ Knowledge Graph

✓ AI Chat

✓ Citation

✓ Dashboard

✓ Timeline

✓ Claim Verification

---

## Should Have (P1)

✓ Search

✓ Graph Filter

✓ Suggested Questions

✓ Analytics

✓ Admin Dashboard

---

## Nice to Have (P2)

✓ Multi-language

✓ Voice Input

✓ Export PDF

✓ User Feedback

✓ Notification

---

# 50. Out of Scope

Các chức năng sau KHÔNG thuộc phạm vi Hackathon.

❌ Real-time Social Crawling

❌ Production-scale Knowledge Graph

❌ Multi-tenant

❌ Enterprise Authentication

❌ Distributed Database

❌ Kafka

❌ Kubernetes

❌ Auto-scaling

❌ Fine-tuned LLM

❌ AI Agent tự động cập nhật dữ liệu

❌ Mobile App

❌ Thanh toán

---

# 51. Development Principles

Toàn bộ hệ thống phải tuân theo các nguyên tắc sau.

## Principle 1

Simple First.

Không over-engineering.

---

## Principle 2

Working Demo > Perfect Code.

Ưu tiên demo chạy được.

---

## Principle 3

Source Citation là bắt buộc.

AI không được trả lời nếu không có nguồn.

---

## Principle 4

Knowledge Graph là trung tâm.

Chatbot chỉ là giao diện khai thác tri thức.

---

## Principle 5

Không Hallucination.

Nếu không tìm thấy dữ liệu.

AI phải nói:

"Tôi chưa có đủ căn cứ để trả lời."

---

# 52. AI Design Principles

LLM KHÔNG phải Database.

Knowledge Graph mới là nguồn dữ liệu chính.

Retriever KHÔNG được bỏ qua.

LLM chỉ tổng hợp.

Không tự suy luận ngoài dữ liệu.

Citation luôn hiển thị.

---

# 53. Demo Scenario

Demo gồm 5 bước.

---

Demo 1

Upload Regulation

↓

Parse

↓

Knowledge Graph

↓

Done

---

Demo 2

Legal Chat

↓

Ask Question

↓

Citation

↓

Timeline

---

Demo 3

Knowledge Graph

↓

Search

↓

Expand Node

↓

Show References

---

Demo 4

Claim Verification

↓

Paste Social Post

↓

Extract Claim

↓

Legal Verification

↓

Correct / Incorrect

↓

Citation

---

Demo 5

Dashboard

↓

Trending Topic

↓

Risk

↓

Graph

↓

Timeline

↓

Analytics

---

# 54. User Interface Pages

Landing Page

Chat Page

Dashboard

Knowledge Graph

Timeline

Claim Verification

Document Upload

Admin

About

---

# 55. GitHub Repository Structure

LexPulse-AI/

README.md

LICENSE

.env.example

docker-compose.yml

/frontend

/backend

/docs

/dataset

/scripts

/tests

/assets

/.github

---

# 56. README Requirements

README phải bao gồm:

Project Overview

Architecture

Installation

Tech Stack

Folder Structure

Demo

Dataset

Roadmap

License

Team

---

# 57. Coding Guidelines

Python

PEP8

Black

isort

mypy

---

Frontend

ESLint

Prettier

TypeScript Strict

---

Git

Feature Branch

Pull Request

Meaningful Commit

---

# 58. Testing Strategy

Backend

Unit Test

API Test

---

Frontend

Component Test

---

AI

Retriever Test

Citation Test

Knowledge Graph Test

Claim Verification Test

---

# 59. Risk Assessment

Risk 1

Dataset không đủ.

Mitigation

Chuẩn bị dataset trước Hackathon.

---

Risk 2

LLM trả lời sai.

Mitigation

Citation Validation.

---

Risk 3

Knowledge Graph lỗi.

Mitigation

Fallback sang Citation.

---

Risk 4

API chậm.

Mitigation

Caching.

---

Risk 5

Demo lỗi.

Mitigation

Offline Dataset.

---

# 60. Future Roadmap

Version 2

Realtime Crawling.

---

Version 3

Multi-Agent.

---

Version 4

Government API.

---

Version 5

Legal Recommendation.

---

Version 6

Compliance Monitoring.

---

Version 7

Enterprise SaaS.

---

# 61. Success Criteria

Sau Hackathon.

Người dùng có thể:

✓ Upload văn bản.

✓ AI hiểu.

✓ Knowledge Graph sinh tự động.

✓ Chat có Citation.

✓ Verify Social Posts.

✓ Dashboard hoạt động.

✓ Timeline hoạt động.

✓ Demo ổn định.

---

# 62. Definition of Done

Dự án được coi là hoàn thành khi:

✓ Frontend hoàn chỉnh.

✓ Backend hoàn chỉnh.

✓ AI Chat hoạt động.

✓ RAG hoạt động.

✓ Knowledge Graph hoạt động.

✓ Dashboard hoạt động.

✓ API hoạt động.

✓ GitHub đầy đủ.

✓ Docker chạy được.

✓ README hoàn chỉnh.

✓ Demo thành công.

---

# 63. Instructions for AI Development

Toàn bộ dự án phải được xây dựng theo các quy tắc sau:

- Không tự ý thay đổi yêu cầu trong PRD.
- Không thêm tính năng ngoài MVP nếu chưa hoàn thành P0.
- Không sử dụng công nghệ khác khi chưa có lý do rõ ràng.
- Mọi câu trả lời AI phải dựa trên dữ liệu đã được lập chỉ mục.
- Mọi chức năng phải có khả năng mở rộng sau Hackathon.
- Mã nguồn phải rõ ràng, có cấu trúc và dễ bảo trì.
- Mỗi module phải hoạt động độc lập thông qua API.
- Toàn bộ kiến trúc phải ưu tiên tính ổn định hơn sự phức tạp.

---

# End of Product Requirement Document

Version 1.0

LexPulse AI

Hackathon MVP

Single Source of Truth
