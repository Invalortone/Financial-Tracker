# Imports the module for a warning message dialog.
from tkinter.messagebox import askyesno

# Links the function file with the branch file.
from function import *


# Defines the reset balance function
def resetBalance(balance, currentBalance, currency, sideMenu, main):

      # Gives a warning to you for confirmation.
      warning = askyesno(title='Confirmation', message='Are you sure that you want to reset?')

      # Detects if the warning's answer is yes.
      if warning:

        # Hides the side menu.
        sideMenu.place_forget()

        # Catches the chosen balance from the media folder.
        with open(r'ft-media/ft-balance.txt') as file:
           chosenBalance = str(file.readlines())

        # Removes unnecessary characters from the chosen balance.
        chosenBalance = chosenBalance.lstrip("['").rstrip("']")

        # Replaces the balances to zero.
        with open(r'ft-media/ft-balance.txt', 'w') as file:
          file.write(str(0.00))

        # Sets the balance to zero.
        balance.set(str(0.00))

        # Catches the chosen currency from the media folder.
        with open(r'ft-media/ft-currency.txt') as file:
           chosenCurrency = str(file.readlines())

        # Removes unnecessary characters from the chosen balance.
        chosenCurrency = chosenCurrency.lstrip("['").rstrip("']")

        # Replaces the currency to the default dollars.
        with open(r'ft-media/ft-currency.txt', 'w') as file:
          file.write("$")

        # Sets the currency to the default dollars.
        currency.set("$")

        # Refreshes the text to display the changes.
        currentBalance.config(text=str(balance.get()) + currency.get())

        # Goes back to home.
        main()

        # Detects if the user answers 'no'.
      else:

          # Hides the side menu.
          sideMenu.place_forget()

          # Goes back to home.
          main()
