Gemini said
Đây là nội dung hoàn chỉnh cho file DOCUMENTATION.md được chuẩn hóa định dạng Markdown để bạn có thể push trực tiếp lên GitHub. Tài liệu này được thiết kế để làm nổi bật tư duy hệ thống và khả năng giải quyết vấn đề theo đúng yêu cầu từ phía Datacom.

AI Japanese Proficiency Assessment Assistant (N5–N3)
1. Problem Definition
Người học tiếng Nhật thường gặp khó khăn trong việc tự xác định trình độ để chọn tài liệu học tập phù hợp. Dự án này cung cấp một công cụ chẩn đoán giúp ước lượng trình độ JLPT (từ N5 đến N3) và đưa ra các gợi ý tài liệu học tập dựa trên kết quả thực tế.

2. System Architecture
Dự án được triển khai dưới dạng ứng dụng Full-stack để chứng minh khả năng thiết kế hệ thống chuyên nghiệp:


Backend (FastAPI/Python): Đóng vai trò là "Bộ não" (The Brain) của trợ lý, chịu trách nhiệm xử lý logic đánh giá và tính toán toán học.


Frontend (ReactJS + Tailwind CSS): Cung cấp giao diện người dùng hiện đại, xử lý việc thực hiện bài kiểm tra và trực quan hóa dữ liệu.

Communication: Giao tiếp giữa FE và BE thông qua REST API (JSON).

3. Core AI Logic & Decisions
Hệ thống sử dụng chiến lược đánh giá lai (Hybrid Evaluation Strategy) để đảm bảo tính chính xác và khả năng giải trình:

A. Rule-based Evaluation (Hệ thống dựa trên luật)
Trước khi tính toán cấp độ cuối cùng, hệ thống áp dụng các ngưỡng điểm tối thiểu cho từng kỹ năng (Vocabulary, Grammar).

Ví dụ: Cấp độ N3 yêu cầu từ vựng ≥70% và ngữ pháp ≥60%.

Quyết định: Việc này đảm bảo người dùng có năng lực nền tảng vững chắc trước khi được xem xét ở các cấp độ cao hơn.

B. Similarity Scoring (Tính toán độ tương đồng)
Hệ thống đại diện kết quả của người dùng dưới dạng một Vector năng lực: V 
user
​
 =[Vocab,Grammar,Reading]. Chúng tôi sử dụng thuật toán Cosine Similarity để so khớp vector này với các Profile chuẩn của JLPT (N5, N4, N3).

Công thức toán học:

Similarity= 
∥A∥∥B∥
A⋅B
​
 

Lý do chọn Cosine Similarity: Phương pháp này tập trung vào sự phân bổ tương đối giữa các kỹ năng thay vì chỉ nhìn vào tổng điểm, giúp nhận diện profile năng lực một cách chính xác hơn.

4. Technical Challenges & Reasoning

Sử dụng Python: Mặc dù đề bài không khuyến khích, tôi chọn Python cho Backend vì các thư viện tính toán vector và xử lý dữ liệu (như Math, Collections) rất mạnh mẽ, phù hợp để xây dựng "bộ não" AI.


Security: API Key của Gemini được quản lý thông qua biến môi trường (.env) và được cấu hình trong .gitignore để tránh rò rỉ dữ liệu.

Resilience (Tính bền bỉ): Hệ thống được thiết kế với cơ chế Fallback. Nếu dịch vụ AI bên ngoài gặp sự cố, hệ thống tự động chuyển sang bộ câu hỏi tĩnh chất lượng cao để đảm bảo trải nghiệm người dùng không bị gián đoạn.

5. Limitations and Bias (Hạn chế và Định kiến)
Tuân thủ các nguyên tắc về đạo đức và giới hạn của AI:


Thiếu kỹ năng Nghe/Nói: Do giới hạn về phạm vi và trình duyệt, hệ thống hiện chỉ tập trung vào kỹ năng đọc hiểu và ngôn ngữ.


Guessing Bias: Bài trắc nghiệm ngắn có thể bị ảnh hưởng bởi yếu tố may mắn khi người dùng chọn đại đáp án.


Linguistic Bias: Việc sử dụng tiếng Anh trong các tùy chọn trả lời có thể tạo lợi thế cho những người học đã thạo tiếng Anh.