# Imports modules needed to create a software and design it, (Tkinter).
import tkinter as lk


# Defines the hover effect for the 'Top Bar'.
def topBarEntry(e):
    e.widget['background'] = '#212126'
def topBarExit(e):
    e.widget['background'] = '#1d1d24'

# Defines the hover effect for the 'Body'.
def bodyEntry(e):
    e.widget['background'] = '#303030'
def bodyExit(e):
    e.widget['background'] = '#242424'

# Defines the hover effect for the 'Menu'.
def menuEntry(e):
    e.widget['background'] = '#212126'
def menuExit(e):
    e.widget['background'] = '#292930'

# Defines the class needed to 
# create an entry that only accepts float types.
class FloatEntry(lk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        vcmd = (self.register(self.validate),'%P')
        self.config(validate="all", validatecommand=vcmd)

    def validate(self, text):
        if (
            all(char in "0123456789.-" for char in text) and

            # all characters are valid
            "-" not in text[1:] and 
            
            # "-" is the first character or not present
            text.count(".") <= 1): 
            
            # only 0 or 1 periods
                return True
        else:
            return False

