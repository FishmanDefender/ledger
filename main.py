#!/usr/bin/env python3
import sys
import os
from tkinter import * # This is insecure import! Modify if conflicts arise!
sys.path.append('./src')
from ledger import *
from ledgerhandler import *
from addledgerprompt import *
from removeledgerprompt import *
from newpanedwindow import *


#########################################################
#
#   Description: Main module. This is where all calls to ledgers will be made.
#
#########################################################

class Window(Frame):
    '''
    Copied from (https://pythonprogramming.net/python-3-tkinter-basics-tutorial/). Creates a Tkinter frame and sets its master as the
    class master.
    '''

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.current_ledger = None
        self.ledger_handler = LedgerHandler()
        self.init_window()
        self.init_panedwindow()

    def init_window(self):
        '''
        This initializes the window with things like Title, Packing Strategy, etc.
        '''

        # Sets the master widget title
        self.master.title('Michael\'s Ledger Manager')

        # Sets Packing Strategy to fill
        self.pack(fill=BOTH, expand=1)

        # Adds the top-level menue
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Adds a file object
        file = Menu(menu, tearoff=0)

        # Adds command to the menu option with the name 'exit'
        file.add_command(label='Exit', command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # Adds another file object
        edit = Menu(menu, tearoff=0)

        # adds another command, this one without a command
        edit.add_command(label='Undo')

        # added a file menu option
        menu.add_cascade(label='Edit', menu=edit)

        # Adds the 'Ledger' drop-down menu
        ledger_menu = Menu(menu, tearoff=0)
        ledger_menu.add_command(label='Open...', command=self.add_new_ledger)
        ledger_menu.add_command(label='Remove...', command=self.remove_ledger)
        menu.add_cascade(label='Ledger', menu=ledger_menu)

    def init_panedwindow(self):
        '''
        Creates the panedwindow class which will be used as the master for the ledgerview and entryview classes
        '''

        # Adds a NewPanedWindow as a child of Window
        self.panedwindow = NewPanedWindow(self)

    def client_exit(self):
        '''
        A basic exit command
        '''
        exit() # Exits the program

    def add_new_ledger(self):
        '''
        Method called by the 'New...' button under the 'Ledger' menu
        '''

        # Creates a NewLedgerPrompt class
        newprompt = NewLedgerPrompt(self)

    def remove_ledger(self):
        '''
        Method called by the 'Close...' button under the 'Ledger' menu
        '''

        # Creates a RemoveLedgerPrompt class
        newprompt = RemoveLedgerPrompt(self)



# ledger1 = Ledger('test.csv')
# print(ledger1.transaction_list) #Used in debugging
# ledger1.write()

root = Tk()         # Declaring Tkinter root

# Setting size of main window
root.geometry('1200x800')

top = Window(root)  # Declaring the root Frame
root.mainloop()     # Running the Tkinter root mainloop
