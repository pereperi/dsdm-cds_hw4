import pandas as pd
import datetime


##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

from functools import reduce

def count_simba(strings):
    # Use map to count occurrences of "Simba" in each string
    counts = map(lambda s: s.count("Simba"), strings)
    
    # Use reduce to sum up the counts
    total = reduce(lambda acc, x: acc + x, counts)
    
    return total

# Test the function
test_strings = ["Simba and Nala are lions.", 
                "I laugh in the face of danger.",
                "Hakuna matata", 
                "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

print(count_simba(test_strings))



# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

import pandas as pd
import datetime

def get_day_month_year(dates):
    # Use map to extract day, month, and year from each date
    extracted_data = map(lambda date: (date.day, date.month, date.year), dates)
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(extracted_data, columns=['day', 'month', 'year'])
    
    return df

# Test the function
test_dates = [datetime.date(2021, 1, 10), 
              datetime.date(2022, 2, 20),
              datetime.date(2023, 3, 30)]
print(get_day_month_year(test_dates))



# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy.distance import geodesic

def compute_distance(coords):
    # Use map to compute the distance for each pair of coordinates
    distances = map(lambda coord_pair: geodesic(coord_pair[0], coord_pair[1]).kilometers, coords)
    
    return list(distances)

# Test the function
test_coords = [((41.23,23.5), (41.5, 23.4)), 
               ((52.38, 20.1),(52.3, 17.8))]
print(compute_distance(test_coords))


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13

def sum_general_int_list(sum_list):
    if type(sum_list) != list:
        return sum_list
    if sum_list == []:
        return 0
    return sum_general_int_list(sum_list[0]) + sum_general_int_list(sum_list[1:])


list_int = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
print(sum_general_int_list(list_int))
