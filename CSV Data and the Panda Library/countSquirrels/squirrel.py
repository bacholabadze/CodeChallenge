import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels, red_squirrels, black_squirrels)

data_dict = {
    "Fur Color": ["Gray", 'Cinnamon', "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

