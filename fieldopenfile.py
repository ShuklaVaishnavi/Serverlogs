import pandas as pd

# Open the file and read its contents
with open('test.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.strip().split('\n')

# Create a list of lists to store the data
data_list = []
for line in lines:
    fields = line.split()
    # Exclude the '$' symbol
    data_list.append([field for field in fields if field != '$'])

# Get the number of columns
num_cols = len(data_list[0])

# Create a list of column names
column_names = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11']

# Reshape the data_list to have a consistent number of columns
data_list = [fields[:num_cols] for fields in data_list]

# Create a new DataFrame with the data_list and column names
df = pd.DataFrame(data_list, columns=column_names[:num_cols])

# Print the DataFrame
print(df)

