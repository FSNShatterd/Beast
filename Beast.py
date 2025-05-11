print("Hello! My name is Beast.\n")
name = input("What is your name? ")

print("Nice to meet you " + name + "\n")

list1 = ['Roger', 'Dave', 'Mica', 'Arthur', 'Dutch']
list2 = ['Apples', 'Banannas', 'Pears', 'Grapes', 'Blueberrys']
list3 = ['China', 'United States', 'Russia', 'Iraq', 'Brazil']

print("Which list would you like?\n")

print("list1, list2, list3") 

choice = input()
if choice == "list1":
    print(list1)
    
    person =input("Which person did you need?\n")
    
    print("Ok i will send in " + person +"\n")
    
    list1.append(input("Would you like to add anything to the list. If so type it here.\n"))
    
    print(list1)
    
    exit()
elif choice == "list2":             # If making stuff like this make sure it is like this blank == "blank" 
    
    print(list2)
    
    item = input("Which one of these items did you need?\n")
    
    quantity = input("How many would you like?\n")
    
    print("Ok so you wanted " + quantity + " " + item + ".")
    
    list2.append(input("Would you like to add anything to the list. If so type it here.\n"))
    print(list2)
    exit()
elif choice == "list3":
    
    print(list3)
    
    country= input("Which country are you needing to go to? \n")
    
    print("Ok i will set up the flight too " + country)
    
    list3.append(input("Would you like to add anything to the list. If so type it here.\n"))
    print(list3)
    exit()
else:
    
    print("Thats not a choice.\n")
    
    print("You need to leave!")
    
    exit()

