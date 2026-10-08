import numpy as np


def analyze_students(students: np.ndarray) -> dict[str, object]:
    """Анализирует результаты студентов."""

    if students.size == 0:
        return {
            "student_count": 0,
            "average_age": None,
            "average_score": None,
            "passed_count": 0,
            "failed_count": 0,
            "best_score": None,
            "passed_students": [],
            "high_score_students": [],
            "pass_rate": None,
            "average_passed_score": None,
        }

    ages = students[:, 0]
    scores = students[:, 1]
    exam_results = students[:, 2]

    passed_mask = exam_results == 1
    failed_mask = exam_results == 0
    high_score_mask = scores >= 70

    student_count = students.shape[0]
    passed_count = int(np.sum(passed_mask))
    failed_count = int(np.sum(failed_mask))

    if passed_count > 0:
        average_passed_score = float(np.mean(scores[passed_mask]))
    else:
        average_passed_score = None

    return {
        "student_count": student_count,
        "average_age": float(np.mean(ages)),
        "average_score": round(float(np.mean(scores)), 2),
        "passed_count": passed_count,
        "failed_count": failed_count,
        "best_score": np.max(scores).item(),
        "passed_students": students[passed_mask].tolist(),
        "high_score_students": students[high_score_mask].tolist(),
        "pass_rate": round(passed_count / student_count * 100, 2),
        "average_passed_score": round(average_passed_score, 2),
    }


students = np.array([
    [18, 72, 1],
    [19, 45, 0],
    [20, 88, 1],
    [21, 59, 0],
    [22, 91, 1],
    [23, 67, 1],
    [24, 38, 0],
])

result = analyze_students(students)

for key, value in result.items():
    print(f"{key}: {value}")