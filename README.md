# AI Japanese Assessment - Backend

[cite_start]This is the core logic ("the brain") of the assistant, built with Python and FastAPI[cite: 6, 26].

## Setup & Installation
1. Navigate to the backend folder.
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn

3. Run the server:
   ```bash
   python -m uvicorn app:app --reload

## Key Files
app.py: Handles API endpoints (GET /questions, POST /evaluate).

logic.py: Contains the Cosine Similarity and Rule-based evaluation logic.

questions.py: Static question bank for JLPT N5–N3 assessment.