from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from questions import generate_dynamic_questions # File câu hỏi cũ của bạn
from logic import evaluate_user_performance

app = FastAPI(title="AI Japanese Assessment API")

# Cấu hình CORS để ReactJS truy cập được
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

class Answer(BaseModel):
    question_id: int
    user_answer: str

class Submission(BaseModel):
    answers: List[Answer]

@app.get("/questions")
def get_questions():
    dynamic_qs = generate_dynamic_questions()
    if not dynamic_qs:
        return [] # Trả về bộ câu hỏi cũ nếu AI lỗi (Fallback)
    
    # Lưu đáp án vào một biến global tạm thời để chấm điểm sau đó
    # Trong thực tế nên dùng Session hoặc Cache
    global current_questions
    current_questions = dynamic_qs
    
    return [{"id": q["id"], "question": q["question"], "options": q["options"], "type": q["type"]} for q in dynamic_qs]

@app.post("/evaluate")
def evaluate(submission: Submission):
    results = []
    # Tạo map để tìm câu hỏi nhanh hơn
    q_map = {q["id"]: q for q in current_questions}
    
    for ans in submission.answers:
        q = q_map.get(ans.question_id)
        if q:
            correct = 1 if ans.user_answer == q["answer"] else 0
            results.append({"type": q["type"], "correct": correct})

    evaluation = evaluate_user_performance(results)
    return evaluation

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)