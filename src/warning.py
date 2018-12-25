#!/usr/bin/env python3

import sys
import os
import csv
from tkinter import *
from tkinter import messagebox

class Warning():
    '''
    A warning popup box with text as an argument.
    '''

    def __init__(self, master=None, text=None):
        self.message = str(text)
        self.init_warning()

    def init_warning(self):
        '''
        Builds the warning box
        '''

        messagebox.showerror('Ledger Error', self.message)
