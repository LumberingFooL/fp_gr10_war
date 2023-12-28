#This files is responsible for all the calculations and will perform certain actions depending what is called upon from main.py (like the cpu)

from Graphics import*

def intro(dealer,player,deck): #Gives the starting hand to the dealer and player
  for i in range(0,2,1): #2 cards each, removes the cards from the main deck
    dealer.append(deck.pop())
    player.append(deck.pop())

  intro_gateway(dealer,player) #already explained in Graohics.py
  if (player[0] == player[1] or (player[0] == "Ace" and player[1] == "Ace") or (player[0] == "Jack" and player[1] == "Jack") or (player[0] == "Queen" and player[1] == "Queen") or (player[0] == "King" and player[1] == "King")):
    split = input("Do you want to split? ")
    if (split == "yes"):
      return True
  return False #sees if your starting hand has 2 of the same cards and asks you if you want to split them into 2 seperate hands. Returns the true and false bool accordingly

def p_giver(player,dealer,deck): #Gives the player a card after they hit and removes that card from the main deck
  player.append(deck.pop())

  intro_gateway(dealer,player)

def ai_giver(dealer,player,deck): #Gives the dealer a card and removes that card from the main deck
  dealer.append(deck.pop())

  gateway(dealer,player) #already explained in Graohics.py

def split_ai_giver(dealer,player,player_split,deck):
  dealer.append(deck.pop())

  split_gateway(dealer,player,player_split)
  
def checker(x,streak): #Calculates the hand value by adding every card up 
  copy = x[:] #creates a copy list
  counter = 0 #What everything adds up into
  special_numbers(copy) #If there are any facecards it calculates the values of those and replaces the strings with their corresponding integer value in the copied list
  for i in range(0, len(copy), 1):
    counter += copy[i] #adds everything up
  if counter > 21:
    return counter, streak #returns the values
  else:
    streak += 1 #adds to the streak if under 21
    return counter, streak # returns values
  
def special_numbers(x): #Replaces the strings with their corresponding integer counterparts so that the program can add the numbers up 
  Ace = 0
  ace_control = 0 #the counter that tracks the value of everything aexcept the ace so that the ace can become its expected value
  for i in range(0, len(x), 1):
    if (x[i] == "King"):
      x.remove("King")
      x.insert(i,10)
    elif (x[i] == "Queen"):
      x.remove("Queen")
      x.insert(i,10)
    elif (x[i] == "Jack"):
      x.remove("Jack")
      x.insert(i,10)
    elif (x[i] == "Ace"):
      Ace += 1 #counts how many aces there are so the for loop down below can loop the correct amount of times
    else:
      pass
  if (Ace > 0):
    for i in range(0, Ace, 1):
      for i in range(0, len(x), 1):
        if (x[i] == "Ace"):
          continue
        ace_control += x[i]
      if (ace_control+11 > 21): #if ace with the value 11 would make the hand value over 21, then assign the ace value with 1
        x.remove("Ace")
        x.insert(i,1)
      else: #if it doesn't assign the value 11
        x.remove("Ace")
        x.insert(i,11)

def split(player, player_split, dealer, deck): #splits the hand into 2. And appends a card for each of the new hand
  player_split.append(player.pop())
  player_split.append(deck.pop())
  player.append(deck.pop())
  intro_split_gateway(dealer,player,player_split) #same thing as intro_gateway but it prints the extra hand as well

def p_giver_split(player,player_split,dealer,deck,split_): 
  player.append(deck.pop()) #same thing as p_giver but gives a card to either the main hand or the split hand
  if (split_ == False): #If the player wants to add a card to the split hand
    intro_split_gateway(dealer,player_split,player)
  else: #If the player is still adding cards to the first hand(hand 1)
    intro_split_gateway(dealer,player,player_split)