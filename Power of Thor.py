import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
x, y, tx, ty = [int(i) for i in input().split()]

# game loop
drc = ()
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.    
    
    if tx==x:
        if ty>y:
            ty -= 1
            print('N')
        else:
            ty += 1
            print('S')
    if ty==y:
        if tx<x:
            print('E')
        else:
            print('W')

    if tx!=x and ty!=y and tx<x:
        if ty>y:
            tx += 1
            ty -= 1
            print('NE')
        else:
            tx += 1
            ty += 1
            print('SE') 

    if tx!=x and ty!=y and tx>x:
        if ty>y:
            tx -= 1
            ty -= 1
            print('NW')
        else:
            tx -= 1
            ty += 1
            print('SW')
            
###############################################################


while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    next_x = initial_tx - light_x
    next_y = initial_ty - light_y
    move = ''
    if (next_y < 0):
        move+='S'
        initial_ty += 1
    if (next_y > 0):
        move+='N'
        initial_ty -= 1
    if (next_x < 0):
        move+='E'
        initial_tx += 1
    if (next_x > 0):
        move+='W'
        initial_tx -= 1
    print(initial_t
          
 #####################################################
          while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print

    resultx, initial_tx = ("E", initial_tx+1) if light_x > initial_tx else (("W", initial_tx-1) if light_x != initial_tx else ("", initial_tx))
    resulty, initial_ty = ("S", initial_ty+1) if light_y > initial_ty else (("N", initial_ty+1) if light_y != initial_ty else ("", initial_ty))
    
    print(resulty+resultx)
