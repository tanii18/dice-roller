import random

while True:

  print("welcome to dice roller")
  input("enter to roll dice")

  roll=random.randint(1,6)
  print(f"you rolled a, {roll}")
  play_again=input("wanna play again?yes or no").lower()
  if play_again == "no":
   print("thanks for playing hope u enjoyed")
   break