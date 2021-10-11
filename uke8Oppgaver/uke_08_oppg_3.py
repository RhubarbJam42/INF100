def meal_list(fridge, ingredient_list):
    """
  1. set up a tally that counts the ingredients you do have for a given meal in your fridge
  2. _for each_ ingredient in a meal
  3. check _if_ that ingredient is in your fridge
  4. _add_ to tally of ingredients for a given meal that are in your fridge
  5. once you have looped through the ingredient list, check _if_ your count tally matches the number of items in the ingredient list
  """
    count = 0
    for ingredient in ingredient_list:
        if ingredient in fridge:
            count += 1

    return count == len(ingredient_list)


def meal_options(fridge, meals):
    """
  1. _for each_ tuple pair in meals
  2. run meal_list()
  3. _if_ function evaluates to `True`, then add to a new list of meals that are possible to make
  """
    meal_options_ls = []
    for i, n in enumerate(meals):
        if meal_list(fridge, meals[i][1]):
            meal_options_ls.append(meals[i][0])
    return meal_options_ls


# contents of my fridge, in a list
my_fridge = ["tomato sauce", "mustard", "potatoes", "carrots", "chicken", "frozen fish"]

# ingredients for all 4 meals in tuple
meal_recipes = [
    # name of dish [0], ingredients [1]
    ("fish_sticks", ["frozen fish", "potatoes", "mustard"]),
    ("chicken_curry", ["chicken", "curry paste", "carrots", "potatoes", "rice"]),
    ("chicken_veg", ["chicken", "potatoes", "carrots"]),
    ("pasta", ["spaghetti", "tomato sauce"]),
]

#test
#print(meal_options(my_fridge, meal_recipes))

