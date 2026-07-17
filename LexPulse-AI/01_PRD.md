# Product Requirement Document (PRD)

---

# Project Information

## Project Name

LexPulse AI

## Tagline

Transform Legal Documents & Public Discourse into Actionable Intelligence

## Version

1.0 (Hackathon MVP)

## Development Type

AI-powered Legal Intelligence Platform

## Team

Hackathon Team

## Target Competition

Legal Knowledge Graph — Tracking New Regulations & Public Discourse

---

# 1. Executive Summary

## 1.1 Overview

LexPulse AI là nền tảng AI Legal Intelligence được thiết kế để giúp người dân, doanh nghiệp và cơ quan quản lý nhanh chóng hiểu các quy định pháp luật mới, đánh giá tác động của chúng, theo dõi phản ứng của cộng đồng và phát hiện các thông tin sai lệch liên quan đến chính sách.

Khác với chatbot pháp lý truyền thống chỉ trả lời câu hỏi dựa trên Retrieval-Augmented Generation (RAG), LexPulse AI kết hợp ba thành phần cốt lõi:

- Knowledge Graph
- Advanced RAG
- Public Discourse Intelligence

Hệ thống không chỉ trả lời "Luật quy định gì?" mà còn trả lời:

- Điều luật nào đang được thảo luận nhiều nhất?
- Người dân đang hiểu sai điều gì?
- Điều luật nào đã được sửa đổi?
- Điều khoản nào còn hiệu lực?
- Nội dung trên mạng xã hội có đúng với quy định pháp luật hay không?

Mục tiêu cuối cùng là xây dựng một AI Legal Intelligence Platform thay vì chỉ là một AI Chatbot.

---

# 2. Background

Ngày 01/07/2026 đánh dấu thời điểm nhiều luật, nghị định và thông tư mới bắt đầu có hiệu lực tại Việt Nam.

Khối lượng văn bản rất lớn.

Một quy định thường:

- tham chiếu nhiều điều luật khác
- sửa đổi từng phần
- có nhiều phiên bản
- nằm ở nhiều văn bản khác nhau

Điều này khiến:

- Người dân khó hiểu luật.
- Doanh nghiệp khó đảm bảo tuân thủ.
- Cơ quan quản lý khó theo dõi phản ứng xã hội.

Song song với đó, Facebook, TikTok, Threads và các diễn đàn trực tuyến tạo ra hàng nghìn bài viết thảo luận về luật mới.

Nhiều bài đăng:

- thiếu ngữ cảnh
- trích dẫn sai
- diễn giải sai
- lan truyền thông tin chưa được kiểm chứng

Hiện nay chưa có một nền tảng nào có khả năng kết nối giữa văn bản pháp luật và các cuộc thảo luận này để tạo thành một hệ thống phân tích thống nhất.

---

# 3. Problem Statement

Các hệ thống hiện nay tồn tại nhiều hạn chế.

## 3.1 Legal Search

Các công cụ tìm kiếm văn bản pháp luật chủ yếu trả về danh sách tài liệu.

Người dùng vẫn phải tự đọc.

---

## 3.2 Traditional RAG

Traditional RAG chỉ tìm kiếm các đoạn văn giống với câu hỏi.

Không hiểu:

- điều luật
- khoản
- điểm
- quan hệ giữa các văn bản
- sửa đổi
- thay thế
- hiệu lực

Điều này có thể dẫn đến việc AI trả lời dựa trên văn bản đã hết hiệu lực.

---

## 3.3 Lack of Knowledge Graph

Hiện nay gần như không có hệ thống nào mô hình hóa:

Luật

↓

Điều

↓

Khoản

↓

Điểm

↓

Quan hệ

↓

Tham chiếu

↓

Sửa đổi

↓

Thay thế

↓

Hiệu lực

thành một Knowledge Graph.

Điều này khiến AI không thể suy luận chính xác.

---

## 3.4 Public Discourse

Người dân chủ yếu tiếp cận luật thông qua:

- Facebook
- TikTok
- Threads
- Báo chí

Trong khi đó:

không có hệ thống nào liên kết

"Một bài đăng"

↓

"Điều luật tương ứng"

↓

"Mức độ chính xác"

↓

"Giải thích"

---

## 3.5 Communication Risk

Cơ quan quản lý hiện nay rất khó biết:

- điều luật nào đang bị hiểu sai nhiều nhất
- chủ đề nào đang trở thành xu hướng
- thông tin nào đang lan truyền sai
- cần truyền thông nội dung gì trước

---

# 4. Vision

LexPulse AI hướng tới trở thành nền tảng AI Legal Intelligence đầu tiên tại Việt Nam có khả năng:

