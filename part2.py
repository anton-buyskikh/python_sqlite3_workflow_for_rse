#
# Part II: data update 
# 1. select data from a table
# 2. update a table
#

# %% libraries

import aux

# %% retrive data

db_filename = 'tutorial.db'

conditions = dict(shape = 'rectangle')
column_list = ['colour', 'height', 'width', 'area']

output = aux.select_from_table_where(db_filename,
                                     conditions,
                                     column_list)
print(column_list)
print(*output, sep='\n')

# NOTE: area is not filled

# NOTE: SQLAlchemy allowes you to have more flexibility

# %% update the table with data for area

aux.update_rectangle_area_where(db_filename, dict(colour = 'green'))

output = aux.select_from_table_where(db_filename,
                                     conditions,
                                     column_list)

print(column_list)
print(*output, sep='\n')

# %% update the rest

aux.update_rectangle_area_where(db_filename)

output = aux.select_from_table_where(db_filename,
                                     conditions,
                                     column_list)

print(column_list)
print(*output, sep='\n')
