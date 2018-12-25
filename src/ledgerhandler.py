#!/usr/bin/env python3

import sys
import os
import csv
from ledger import *

class LedgerHandler(object):
    '''
    This creates a ledgerhandler, which keeps a list of all loaded ledgers.
    '''

    def __init__(self):
        self.ledgerdict = {}

    def open_ledger(self, ledger):
        '''
        Opens the ledger of the name 'ledger'
        '''

        new_ledger = Ledger(str(ledger))
        self.ledgerdict[str(ledger)] = new_ledger
        print('Added ' + str(ledger))

    def close_ledger(self, ledger):
        '''
        Closes ledger of name 'ledger'
        '''

        self.ledgerdict[str(ledger)].write()
        del self.ledgerdict[str(ledger)]
        print('Removed ' + str(ledger))