- Hiểu cấu trúc văn bản pháp luật.
- Hiểu mối quan hệ giữa các văn bản.
- Hiểu lịch sử sửa đổi.
- Hiểu các cuộc thảo luận xã hội.
- Giải thích quy định bằng ngôn ngữ tự nhiên.
- Hỗ trợ ra quyết định dựa trên dữ liệu.

Thay vì chỉ "Search",

LexPulse AI sẽ "Understand".

---

# 5. Product Objectives

## Objective 1

Cho phép người dùng hỏi pháp luật bằng ngôn ngữ tự nhiên.

Ví dụ:

"Từ ngày 1/7/2026 người dưới 18 tuổi có được mở tài khoản ngân hàng không?"

AI phải trả lời:

- ngắn gọn
- dễ hiểu
- có citation
- có điều luật
- có mức độ tin cậy

---

## Objective 2

Tự động phân tích văn bản pháp luật.

Trích xuất:

- Subject
- Obligation
- Right
- Penalty
- Deadline
- Related Document
- Effective Date
- Expiration Date

---

## Objective 3

Tự động xây dựng Legal Knowledge Graph.

Knowledge Graph phải thể hiện được:

- điều luật
- khoản
- điểm
- quan hệ
- tham chiếu
- sửa đổi
- thay thế
- hiệu lực

---

## Objective 4

Theo dõi Public Discourse.

Thu thập dữ liệu mạng xã hội mẫu.

Xác định:

- Topic
- Trend
- Sentiment
- Claim
- Engagement

Sau đó liên kết tới điều luật tương ứng.

---

## Objective 5

Phát hiện thông tin sai lệch.

Ví dụ:

Facebook Post

↓

Claim Extraction

↓

Knowledge Graph

↓

Legal Verification

↓

Result

- Correct
- Incorrect
- Misleading
- Missing Context

---

## Objective 6

Cung cấp Dashboard giúp:

- theo dõi luật mới
- theo dõi xu hướng
- theo dõi hiểu sai
- theo dõi rủi ro truyền thông

---

# 6. Hackathon Goal

Đây là MVP được xây dựng trong thời gian 35 giờ.

Mục tiêu không phải là xây dựng một hệ thống pháp luật quốc gia hoàn chỉnh.

Mục tiêu là chứng minh:

- AI có thể hiểu cấu trúc pháp luật.
- AI có thể xây Knowledge Graph.
- AI có thể kiểm chứng thông tin mạng xã hội.
- AI có thể giải thích luật có nguồn trích dẫn.

Nếu MVP thành công, hệ thống có thể mở rộng cho hàng triệu văn bản pháp luật sau hackathon.

---

# 7. Success Metrics

## Functional

✓ Upload tài liệu

✓ Parse thành công

✓ Sinh Knowledge Graph

✓ Chat thành công

✓ Citation chính xác

✓ Dashboard hoạt động

---

## Performance

Simple Question

<5 seconds

Complex Question

<30 seconds

Graph Visualization

<2 seconds

Upload

<10 seconds

---

## AI Quality

Citation Accuracy

>90%

Retrieval Accuracy

>90%

Hallucination

<5%

Knowledge Graph Accuracy

>90%

---

# 8. Project Limitations

Để đảm bảo hoàn thành trong 35 giờ, MVP sẽ có các giới hạn sau:

- Chỉ xử lý tập dữ liệu pháp luật mẫu (10–20 văn bản).
- Chỉ sử dụng dữ liệu mạng xã hội mẫu (100–500 bài viết hoặc bình luận).
- Không crawl mạng xã hội theo thời gian thực.
- Không thay thế tư vấn pháp lý chuyên nghiệp.
- Chỉ tập trung vào một số lĩnh vực pháp luật phục vụ demo.
- Việc cập nhật văn bản mới được thực hiện thủ công hoặc theo lô (batch), không yêu cầu đồng bộ thời gian thực.
- Hệ thống ưu tiên tính chính xác và khả năng trình diễn hơn phạm vi dữ liệu.

---

# 9. Definition of Success

Sau khi hoàn thành Hackathon, sản phẩm phải đạt được các tiêu chí sau:

- Một website hoàn chỉnh với giao diện trực quan.
- Người dùng có thể tải lên hoặc chọn văn bản pháp luật mẫu.
- AI trả lời bằng ngôn ngữ tự nhiên kèm nguồn trích dẫn rõ ràng.
- Knowledge Graph hiển thị quan hệ giữa các điều luật.
- Dashboard thể hiện xu hướng thảo luận, các hiểu lầm phổ biến và mức độ rủi ro truyền thông.
- Toàn bộ hệ thống có thể demo ổn định trong vòng 5–7 phút mà không cần thao tác kỹ thuật phức tạp.
