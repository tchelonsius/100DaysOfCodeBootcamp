# Day 25: CSV Data and Pandas Library

# import csv
#
# temperatures = []
#
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])