# Imports modules needed to create a software and design it, (Tkinter).
import tkinter as lk
from tkinter.font import Font
from tkinter import ttk

# Links the function file with the branch file.
from function import *


# Defines the choose currency functions.
# Catches objects from the main file as parameters.
def chooseCurrency(body, currency, sideMenu, main, currentBalance, balance):

    # Removes the widgets inside the body and the side menu.
    for widget in body.winfo_children():
      widget.place_forget()
    sideMenu.place_forget()

    # Defines the variable used to catch the answer of the dropdown.
    dropdownAnswer = lk.StringVar()

    # Sets the default dropdown answer as the 'US Dollar ($)'.
    dropdownAnswer.set("US Dollar ($)")

    # Composes the 'Dropdown Menu' widget and
    # removes unnecessary highlighting.
    currencyDropdown = ttk.Combobox(body, textvariable=dropdownAnswer)
    currencyDropdown['values'] = ["US Dollar ($)", "UK Pound (£)", "Japan Yen (¥)", "Euro (€)"]
    currencyDropdown['state'] = 'readonly'
    currencyDropdown['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    currencyDropdown.place(x=280, y=70, width=250)
    currencyDropdown.bind("<<ComboboxSelected>>", lambda e: emptyHighlight.focus())

    # Defines the function for the submit button.
    def currencySubmit():

      # Checks if the dropdown answer is 
      # a value from the dropdown options.
      if dropdownAnswer.get() == "US Dollar ($)":

        # Finds the currency from the media folder.
        with open(r'ft-media/ft-currency.txt') as file:
           chosenCurrency = str(file.readlines())
        
        # Removes unnecessary characters and 
        # sets the file's contents as the currency.
        chosenCurrency = chosenCurrency.lstrip("['").rstrip("']")
        currency.set("$")

        # Changes the currency from the media folder.
        with open(r'ft-media/ft-currency.txt', 'w') as file:
          file.write("$")

        # Refreshes the text to display the changes.
        currentBalance.config(text=balance.get() + str(currency.get()))

      elif dropdownAnswer.get() == "UK Pound (£)":

        # Finds the currency from the media folder.
        with open(r'ft-media/ft-currency.txt') as file:
           chosenCurrency = str(file.readlines())
        
        # Removes unnecessary characters and 
        # sets the file's contents as the currency.
        chosenCurrency = chosenCurrency.lstrip("['").rstrip("']")
        currency.set("£")

        # Changes the currency from the media folder.
        with open(r'ft-media/ft-currency.txt', 'w') as file:
          file.write("£")

        # Refreshes the text to display the changes.
        currentBalance.config(text=balance.get() + str(currency.get()))

      elif dropdownAnswer.get() == "Japan Yen (¥)":

        # Finds the currency from the media folder.
        with open(r'ft-media/ft-currency.txt') as file:
           chosenCurrency = str(file.readlines())
        
        # Removes unnecessary characters and 
        # sets the file's contents as the currency.
        chosenCurrency = chosenCurrency.lstrip("['").rstrip("']")
        currency.set("¥")

        # Changes the currency from the media folder.
        with open(r'ft-media/ft-currency.txt', 'w') as file:
          file.write("¥")

        # Refreshes the text to display the changes.
        currentBalance.config(text=balance.get() + str(currency.get()))

      elif dropdownAnswer.get() == "Euro (€)":

        # Finds the currency from the media folder.
        with open(r'ft-media/ft-currency.txt') as file:
           chosenCurrency = str(file.readlines())
        
        # Removes unnecessary characters and 
        # sets the file's contents as the currency.
        chosenCurrency = chosenCurrency.lstrip("['").rstrip("']")
        currency.set("€")

        # Changes the currency from the media folder.
        with open(r'ft-media/ft-currency.txt', 'w') as file:
          file.write("€")

        # Refreshes the text to display the changes.
        currentBalance.config(text=balance.get() + str(currency.get()))

      # Gives the default value for the currency
      else:

        # Finds the currency from the media folder.
        with open(r'ft-media/ft-currency.txt') as file:
           chosenCurrency = str(file.readlines())

        # Removes unnecessary characters and
        # sets the file's contents as the currency.
        chosenCurrency = chosenCurrency.lstrip("['").rstrip("']")
        currency.set("$")
        
        # Changes the currency from the media folder.
        with open(r'ft-media/ft-currency.txt', 'w') as file:
          file.write("$")

        # Refreshes the text to display the changes.
        currentBalance.config(text=balance.get() + str(currency.get()))

    # Defines the back to home function
    def chooseCurrencyPage():

      # Removes the widgets inside the body.
      for widget in body.winfo_children():
        widget.place_forget()

      # Executes the main function.
      main()

    # Creates an empty label to switch the highlighting to.
    emptyHighlight = lk.Label(body, text="", bg="#242424")
    emptyHighlight.pack()

    # Creates the submit currency button.
    submitCurrency = lk.Button(body, text="Submit", bd=0, fg="#ffffff", bg="#242424", command=currencySubmit)
    submitCurrency['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    submitCurrency.place(x=350, y=175)

    # Gives the button a hover effect.
    submitCurrency.bind('<Enter>', bodyEntry)
    submitCurrency.bind('<Leave>', bodyExit)

    # Creates the back to home button.
    backToHome = lk.Button(body, text="Back", bd=0, fg="#ffffff", bg="#242424", command=chooseCurrencyPage)
    backToHome['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
    backToHome.place(x=700, y=275)

    # Gives the button a hover effect.
    backToHome.bind('<Enter>', bodyEntry)
    backToHome.bind('<Leave>', bodyExit)


