import random

print("Введите число раундов")
rounds = int(input())
print("Введите максимальное число")
max_number = int(input())
win_rounds = 0
for i in range(0, rounds):
    print("Введите ваше число")
    human_number = int(input())
    pc_number = random.randint(1, max_number)
    if human_number == pc_number:
        win_rounds += 1
        print("Вы выиграли!")
    else:
        print("Вы проиграли:(")

human_percent = round(win_rounds/rounds*100, 1)
pc_percent = round(1/max_number*100, 1)
print("Вы выиграли", win_rounds, "из", rounds, "раундов")
print("У вас", human_percent, "%, а у ПК", pc_percent, "%")
if human_percent > pc_percent:
    if human_percent == 100 and pc_percent != 100:
        print("Вы выиграли все раудны и не оставили роботам ни шанса!👑")
    else:
        print("Сегодня мы победили благодаря Вам!🖤")
elif human_percent == pc_percent:
    print("Равная борьба🤝")
else:
    print("Не сегодня, кожаный мешок😈")
