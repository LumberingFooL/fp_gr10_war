from Functions import *
from Graphics import *
import random
import os

score_p = 0 #sets the score for the the player and ai
score_ai = 0

print("The rules:\n1.The top hand of is the dealer and the bottom is yours,\nthe player\n2.The goal is to get as close to 21 as possible\nwhile not going over. This would result in a lose\n3.You both get 2 cards to start\nbut one of the dealers card is hidden\n4.If you get 5 cards without busting you instantly win\n5.If you get the same cards in the starting hand you can split.\nThis means you get 2 chances to win but alse 2 chances to lose\n6.Aces count as either 1s or 11s depending on your hand,\nThe value will update accordingly\nas you hit as to not put you over 21\n") #explains the rules 

while True: #Main gameplay loop
  start = input("Do you want to play Blackjack?\n") #self explanitory
  if (start == "yes" or start == "y" or start == "Yes"): 
    os.system("clear")
    pass
  else:
    os.system("clear")
    break

  score_display(score_p,score_ai) #displays the score

  deck = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]*4 #creates the deck
  random.shuffle(deck) #shuffles the deck
  dealer = [] #creates the lists for the dealer,player, and split
  player = []
  player_split = []
  split_ = intro(dealer,player,deck) #gives the starting hand to the dealer and player 
  streak = 2 #streak, if player gets five cards they automatically win
  boss = False #if they do get 5 cards, it makes this value true so that it doesn't run something else it shouldn't

  if (split_ == True): #The gameplay if the player wants to split
    win_split = 0 #keeps track which hand is a bust or passes the hit/stand portion for the player
    os.system("clear")
    score_display(score_p,score_ai)
    split(player,player_split,dealer,deck) #explained already in functions

    for i in range(1,3,1): #goes through the loop twice since there are 2 hands now for the player
      if (i == 2): #Once it is the second hand, it switches the lists around so that i don't have to copy the whole gameplay loop again 
        counter_p_split = counter_p
        copy = player[:]
        player = player_split[:]
        player_split = copy[:]
        split_ = False #explained already
        streak = 2 #resets the streak for the second hand
      while True: #hit/stand gameplay loop
        user = input("\nHit or stand: ") #self explainitory
      
        if (user == "hit" or user == "Hit" or user == "h" or user == "yes" or user == "y"): #if they want to hit 
          os.system("clear")
          score_display(score_p,score_ai)
          p_giver_split(player,player_split,dealer,deck, split_)#gives either hand1 or hand 2 a card depending on the if (i == 2): thing explained above
          counter_p,streak = checker(player,streak) #check the value of the hand
          if (counter_p <= 21): #if counter is under or equal to 21
            if (streak == 5 or counter_p == 21): #self explainitory, explained what streak was already
              if (streak == 5): 
                boss = True
                print("Hand", i, "is a win\n")
                score_p += 1 #adds to the score of the player
              win_split += i #records the hand if they win/pass
              break
          else:
            print("Hand", i, "is a bust\n") #if the counter is over 21
            score_ai += 1 #the dealer gets a point
            break
        else: #if they respond no
          counter_p,streak = checker(player,streak) #records the value of the hand of the player for the dealer game loop
          win_split += i #explained already
          break

    copy = player[:] #resets the lists back to the way they were 
    player = player_split[:]
    player_split = copy[:]

    if ((win_split==1 or win_split==2 or win_split==3) and boss == False): #checks to see if there are any passing hands or if the player got a 5 for the streak
      if (win_split==1): #if hand 1 passed
        win = True
        os.system("clear")
        score_display(score_p,score_ai)
        split_gateway(dealer,player,player_split)
        counter_ai,streak = checker(dealer,streak)
        while (counter_ai <= 21): #while the dealer is under 21
          if (counter_ai >= counter_p_split): #if its equal to or greator than hand 1
            if (counter_ai == counter_p_split): #if its equal
              print("Hand 1 is a standoff, tie\nHand 2 is a bust")
              win = False
              break
            else: #if its greater than
              print("Both hands are a bust\n")
              score_ai += 1
              win = False
            break
          os.system("clear")
          score_display(score_p,score_ai)
          split_ai_giver(dealer,player,player_split,deck) #gives a card to the dealer
          counter_ai,streak = checker(dealer,streak) #checks and records the score of the dealer
        if (win == True): #if hand 1 beats the dealer
          print("Hand 1 is a win\nHand 2 is a bust\n")
          score_p += 1

      #the gameplay loops for if both hands passed is the same as the one already explained. Except, the dealers hand is compared to both hands
      elif (win_split == 3): #if both hands passed
        win = True
        os.system("clear")
        score_display(score_p,score_ai)
        split_gateway(dealer,player,player_split)
        counter_ai,streak = checker(dealer,streak)
        while (counter_ai <= 21):
          if (counter_ai >= counter_p or counter_ai >= counter_p_split):
            if (counter_ai == counter_p):
              print("Hand 2 is a standoff, tie\n")
              counter_p = 50
              win = False
              break
            if (counter_ai == counter_p_split):
              print("Hand 1 is a standoff, tie\n")
              counter_p_split = 50
              win = False
              break
            if (counter_ai > counter_p):
              print("Hand 2 is a bust\n")
              counter_p = 50
              score_ai += 1
              win = False
            if (counter_ai > counter_p_split):
              print("Hand 1 is a bust\n")
              counter_p_split = 50
              score_ai += 1
              win = False
            break
          os.system("clear")
          score_display(score_p,score_ai)
          split_ai_giver(dealer,player,player_split,deck)
          counter_ai,streak = checker(dealer,streak)
        if (counter_p < 50):
          print("Hand 2 is a win\n")
          score_p += 1
        if (counter_p_split < 50):
          print("Hand 1 is a win\n")
          score_p += 1

      #same as if hand 1 passed but for hand 2
      elif (win_split == 2): #if the second hand passed 
        win = True
        os.system("clear")
        score_display(score_p,score_ai)
        split_gateway(dealer,player,player_split)
        counter_ai,streak = checker(dealer,streak)
        while (counter_ai <= 21):
          if (counter_ai >= counter_p):
            if (counter_ai == counter_p):
              print("Hand 2 is a standoff, tie\nHand 1 is a bust\n")
              win = False
              break
            else:
              print("Both hands are a bust\n")
              score_ai += 1
              win = False
            break
          os.system("clear")
          score_display(score_p,score_ai)
          split_ai_giver(dealer,player,player_split,deck)
          counter_ai,streak = checker(dealer,streak)
        if (win == True):
          print("Hand 2 is a winn\nHand 1 is a bust\n")
          score_p += 1

  else: #If the player decides not to split or is unable to due to their hand. All of these things inside this condition have already been explained in the split condition. Except this time the program doesn't have to deal with the extra hand
    while True:
      user = input("\nHit or stand: ")
    
      if (user == "hit" or user == "Hit" or user == "h" or user == "yes" or user == "y"):
        os.system("clear")
        score_display(score_p,score_ai)
        p_giver(player,dealer,deck)
        counter_p,streak = checker(player,streak)
        if (counter_p <= 21):
          if (streak == 5 or counter_p == 21):
            if (streak == 5):
              boss = True
              print("Winner\n")
              score_p += 1
            win = True
            break
        else:
          win = False
          print("You busted\n")
          score_ai += 1
          break
      else:
        counter_p,streak = checker(player,streak)
        win = True
        break
    
    if (win == True and boss == False):
      os.system("clear")
      score_display(score_p,score_ai)
      gateway(dealer,player)
      counter_ai,streak = checker(dealer,streak)
      while (counter_ai <= 21):
        if (counter_ai >= counter_p):
          if (counter_ai == counter_p):
            print("Standoff, tie\n")
            win = False
            break
          else:
            print("You busted\n")
            score_ai += 1
            win = False
          break
        os.system("clear")
        score_display(score_p,score_ai)
        ai_giver(dealer,player,deck)
        counter_ai,streak = checker(dealer,streak)
      if (win == True):
        print("Winner\n")
        score_p += 1