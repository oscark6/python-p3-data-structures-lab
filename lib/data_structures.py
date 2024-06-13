spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
# Example usage
result = get_names(spicy_foods)
print(result)  




##...
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
# Example usage
result = get_spiciest_foods(spicy_foods)
print(result)

 


##...
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
# Example usage
print_spicy_foods(spicy_foods)




##...
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # If no matching cuisine is found
# Example usage
result_american = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result_american)

result_thai = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(result_thai)




##...
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
# Example usage
print_spiciest_foods(spicy_foods)






##...
class TestDataStructures:
    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        },
    ]

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)

def test_get_average_heat_level(self):
    '''contains function get_average_heat_level that returns average of heat_levels in spicy_foods.'''
    assert(get_average_heat_level(TestDataStructures.SPICY_FOODS) == 6)

print(f"The average heat level of the spicy foods is: {get_average_heat_level(TestDataStructures.SPICY_FOODS)}")



##....
def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

# Example spicy_foods list
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# New spicy food to add
new_spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}

# Adding new spicy food to the list
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)

# Printing updated list
for food in updated_spicy_foods:
    print(food)