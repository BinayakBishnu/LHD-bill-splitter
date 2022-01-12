if __name__ == '__main__':
    print("Separate drink file")


def separate():
    drink_separate = 'X'

    while drink_separate != 'Y' or drink_separate != 'N' or drink_separate != 'y' or drink_separate != 'n':
        drink_separate = input("Drink bill separate? (Y/N) ")

        if drink_separate == 'Y' or drink_separate == 'y':
            meal_amount = float(input("Meal: "))
            drink_amount = float(input("Drink: "))
            return meal_amount, drink_amount

        elif drink_separate == 'N' or drink_separate == 'n':
            whole_meal_amount = float(input("Amount: "))
            return whole_meal_amount, 0

        else:
            continue
