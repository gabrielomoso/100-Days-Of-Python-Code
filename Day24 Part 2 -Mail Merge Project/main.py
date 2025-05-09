#This program creates letters for a list of names in a file



#Getting list of names to send the letter to
with open("Input/Names/invited_names.txt") as names:
    all_names = []  #Declaring an empty list
    file_names = names.readlines()  #The readlines() method reads each line and saves it as a list

    #This takes every name and removes the spaces
    for name in file_names:
        all_names.append(name.strip()) #The strip() method removes all spaces in a string


#Getting the letter i want to modify
with open("Input/Letters/starting_letter.txt") as data:
    letter = data.read()


#Using the list of names to modify the letter and create each letter for each name in a seperate folder
for name in all_names:
    new_letter = letter.replace("name", name)
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as data:
        data.write(new_letter)


