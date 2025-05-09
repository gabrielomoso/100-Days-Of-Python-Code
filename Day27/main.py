from tkinter import * #This line imports all the classes in the tkinter module

font = ("Arial", 18)

#Setting up the GUI window
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

#Setting the entry box
entry = Entry(width=10)
entry.grid(row=0, column=1)

#Setting up the Labels
miles = Label(text="Miles", font=font)
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to", font=font)
is_equal_to.grid(row=1, column=0)

answer = Label(text=0, font=font)
answer.grid(row=1, column=1)

km = Label(text="Km", font=font)
km.grid(row=1, column=2)



def calculate_button():
    """This function calculates and shows the KM per miles"""
    answer.config(text=round(float(entry.get()) * 1.609))


#Setting up the button
calculate = Button(text="Calculate", command=calculate_button) #The command attribute calls the calculate_button function when the button is clicked
calculate.grid(row=2, column=1)



window.mainloop() #This keeps the window on the screen