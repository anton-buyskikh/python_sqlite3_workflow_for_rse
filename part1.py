#
# Part I: data collection 
# 1. create a database 
# 2. create a table
# 3. insert data
#

# %% libraries

import aux
import datetime

# ACTION: show the content of aux

# %% create a database with a table

db_filename = 'tutorial.db'

aux.create_table_geometric_shapes(db_filename)

# ACTION: show that the table is created via termial
# $ sqlitebrowser tutorial.db

# %% add data in the table

data = dict(shape = 'rectangle', 
            height = 1.0, 
            width = 1.0, 
            colour = 'red',
            datetime = datetime.datetime.now().__str__())

aux.insert_into_geometric_shapes(db_filename, data)

# ACTION: show that the data is in the table

# NOTE:  datetime or commit hash is useful in combination with git so as to
# match each data entry with the software version

# %% add more data

for height in [2.8, 3.7, 5.4]:
  for width in [0.5, 1.4, 3.6]:
    for colour in ['blue', 'black', 'green']:
      data = dict(shape = 'rectangle', 
                  height = height, 
                  width = width, 
                  colour = colour,
                  datetime = datetime.datetime.now().__str__())
      
      aux.insert_into_geometric_shapes(db_filename, data)
      
# ACTION: show that the data is in the table. show basic filters
