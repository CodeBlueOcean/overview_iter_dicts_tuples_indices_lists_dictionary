import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user = input("Enter to pick a card")
    if user.casefold() == "q":
        print("The game has ended")
        exit()
    card = random.choice(diamonds)
    # Random Card from Diamonds Deck
    hand.append(card)
    # Remove that card from the diamonds, 
    diamonds.remove(card)
    # Print the contents of both decks
    print(hand)
    print(diamonds)
    if not diamonds:
        print("There are no more cards to pick")
 
