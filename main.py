#!/usr/bin/env python3
import sys
import os
from ledger import *

#########################################################
#
#   Description: Main module. This is where all calls to ledgers will be made.
#
#########################################################

ledger1 = Ledger('test.csv')
print(ledger1.transaction_list)
ledger1.write()
