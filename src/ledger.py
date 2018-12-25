#!/usr/bin/env python3

import sys
import os
import csv
from pathlib import Path

class Ledger(object):
    '''
    This ledger class holds all transactions to and from a single account.
    '''

    def __init__(self, iofile):
        '''
        Reads in a file passed as an argument in the 'Ledgers' subdirectory then creates the transaction_list.
        Modifying the transaction_list modifies the ledger.
        '''

        cwd = os.getcwd()
        ledger_dir = str(cwd) + '/Ledgers'
        file_loc = ledger_dir + '/' + str(iofile)
        file = Path(file_loc)

        if not file.is_file():
            f = open(file_loc,"w+")
            f.close()

        if not (iofile.endswith('.csv')):
            raise InputError('File is not a csv file!')

        # self.headers = ['Date', ' Account', ' Reference Number', ' Debit', ' Credit', ' Description']

        self.file_loc = file_loc
        self.transaction_list = []

        with open(file_loc, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                l = []
                for x in row:
                    x = x.strip()
                    try:
                        x = float(x)
                    except:
                        x = x
                    l.append(x)
                self.transaction_list.append(l)

    def write(self):
        '''
        Writes out the current ledger to its associated ledger file. This will overwrite previous versions of the ledger.
        '''

        with open(str(self.file_loc), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in self.transaction_list:
                i = 0
                nrow = []
                for x in row:
                    if i == 0:
                        nrow.append(str(x))
                        i = 1
                    else:
                        nrow.append((' ' + str(x)))
                writer.writerow(nrow)
