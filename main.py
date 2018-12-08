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

        self.file_loc = file_loc
        self.transaction_list = []

        with open(file_loc, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.transaction_list.append(row)

    def __del__(self):

        with open(self.file_loc, 'w', newline='') as csv_file:
            csv.writer(csv_file)
            writer.writerows(self.transaction_list)

        del self.transaction_list
        del self.file_loc
        del self

ledger1 = Ledger('test.csv')
