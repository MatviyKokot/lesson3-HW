# Level 1


# name = input("Enter your name: ")
# age = input("How old are you? ")
# game= input("What is your favorite game? ")

# print(f"Hello, {name}!\n You are {age} years old.\n Your favorite game is {game}.\nYou are going to turn {int(age) + 1} next year!")

#Level 2


# price= float(input("How much does it cost? "))
# ammount= int(input("How many do you want to buy? "))

# print(f"You are buying {product}")
# print(f"Each {product} costs {price}£")
# print(f"You want to buy {ammount} {product}(s)")
# print(f"The total cost is {price * ammount}£")

#Level 3


name= input(" Name: ")
work_day= int(input("Minutes of game time in a work day: "))
weekend_day= int(input("Minutes of game time in a weekend day: "))

print(f"{name} plays:\n {work_day *5} minutes in a work week\n {weekend_day * 2} minutes in a weekend\n {work_day * 5 + weekend_day * 2} minutes in a week\n Which is equal to {(work_day * 5 + weekend_day * 2) / 60} hours in a week")