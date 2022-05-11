# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 21:48:32 2022

@author: Sai Prathap
"""

import random
def dice(score):
    die = random.randint(1, 6)
    print("You got ",die)
    score = score + die
    print("Your present score is ",score)
    score = ladder(score)
    score = snake(score)
    return score
def snake(score):
    danger = {44:19, 46:5 ,48:9 ,52:11 ,55:7,59:19,69:33,73:1,83:19,92:51,95:24,98:28}
    if score in danger.keys():
        print("You got bitten with a snake at " , score)
        score = danger[score]
        print("You are falling down to ",score)
    return score
def ladder(score):
    luck = {8:26,21:82,50:91,54:93,62:96,66:87,80:100,}
    if score in luck.keys():
        print("Hey! you are lucky you got a ladder at ",score)
        score = luck[score]
        print("You moved up to ",score)
    return score
def play():
    p1 = input("Player 1 , Please Enter your name : ")
    p2 = input("Player 2 , please Enter your name : ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(pp1 <= 100 and pp2 <= 100):
        if turn %2 == 0:
            print(p1," it's your turn")
            x= input()
            pp1 = dice(pp1)
        else:
            print(p2," it's your turn")
            x=input()
            pp2 = dice(pp2)
        turn += 1
    if pp1 > pp2:
        winner = p1
    elif pp1 < pp2:
        winner = p2
    else:
        winner  = "Both the players"
    print("Congratulations ",winner," for winning the match ")
    print("Thank you ",p1,"and ",p2," for playing the game ,hope I see you back again")
play()