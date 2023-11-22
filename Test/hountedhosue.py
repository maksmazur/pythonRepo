
print("Welcome to hounted house.\nYour mission is to survive and find the treasure.")

choice1 = input('You\'re in the old house, Where you want to go? Type "stairs" or "basement".').lower()
if choice1 == "basement":
    choice2 =input('You\'ve come to basement. There is an chair on the middle of the basement and also you see door.Type "sit" to sit on the chair. Type "door" to go throught the doors".').lower()
    if choice2 == "door":
        choice3 = input('There is a two boxes one created by gold and other is wooden. Type "gold" or "wood"')
        if choice3 =="wood":
                print("You Find the treasure")
        else:
                print("You where killed by mimic")
    else:
        print("Game over you where killed by ghost")    
          
if choice1 == "stairs":
    print("Game over you where killed by oldman")




