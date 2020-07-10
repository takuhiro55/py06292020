#!/usr/bin/env python3

import sqlite3

# following command will create db if t does not exist
# Otherwise, it will open
conn = sqlite3.connect('test.db')
print("Opened database successfully")


