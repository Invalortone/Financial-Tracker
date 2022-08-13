# Imports modules needed to create a software and design it, (Tkinter).
import tkinter as lk
from tkinter.font import Font

# Links the function file with the branch file.
from function import *


# Defines the increase balance function.
def decreaseBalance(body, balance, currentBalance, main, currency):
    
    # Removes the widgets inside the body.
    for widget in body.winfo_children():
      widget.place_forget()

    # Creates the subtrahend Float
    # (Entry that only accepts float/int types) Entry.
    subtrahend = FloatEntry(body)
    subtrahend['font'] = Font(family="Roboto Condensed", size="30", weight="bold")
    subtrahend.place(x=350, y=75, width=100)

    # Defines the submit subtrahend function
    def submitSubtrahend():

        # Catches the chosen balance from the media folder.
        with open(r'ft-media/ft-balance.txt') as file:
           chosenBalance = str(file.readlines())
        
        # Removes unnecessary characters.
        chosenBalance = chosenBalance.lstrip("['").rstrip("']")

        # Gets the difference of the balance from the media folder(chosenBalance)
        # and the subtrahend entry.
        difference = float(chosenBalance[0:]) - float(subtrahend.get())
        
        # Sets the file's contents as the balance.
        balance.set(str(difference))
        
        # Changes the balance from the media folder.
        with open(r'ft-media/ft-balance.txt', 'w') as file:
          file.write(str(difference))

        # Refreshes the text to display the changes.
        currentBalance.config(text=str(balance.get()) + currency.get())

        # Deletes the entry content after submission.
        subtrahend.delete(0, 'end')

    # Defines the back to home function.
    def decreaseBalanceFunction():

       # Removes the widgets inside the body.
      for widget in body.winfo_children():
        widget.place_forget()

      # Executes the main function.
      main()

    # Creates the submit subtrahend button.
    submitSubtrahend = lk.Button(body, text="Submit", bd=0, fg="#ffffff", bg="#242424", command=submitSubtrahend)
    submitSubtrahend['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    submitSubtrahend.place(x=350, y=175)

    # Binds the submit subtrahend button with the hover effect.
    submitSubtrahend.bind('<Enter>', bodyEntry)
    submitSubtrahend.bind('<Leave>', bodyExit)

    # Creates the back to home page.
    backToHome = lk.Button(body, text="Back", bd=0, fg="#ffffff", bg="#242424", command=decreaseBalanceFunction)
    backToHome['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    backToHome.place(x=700, y=275)

    # Binds the backToHome button with a hover effect.
    backToHome.bind('<Enter>', bodyEntry)
    backToHome.bind('<Leave>', bodyExit)
