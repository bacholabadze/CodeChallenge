import pandas

#################################################################################
# import csv
#
# temperature = []
#
# with open("weather_data.csv", mode='r') as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

#################################################################################

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)


# Average Temperature
# data_list = data["temp"].tolist()
# avg_temp = sum(data_list)/len(data_list)
# print(avg_temp)


# print("Average temperature: ", data["temp"].mean())
#
# print("Maximum temperature: ", data["temp"].max())

# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == 'Monday'])

# Print the row of data which had the highest temperature
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_F = int(monday.temp) * 9/5 + 32
# print(monday_F)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Jane", "Angela"],
    "scores": [76, 56, 83]
}
student_data = pandas.DataFrame(data_dict)
# print(student_data)
student_data.to_csv('students_data.csv')
