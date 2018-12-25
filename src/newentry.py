#!/usr/bin/env python3

import sys
import os
import csv
from warning import *
from tkinter import *

class NewEntry(Frame):
    '''
    This entry class prints all of the information in proper format from the passed ledger entry
    '''

    def __init__(self, master=None, entry=None):
        Frame.__init__(self, master)
        self.master = master
        if entry == None:
            self.entry = []
        elif not isinstance(entry, list):
            warning = Warning('ERROR! \nEntry was not a List!')
        else:
            self.entry = entry
        self.build_entry()

    def build_entry(self):
        '''
        Constructs the Tkinter-formatted entry
        '''

        # Adds a Label list
        label_list = []

        for elem in self.entry:
            label_list.append(Label(self, text=str(elem)))

        for i in range(len(self.entry)):
            label_list[i].pack(side=LEFT)
