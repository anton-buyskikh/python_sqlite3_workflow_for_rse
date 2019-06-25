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
                  colour text not null,
                  height real,
                  width real,
                  area real,
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



def select_from_table_where(db_filename,
                            conditions=None,
                            column_list=['*']):
  """ Return data from a table with conditions
  
  Inputs
  ------
  db_filename : str
    database filename
  conditions : dict
    dictionary with arguments OR None
  column_list : list of str
    columns, by default return all columns
    
  Outputs
  -------
  output : list
    raws with data 
  """
  if conditions != None:
    condition_pairs = build_condition_pairs(conditions)
  column_names = ', '.join(column_list) + ' '
  
  con = sqlite3.connect(db_filename)
  cur = con.cursor()
  
  if conditions == None:
    output = cur.execute('select ' + column_names +
                         'from geometric_shapes;').fetchall()
  else:
    output = cur.execute('select ' + column_names +
                         'from geometric_shapes ' +
                         'where ' + condition_pairs + ';').fetchall()
  con.close()
  return output



def build_condition_pairs(conditions):
  """ Return the list of parameter pairs in a form of strings
  
  Inputs
  ------
  conditions : dict
    dictionary with arguments
  
  Outputs
  -------
  condition_pairs : list of str
    parameter pairs in strings
  """
  condition_pairs = []
  for key in conditions.keys():
    if type(conditions[key]) == str:
      condition_pairs.append(key + '="' + conditions[key] + '"')
    else:
      condition_pairs.append(key + '=' + str(conditions[key]))
  condition_pairs = ' and '.join(condition_pairs)    
  
  return condition_pairs



def update_rectangle_area_where(db_filename,
                                conditions=None):
  """ Update are of rectangles with conditions
  
  Inputs
  ------
  db_filename : str
    database filename
  conditions : dict
    dictionary with arguments OR None
    
  Outputs
  -------
  None
  """
  if conditions != None:
    condition_pairs = build_condition_pairs(conditions)
  
  con = sqlite3.connect(db_filename)
  cur = con.cursor()
  if conditions == None:
    cur.execute('update geometric_shapes ' +
                'set area = height*width ' + 
                'where shape = "rectangle";')
  else:
    cur.execute('update geometric_shapes ' +
                'set area = height*width ' + 
                'where shape = "rectangle" and ' + condition_pairs + ';')
  con.commit()
  con.close()



def add_columns_to_geometric_shapes(db_filename,
                                    column_dict):
  """ Add columns in geometric_shapes.
  
    Inputs
  ------
  db_filename : str
    database filename
  column_dict : dict
    dictionary with columns names and types
    
  Outputs
  -------
  None
  """
  con = sqlite3.connect(db_filename)
  cur = con.cursor()
  for key in column_dict.keys():
    cur.execute('alter table geometric_shapes ' +
                'add ' + key + ' ' + column_dict[key] + ';')
  con.commit()
  con.close()
