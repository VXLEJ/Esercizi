#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
"""
def display_message():
    print('In this chapter i am learning python functions')

display_message()
"""
#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book(Title:str):
    print(f'my favorite book is {Title}')
favorite_book('Covering Fire')
"""
#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size,message):
    print(f'the size of the shirt is {size} and the message is {message}')
make_shirt(12,'Highway to hell')
make_shirt(size=12,message='Highway to hell')
"""

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
def make_shirt(size='L',message = "i love python"):
    print(f'making a size: {size} of {message} shirts')
make_shirt()
make_shirt(size='M')
make_shirt(size='S',message='Different message')
"""

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
"""
def describe_city(name,country = 'California'):
    return f"{name}, {country}"

describe_city(name = 'Los Angeles')
describe_city(name = 'San Francisco')
describe_city(name = 'Roma',country = 'Italy')
"""
#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(name,country):
    return f"{city}, {country}"
a = city_country(name='Rio de Janiero',country=' Brasil') 
b = city_country(name='Barcelona',country=' Spain') 
c = city_country(name='Marseille',country=' France')
print(a,'\n',b,'\n',c) 
"""
#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
"""
def make_album(Artist,Album) -> dict:
    Music:dict = {Artist,Album}
    return Music

Alb01:dict = make_album('Mostro','Ogni maledetto giorno')
Alb02:dict = make_album('Salmo','Hellvisback')
Alb03:dict = make_album('Noyz Narcos','Enemy')

print(Alb01,'\n',Alb02,'\n',Alb03)
"""
"""
def make_album2(Artist2,Album2,Nsong = None) -> dict:
    Music2:dict = {'Artist: ': Artist2,'Album: ': Album2,'Songs: ': Nsong}
    return Music2

alb01:dict = make_album2('Mostro','Ogni maledetto giorno',10)
alb02:dict = make_album2('Salmo','Hellvisback',15)
alb03:dict = make_album2('Noyz Narcos','Enemy',7)

print(alb01,'\n',alb02,'\n',alb03)
"""
#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
"""
user: dict = {}

i = 1
while i<3:
    i+=1
    user = make_album2(Artist2=input('inserisci artista: '),Album2=input('inserisci album: '),Nsong=input('inserisci il numero di canzoni: '))
    print(user)
"""

#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
"""
Messages: list = ['Never give up','Just do it','Life is one']

def show_messages(l):
    for message in l:
        print(message)
show_messages(Messages)
"""
#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.







#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 

#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches: import module_name from module_name import function_name from module_name import function_name as fn import module_name as mn from module_name import *
#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section

# Funzione Bubble sort

def bubble_sort(v) -> list:
    v = [1,3,2,6,4,8,7,5]
    for i in range(len(v)):
        for j in range(len(v) - 1):
            if v[j] > v[j+1]:
                temp: int = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
    return v


v = [1,3,2,6,4,8,7,5]
print(bubble_sort(v))

def bubble_sort2():
    c = list(range(1000001,1))
    for i in range(len(c)):
        for j in range(len(c) - 1):
            if c[j] < c[j+1]:
                temp: int = c[j]
                c[j] = c[j+1]
                c[j+1] = temp
    return c

c = list(range(1000001,1))
print(bubble_sort2(c))