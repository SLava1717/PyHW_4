#конфетки)))
from random import randint
play1 = input("Введите имя игрока 1: ")
play2 = input("Введите имя игрока 2: ")
candy = int(input("Введите кол-во конфет для игры: "))

turn = randint(0,1)
if turn == 1:
    print(f"ходит  {play1}")
else:
    print(f"ходит  {play2}")

def play_candy(name):
    N = int(input(f"{name} введите кол-во конфет от 1 до 28: "))
    while 28 < N < 1:
        N = int(input("корректное число конфет: "))
    return N

while candy > 28:
    if turn:
        x = (play_candy(play1))
        candy = candy - x
        turn = 0
        print(f"Ходил {play1}. Осталось на столе {candy} конфет.")
    else:
        x = (play_candy(play2))
        candy = candy - x
        turn = 1
        print(f"Ходил {play2}. Осталось на столе {candy} конфет.")

if turn:
    print(f"WIN {play1} WIN")
else:
    print(f"WIN {play2} WIN")