from random import *
from os import system



print("Select one Mark 'X' or 'O'")
user=input().upper()
if user=='X' or user=="O":
    if user=='X':
        computer='@'
    else:
        computer='X'
        user='@'
else:
    print("Wrong Selection!!!")
def drawboard(board):
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    print("-"*12)
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("-"*12)
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print(" \n \n")

board=[]
input_option=list(range(0,9))
for i in range(0,9):
    board.append(str(i))

def computer_turn():
    if len(input_option) == 0:
        print("MAtCH DrAw")
        input()
        exit()
    place=sample(input_option,1)
    input_option.remove(place[0])
    board[place[0]]=computer
    if computerWinner() == True:
        print("Computer WON MATCH")
        input()
        exit()

def computerWinner():
    if(
        board[6]==board[7]==board[8]==computer or
        board[3]==board[4]==board[5]==computer  or
        board[0]==board[1]==board[2]==computer  or
        board[0]==board[4]==board[8]==computer  or
        board[2]==board[4]==board[6]==computer  or
        board[0]==board[3]==board[6]==computer  or
        board[1]==board[4]==board[7]==computer  or
        board[2]==board[5]==board[8]==computer

    ):
        return True
def userWinner():
    if(
        board[6]==board[7]==board[8]==user or
        board[3]==board[4]==board[5]==user  or
        board[0]==board[1]==board[2]==user  or
        board[0]==board[4]==board[8]==user  or
        board[2]==board[4]==board[6]==user  or
        board[0]==board[3]==board[6]==user  or
        board[1]==board[4]==board[7]==user  or
        board[2]==board[5]==board[8]==user

    ):
        return True


def player_turn():

    if len(input_option) == 0:
        print("MATCH DRAW")
        input()
        exit()
    print("Player Turn")
    print("Options Are ",input_option)
    place=int(input())
    if place in input_option:
        input_option.remove(place)
        board[place]=user
    if userWinner() == True:
        print("User WON MATCH")
        input()
        exit()



drawboard(board)
print("START HERE !!!!")
while(1):
        print("\n"*2)
        computer_turn()
        drawboard(board)
        player_turn()
        drawboard(board)
