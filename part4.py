#
# Part IV: visualisation 
# 1. plot a histogram example
#

# %% libraries

import aux
import matplotlib.pyplot as plt
import numpy as np

# %% plot histogram

# obtain data
output = aux.select_from_table_where(db_filename='tutorial.db',
                                     conditions=None,
                                     column_list=['area'])

# transform to np.array for convenience
output = np.array(output)

plt.hist(output)
plt.xlabel('area')
plt.ylabel('count')
plt.show()

# NOTE: pandas.read_sql + SQLALchemy provide a more professional solution 
# for visulalization