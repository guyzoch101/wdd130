# allowing the user to input a country and find the max and min life expectancy of that country
# calculate the difference between the max and min life expectancy of that country
max_expectancy = 0
min_expectancy = 10000

with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_expectancy_entity = entity
            max_expectancy_year = year

with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_expectancy_entity = entity
            min_expectancy_year = year
        
year_enquired = int(input('Enter the year of interest: '))

print()
print(f'The overall max life expectancy is: {max_expectancy} from {max_expectancy_entity} in {max_expectancy_year}')
print(f'The overall min life expectancy is: {min_expectancy} from {min_expectancy_entity} in {min_expectancy_year}')

max_expectancy_enquired = 0
min_expectancy_enquired = 10000

with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if expectancy > max_expectancy_enquired and year == year_enquired:
            max_expectancy_enquired = expectancy
            max_expectancy_entity_enquired = entity

with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if expectancy < min_expectancy_enquired and year == year_enquired:
            min_expectancy_enquired = expectancy
            min_expectancy_entity_enquired = entity

total_expectancy = 0
total_entities = 0
with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if year == year_enquired:
            total_expectancy += expectancy
            total_entities += 1
average_expectancy = total_expectancy / total_entities

print()
print(f'For the year {year_enquired}:')
print(f'The average life expectancy across all countries was {round(average_expectancy, 2)}')
print(f'The max life expectancy was in {max_expectancy_entity_enquired} with {max_expectancy_enquired}')
print(f'The min life expectancy was in {min_expectancy_entity_enquired} with {min_expectancy_enquired}')

print()
entity_enquired = input('Enter the country of interest: ').lower()

max_expectancy_enquired = 0
min_expectancy_enquired = 10000

with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if expectancy > max_expectancy_enquired and entity.lower() == entity_enquired:
            max_expectancy_enquired = expectancy
            max_expectancy_year_enquired = year

with open('week06/life-expectancy.csv') as dataset:
    next(dataset)
    for list in dataset:
        parts = list.split(',')
        
        entity = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2].strip())
        expectancy = float(parts[3].strip())
        
        if expectancy < min_expectancy_enquired and entity.lower() == entity_enquired:
            min_expectancy_enquired = expectancy
            min_expectancy_year_enquired = year

print()
print(f'In {entity_enquired.title()}:')
print(f'The max life expectancy was {max_expectancy_enquired} in {max_expectancy_year_enquired}')
print(f'The min life expectancy was {min_expectancy_enquired} in {min_expectancy_year_enquired}')

difference = round(max_expectancy_enquired - min_expectancy_enquired, 4)
print(f'The difference between the max life expectancy and the min life expectancy was {difference}')