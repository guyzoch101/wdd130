'''In many countries, food is stored in steel cans (also known as tin cans) 
that are shaped like cylinders. There are many different sizes of steel cans. 
The storage efficiency of a can tells us how much a can stores versus how much 
steel is required to make the can. Some sizes of cans require a lot of steel 
to store a small amount of food. Other sizes of cans require less steel and 
store more food. A can size with a large storage efficiency is considered more 
friendly to the environment than a can size with a small storage efficiency.

The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.'''

import math

# defining global variables for calulations in the programme

# a list for the names of the cans
name_list = ['#1 Picnic', '#1 Tall', '#2', '#2.5',
    '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10',
    '#211', '#300', '#303']

# a list for the radii of the cans
radii_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
    5.40, 6.83, 15.72, 6.83, 7.62, 8.10]

# a list for the heights of the cans
height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
    8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

# cost_per_can_list = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
#     0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

# an empty list for output of storage efficiency
storage_efficiency_list = []

def main():
    # i for iterating through the radii list and height list
    i = 0
    
    # iterating all data in the radii and height list
    for (radius, height) in zip(radii_list, height_list):
        radius = radii_list[i]
        
        height = height_list[i]
        
        i += 1
        
        # computing the volume and surface area for each radius and height value
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        
        # computing the storage efficciency and storing the value in a list
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        
        storage_efficiency_list.append(storage_efficiency)
    
    # j for iterating through the name and storgae efficiency lists
    j = 0
    
    # iterating all data in the name and storage efficiency lists
    # then printing the name with its corresponding stroage efficiency
    for (name, storage_efficiency) in zip(name_list, storage_efficiency_list):
        name = name_list[j]
        
        storage_efficiency = storage_efficiency_list[j]
        
        j += 1
        
        print(f'{name} {storage_efficiency}')
    
    pass


def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = round(volume / surface_area, 2)
    return storage_efficiency


main()