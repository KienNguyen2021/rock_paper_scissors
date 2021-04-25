import random

game_images = ["rock", "paper", "scissors"]
user_choice = int (input(" What do choose ? Type 0 for Rock, 1 for Paper, 2 for Scissor. \n"))

if user_choice >=3 or user_choice < 0 :
    print (" You enter invalid number ! ")
else :
    print(game_images[user_choice])

#computer choice : use random number
computer_choice = random.randint (0,2)
# print (f" Computer chose {computer_choice}")
print (f" Computer chose : ")
print ( game_images[computer_choice])

# compare 2 choices for the logic

# if user_choice >= 3 or user_choice < 0 : 
#   print (" You typed invalid number, you lose ! ")

if user_choice == 0 and computer_choice == 2 :
    print ( " You win ! ")
elif computer_choice == 0 and user_choice == 2:
    print (" You lose ")    
elif computer_choice > user_choice :
    print (" You lose! ")    
elif user_choice > computer_choice :
    print (" You win !")    
elif computer_choice == user_choice :
    print (" It is a draw ")    
# elif user_choice >= 3 or user_choice < 0 :   when use enter 245, it print Computer win
 #   print (" You typed invalid number, you lose ! ")    