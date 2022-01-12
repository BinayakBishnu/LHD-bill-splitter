import separate_drinks
import divide_amount

print("Welcome to the bill splitter")

amount_tuple = separate_drinks.separate()
print(amount_tuple)

gross_amount = sum(list(amount_tuple))
print(gross_amount)

number_of_people = int(input('Number of people: '))

people_list = {'meal': [], 'drinks': []}
meal_divided_list = {}
drinks_divided_list = {}

print("Who all are there? ")
stop = number_of_people

while stop > 0:
    name = input('Name: ')
    stop -= 1

    people_list['meal'].append(name)

print('Dividing meal amount')
if people_list['meal'] != []:
    meal_divided_list = divide_amount.divide(
        amount_tuple[0], people_list['meal'])


if amount_tuple[1] != 0:
    print("Who all had drinks? ")
    stop = 'random'
    print("Type x to stop")
    while stop != 'x':
        name = input('Name: ')
        stop = name
        if name == 'x':
            break
        people_list['drinks'].append(name)

    print('Dividing drinks amount')
    if people_list['drinks'] != []:
        drinks_divided_list = divide_amount.divide(
            amount_tuple[0], people_list['drinks'])


print()
print('List of people')
print(people_list)
print()
print('Meal amount division:')
print(meal_divided_list)
print()
print('Drinks amount division:')
print(drinks_divided_list)
print()


total_personwise_list = {}
if amount_tuple[1] == 0:
    total_personwise_list = meal_divided_list.copy()

elif amount_tuple[1] != 0:
    for person1 in people_list['meal']:
        for person2 in people_list['drinks']:
            if person1 == person2:
                total_personwise_list[person1] = meal_divided_list[person1] + \
                    drinks_divided_list[person1]

            else:
                total_personwise_list[person1] = meal_divided_list[person1]

print('\n---Final bill split---')
print(total_personwise_list)


bill_data = ''

temp = []
for components in total_personwise_list.items():
    temp_list = [str(i) for i in components]
    b = ': '.join(temp_list)
    temp.append(b)

all_totals = '; '.join(temp)
print(all_totals)

with open('bills.txt', 'a') as f:
    f.write(all_totals)
    f.write("\n\n")
