"""
WORKFLOW OF PROJECT 
1-Input From User(Rock,Paper,Scissor)
2-Computer Choice(Computer will choose randomly not conditionally)
3-Result Print
Logic:
Case:
A - Rock
Rock - Rock = tie
Rock - Paper = Paper win 
Rock - Scissor = Rock win 

B - Paper 
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor 
Scissor - Scissor = tie
Scissor - Rock = Rock win 
Scissor - Paper = Scissor win 

"""
import random
item_list= ["Rock","Paper","Scissor"]
user_choice = input("Enter your move = Rock,Paper,Scissor :")
Comp_Choice = random.choice(item_list)
print(f"User Choice = {user_choice}, Computer Choice = {Comp_Choice}")

if user_choice==Comp_Choice :
    print("Both Choices Same : Match Tie")

elif user_choice == "Rock":
    if Comp_Choice == "Paper":
      print("Paper Covers Rock = Computer Win")    
    else:
     print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if Comp_Choice == "Scissor":
      print("Scissor cuts Paper  = Computer Win")    
    else:
     print("Paper Covers Rock = You Win")

elif user_choice == "Scissor":
    if Comp_Choice == "Rock":
      print("Rock Smashes Scissor = Computer Win")    
    else:
     print("Scissor cuts paper = You Win")

