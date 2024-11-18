people_list = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 100

for people in people_list:
    print(people)

for people_line in people_list:
    new_list = people_line.split()
    name = new_list[0]
    age = int(new_list[1])
    
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f'Youngest person: {youngest_name} - {youngest_age}')