import random

rock = '''
HEAVY SHIT AT ME!!! THAT HEAVY SHIT!!!"   _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/ '''


paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|     '''


scissors = ''' 
  ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/   '''

game_images = [rock,paper,scissors]

user_choice = int(input("Whats do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("You type invalid number YOU LOSE!!! LOSER")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)

    print(f"Computer chose {computer_choice}")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("User win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("Is a draw")
    else:
        print("You type invalid number YOU LOSE!!! LOSER")

