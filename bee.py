WORDS = {"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPHIC":7}
total = 0
def main():
    print("Welcome to spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{(len(WORDS))} words left!")
        guess = input("Guess a word: ")
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You Won!!")
        if guess in WORDS.keys():
            global total
            points = WORDS.pop(guess)
            print(f"Good Job! you scored {points} Points")
            total = total + int(points)
            print (f"Total Point {total}")
print("That is Game Over")
for key, values in WORDS.items():
    print(f"{key} was worth {values}")
main()
