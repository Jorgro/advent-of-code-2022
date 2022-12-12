
shape_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}




with open("day2/input.txt", "r") as f:
    total_score = 0
    for line in f:
        s = line.strip().split(" ")

        total_score += shape_scores[s[1]]

        if s[0] == "A":
            if s[1] == "X":
                total_score += 3
            elif s[1] == "Y":
                total_score += 6
        elif s[0] == "B":
            if s[1] == "Y":
                total_score += 3
            elif s[1] == "Z":
                total_score += 6
        elif s[0] == "C":
            if s[1] == "Z":
                total_score += 3
            elif s[1] == "X":
                total_score += 6

print(total_score)
