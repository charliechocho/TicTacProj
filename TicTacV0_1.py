# -*- coding: utf-8 -*-
import os

def reset():
    choice_li = [x for x in range(1,10)]
    return choice_li


def prn_brd():
    os.system('clear')
    print '*' * 9

    print '* %s|%s|%s *' % (choice_li[0], choice_li[1], choice_li[2])
    print '* %s|%s|%s *' % (choice_li[3], choice_li[4], choice_li[5])
    print '* %s|%s|%s *' % (choice_li[6], choice_li[7], choice_li[8])

    print '*' * 9

def go_home():
    print 'Game Over'
    exit()

def chk_input(move, sign, turn):
    move -= 1
    if choice_li[move] == 'O' or choice_li == 'X':
        return turn, 'Already taken, try again', sign
    else:
        if sign == 'O':
            updt_li(move, sign)
            turn +=1
            sign = 'x'
        else:
            updt_li(move, sign)
            turn +=1
            sign = 'o'

        return turn, '', sign


def updt_li(move, plr):
    #move -= 1
    choice_li[move] = plr


def gamer_init():
    crkl = raw_input('Gamer Circle, enter your name!: ')
    cros = raw_input('Gamer Cross, enter your name!: ')
    return crkl, cros

def game_on(o, x):
    plr = o
    turn = 1
    while turn < 10:
        if plr == o:
            turn, rslt, sign = chk_input(int(raw_input('Vilken Siffra %s? ' % (o))), 'O', turn)
            prn_brd()
            print rslt, sign, turn
            plr = x
        elif plr == x:
            turn, rslt, sign = chk_input(int(raw_input('Vilken Siffra %s? ' % (x))), 'X', turn)
            prn_brd()
            print rslt, sign, turn
            plr = o




print 'Hello %s! Do you want to play a game' % (os.getenv('USER'))
answ = raw_input('(y/n)   :')

if answ == 'y':
    choice_li = reset()
    #print choice_li
    prn_brd()
    gmr_o, gmr_x = gamer_init()
    game_on(gmr_o, gmr_x)
    exit()
else:
    go_home()
