#  Question 1¶
# In the House Prices - Advanced Regression Techniques competition, you need to use information like the number of bedrooms and bathrooms to predict the price of a house. Inspired by this competition, you'll write your own function to do this.

# In the next code cell, create a function get_expected_cost() that has two arguments:

# beds - number of bedrooms
# baths - number of bathrooms
# It should return the expected cost of a house with that number of bedrooms and bathrooms. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000.
# each bedroom adds 30000 to the expected cost
# each bathroom adds 10000 to the expected cost.
# For instance,

# a house with 1 bedroom and 1 bathroom has an expected cost of 120000, and
# a house with 2 bedrooms and 1 bathroom has an expected cost of 150000. 


# TODO: Complete the function
def get_expected_cost(beds, baths):
    cost_beds= 30000* beds
    cost_baths= 10000 * baths
    value = 80000 + cost_beds + cost_baths
    return value

# TODO: Use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)