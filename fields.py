import numpy as np
import pandas as pd

data = """270454.ANTYA   $ lucky.s $ serialq  xoopic_0.* 243403   1   1    --  360:0 R 48:35
270458.ANTYA   $ suruj.k $ mediumq  spot_k1.0*  76343   4   8    --  48:00 R 39:04
270459.ANTYA   $ suruj.k $ mediumq  spot_k4.0* 196850   4   8    --  48:00 R 38:56
270474.ANTYA   $ sagar.c $ mediumq  n16_non_l* 264967  48  15    --  48:00 R 26:45"""

# Split the data into lines
lines = data.strip().split('\n')

# Create a list of lists to store the data
data_list = []
for line in lines:
    fields = line.split()
    # Exclude the '$' symbol
    data_list.append([field for field in fields if field != '$'])

# Convert the data_list to a NumPy array
data_array = np.array(data_list)

# Get the number of columns
num_cols = data_array.shape[1]

# Create a list of column names
column_names = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11']

# Reshape the data_array to have 12 columns
data_array = data_array.reshape(-1, num_cols)

# Create a new DataFrame with the data_array and column names
df = pd.DataFrame(data=data_array, columns=column_names[:num_cols])

# Print the DataFrame
print(df)