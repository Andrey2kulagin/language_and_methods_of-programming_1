simv = input("введите букву ")
num = int(input("Введите цифру "))
black_team = ["a", "e", "c", "g"]
if simv in black_team:
    if num % 2 == 0:
        print("white")
    else:
        print("black")
else:
    if num % 2 == 0:
        print("black")
    else:
        print("white")
