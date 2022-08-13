# Imports modules needed to create a software and design it, (Tkinter).
import tkinter as lk
from tkinter.font import Font

# Links the function file with the branch file.
from function import *


# Defines the increase balance function.
def increaseBalance(body, balance, currentBalance, main, currency):
    
    # Removes the widgets inside the body.
    for widget in body.winfo_children():
      widget.place_forget()

    # Creates the addend Float
    # (Entry that only accepts float/int types) Entry.
    addend = FloatEntry(body)
    addend['font'] = Font(family="Roboto Condensed", size="30", weight="bold")
    addend.place(x=350, y=75, width=100)

    # Defines the submit addend function
    def submitAddend():

        # Catches the chosen balance from the media folder.
        with open(r'ft-media/ft-balance.txt') as file:
           chosenBalance = str(file.readlines())
        
        # Removes unnecessary characters.
        chosenBalance = chosenBalance.lstrip("['").rstrip("']")

        # Gets the sum of the balance from the media folder(chosenBalance)
        # and the addend entry.
        sum = float(chosenBalance[0:]) + float(addend.get())
        
        # Sets the file's contents as the balance.
        balance.set(str(sum))
        
        # Changes the balance from the media folder.
        with open(r'ft-media/ft-balance.txt', 'w') as file:
          file.write(str(sum))

        # Refreshes the text to display the changes.
        currentBalance.config(text=str(balance.get()) + currency.get())

        # Deletes the entry content after submission.
        addend.delete(0, 'end')

    # Defines the back to home function.
    def increaseBalanceFunction():

       # Removes the widgets inside the body.
      for widget in body.winfo_children():
        widget.place_forget()

      # Executes the main function.
      main()

    # Creates the submit addend button.
    submitAddend = lk.Button(body, text="Submit", bd=0, fg="#ffffff", bg="#242424", command=submitAddend)
    submitAddend['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    submitAddend.place(x=350, y=175)

    # Binds the submit addend button with the hover effect.
    submitAddend.bind('<Enter>', bodyEntry)
    submitAddend.bind('<Leave>', bodyExit)

    # Creates the back to home page.
    backToHome = lk.Button(body, text="Back", bd=0, fg="#ffffff", bg="#242424", command=increaseBalanceFunction)
    backToHome['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    backToHome.place(x=700, y=275)

    # Binds the backToHome button with a hover effect.
    backToHome.bind('<Enter>', bodyEntry)
    backToHome.bind('<Leave>', bodyExit)
