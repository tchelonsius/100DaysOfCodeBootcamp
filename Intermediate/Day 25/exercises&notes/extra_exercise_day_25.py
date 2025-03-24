# The squirrel_data.csv file contains data about squirrels from the central park,
# collected in 2018/19. The goal of today's exercise is to create a new csv file
# with the amount of squirrels of each primary color existent.

import pandas

data = pandas.read_csv("squirrel_data.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]

gray_amount = len(gray)
black_amount = len(black)
cinnamon_amount = len(cinnamon)

data_dict = {
    "Colors": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_amount, black_amount, cinnamon_amount]
}

new_csv = pandas.DataFrame(data_dict)
new_csv.to_csv("squirrel_count.csv")
