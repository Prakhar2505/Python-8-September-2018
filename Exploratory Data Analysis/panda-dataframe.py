import pandas as pd

raw_data = { 'Name': ['Arshad', 'Mohit', 'Kunal', 'Sneha', 'Nidhi', 'Avijit', 'Piyush'],
             'College': ['ITG', 'BKIT', 'DIT', 'GEHU','ITG', 'BKIT', 'DIT'],
             'Address': ['Dehradun', 'Delhi', 'Nainital', 'Dehradun', 'Delhi', 'Nainital', 'Nainital'],
             'Fees': [8000, 7000, 8500, 7500, 8000, 7000, 8500]
            }

dataFrame = pd.DataFrame(data = raw_data)
# print(dataFrame)
print(dataFrame['Fees'])