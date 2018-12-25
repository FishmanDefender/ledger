#!/usr/bin/env python3

import sys
import os
import csv
from warning import *
from tkinter import *
from entryview import *

class NewPanedWindow(PanedWindow):
    '''
    Creates the toplevel paned window class that will serve as the master of all internal classes
    '''

    def __init__(self, master=None):
        PanedWindow.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.init_window()
        self.add_entryview()

    def init_window(self):
        '''
        Sets up the look and layout of the paned window
        '''

        self.borderwidth = 10

    def add_entryview(self):
        '''
        Creates new Frame to hold all the ledger entries
        '''

        # self.ledgerview = Frame(self)
        # self.ledgerview.pack(side=LEFT)
        # testbutton = Button(self.ledgerview, text='test', fg='red')
        # testbutton.pack(side=LEFT)

        self.new_entryview = EntryView(self)
        self.add(self.new_entryview)
