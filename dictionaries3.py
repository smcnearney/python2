meal = {
    "drink": "beer",
    "appetizer": "chips",
    "entree": "tacos",
    "dessert": "churros"
}

print(meal)

#Change drink to green tea and get rid of dessert
#When you pass a dictionary a NEW key, it creates the key
#When you pass a dictionary a key it already has, it REPLACES the key
meal["drink"] = "green tea"
del meal["dessert"]

print(meal)