year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:("Not Leap year")
    else:
        print("its leap year")
else:
    print("Not leap year")
