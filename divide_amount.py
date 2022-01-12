if __name__ == '__main__':
    print("Divide amount file")


def divide(whole_amount, people_list):
    equal_or_not = 'X'
    division = {}

    while equal_or_not != 'Y' or equal_or_not != 'N' or equal_or_not != 'y' or equal_or_not != 'n':
        equal_or_not = input("Divide equally? (Y/N) ")

        if equal_or_not == 'Y' or equal_or_not == 'y':
            divided_amount = float(whole_amount/len(people_list))
            divided_amount = round(divided_amount, 2)

            division = {}
            division = dict.fromkeys(people_list, divided_amount)

            return division

        elif equal_or_not == 'N' or equal_or_not == 'n':
            for person in people_list:
                print('{} pays: (%)'.format(person))
                amt = float(input())
                amt = round((amt*whole_amount)/100, 2)

                division[person] = amt

            return division

        else:
            print('Error! Retry')
            continue
