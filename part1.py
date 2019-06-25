#
# Part I of the tutorial: 
# 1. create a database 
# 2. create a table
# 3. insert data
#

# %% libraries

import aux
import datetime

# %% create a database with a table

db_filename = 'tutorial.db'

aux.create_table_geometric_shapes(db_filename)

# ACTION: show that the table is created via termial
# $ sqlitebrowser tutorial.db

# %% add data in the table

data = dict(shape='rectangle', 
            height=1.0, 
            width=1.0, 
            colour='red',
            datetime=datetime.datetime.now().__str__())

aux.insert_into_geometric_shapes(db_filename, data)

# ACTION: show that the data is in the table

# %% add more data

for height in [5.4, 3.7, 2.8]:
  for width in [0.5, 1.4, 3.6]:
    for colour in ['blue', 'black', 'green']:
      data = dict(shape='rectangle', 
                  height=height, 
                  width=width, 
                  colour=colour,
                  datetime=datetime.datetime.now().__str__())
      
      aux.insert_into_geometric_shapes(db_filename, data)
      
# ACTION: show that the data is in the table
