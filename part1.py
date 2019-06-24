#
# Part I of the tutorial: 
# 1. create a database 
# 2. create a table
# 3. insert data
#

# %% libraries

import sqlite3
import aux

# %% create a database with a table

db_filename = 'geometric_shapes.db'

aux.create_table()

# ACTION: show that the table is created in the termial

# %% add data in the table

data = dict(type='rectangle', height=1.0, width=1.0, colour='red')

aux.insert_into_table()

# ACTION: show that the data is in the table

# %% add more data

aux.insert_into_table()
aux.insert_into_table()

for height in [5.4, 3.7, 2.8]:
  for width in [0.5, 1.4, 3.6]:
    for colour in ['blue', 'black', 'grenn']:
      aux.insert_into_table()
      
# ACTION: show that the data is in the table
