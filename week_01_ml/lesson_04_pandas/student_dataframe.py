import pandas as pd


def analyze_students(
    students: pd.DataFrame,
) -> dict[str, object]:
    """Анализирует таблицу и возвращает данные об..."""
    if students.empty:
        return {
            "student_count": 0,
            "average_age": None,
            "average_score": None,
            "passed_count": 0,
            "failed_count": 0,
            "best_score": None,
            "pass_rate": None,
            "average_passed_score": None,
            "passed_students": None,
            "high_score_students": None,
            "missing_values": None,
        }
    result = {}

    student_count = students.shape[0]
    passed_count = (students["passed"] == 1).sum()
    failed_count = (students["passed"] == 0).sum()

    result["student_count"] = student_count
    result["average_age"] = students["age"].mean().round(2)
    result["average_score"] = students["score"].mean().round(2)
    result["passed_count"] = passed_count
    result["failed_count"] = failed_count
    result["best_score"] = float(students["score"].max())
    result["pass_rate"] = (passed_count / student_count * 100).round(2)
    result["average_passed_score"] = students[students["passed"]== 1]["score"].mean().round(2)
    result["passed_students"] = students[students["passed"] == 1].to_dict(orient="records")
    result["high_score_students"] = students[students["score"] >= 70].to_dict(orient="records")
    result["missing_values"] = missing_values = students.isna().sum().to_dict()
    return result


def clean_students(students: pd.DataFrame) -> pd.DataFrame:
    """Заполняет None данные по средним в таблице"""
    if not students.empty:
        students["age"] = students["age"].fillna(
            students["age"].median()
        )

        students["score"] = students["score"].fillna(
            students["score"].mean()
        )
    print(students.isna().sum())
    return students


students = pd.DataFrame({
    "name": [
        "Анна",
        "Борис",
        "Виктор",
        "Галина",
        "Дмитрий",
        "Елена",
        "Фёдор",
    ],
    "age": [18, 19, 20, 21, 22, None, 24],
    "score": [72, 45, 88, None, 91, 67, 38],
    "passed": [1, 0, 1, 0, 1, 1, 0],
})

result = analyze_students(students)

for key, value in result.items():
    print(f"{key}: {value}")

clean_students = clean_students(students.copy())