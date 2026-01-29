def apply_college_rules(study_hours, attendance, previous_grade):
    # Strong positive case
    if attendance >= 85 and study_hours >= 25 and previous_grade >= 80:
        return 0.95, "A", "Rule-Based"

    # Attendance-based risk
    if attendance < 50:
        if study_hours < 10:
            return 0.20, "D", "Rule-Based"
        else:
            return 0.45, "C", "Rule-Based"

    # Weak history
    if previous_grade < 40:
        if study_hours >= 20 and attendance >= 65:
            return 0.55, "C", "Rule-Based"
        else:
            return 0.30, "D", "Rule-Based"

    return None, None, None


def grade_to_probability(grade):
    return {
        "A": 0.95,
        "B": 0.80,
        "C": 0.60,
        "D": 0.30
    }.get(grade, 0.5)

def risk_level(p):
    if p < 0.35:
        return "Very High", "🔴", "error"
    elif p < 0.55:
        return "High", "🟠", "warning"
    elif p < 0.75:
        return "Medium", "🟡", "warning"
    elif p < 0.90:
        return "Low", "🟢", "success"
    else:
        return "Very Low", "💚", "success"
