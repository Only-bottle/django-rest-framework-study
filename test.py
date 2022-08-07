from collections import Counter

def solution(data):
    left, right = data
    left_c = Counter(left)
    right_c = Counter(right)

    def _get_score(items):
        score = 0
        for key, value in items.items():
            if key == "!":
                score += value * 2
            else:
                score += value * 3
        return score

    left_score = _get_score(left_c)
    right_score = _get_score(right_c)
    
    if left_score == right_score:
        return "무승부"
    elif left_score > right_score:
        return "첫 번째"
    elif left_score < right_score:
        return "두 번째"

print(solution(["?!", "????!!!!?"]))