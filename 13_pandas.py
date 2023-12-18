import pandas as pd

# The pandas library is used for analyzing data.
# It can read/write .csv and .json files and clean their data.
# It can correlate two or more columns.
# Find the average, max or min values, even delete values.
# You can install pandas with:
#   sudo pip3 install pandas
#   sudo pip3 install pandas-stubs

print("________ Loading a .csv File ________")
data = pd.read_csv('13_data.csv')
print(data.to_string())


print("\n________ Create Pandas DataFrame from a Python Dictionary ________")
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'speed': [100, 80, 20]
}
car_data = pd.DataFrame(mydataset)
print(car_data)


print("\n________ Create Pandas Series from Python List ________")
# Notice how Pandas indexes the data starting with 0.
my_list = [5, 9, 2]
my_series = pd.Series(my_list)
print(my_series)


print("\n________ Accessing Data ________")
print(my_series[1])


print("\n________ Creating your own index labels ________")
my_series = pd.Series(my_list, index=['A', 'B', 'C'])
print(my_series)
print(my_series['C'])
