#!/usr/bin/env python3

import sys
import os
import csv

class Ledger(object):

    """
    This ledger class holds all transactions to and from a single account.
    """

    def __init__(self, iofile):

        cwd = os.getcwd()
        ledger_dir = str(cwd) + '/Ledgers'
        file_loc = ledger_dir + '/' + str(iofile)

        if not (iofile.endswith('.csv')):
            raise InputError('File is not a csv file!')

        self.headers = ['Date', 'Account', 'Reference Number', 'Debit', 'Credit', 'Description'] #TODO Make this not hard-coded

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

        with open(str(self.file_loc), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            i = 0
            for row in self.transaction_list:
                if i == 0:
                    row = list((str(x)) for x in row)
                else:
                    row = list((' ' + str(x)) for x in row)
                i += 1
                writer.writerow(row)


ledger1 = Ledger('test.csv')
print(ledger1.transaction_list)
ledger1.write()
