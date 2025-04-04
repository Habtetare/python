def main():
    difficulty = input("Difficulty or Casual?")
    if not difficulty == "Difficulty" or difficulty == "Casual":
        print("I don't recommend")
        return

    player = input("Multiplayer or single-player")
    if not player == "Multiplayer" or player == "single-player":
        print("I don't recommend")
        return

    if difficulty == "Difficult" and player == "Multyplayer":
            recommend("Poker")
    elif difficulty == "Difficult" and player == "single-player":
            recommend("klondike")
    elif difficulty == "Casual" and player == "Multyplayer":
            recommend("Hearts")
    else:
            recommend("Cloks")

def recommend(game):
    print("You May like",game)


main()
