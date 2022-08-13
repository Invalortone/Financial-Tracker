# Imports modules needed to create a software and design it, (Tkinter).
import tkinter as lk
from tkinter.font import Font

# Imports module needed to open links.
import webbrowser

# Links the branch files with the main file.
from function import *
from branch.increaseFunction import *
from branch.decreaseFunction import *
from branch.changeCurrency import *
from branch.resetFunction import *


# Creates the main window and its dimensions.
win = lk.Tk()
win.configure(width="1000", height="650", background="#303136")
win.title("Financial Tracker")
win.resizable(False, False)

# Adds the main window's icon.
win.iconbitmap(r"ft-media/icon.ico/")

# Defines the String Variables to show the current balance.
balance = lk.StringVar()
currency = lk.StringVar()

# Finds the currency from the media folder.
with open(r'ft-media/ft-currency.txt') as file:
    chosenCurrency = str(file.readlines())

# Removes unnecessary characters and 
# sets the file's contents as the currency.
chosenCurrency = chosenCurrency.lstrip('[\'').rstrip(']\'')
currency.set(chosenCurrency)

# Finds the balance from the media folder.
with open(r'ft-media/ft-balance.txt') as file:
    cash = str(file.readlines())

# Removes unnecessary characters and
# sets the file's contents to the balance.
cash = cash.lstrip('[\'').rstrip(']\'')
balance.set(cash)

# Defines the top bar as a frame and designs it.
topBar = lk.Frame(win, background="#1d1d24")
topBar.place(x=100, y=50, width=800, height=75)

# Creates the title for the window and defines its font.
heading = lk.Label(topBar, text="Finance Tracker", bg="#1d1d24", fg="#e2e2e2")
heading['font'] = Font(family="Roboto Condensed", size="20", weight="normal")
heading.place(x=30, y=20)

# Creates the frame shown behind the balance.
balanceFrame = lk.Frame(win, background="#202020", bd=5)
balanceFrame.place(x=100, y=135, width=800, height=125)

# Creates the header defined for the balance and its font.
balanceHeader = lk.Label(balanceFrame, text="Balance : ", bg="#202020", fg="#e2e2e2")
balanceHeader['font'] = Font(family="Roboto Condensed", size="30", weight="bold")
balanceHeader.place(x=265, y=35)

# Displays the current balance from the ft-media folder. 
currentBalance = lk.Label(balanceFrame, text=balance.get() + currency.get(), bg="#202020", fg="#e2e2e2")
currentBalance['font'] = Font(family="Roboto Condensed", size="30", weight="bold")
currentBalance.place(x=425, y=35)

