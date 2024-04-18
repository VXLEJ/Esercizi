# Valerio Gamba
# 17/04/2024

print("hello world")
print("\nNew exercise\n")
# 2-3. Personal Message: Use a variable to represent a person’s name
# and print a message to that person.
# Your message should be simple, such as
# “Hello Eric, would you like to learn some Python today?”

Name: str = "Tyler"
Message: str = f"Ciao {Name}, ti va di imparare un po di python insieme"
print(Message)

print("\nNew exercise\n")
# 2-4. Name Cases: Use a variable to represent a person’s name,
# and then print that person’s name in lowercase, uppercase, and title case.

print(str.lower(Name))
print(str.upper(Name))
print(str.title(Name))

print("\nNew exercise\n")
# 2-5. Famous Quote: Find a quote from a famous person you admire.
# Print the quote and the name of its author.
# Your output should look something like the following, including the quotation marks: Albert Einstein once said,
# “A person who never made a mistake never tried anything new.”

Famous: str = "Flavio Renato"
Frase: str = "SI VIS PACEM PARA BELLUM"

print("{} said \"{}\"".format(Famous,Frase))


# Il 2.6 è stato gia svolto nel 2.5 utilizzando un lo stesso metodo richiesto

print("\nNew exercise\n")
# 2-8. File Extensions: Python has a removesuffix()
# method that works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the file extension,
# like some file browsers do.

Filename: str = "Python_notes.txt"
print(Filename.removesuffix(".txt"))

print("\nNew exercise\n")
# 3-1. Names: Store the names of a few of your friends
# in a list called names.
# Print each person’s name by accessing each element
# in the list, one at a time.

Namelist: list = ["Leonardo","Daniele"]
for names in Namelist:
    print(names)

print("\nNew exercise\n")
# 3-2. Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, 
# print a message to them.
# The text of each message should be the same,
# but each message should be personalized with the person’s name.

messages: str = ("left the chat")
for names in Namelist:
    print("{}: {}".format(names,messages))

print("\nNew exercise\n")
# 3-3. Your Own List: Think of your favorite mode of transportation,
# such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items,
# such as “I would like to own a Honda motorcycle.”

Myownlist: list = ["Land Rover Defender","Assault helicopter","tank"]
TextEX: str = "i would like to own a"
for vehicles in Myownlist:
    print("{} {}".format(TextEX,vehicles))

print("\nNew exercise\n")
# 3-4. Guest List: If you could invite anyone,
# living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
dinnerguests: list = ["Steven Yeunn","Andrew Lincoln","Jeffrey Dean Morgan"]
invite = "Would like to eat with me?"

for guests in dinnerguests:
    print("Hey {} {}".format(guests,invite))

print("steven yeun") # for exercise n° 3.5
print("\nNew exercise\n")
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4.
# Add a print() call at the end of your program,
# stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest
# who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages,
# one for each person who is still in your list.

new_guest = "Norman Reedus"
dinnerguests.pop(0)
dinnerguests.append(new_guest)
for guests in dinnerguests:
    print("Hey {} {}".format(guests,invite))

print("\nNew exercise\n")
# 3-6. More Guests: You just found a bigger dinner table,
# so now more space is available.
# Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5.
# Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

new_guests: list = ["Melissa McBride","Christian Serratos","Seth Gillian","Chandler Riggs","John Bernthal"]

informing: str = "Just found a brand new table, it's bigger so more people are coming"
for guests in dinnerguests:
    print("Hey {} {}".format(guests,informing))


for i in new_guests:
    dinnerguests.append(i)

for guests in dinnerguests:
    print("Hey {} {}".format(guests,invite))

print("\nNew exercise\n")
# 3-7. Shrinking Guest List: You just found out that your new dinner
# table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

Deleted: str = dinnerguests.pop(1)
for i in range(5):
    #if dinnerguests != "Norman Reedus" and "Andrew Lincoln":
    #    print("Sorry {} you can't come anymore".format(guests))
    Deleted = dinnerguests.pop(2)
    print("sorry {} you can't come".format(Deleted))

print(dinnerguests)

print("\nNew exercise\n")
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

Travels: list = ["Nepal","Texas","Austria","Amsterdam","Canada"]
print(Travels)

Alphabetical_order = sorted(Travels)
print(Alphabetical_order)

Alphabetical_order.reverse()
print(Alphabetical_order)

print(Travels)

Travels.reverse()
print(Travels)

Travels.reverse()
print(Travels)

Travels.sort()
print(Travels)

Travels.sort(reverse=True)
print(Travels)


print("\nNew exercise\n")
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3,
# use len() to print a message indicating the number of people you’re inviting to dinner.

print(len(dinnerguests))

print("\nNew exercise\n")
# 3-10. Every Function: Think of things you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, languages,
# or anything else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

Guns: list = ["M4","TAQ-66","Kastov-762","M13B","FTAC-RECON","STB-556","LA-B-330","X12","X13-AUTO","P890","USP-45"]
print("This is the list\n",Guns,"\n")

for weapons in Guns:
    print(str.lower(weapons))
    print(str.upper(weapons))
    print(str.title(weapons))

print("\nFormat function\n")

for weapons in Guns:
    print("i would like to buy a {}".format(weapons))

print("\npop, append and len functions\n")

new_gun: str = "Beretta-M9"
Guns.append(new_gun)
print(Guns)

print("\nRemoving Beretta-M9...\n")
Guns.pop(11)
print(Guns)

print("\nSorted, sort and reverse functions\n")

Alphabetical_Guns = sorted(Guns)
print(Alphabetical_Guns)

print("\n Reversed \n")

Guns.reverse()
print(Guns)
print("\n sort \n")
Guns.reverse()

Guns.sort()
print(Guns)


print("\nNew exercise\n")
# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

Tyler = {"First name":"Tyler","Last name":"Rake","Age":"40","City":"Sidney"}
print(Tyler["First name"],Tyler["Last name"],Tyler["Age"],Tyler["City"])


print("\nNew exercise\n")
#