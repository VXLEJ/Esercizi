# 4-1. Pizzas:
"""Pizzas = ['Margherita', 'Crostino', 'Patatine fritte e Wurstel']

for Pizza in Pizzas:
    print(Pizza)

sentence = 'Ordinerò una '

for Pizza in Pizzas:
    print(sentence, Pizza)
"""

# 4-2. Animals:
"""Animals = ['Cane', 'Gatto', 'Criceto']

for Animal in Animals:
    print(Animal)

descanimals = {'Cane': 'Miglior amico dell uomo', 'Gatto': 'Felino feroce', 'Criceto': 'ottimo per i bambini'}

sentence2 = 'sono tre ottimi animali'

for Animal in Animals:
    print(Animal, sentence2)
"""

# 4-3. Counting to Twenty:
"""for number in range(1, 21):
    print(number)
"""

# 4-4. One Million:
"""for number4 in range(1, 1000001):
    print(number4)
"""

# 4-5. Summing a Million:
"""million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))
"""

# 4-6. Odd Numbers:
"""for numbers in range(1, 21, 2):
    print(numbers)
"""

# 4-7. Threes:
"""for numbers in range(3, 31, 3):
    print(numbers)
"""

# 4-8. Cubes:
"""Cubes = [i ** 3 for i in range(1, 11)]
print(Cubes)
"""

# 4-9. Cube Comprehension:
"""Cubes = [i ** 3 for i in range(11)]
print(Cubes)
"""

# 4-10. Slices:
"""print('first three items: ', Cubes[0:3])
print('three items in the middle: ', Cubes[3:6])
print('last three items: ', Cubes[-3:])
"""

# 4-11. My Pizzas, Your Pizzas:
"""newpizza = 'Diavola'
newpizza2 = 'Napoli'
Pizzas.append(newpizza)
friend_pizzas = ['Margherita', 'Crostino', 'Patatine fritte e Wurstel']
friend_pizzas.append(newpizza2)
print('my favorite pizzas are: ', Pizzas)
print('my friend s favorite pizzas are: ', friend_pizzas)
"""

# 4-15. Code Review:
"""pizzas = ['Margherita', 'Crostino', 'Patatine fritte e Wurstel']
for pizza in pizzas:
    print(pizza)

sentence = 'Ordinerò una '

for pizza in pizzas:
    print(sentence, pizza)

for number in range(1, 21):
    print(number)

for number in range(2, 21, 2):
    print(number)
"""

# 5-1. Conditional Tests:
"""Car = 'Citroen'
Model = 'C1'
Color = 'White'
print("is car 'Citroen'? I predict True.")
print(Car == 'Citroen')

print("is car 'Audi'? I predict False")
print(Car == 'Audi')

print("is Model 'C1'? I predict True")
print(Model == 'C1')

print("is Model 'C3'? I predict False")
print(Model == 'C3')

print("is Color 'White'? I predict True")
print(Color == 'White')

print("is Color 'Black'? I predict False")
print(Color == 'Black')

print("is Color 'Yellow'? I predict False")
print(Color == 'Yellow')

print("is Color 'Green'? I predict False")
print(Color == 'Green')

print("is Model 'C2'? I predict False")
print(Model == 'C2')

print("is car 'BMW'? I predict False")
print(Car == 'BMW')
"""

# 5-2. More Conditional Tests:
"""Gbrand = 'Glock'
Gmodel = '17'
magazine = 9
Gcaliber = '9mm'

print("is brand Glock? I predict True")
print(Gbrand == 'Glock')

print('is it a Beretta? I predict False')
print(Gbrand == 'Beretta')

print('is a model 17? i predict True')
print(Gmodel == '17')

print('is a model 18? i predict False')
print(Gmodel == '18')

print('is magazine 9? i predict True')
print(magazine == 9)

print('is magazine 13? i predict False')
print(magazine == 13)

print('is caliber 9mm? i predict True')
print(Gcaliber == '9mm')

print('is caliber 12mm? i predict False')
print(Gcaliber == '12mm')
"""

# 5-3. Alien Colors #1:
"""Alien_color = input('Scegliere un colore: ')

if Alien_color == 'Verde':
    print('hai fatto 5 punti')
"""

# 5-4. Alien Colors #2:
"""Alien_color = input('Choose a color: ')
if Alien_color == 'Green':
    print('Hai guadagnato 5 punti')
else:
    print('hai appena guadagnato 10 punti')
"""

# 5-5. Alien Colors #3:
"""Alien_color = input('Choose a color: ')
if Alien_color == 'Green':
    print('you earned 5 points')
elif Alien_color == 'Red':
    print('You killed a red one, 50 points earned')
else:
    print('You earned 10 points for the special kill')
"""

# 5-6. Stages of Life:
"""age = 25
if age < 2:
    print("the person is a baby")
elif age < 4:
    print("the person is a toddler")
elif age < 13:
    print("the person is a kid")
elif age < 20:
    print("the person is a teenager")
elif age < 65:
    print("the person is an adult")
else:
    print("the person is an elder")
"""

# 5-7. Favorite Fruit:
"""favorite_fruits = ['Apple', 'Banana', 'Orange']

if 'Apple' in favorite_fruits:
    print("You really like Apples!")
if 'Grape' in favorite_fruits:
    print("You really like Grapes!")
if 'Banana' in favorite_fruits:
    print("You really like Bananas!")
if 'Pineapple' in favorite_fruits:
    print("You really like Pineapples!")
if 'Orange' in favorite_fruits:
    print("You really like Oranges!")
"""

#5-8. Hello Admin:
"""
usernames: list = ['Admin','Alpha1','Bravo2']

if 'Admin' in usernames:
    print('Hello admin, would you like to see a status report?')
elif 'Alpha1' in usernames:
    print('Hi Alpha1, Thanks for logging in')
elif 'Bravo2' in usernames:
    print('Hi Bravo2, Thanks for logging in')
"""
#5-9. No Users:
"""
usernames: list = []

if not usernames:
    print('We need to find some users!')
"""

#5-10. Checking Usernames:
"""
Current_users: list = ['Alpha','Bravo','Charlie','Delta','Echo']
New_users: list = ['Foxtrot','Gamma','Hotel','Alpha','Juliet']

for i,f in zip(Current_users,New_users):
    if i == f:
        print(f,'Username already exist, create a new one')
    else:
        print('Correct username')
Current_users_1: list = []

for h in New_users:
    curr: str = h.lower()
    Current_users_1.append(curr)
for i,f in zip(Current_users,Current_users_1):
    if i == f:
        print(f,'Username already exist, create a new one')
    else:
        print('Correct username')
"""

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""
Lista1_9= list(range(1, 10))
for number in Lista1_9:
    if number == 1:
        print(number,'st')
    elif number == 2:
        print(number,'nd')
    elif number == 3:
        print(number,'rd')
    else:
        print(number,'th')
"""