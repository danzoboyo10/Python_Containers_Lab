# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ["Danny", "Steve", "Jim", "Todd"]
print(students[1])
print(students[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foods = ("cheese burger", "hot dog", "celery", "pizza" )
for food in foods:
  print(f"{food} goes here is a good food")


# Exercise 3
# Using a forloop, print just the last two food strings from foods.
for i in range(len(foods)):
  print(foods[-1])
  print(foods[-2])


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

  home_town = {
  'city': 'Winchester',
  'state': 'Massachusetts',
  'population': '27,912'
}
  print(f"I was born in {home_town['city']}, {home_town['state']}, population of {home_town['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:

for key, value in home_town.items():
  print(f"{key} = {value}")


# Exercise 6
# Create an empty list named cohort.
# Using a for loop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:
# Iterate over cohort printing out each element.

cohort = []
for student in students:
  cohort.append(student)
print(cohort)



# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students = ["Tina is awesome", "Fred is awesome", "Harry is awesome", "Bill is awesome"]
for awesome_student in awesome_students:
  print (awesome_student)



# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.



foods = ("cheese burger", "hot dog", "celery", "pizza" )
for food in foods:
  if food.__contains__('a'):
    print(food)
  else:
    print('No foods contain the letter a')

