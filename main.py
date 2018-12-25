#!/usr/bin/env python3
import sys
import os
from ledger import *
from tkinter import * # This is insecure import! Modify if conflicts arise!
sys.path.append('./src')


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
        self.init_window()
        self.add_ledgerview()

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

    def add_ledgerview(self):
        '''
        Creates new Frame to hold all the ledger entries
        '''

        self.ledgerview = Frame(self)
        self.ledgerview.pack(side=LEFT)
        testbutton = Button(self.ledgerview, text='test', fg='red')
        testbutton.pack(side=LEFT)

    def client_exit(self):
        '''
        A basic exit command
        '''
        exit()

ledger1 = Ledger('test.csv')
# print(ledger1.transaction_list) #Used in debugging
# ledger1.write()

root = Tk()         # Declaring Tkinter root

# Setting size of main window
root.geometry('1200x800')

top  = Window(root) # Declaring the root Frame
root.mainloop()     # Running the Tkinter root mainloop
