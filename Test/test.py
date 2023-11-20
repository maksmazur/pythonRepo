#data types
print("Hello"[4])


#Integer

print(123 + 345)
print(123_234_444 + 1)

#flout
print(3.14159 + 1.23)

#boolean
True
False

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

a  = float(123)

print(type(a))


#two_digit_number = input("Podaj numer: ")

#first_digit = (int(two_digit_number[0]))
#second_digit = (int(two_digit_number[1]))

#print (first_digit + second_digit)

#math operators

3 + 5
7 - 4
3 * 2
6 / 2
2 ** 2

#height = input("wzrost: ")
#weight = input(" waga ")

#height_input = float(height)
#weight_input = float(weight)

#print(int(weight_input / (height_input ** 2)))

print(round(8 / 3))  # round zaokrągla 2,6  = 3 etc
print(round(2.6666666666, 3))

print(8 // 3)  # automatycznie kowenrtuje do int

result = ( 4/ 2)
result /=  2
print (result)

score = 0
height = 1.8
isWining = True
#f-type
print(f"your score is {score}, your height is {height}. you are wining is{isWining}")

age = input("Wiek: ")

years = 90 - int(age)
weeks = years + 52
print(f"You have {weeks} weeks")