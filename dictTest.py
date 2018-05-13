import random

choice_dict = {}
moves = ['X', 'O']
x = 1
while x < 10:
    choice_dict[x] = random.choice(moves)
    x += 1

def win(x, y):
    print 'Yay!! Win! %s (%s)' % (x, y)

cross_ltr = []
cross_rtl = []
vals = list(choice_dict.viewvalues())

for i in range(0,9,4):
    cross_ltr.append(vals[i])
    print cross_ltr

for i in range(2,7,2):
    cross_rtl.append(vals[i])
    print cross_rtl



if vals[0:3].count('O') == 3 or vals[0:3].count('X') == 3:
    win(vals[0:3], 'top')
if vals[3:6].count('O') == 3 or vals[3:6].count('X') == 3:
    win(vals[3:6], 'middle')
if vals[6:9].count('O') == 3 or vals[6:9].count('X') == 3:
    win(vals[6:9], 'bottom')
if cross_ltr.count('O') == 3 or cross_ltr.count('X') == 3:
    win(cross_ltr, 'cross_ltr')
if cross_rtl.count('O') == 3 or cross_rtl.count('X') == 3:
    win(cross_rtl, 'cross_rtl')

print '\n',vals
