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
    print 'Game Over'
    exit()

def is_number(no):
    try:
        return int(no)
    except ValueError:
        return False

def keep_sign(si):
    if si == 'O':
        return 'X'
    else:
        return 'O'


def chk_input(move, sign, turn):
    chk_no = is_number(move)
    if chk_no == False:
        #sign = keep_sign(sign)
        return turn, 'Wrong input! Must be a NUMBER! ', sign
    elif int(move) <= 0 or int(move) >= 10:
        #sign = keep_sign(sign)
        return turn, 'Wrong input! Must be NUMBER 1-9! ', sign
    else:
        move = int(move)
        if choice_dict[move] == 'O' or choice_dict == 'X':
            #sign = keep_sign(sign)
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
        turn, rslt, r_sign = chk_input(raw_input('Vilken Siffra %s? ' % (plr)), sign, turn)
        prn_brd()
        print rslt, sign, turn, plr
        print choice_dict
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
    #print choice_dict
    prn_brd()
    gmr_o, gmr_x = gamer_init()
    game_on(gmr_o, gmr_x)
    print 'All the moves have been played!'
    exit()
else:
    print '\n\nHave a great day!!'
    go_home()
