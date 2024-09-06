import random
running=True
while running:
    points = int(input("enter how many points to play: "))
    win=1
    lose = 0
    score = 2
   
    for i in range(points):
        
    


        options = ("rock","paper","scissor")
        player = None
        computer = random.choice(options)
        
        while player not in options:
            player=input("enter a choice(rock,paper,scissor): ")
    
        
        print(f"player: {player}")
        print(f"computer: {computer}")

        if player == computer:
            print("its a tie")
        elif player == "rock" and computer == "scissor":
            print("you win")
        elif player == "paper" and computer == "rock":
            print("you win")
        elif player == "scissor" and computer == "paper":
            print("you win")
        else:
            print("you lose")

    if not  input("play again? (y/n)") .lower() == "y":
    
     running = False

print("thanks for playing")
