#
# Part III: project expansion
# 1. add circles, triangles which have area and colour as well as rectangles,
#    but do not have height and width
# 2. 3 ways depending on YOUR project details:
#   - new database
#   - new table in the same database
#   - new features in the same table    (here we follow this path)
#

# %% libraries

import aux
import numpy as np

# %% add triangle edges

db_filename = 'tutorial.db'

column_dict = dict(edge1 = 'real',
                   edge2 = 'real',
                   edge3 = 'real')

aux.add_columns_to_geometric_shapes(db_filename, column_dict)

# ACTION: show new columns in sqlitebrowser

# NOTE: columns can be added in sqlitebrowser as well

# %% add circle radius

aux.add_columns_to_geometric_shapes(db_filename, dict(radius='real'))

# %% add some triangles

for edge1 in [1.0, 1.5]:
  for edge2 in [1.0, 1.5]:
    for edge3 in [1.0, 1.5]:
      p = (edge1 + edge2 + edge3)/2.0      
      for colour in ['blue', 'black', 'green', 'red']:
        data = dict(shape = 'triangle', 
                    edge1 = edge1, 
                    edge2 = edge2,
                    edge3 = edge3,
                    colour = colour,
                    area = np.sqrt(p * (p - edge1) * (p - edge2) * (p - edge3)),
                    datetime = datetime.datetime.now().__str__())
      
        aux.insert_into_geometric_shapes(db_filename, data)

# %% add some circles

for radius in [1.0, 1.5]:
  for colour in ['blue', 'black', 'green', 'red']:
    data = dict(shape = 'circle', 
                radius = radius,
                colour = colour,
                area = np.pi * radius**2,
                datetime = datetime.datetime.now().__str__())
  
    aux.insert_into_geometric_shapes(db_filename, data)

# ACTION: show new data in sqlitebrowser. work with filters.
