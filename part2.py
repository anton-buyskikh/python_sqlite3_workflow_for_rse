#
# Part II: data update 
# 1. select data from a table
# 2. update a table
#

# %% libraries

import aux

# %% retrive data

db_filename = 'tutorial.db'

conditions = dict(shape='rectangle',
                  colour='green')

output = aux.select_from_table_where(db_filename,
                                     conditions,
                                     column_list=['height', 'width', 'area'])

print(*output, sep='\n')

# NOTE: area is not filled

# %% update the table
