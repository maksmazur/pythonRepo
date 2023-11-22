#print("cos tam")
#height = int(input("Whats is your height"))

##if height > 120:
   # print("you can ride")
#else:
 #   print(" NO !")


#number = int(input())

#if number % 2 == 0:
 #   print("this is an even number")
#else:
 #   print("This is an odd number")

print("Hi")
height = int(input("What is your height"))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("Whats your age?"))
    if age < 12:
        print("Children ticket are: 5$")
        bill = 5
    elif age <= 18:
        print("Youth tickets are: 7$")
        bill = 7
    elif age >= 45 and age <=55:
        print("You have free ride!!!!!")
    else:
        print("Adult tickes are: 12$")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"Your finally bill is {bill}")

else:
    print("Sorry not for you :) ")