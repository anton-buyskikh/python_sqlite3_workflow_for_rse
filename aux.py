#
# This module has auxiliary functions for work with SQL databases. 
# Please refer to SQLAlchemy for more professional solutions.
#

# %% libraries

import sqlite3

# %% functions

def create_table_geometric_shapes(db_filename):
  """ Create geometric_shapes table.
  
  Inputs
  ------
  db_filename : str
    database filename
    
  Outputs
  -------
  None
  """  
  con = sqlite3.connect(db_filename)
  cur = con.cursor()
  cur.execute(""" create table if not exists geometric_shapes(
                  shape text not null,
                  height real,
                  width real,
                  colour text not null,
                  datetime text not null); """)
  con.commit()
  con.close()
  print(db_filename, 'database and geometric_shapes table are created')



def insert_into_geometric_shapes(db_filename, data):
  """ Insert data into geometric_shapes table.
  
  Inputs
  ------
  db_filename : str
    database filename
  data : dict
    data dictionary 
    
  Outputs
  -------
  None
  """
  con = sqlite3.connect(db_filename)
  cur = con.cursor()
  cur.execute('insert into geometric_shapes(' + ', '.join(data.keys()) + ') ' + 
              'values(' + ', '.join('?'*len(data)) + ');',
              [data[k] for k in data.keys()])
  con.commit()
  con.close()
  print('Data saved geometric_shapes table in', db_filename, 'database')



def select_from_table():
  """ Seletc data from a table.
  """
  pass



def add_column():
  """ Add column in a table.
  """
  pass
