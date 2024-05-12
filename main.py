import random
CompChoice = random.randint(0,2)

print("Welcome to Snake, Water, Gun!\n")
print("Snake = 0, \nWater = 1, \nGun = 2\n")
i = 0
while True:
 UserChoice = int(input("\nEnter 0 for Snake, 1 for Water, 2 for Gun: "))
  
 if CompChoice == UserChoice:
  print(f"Draw! You Both Chooses Same\nComputer Choice: {CompChoice} \nYour Choice: {UserChoice}")
 elif (CompChoice == 0 and UserChoice == 1):
  print(f"You Lose! \nComputer Choice: {CompChoice}\nYour Choice: {UserChoice}\nSnake drinks water")
 elif (CompChoice == 0 and UserChoice == 2):
  print(f"You Win! \nComputer Choice: {CompChoice}\nYour Choice: {UserChoice}\nGun kills snake")
  i = i+1
 elif(CompChoice == 1 and UserChoice == 0):
  print(f"You Win! \nComputer Choice: {CompChoice}\nYour Choice: {UserChoice}\nSnake drinks water")
  i = i+1 
 elif(CompChoice == 1 and UserChoice == 2):
  print(f"You Lose! \nComputer Choice: {CompChoice}\nYour Choice: {UserChoice}\nGun drowns in water")
 elif(CompChoice == 2 and UserChoice == 0):
  print( f"You Lose! \nComputer Choice: {CompChoice}\nYour Choice: {UserChoice}\nGun kills snake")
 elif(CompChoice == 2 and UserChoice == 1):
  print( f"You Win! \nComputer Choice: {CompChoice}\nYour Choice: {UserChoice}\nGun drowns in water")
  i = i+1 
 
 else:
  print("\nInvalid Choice\n") 
  print(f"You Won {i} times")
  break
   

  

