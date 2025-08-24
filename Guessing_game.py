"""Welcome to the Number Guessing Game! 
Instructions to Play are as follows:-
1. The computer will randomly select a number from 1 to 100.
2. Your job is to guess the number.
3. After every guess you will get a hint. The hint will tell you whether your guess is higher
   than the number by displaying 'too high' or lower than the number by displaying 'too low'.
4. You can exit the game whenever you want by typing 'exit'.
5. The game will track your number of attempts in a round and use it to display your best
   score across multiple rounds. """
import random #random module helps with generation of rnadom numbers.
def Start_Game():
    num=random.randint(1,100) #tells the computer to go in random module and select a number between 1 to 100.
    attempts=0
    print("Let's start the game")
    print("I have picked a number.Your turn now!")
    while True:
        guess=input("Your guess\n")
        if guess.lower()=="exit": # makes input lowercase i.e. case insensitive so EXIT or exit or Exit all works.
            print("Thanks for playing.Quitting the round in 3 2 1!")
            return
        if not guess.isdigit(): #Checks if the input in numbers or not.
            print("Well, that doesn't look like a number.Try again!\n")
            continue
        guess=int(guess)#Converts the number from string to integers for further tasks.
        attempts +=1#Increases number of attempt by +1 with every guess made by the user.
        #Now! Let's start comparing the random number with guesses of the user.
        if guess<num:
            print("Too low!Try something big.")
        elif guess>num:
            print("Too high!Not that big.")
        else:
            print(f"Congratulations!You won the game in {attempts} attempts.")
            return attempts
        #Creating a menu for the game to arrange it in better way.
def main():
    print("Welcome to the guessing game!")
    best_score = None
    games_played = 0
    games_won = 0

    while True:
        print("Menu")
        print("1. Start New Game")
        print("2. Show best score")
        print("3. Exit")
        choice = input("Choose an option\n")

        if choice == "1": # '==' is used to compare if two things are equal.
            result = Start_Game()
            games_played += 1
            if result is not None:
                games_won += 1
                if best_score is None or result < best_score:
                    best_score = result
        elif choice == "2":
            print("\nGame stats are:-")
            print(f"Games Played = {games_played}")#f is used to place a variable in the print statement directy by using these {} brackets. 
            print(f"Games Won = {games_won}")
            if best_score is not None:
                print(f"Best Score = {best_score}")
            else:
                print("Best Score=None(Play a game first to get the best score!)")
        elif choice == "3":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1, 2 or 3 only")

if __name__ == "__main__":
    main()        