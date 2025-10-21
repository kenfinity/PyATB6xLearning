# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs - score -> int
# 2 ->  O/p -> str -> A, B

try:
    score = int(input("Enter a score: ").strip())
    if score > 100 or score < 0:
        print("❌ Score must be between 0 and 100.")
    else:
        if score >= 90 and score <= 100:
            print("A")
        elif score >= 80 and score <= 89:
            print("B")
        elif score >= 70 and score <= 79:
            print("C")
        elif score >= 60 and score <= 69:
            print("D")
        else:
            print("F")
except ValueError:
    print("Enter a numeric value")

