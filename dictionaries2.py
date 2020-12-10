meal = {
    "drink": "beer",
    "appetizer": "chips",
    "entree": "tacos",
    "dessert": "churros"
}

print(meal)

# Add a new key pair with key and string
meal["water"] = "fizzy"

# Add a new key pair with key and Boolean
meal["quesadilla"] = False

print(meal)

if "quesadilla" in meal and "quesadilla" == True:
    print("Sean had a quesadilla")
else:
    print("Sean did NOT have a quesadilla")