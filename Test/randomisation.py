import random


c = random.randint(100,200)
d = random.randint(1,50)
print(c)
print (d)
print (c + d)



throw = random.randint(1,2)
if throw == 1:
    print("Heads")
else:
    print("tail")
print(throw)


#list

randomList = ["Elo","Mordo","Jak","Zrobic","Teraz","To"]
randomList.extend("Maks")
print (len(randomList))


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

print("Szukajka")

line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]

map = [line1,line2,line3]
print("Hidding your treasure1 X mars the spot")
position = input()

letter = position[0].lower()
abc = ["a","b","c"]
letters_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letters_index] = "x"


print(f"{line1}\n{line2}\n{line3}")