while True:
    try:
        score = float(input("Enter your score: "))
        if score > 100 or score < 0:
            print("Enter a valid score (0-100) %")
        elif score >= 90:
            print(f"Your score is {score} % and grade is A - Excellent")
        elif score >= 80:
            print(f"Your score is {score} % and grade is B - Good Job")
        elif score >= 70:
            print(f"Your score is {score} % and grade is C - Nice Try")
        elif score >= 60:
            print(f"Your score is {score} % and grade is D - You can Do better")
        else:
            print(f"Your score is {score} % and grade is F - Poor")
    except ValueError:
        print("Enter a valid score")
    tryagain = input("Do you want to try again?(y/n)")
    if tryagain == 'n':
        print("Thank you for today")
        break