# -*- coding: utf-8 -*-
import os

def reset():
    choice_dict = {}
    for i in range(1,10):
        choice_dict[i] = i
    return choice_dict

def prn_brd():
    os.system('clear')

    print '*' * 9

    print '* %s|%s|%s *' % (choice_dict[1], choice_dict[2], choice_dict[3])
    print '* %s|%s|%s *' % (choice_dict[4], choice_dict[5], choice_dict[6])
    print '* %s|%s|%s *' % (choice_dict[7], choice_dict[8], choice_dict[9])

    print '*' * 9

def go_home():
    os.system('clear')
    print 'Game Over! Thanks for playing!!'
    exit()

def is_number(no):
    try:
        return int(no)
    except ValueError:
        return False

def chk_stat():
    cross_ltr = []
    cross_rtl = []
    vals = list(choice_dict.viewvalues())
    #print vals

    for i in range(0,9,4):
        cross_ltr.append(vals[i])

    for i in range(2,7,2):
        cross_rtl.append(vals[i])

    if vals[0:3].count('O') == 3 or vals[0:3].count('X') == 3:
        return 'win', 'top'

    if vals[3:6].count('O') == 3 or vals[3:6].count('X') == 3:
        return 'win', 'middle'

    if vals[6:9].count('O') == 3 or vals[6:9].count('X') == 3:
        return 'win', 'bottom'

    if cross_ltr.count('O') == 3 or cross_ltr.count('X') == 3:
        return 'win', 'Cross Left to Right'

    if cross_rtl.count('O') == 3 or cross_rtl.count('X') == 3:
        return 'win', 'Cross Right to Left'
    else:
        return 'cont', ''

def win(x):
    os.system('clear')
    prn_brd()
    print '''
    \n\nGame over!!
    Player %s wins!!
    ''' % (x)
    exit()

def chk_input(move, sign, turn):
    if move == 'x' or move == 'X':
        go_home()

    chk_no = is_number(move)
    if chk_no == False:
        return turn, 'Wrong input! Must be a NUMBER! ', sign
    elif int(move) <= 0 or int(move) >= 10:
        return turn, 'Wrong input! Must be NUMBER 1-9! ', sign
    else:
        move = int(move)
        if choice_dict[move] == 'O' or choice_dict[move] == 'X':
            return turn, 'Already taken, try again ', sign
        else:
            if sign == 'O':
                updt_dict(move, sign)
                turn +=1
                sign = 'X'
            elif sign == 'X':
                updt_dict(move, sign)
                turn +=1
                sign = 'O'

            return turn, '', sign


def updt_dict(move, sign):
    choice_dict[move] = sign


def gamer_init():
    crkl = raw_input('Gamer Circle, enter your name!: ')
    cros = raw_input('Gamer Cross, enter your name!: ')
    return crkl, cros

def game_on(o, x):
    turn = 1
    plr = o
    sign = 'O'
    while turn < 10:
        print 'Skriv x om du vill avsluta!'
        turn, rslt, r_sign = chk_input(raw_input('Vilken Siffra %s? ' % (plr)), sign, turn)
        prn_brd()
        stat, row = chk_stat()
        #print stat, row
        if stat == 'win':
            win(plr)

        #print rslt, sign, turn, plr
        #print choice_dict

        if r_sign == sign:
            pass
        else:
            if r_sign == 'X':
                plr = x
                sign = 'X'
            else:
                plr = o
                sign = 'O'



print 'Hello %s! Do you want to play a game' % (os.getenv('USER'))
answ = raw_input('(y/n)   :')

if answ == 'y':
    choice_dict = reset()
    prn_brd()
    gmr_o, gmr_x = gamer_init()
    game_on(gmr_o, gmr_x)
    os.system('clear')
    print '\n\n It is a draw!! All the moves have been played! Thanks %s and %s!!' % (gmr_o, gmr_x)
    exit()
else:
    go_home()
