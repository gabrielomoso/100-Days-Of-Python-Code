#TODO 1. Creating a dictionary from the data in the nato file

import pandas  #Importing the pandas module

nato = pandas.read_csv("nato_phonetic_alphabets.csv") #Saving the data from the file into the variable nato

#The iterrows() from the pandas module seperates the indexs from the actual data
#Now we seperate them using a turple format of (index, row)
#Then we tap into the attributes of each row by using the name of the column in the file
#Then save them as a dictionary in the variable nato_dict...... All this done in one line of code😏
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name: ").upper() #Getting the user input and saving it as uppercase

code = [nato_dict[key] for key in name] #Using each letter of the name to get the value from our nato_dict and appending into the code as a list
print(code) #Printing the results
