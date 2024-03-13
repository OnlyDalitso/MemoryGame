# Variables to hold the size of the tract and number of acres.
tractSize = 0.0
acres = 0.0

# Constant for the number of square feet in an acre.
SQ_FEET_PER_ACRE = 43560

# Get the square feet in the tract.
tractSize = float(input("Enter the number of square feet for the tract."))

# Calculate the agreage.
acres = float(tractSize)/SQ_FEET_PER_ACRE

# Print the number of acres.
print("The size of that is", format(acres, '.2f'),"acres.")
