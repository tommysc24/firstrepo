import random

class player 
  def __init__(self, name, score): 
    self.name = name 
    self.score = score
p1 = player("Dougie", 0)
p2 = player("Roberto", 0)
print(p1.name + "goes first!")
#make the deck 
deck = []
def make_deck():
  for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
    for number in (2, 15):
      deck.append((suit, number))

def card_name(card):
  if card[0] <= 10:
    number = str(card[0])
  if card[0] == 11:
    number = "Jack"
  if card[0] == 12:
    number = "Queen"
  if card[0] == 13:
    number = "King"
  if card[0] == 14:
    number = "Ace"
  card_thing = number + " of " + card[1]
  return card_thing 

print(deck)

class draw_card 
  import random 
  import card_thing
  def __init__(self, card): 
    card = card_thing
    self.card = random.deck[0]
    deck.remove(deck[0])
    print(card)
    print("Player" + " drew the" + card)
   super(player)

   



#random draws from deck
random.draw(deck)

#each player draws card 
while True:
  player_one_card = draw_card.p1
  player_two_card = draw_card.p2
#compare to see who wins
  if player_one_card[0] > player_two_card[0]:
    winner = "Player one"
    player_one_score += 2
  if player_one_card[0] > player_two_card[0]:
    winner = "Player two"
    player_two_score += 2
  else:
    winner = "No one"
  print(Winner + "wins!")
  print(player_one_score)
  print(player_two_score)
  option = input("Type enter to play again or quit to quit")
  if option == casefold("enter"):
    continue 
  if option == casefold("quit"):
    break
