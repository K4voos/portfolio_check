import csv
from tkinter import filedialog


def get_input():
    # Keys are prices and values are amounts.
    entry_history = {}
    init = input("Press 'o' to open an existing file, or anything else for new operation: ")

    if init == 'o':
        entry_history = open_file()
    else:
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


def open_file():
    entry = {}
    file_name = filedialog.askopenfilename(initialdir="/", title="Select File",
                                           filetypes=(("SCV files", "*.csv"), ("all files", "*.*")))
    f = open(file_name, 'r')
    csv_reader = csv.reader(f)
    next(csv_reader)
    for line in csv_reader:
        entry[float(line[0])] = float(line[1])
    f.close()

    for price, amount in entry.items():
        print("Prince: ", price)
        print("Amount: ", amount)
    return entry


def save_to_file(dictionary):
    file_name = filedialog.asksaveasfilename(initialdir="/", title="Select File",
                                             filetypes=(("SCV files", "*.csv"), ("all files", "*.*")))
    if '.csv' not in file_name:
        file_name += '.csv'
    f = open(file_name, "w", newline="")
    writer = csv.writer(f)
    writer.writerow(("price", "amount"))
    for price, amount in dictionary:
        writer.writerow((price, amount))
    f.close()
    print('File saved successfully.')


def calculate_average(dictionary):
    total_amount = 0
    ave = 0
    for price, amount in dictionary.items():
        ave += price * amount
        total_amount += amount
    ave /= total_amount
    return ave, total_amount


def calculate_profit(price_amount):
    current_price = float(input("Please enter current price: "))
    total_profit = (current_price - price_amount[0]) * price_amount[1]
    print('\nTotal profit (negative means loss): {:+.4f}'.format(total_profit))
    percentage = (current_price - price_amount[0]) / price_amount[0] * 100
    print('Total profit percentage: {:+.4f}%\n'.format(percentage))


this_input = get_input()
this_average = calculate_average(this_input)
print('\nYour average entry price is: {:.4f} USD\n'.format(this_average[0]))

calculate_profit(this_average)

save = input("Do you want to save this as a new file? (y/n): ")
if save == 'y':
    save_to_file(this_input)

input('\nPress Enter to exit.')