# Defines the main page function. 
def main():

    # Creates the main body frame.
    body = lk.Frame(win, background="#242424")
    body.place(x=100, y=260, width=800, height=350)

    # Creates the menu button and its font.
    menuButton = lk.Button(topBar, text="☰", fg="#e2e2e2", bg="#1d1d24", bd=0, cursor="hand2", command= lambda: menu(menuButton))
    menuButton['font'] = Font(family="MS Sans Serif", size="20", weight="normal")
    menuButton.place(x=725, y=0, width=75, height=75)

    # Binds the menu button with a hover effect.
    menuButton.bind('<Enter>', topBarEntry)
    menuButton.bind('<Leave>', topBarExit)

    # Creates the button to increase your balance.
    gainButton = lk.Button(body, text="Gain", bd=0, fg="#ffffff", bg="#242424", cursor="hand2", command= lambda: increaseBalance(body, balance, currentBalance, main, currency))
    gainButton['font'] = Font(family="Roboto Condensed", size="30", weight="bold")
    gainButton.place(x=50, y=150, width=175)

    # Binds the gain button with a hover effect.
    gainButton.bind('<Enter>', bodyEntry)
    gainButton.bind('<Leave>', bodyExit)
    
    # Creates the button to decrease your balance.
    lossButton = lk.Button(body, text="Loss", bd=0, fg="#ffffff", bg="#242424", cursor="hand2", command= lambda: decreaseBalance(body, balance, currentBalance, main, currency))
    lossButton['font'] = Font(family="Roboto Condensed", size="30", weight="bold")
    lossButton.place(x=575, y=150, width=175)

    # Binds the loss button with a hover effect.
    lossButton.bind('<Enter>', bodyEntry)
    lossButton.bind('<Leave>', bodyExit)

    # Defines the side menu function 
    # that displays after pressing the menu button.
    def menu(self):

        # Disables the menu button to avoid duplicate menus.
        self["state"] = "disabled"

        # Removes the hover effect on the menu button.
        self.unbind('<Enter>')
        self.config(cursor="arrow")
    
        # Displays the side menu as a frame.
        sideMenu = lk.Frame(win, background="#292930")
        sideMenu.place(x=000, y=0 , width=200, height=650)

        # Creates the side menu's header.
        menuHeader = lk.Label(sideMenu, text="MENU", bg="#292930", fg="#ffffff")
        menuHeader['font'] = Font(family="Roboto Condensed", size="20", weight="bold")
        menuHeader.place(x=60, y=20)
    
        # Defines the exit menu function.
        def exitMenu():

            # Removes the widgets inside the sideMenu and its self.
            for widget in sideMenu.winfo_children():
                widget.place_forget()
            sideMenu.place_forget()

            # Enables the menu button.
            self["state"] = "normal"

            # Gives the menu button its hovering effect back.
            self.bind('<Enter>', menuEntry)
            self.config(cursor="hand2")

        # Creates the exit button to close the menu.
        exitMenuButton = lk.Button(sideMenu, text="✖", bd=0, fg="#ffffff", bg="#292930", cursor="hand2", command=exitMenu)
        exitMenuButton['font'] = Font(family="Roboto Condensed", size="10", weight="bold")
        exitMenuButton.place(x=150, y=0, width=50, height=50)

        # Creates the menu option "Currency" 
        # that is linked with the currencyFunction branch file.
        buttonCurrency = lk.Button(sideMenu, text="CURRENCY", bd=0, fg="#ffffff", bg="#292930", cursor="hand2", command= lambda: chooseCurrency(body, currency, sideMenu, main, currentBalance, balance))
        buttonCurrency['font'] = Font(family="Roboto Condensed", size="15", weight="bold")
        buttonCurrency.place(x=0, y=150, width=200, height=50)

        # Adds the hover effect with the currency button.
        buttonCurrency.bind('<Enter>', menuEntry)
        buttonCurrency.bind('<Leave>', menuExit)

        # Creates the menu option "Github Page" to open invalortone's page.
        githubLink = lk.Button(sideMenu, text="GITHUB PAGE", bd=0, fg="#ffffff", bg="#292930", cursor="hand2", command= lambda: webbrowser.open("https://github.com/Invalortone",new=1))
        githubLink['font'] = Font(family="Roboto Condensed", size="15", weight="bold")
        githubLink.place(x=0, y=250, width=200, height=50)

        # Adds the hover effect with the github page button.
        githubLink.bind('<Enter>', menuEntry)
        githubLink.bind('<Leave>', menuExit)

        # Creates the menu option "Reset" that resets the balance and currency.
        resetButton = lk.Button(sideMenu, text="RESET", bd=0, fg="#ffffff", bg="#292930", cursor="hand2", command= lambda: resetBalance(balance, currentBalance, currency, sideMenu, main))
        resetButton['font'] = Font(family="Roboto Condensed", size="15", weight="bold")
        resetButton.place(x=0, y=200, width=200, height=50)

        # Adds the hover effect with the reset Button.
        resetButton.bind('<Enter>', menuEntry)
        resetButton.bind('<Leave>', menuExit)

# Displays the main page when the program is run.
main()

# Displays the window.
win.mainloop()
