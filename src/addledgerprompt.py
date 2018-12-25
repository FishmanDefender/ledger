#!/usr/bin/env python3

import sys
import os
import csv
from tkinter import *

class NewLedgerPrompt(Toplevel):
    '''
    Creates a popup window that lets the user input the name of a new .csv ledger file
    '''

    def __init__(self, master=None):
        Toplevel.__init__(self, master, bd=40)
        self.master = master
        self.init_ledgerprompt()

    def init_ledgerprompt(self):
        '''
        Builds the ledger popup window
        '''

        # TODO Make this window aggressive (take and keep focus [self.grab_set()])

        # Adds the title of the Toplevel
        self.title('Add Ledger')

        # Sets size of the Toplevel
        self.geometry('500x200')

        # Sets the Toplevel as a transient of top
        self.transient(self.master)

        # Adds the textbox
        text1 = Label(self, text='Enter new ledger name:', padx = 5, pady = 5, width = 80, justify=LEFT)
        text1.pack(side=TOP)

        # Adds a box for user entry
        self.entry1 = Entry(self, exportselection=0, width = 80)
        self.entry1.pack(side=TOP)

        # Adds a 'cancel' button to the lower left
        cancel = Button(self, text='Cancel', command=self.destroy)
        cancel.pack(side=LEFT)

        # Adds a 'create' button to the lower right
        create = Button(self, text='Create', command=self.add_ledger)
        create.pack(side=RIGHT)

    def add_ledger(self):
        '''
        Method called by the 'Create' button on the transient prompt
        '''

        new_ledger = str(self.entry1.get()) + '.csv'
        self.master.ledger_handler.open_ledger(new_ledger)
        if self.master.current_ledger == None:
            self.master.current_ledger = new_ledger
        self.master.panedwindow.new_entryview.update_entryview()
        self.destroy()
