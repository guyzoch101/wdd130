items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

import math
boxes = math.ceil(items / items_per_box)

print(f'For {items}, packing {items_per_box} itmes in each box, you will need {boxes} boxes.')