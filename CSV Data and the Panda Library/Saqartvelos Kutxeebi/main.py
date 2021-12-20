import turtle
import pandas

ALIGNMENT = "center"
FONT = ("arial", 12, "normal")

screen = turtle.Screen()
screen.title("საქართველოს კუთხეები")

image = "georgia_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("kutxeebi.csv")
regions = data["კუთხე"].to_list()


def display_region(data_region):
    new_region = turtle.Turtle()
    new_region.hideturtle()
    new_region.color('black')
    new_region.penup()
    new_region.goto(int(data_region.x), int(data_region.y))
    new_region.write(f"{data_region['კუთხე'].item()}", align=ALIGNMENT, font=FONT)


correct_answers = []
missing_regions = []
correct_ans_count = 0
while correct_ans_count != 12:
    answer = screen.textinput(title=f"{correct_ans_count}/12 გამოცნობილი კუთხე", prompt="შეიყვანე კუთხის დასახელება")
    for region in regions:
        if answer == region and answer not in correct_answers:
            correct_ans_count += 1
            correct_answers.append(answer)
            region_data = data[data['კუთხე'] == answer]
            display_region(region_data)
    if answer == 'დასრულება':
        missing_regions = [region for region in regions if answer == 'დასრულება' and region not in correct_answers]
        new_data = pandas.DataFrame(missing_regions)
        new_data.to_csv("გამოტოვებული კუთხეები.csv")
        break
