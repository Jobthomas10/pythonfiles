print("Welcome to the stick game")
print("The player who takes the last stick will lose")
player1 = input("enter your name")
player2 = input("enter your name")
def stick_game(n):
    while n>0:
        sticks1 = int(input(f"{player1},You may pick 1,2 or 3 sticks: "))
        if sticks1 > 3 or sticks1 == 0:
            print("CHEATER BOII")
            print(player1, "HAS BEEN DISQUALIFIED,GAME IS BEING TERMINATED....")
            print(player2, "WINS!!")
            break
        if sticks1 == 1 or sticks1 == 2 or sticks1 == 3 and n == 0:
            print(player1, "Picks the last and loses the game! :(")
            print()
            print(player2, "WINS!!")
            break
            print(player1, "took", sticks1, "sticks")
            n = n - sticks1
            print(n, "Sticks remain")
            sticks2 = int(input(f"{player2},You may pick 1,2 or 3 sticks: "))
            print()
        if sticks2 > 3 or sticks2 == 0:
             print("YOU CHEATT")
             print(player2, "HAS BEEN DISQUALIFIED.GAME IS BEING TERMINATED...")
             print(player1, "WINS!!")
             break
        if sticks2 == 1 or sticks2 == 2 or sticks2 == 3 and n == 0:
             print(player2, "Picks the last and loses the game! :(")
             print()
             print(player1, "WINS!!")
             break
    print(player2, "took", sticks2, "sticks")
    print()
    n = n - sticks2
    print(n, "Sticks remain")
stick_game(16)



