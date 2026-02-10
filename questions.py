import google.generativeai as genai
import json
from dotenv import load_dotenv
import os

# Tải các biến từ file .env
load_dotenv()

# Lấy Key từ biến môi trường
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")
# Sử dụng model phiên bản mới nhất
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def generate_dynamic_questions():
    prompt = """
    Generate 5 Japanese proficiency questions (JLPT N5-N3 level).
    Return ONLY a JSON array of objects with this structure:
    {"id": int, "question": "string", "options": ["str", "str", "str", "str"], "answer": "string", "type": "vocab|grammar|reading"}
    """
    try:
        response = model.generate_content(prompt)
        # Làm sạch chuỗi trả về từ AI
        clean_text = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(clean_text)
    except Exception as e:
        print(f"AI Error: {e}")
        # Trả về một bộ câu hỏi mẫu nếu AI gặp lỗi để tránh sập server
        return [
            {
        "id": 1,
        "question": "「水」はどれですか。",
        "options": ["Water", "Fire", "Wind", "Earth"],
        "answer": "Water",
        "type": "vocab"
        },
        {
            "id": 2,
            "question": "「先生」はだれですか。",
            "options": [
                "A student",
                "A teacher",
                "A doctor",
                "A friend"
            ],
            "answer": "A teacher",
            "type": "vocab"
        },
        {
            "id": 3,
            "question": "「行く」の意味はどれですか。",
            "options": ["To go", "To eat", "To see", "To buy"],
            "answer": "To go",
            "type": "vocab"
        },

        # =====================
        # N5 – Grammar (4–5)
        # =====================
        {
            "id": 4,
            "question": "私は毎日学校＿＿行きます。",
            "options": ["を", "に", "で", "が"],
            "answer": "に",
            "type": "grammar"
        },
        {
            "id": 5,
            "question": "これは私＿＿本です。",
            "options": ["の", "に", "を", "で"],
            "answer": "の",
            "type": "grammar"
        },

        # =====================
        # N4 – Vocabulary (6–7)
        # =====================
        {
            "id": 6,
            "question": "「必要」の意味はどれですか。",
            "options": ["Unnecessary", "Important", "Necessary", "Difficult"],
            "answer": "Necessary",
            "type": "vocab"
        },
        {
            "id": 7,
            "question": "「約束」を守ります の意味は？",
            "options": [
                "Break a promise",
                "Keep a promise",
                "Forget a promise",
                "Make a promise"
            ],
            "answer": "Keep a promise",
            "type": "vocab"
        },

        # =====================
        # N4 – Grammar (8–9)
        # =====================
        {
            "id": 8,
            "question": "雨が＿＿、試合は中止になりました。",
            "options": ["降るから", "降ったので", "降るのに", "降れば"],
            "answer": "降ったので",
            "type": "grammar"
        },
        {
            "id": 9,
            "question": "この仕事は一人では＿＿。",
            "options": ["できません", "できます", "しません", "ありません"],
            "answer": "できません",
            "type": "grammar"
        },

        # =====================
        # N4 – Reading (10)
        # =====================
        {
            "id": 10,
            "question": "次の文の意味はどれですか。\n「電車が遅れたので、会議に間に合いませんでした。」",
            "options": [
                "I arrived early for the meeting",
                "I missed the meeting because the train was late",
                "The meeting was canceled",
                "The train arrived on time"
            ],
            "answer": "I missed the meeting because the train was late",
            "type": "reading"
        },

        # =====================
        # N3 – Vocabulary (11–12)
        # =====================
        {
            "id": 11,
            "question": "「影響」の意味はどれですか。",
            "options": ["Effect", "Cause", "Result", "Chance"],
            "answer": "Effect",
            "type": "vocab"
        },
        {
            "id": 12,
            "question": "「解決する」の意味は？",
            "options": [
                "To start a problem",
                "To ignore a problem",
                "To solve a problem",
                "To explain a problem"
            ],
            "answer": "To solve a problem",
            "type": "vocab"
        },

        # =====================
        # N3 – Grammar (13–14)
        # =====================
        {
            "id": 13,
            "question": "忙しい＿＿、彼は毎日運動しています。",
            "options": ["ながら", "のに", "ために", "そうで"],
            "answer": "のに",
            "type": "grammar"
        },
        {
            "id": 14,
            "question": "このアプリは使いやすい＿＿、人気があります。",
            "options": ["から", "そう", "らしい", "ため"],
            "answer": "から",
            "type": "grammar"
        },

        # =====================
        # N3 – Reading (15)
        # =====================
        {
            "id": 15,
            "question": "次の文の意味はどれですか。\n「経験があれば、この仕事はそれほど難しくありません。」",
            "options": [
                "The job is always difficult",
                "The job is easy even without experience",
                "With experience, the job is not very difficult",
                "Experience makes the job impossible"
            ],
            "answer": "With experience, the job is not very difficult",
            "type": "reading"
        }
        ]