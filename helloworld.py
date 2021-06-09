def grade(score):
    if isinstance(score, int):
        if 60 <= score <= 70:
            return "D"
        elif 70 <= score < 80:
            return "C"
        elif 80 <= score < 90:
            return "B"
        elif 90 <= score <= 100:
            return "A"
        else:
            return "not good"
    else:
        print("您输入的不是数字")


scores = [66, 49, 88, 99, 100, -2]
for score in scores:
    print(grade(score))