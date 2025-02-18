import random

def coinToss():
    return random.choice(["Heads", "Tails"])

def playGame():
    print("Welcome to the Coin Toss Game!")
    wins = 0
    losses = 0

    while True:
        guess = input("Guess which side the coin will land on! \n(type 'h' for heads or 't' for tails, and type 'q' to quit):\n")
        if guess == 'q' or guess == 'Q':
            print("Your Final Score is:", wins, "Win(s),", losses, "Loss(es)")
            print("Thank you for playing!")
            break
        if guess not in ['h', 't', 'H', 'T']:
            print("Invalid input. Enter 'h','t', or 'q'.")
            continue
        result = coinToss()
        print("The coin landed on:", result)
        if guess in ['h', 'H']:
            guess = "Heads"
        else:
            guess = "Tails"

        if guess == result:
            print("Congratulations! You won!")
            wins += 1
        else:
            print("Sorry, you lost. Try again!")
            losses += 1

if __name__ == "__main__":
    playGame()
