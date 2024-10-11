score = int(input("Enter Score: "))
possible = int(input("Total possible points: "))
percent = score/possible * 100
if percent < 50:
    print("F")
elif percent >= 51 and percent < 60:
    print("D")
elif percent >= 61 and percent < 75:
    print("C")
elif percent >= 76 and percent < 88:
    print("B")
else:
    print("A")
