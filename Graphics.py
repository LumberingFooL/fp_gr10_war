#These are where the graphics for the cards are stored and printed from, based on what you have in your hand (Like the gpu)
#Note, these graphics have no effect on the actual hand of the dealer/player. It just makes a copy of said hands and prints their graphic card equivilant so that it looks nicer

def graphics(x): #where all the card types are stored
  if (x == 2):
    return(" _____ |2    ||  ^  ||     ||  ^  ||____Z|")
  elif (x == 3):
    return(" _____ |3    || ^ ^ ||     ||  ^  ||____E|")
  elif (x == 4):
    return(" _____ |4    || ^ ^ ||     || ^ ^ ||____h|")
  elif (x == 5):
    return(" _____ |5    || ^ ^ ||  ^  || ^ ^ ||____S|")
  elif (x == 6):
    return(" _____ |6    || ^ ^ || ^ ^ || ^ ^ ||____9|")
  elif (x == 7):
    return(" _____ |7    || ^ ^ ||^ ^ ^|| ^ ^ ||____L|")
  elif (x == 8):
    return(" _____ |8    ||^ ^ ^|| ^ ^ ||^ ^ ^||____8|")
  elif (x == 9):
    return(" _____ |9    ||^ ^ ^||^ ^ ^||^ ^ ^||____6|")
  elif (x == 10):
    return(" _____ |10 ^ ||^ ^ ^||^ ^ ^||^ ^ ^||___0I|")
  elif (x == "Jack"):
    return(" _____ |J  ww|| ^ {)||(.)% || | % ||__%%[|")
  elif (x == "Queen"):
    return(" _____ |Q  ww|| ^ {(||(.)%%|| |%%%||_%%%O|")
  elif (x == "King"):
    return(" _____ |K  WW|| ^ {)||(.)%%|| |%%%||_%%%>|")
  elif (x == "Ace"):
    return(" _____ |A .  || /.\ ||(_._)||  |  ||____V|")

def hidden(): #specifically for the dealer as one of his cards is hidden throughout most of the game to the player
  return(" _____ |\ ~ /||}}:{{||}}:{{||}}:{{||/_~_\|")

def intro_split_gateway(dealer,player,player_split): #same thing as intro_gateway but prints the player_split as well
  visual = []
  for i in range(0,len(dealer)-1,1):
    visual.append(graphics(dealer[i]))
    visual.append(hidden())
  stocks(visual) 

  visual = []
  for i in range(0,len(player),1):
    visual.append(graphics(player[i]))
  stocks(visual)

  visual = []
  for i in range(0,len(player_split),1):
    visual.append(graphics(player_split[i]))
  stocks(visual)

def split_gateway(dealer,player,player_split): #same thing as regular gateway but prints player_split as well
  visual = []
  for i in range(0,len(dealer),1): 
    visual.append(graphics(dealer[i]))
  stocks(visual)

  visual = []
  for i in range(0,len(player),1):
    visual.append(graphics(player[i]))
  stocks(visual)

  visual = []
  for i in range(0,len(player_split),1):
    visual.append(graphics(player_split[i]))
  stocks(visual)

def gateway(dealer,player): #prints each respective hand as the corresponding graphic card
  visual = []
  for i in range(0,len(dealer),1): #calculates which graphic card matches the card in the actual hand and puts those corresponding graphic cards into a new list. This new list is then sent to another function to be printed properly. 
    visual.append(graphics(dealer[i]))
  stocks(visual)

  visual = []
  for i in range(0,len(player),1): #does the same thing as the comment above except this time it's for the player not the dealer
    visual.append(graphics(player[i]))
  stocks(visual)

def intro_gateway(dealer,player): #prints the cards of the player and one of the card for the dealer. Does the same thing as the gateway function but the second card for the dealer is hidden (printed as the hidden card mentionned above)
  visual = []
  for i in range(0,len(dealer)-1,1):
    visual.append(graphics(dealer[i]))
    visual.append(hidden())
  stocks(visual) 

  visual = []
  for i in range(0,len(player),1):
    visual.append(graphics(player[i]))
  stocks(visual)

def stocks(visual): #After the cards have been assigned into their graphic card equivilant, these new lists are sent here to be printed properly
  calculator = len(visual) #calculates how many cards there are
  counter = 0 #determines when to go down a line (because it prints everything top to bottom like a printer)

  for z in range(0,42,7): #prints the first 7 characters of each card (each card has 42 characters)
    for x in range(0,calculator,1): #^^^
      list = [] #new list for each row 
      for i in range(0+z,7+z,1):
        var = visual[x]
        list.append(var[i])
      list="".join(list) #once the 7 first characters of each card are in the list it joins them together to be printed
      counter += 1
      if (counter > calculator): #once they've gone throught the first seven characters for each card it skips to a new line to repeat the process until every card is printed properly
        print("\n" + list,end=" ")
        counter = 1 #resets the counter
      else:
        print(list,end=" ")
  print("\n")

def score_display(score_p,score_ai): #displays the score
  print("Player:", score_p, "-", "Dealer:", score_ai)