import csv

# currency_name = ''
def get_input():
    entry_history = {}
    # currency_name = input("Name the currency you want to check: ")
    while True:
        buy_amount = float(input("How many shares have you bought? (-1 to skip): "))
        if buy_amount == -1:
            break
        buy_price = float(input("At what price you've bought your shares? "))
        if buy_price in entry_history:
            entry_history[buy_price] += buy_amount
        else:
            entry_history[buy_price] = buy_amount
    return entry_history


def save_to_file(dictionary):
    f = open("Portfolio_Checker/entry.csv", "w", newline="")
    writer = csv.writer(f)
    writer.writerow(("price", "amount"))
    for key in dictionary:
        writer.writerow((key, dictionary[key]))
    f.close()


def calculate_average(dictionary):
    total_amount = 0
    ave = 0
    for key in dictionary:
        ave += key * dictionary[key]
        total_amount += dictionary[key]
    ave /= total_amount
    return ave


this_input = get_input()

this_average = calculate_average(this_input)
save_to_file(this_input)
print('\nYour average entry price is: {} dollars.'.format(this_average))

# input('\nPress Enter to exit.')
