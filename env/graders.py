def grade_easy(total_time):
    score = 1 / (1 + total_time)
    return max(0.05, min(score, 0.95))

def grade_medium(total_time):
    score = 1 / (1 + total_time * 1.2)
    return max(0.05, min(score, 0.95))

def grade_hard(total_time):
    score = 1 / (1 + total_time * 1.5)
    return max(0.05, min(score, 0.95))