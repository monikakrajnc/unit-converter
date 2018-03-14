# CONVERTER FOR BAKING UNITS

# All ingredients and units for the code are predefined. In the list "ingredients" contains all available ingredients you can use.
# The "metrics" list contains all the most commonly used units in cooking and baking.
# The "metrics_cup" list contains sublists for each unit, converted from "metrics" units list into cups, based on the ingredient. Because ingredients have different densities.
# There is also a list named "o", containing all words/strings, that need to be excluded from the input.

#PSEUDOCODE

#INPUT:
# Ingredient amount
# Ingredient type
# Unit (unit_1) converted from
# Unit (unit_2) converted to

#PROCESS:
# Split the input into separate strings, by using split function, and make a list of these strings
# From the list of strings remove strings that are not relevant for the code
# After cleaning the list, identify unit you want to convert from and unit you want to convert to, and the ingredient type and amount
# Check if ingredient, and both units are available, if not remind user to change or reenter
# Based on the ingredient, select suitable sublist from "metrics_cup", which contains pre-calculated numbers for conversion between mass and volume
# Based on the unit you have from "metrics" list (which contains unit names), selected the same position in the sublist (from "metrics_cup") and convert the amount of this unit into the cups base unit
# Find desired output unit in the list "metrics" and find the same position in sublist of "metrics_cup". Multiply this value by the amount you calculated in previous step. Round the result.

#OUTPUT:
# Display the converted amount in the desired unit (unit_2)


ingredients = ["flour", "sugar", "butter", "oil", "milk", "cream", "yogurt", "chocolateChip"]
metrics = ["cup", "kilogram", "kilo", "kg", "dekagram", "dag", "dkg", "gram", "g", "ounce", "oz", "pound", "lb", "tbsp", "tsp", "liter", "l", "deciliter", "dl", "milliliter", "ml", "stick"]
metrics_cups = [[1, 0.14, 0.14, 0.14, 14, 14, 14, 140.3, 140.3, 4.95, 4.95, 0.31, 0.31, 16, 48, 0.14, 0.14, 1.4, 1.4, 140, 140, 0],
                [1, 0.2, 0.2, 0.2, 20, 20, 20, 200, 200, 7.05, 7.05, 0.44, 0.44, 16, 48, 0.19, 0.19, 1.9, 1.9, 190, 190, 0],
                [1, 0.26, 0.26, 0.26, 26, 26, 26, 226, 226, 8, 8, 0.5, 0.5, 16, 48, 0, 0, 0, 0, 0, 0, 2],
                [1, 0.223, 0.223, 0.223, 22.33, 22.33, 22.33, 223.34, 223.34, 7.88, 7.88, 0.492, 0.492, 16, 48, 0.24, 0.24, 2.37, 2.37, 236.59, 236.59, 0],
                [1, 0.24, 0.24, 0.24, 24, 24, 24, 240, 240, 8.5, 8.5, 0.53, 0.53, 16, 48, 0.24, 0.24, 2.4, 2.4, 240, 240, 0],
                [1, 0.24, 0.24, 0.24, 24, 24, 24, 240, 240, 8.47, 8.47, 0.53, 0.53, 16, 48, 0.24, 0.24, 2.4, 2.4, 240, 240, 0],
                [1, 0.245, 0.245, 0.245, 24.5, 24.5, 24.5, 245, 245, 8.6, 8.6, 0.5, 0.5, 16, 48, 0.24, 0.24, 2.4, 2.4, 240, 240, 0],
                [1, 0.17, 0.17, 0.17, 17, 17, 17, 170, 170, 6, 6, 0.375, 0.375, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0.12, 0.12, 0.12, 12, 12, 12, 120, 120, 4.233, 4.233, 0.265, 0.265, 16, 48, 0, 0, 0, 0, 0, 0, 0]]
o = ["into", "to", "from", "in", "of", "a", "an", "the"]

all = input("What would you like to convert (for example; 300 ml of milk into cups): ")


c = all.split(" ")

# remove all unnecessary strings from list c
for j in c:
    if j in o:
        c.remove(j)


# remove "s" from all plural words
d = []
for k in c:
    n = len(k)
    if k[n-1] == "s":
        p = k[0:n-1]
        d.append(p)
    else:
        d.append(k)


amount = float(d[0])
unit_1 = d[1]
ingred = d[2]
unit_2 = d[3]


# check if desired ingredient is available in the list of ingredients
i = 0
n = 0
while i < len(ingredients):
    if ingred == ingredients[i]:
        n = 0
    else:
        n += 1
    # if ingredient is not available, ask to enter one from the list
    if n == 8:
        print("Sorry, cannot find the ingredient.\nPlease select one of the following:", ', '.join(ingredients))
        ingred = input("Please enter it here: ")
        i = 0
        n = 0
    i = i + 1


# check if both units are available in list metrics
if unit_1 not in metrics or unit_2 not in metrics:
    while unit_1 not in metrics:                              # prompts the user to enter a valid unit
        print("Cannot find the unit you want to convert from.\nDid you mean one of the following:\n", ', '.join(metrics))
        unit_1 = input("Please enter chosen unit here: ")
    while unit_2 not in metrics:                              # prompts the user to enter a valid unit
        print("Cannot find the unit you want to convert to.\nDid you mean one of the following:\n", ', '.join(metrics))
        unit_2 = input("Please enter chosen unit here: ")


# conversion

for j in range(0, len(ingredients)):
    if ingred == ingredients[j]:                 #find selected ingredient
        z = metrics_cups[j]                      #for the selected ingredient, choose its list of measurements in cups
        for i in range(0, len(metrics)):
            if unit_1 == metrics[i]:             #find the unit that needs to be converted from
                n = amount / z[i]                #convert unit_1 into cups
            if unit_2 == metrics[i]:             #find unit_2
                k = z[i]
        m = n * k                                #convert to desired unit
        if m == 0:
            print("Sorry, but this conversion is not relevant to baking.")
        else:
            print(round(m, 3), unit_2)