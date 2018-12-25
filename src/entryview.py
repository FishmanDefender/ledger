#!/usr/bin/env python3

import sys
import os
import csv
from warning import *
from tkinter import *
from newentry import *

class EntryView(Frame):
    '''
    Creates the entryview class, which will house all of the 'entry' objects.
    '''

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_entryview()
        print('Loaded Entryview')

    def init_entryview(self):
        '''
        Sets up the frame for the entryview
        '''

        self.current_ledger = self.master.master.current_ledger
        self.transaction_list = []


    def update_entryview(self):
        '''
        Updates the frame for the entryview
        '''

        self.current_ledger = self.master.master.current_ledger
        try:
            self.transaction_list = self.master.master.ledger_handler.ledgerdict[self.current_ledger].transaction_list
            self.draw()
        except:
            self.transaction_list = []
            self.draw()
            # warning = Warning(self, 'ERROR! \nCould Not Update EntryView')

    def draw(self):
        '''
        Draws the frame and all of the 'entry' elements
        '''
        for child in self.winfo_children():
            child.destroy()

        for entry in self.transaction_list:
            test_entry = NewEntry(self, entry)
            test_entry.pack(side=TOP)
