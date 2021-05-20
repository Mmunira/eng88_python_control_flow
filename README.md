# Control Flow
### Control flow is very important in any language programming language to control the flow of your conditions and decisions

- if, elif and else conditions

weather = "sunny"

if weather == "sunny": # if this condition is False execute the next line of code
    print("Enjoy the weather") # if true this line will executed
if weather != "sunny":
    print("waiting for the sunshine")
if weather == "cloudy":
    print("still waiting for sunshine")

elif weather == "rainy":
    print("make sure to bring an umbrella")

else:
    print('Opps sorry something went wrong...please try later') # if false this line will be executed

#add a condition to use elif when the condition is False


# Loops are used to ITERATE through data
# Lists, Dictionaries, Sets

#For loop
list_data = [1, 2, 3, 4, 5]
for number in list_data:
    if number == 1:
        print("1 was found")
    if number == 4:
        print("4 was found")
    if number == 5:
        print("5 was found")
    else:
        print("better luck next time")


# Second iteration
student_1 = {
    "name" : "Munira",
    "key" : "value",
    "stream" : "Cyber Security", # strings
    "completed_lessons" : "3", # int
    "completed_lessons_name" : ["variables", "operators" ,"data_collections"] # list

}
for data in student_1.values():
# For values = for data in student_1.values()
    if data == "value":
        break
    print(data)

# While loops

user_prompt = True

while user_prompt:
    age = input("Please enter your age? ")
if age.isdigit():
        user_prompt = False
else:
    print("Please provide your answer in digits")
print(f"your age is {age}")