#!/usr/bin/env python3

import sys
import os
import csv
from warning import *
from tkinter import *

class RemoveLedgerPrompt(Toplevel):
    '''
    Creates a popup window that lets the user input the name of an open .csv ledger file
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
        self.title('Remove Ledger')

        # Sets size of the Toplevel
        self.geometry('500x200')

        # Sets the Toplevel as a transient of top
        self.transient(self.master)

        # Adds the textbox
        text1 = Label(self, text='Enter Name of Ledger:', padx = 5, pady = 5, width = 80, justify=LEFT)
        text1.pack(side=TOP)

        # Adds a box for user entry
        # self.entry1 = Entry(self, exportselection=0, width = 80)
        # self.entry1.pack(side=TOP)

        # Adds a dropdown menu
        values = tuple(self.master.ledger_handler.ledgerdict.keys())
        self.spinbox = Spinbox(self, values=values)
        self.spinbox.pack(side=TOP)

        # Adds a 'cancel' button to the lower left
        cancel = Button(self, text='Cancel', command=self.destroy)
        cancel.pack(side=LEFT)

        # Adds a 'remove' button to the lower right
        create = Button(self, text='Remove', command=self.remove_ledger)
        create.pack(side=RIGHT)

    def remove_ledger(self):
        '''
        Method called by the 'Remove' button on the transient prompt
        '''

        # new_ledger = str(self.entry1.get()) + '.csv'
        new_ledger = str(self.spinbox.get())
        if not new_ledger in self.master.ledger_handler.ledgerdict.keys():
            warning = Warning(self, 'ERROR!! \nNo such Ledger open')
        else:
            self.master.ledger_handler.close_ledger(new_ledger)
            self.master.panedwindow.new_entryview.update_entryview()
            self.destroy()
