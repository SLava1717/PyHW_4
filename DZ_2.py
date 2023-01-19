# крестики нолики
pole = list(range(1,10))
def input_pole(pole):
    print("-"*9)
    for i in range(3):
        print(pole[i+0*3], "|",pole[i+1*3], "|",pole[i+2*3])
        print("-"*9)
# input_pole(pole)


def win(pole):
    win = ((1,2,3),(1,5,9),(1,4,7),(4,5,6),(7,8,9),(2,5,8),(3,6,9),(3,5,7))
    for i in win:
        if pole[i[0]] == pole[i[1]] == pole[i[2]]:
            return pole[i[0]]
    return False

def play(xoxo):
    vol = False
    while not vol:
        play = input("Ваш ход, выберите ячейку"+ xoxo + "==>" )
        try:
            play = int(play)
        except:
            print('что то не то')
            continue
        if play >= 1 and play <= 9:
            if(str(pole[play-1]) not in 'XO'):
                  pole[play-1] = xoxo
                  vol = True
            else:
                print('Занято')
        else:
             print('Еще раз попробуй')


def game(pole):
    county = 0
    gol = False
    while not gol:
        input_pole(pole)
        if county %2 ==0:
            play("X")
        else:
            play("O")
        county+= 1
        if county > 4:
            win_game = win(pole)
            if win_game:
                print(win_game, 'WIN')
                gol = True
                break
            if county == 9:
                print('DRAW')
        input_pole(pole)
game(pole)


#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)