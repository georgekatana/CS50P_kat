def main():
    while True:
    fruit_name=input("Enter Fruit Name ? ")
    fruit_name=fruit_name.casefold()
    print("Calories :",find_calories(fruit_name))


def find_calories(fruit_name):
    fruit_calories =    {
                        "apple":130,
                        "avocado":50,
                        "banana":110,
                        "cantaloupe":50,
                        "grapefruit":60,
                        "grapes":90,
                        "Honeydew melon":50,
                        "kiwifruit":90,
                        "lemon":15,
                        "lime":20,
                        "nectarine":60,
                        "orange":80,
                        "peach":60,
                        "pear":100,
                        "pineaple":50,
                        "plumps":70,
                        "strawberries":50,
                        "sweet cherries":100,
                        "tangerine":50,
                        "watermelon":80,
                        }
    if fruit_name in fruit_calories:
        calorie_value=fruit_calories[fruit_name]
        return calorie_value
main()