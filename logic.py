import math
from collections import defaultdict

# Skill Profiles cho từng cấp độ
JLPT_PROFILES = {
    "N5": [0.6, 0.5, 0.4],
    "N4": [0.7, 0.6, 0.6],
    "N3": [0.8, 0.7, 0.7],
}

# Ngưỡng tối thiểu để đạt cấp độ (Rule-based) [cite: 31]
RULES = {
    "N5": {"vocab": 0.5, "grammar": 0.4},
    "N4": {"vocab": 0.6, "grammar": 0.5},
    "N3": {"vocab": 0.7, "grammar": 0.6},
}

# Gợi ý tài liệu dựa trên kết quả 
RECOMMENDATIONS = {
    "N5": ["Bản tin NHK News Web Easy", "Giáo trình Minna no Nihongo Sơ cấp 1"],
    "N4": ["Giáo trình Genki II", "JLPT N4 Speed Master Vocabulary"],
    "N3": ["Shinkanzen Master N3 Grammar", "Try! JLPT N3"]
}

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0

def evaluate_user_performance(results):
    scores = defaultdict(list)
    for r in results:
        scores[r["type"]].append(r["correct"])

    final_scores = {k: sum(v) / len(v) if v else 0 for k, v in scores.items()}
    user_vector = [final_scores.get("vocab", 0), final_scores.get("grammar", 0), final_scores.get("reading", 0)]

    qualified_levels = [lvl for lvl, req in RULES.items() 
                        if final_scores.get("vocab", 0) >= req["vocab"] and final_scores.get("grammar", 0) >= req["grammar"]]

    best_level = "N5"
    best_similarity = 0
    for level in qualified_levels:
        sim = cosine_similarity(user_vector, JLPT_PROFILES[level])
        if sim > best_similarity:
            best_similarity = sim
            best_level = level

    return {
        "level": best_level,
        "similarity": round(best_similarity, 2),
        "scores": final_scores,
        "recommendations": RECOMMENDATIONS.get(best_level, [])
    }