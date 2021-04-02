import csv
from tkinter import filedialog


# Takes user input as price and amount of shares bought and returns them as a dictionary.
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


# Opens the file and returns prices and amounts as a dictionary.
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


# Saves the existing price-amount dictionary to a .SVC file.
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


# Calculates average entry price, total shares bought and total money spent on current position.
def calculate_average(dictionary):
    total_amount = 0
    bill = 0

    for price, amount in dictionary.items():
        bill += price * amount
        total_amount += amount

    ave = bill / total_amount
    return ave, total_amount, bill


# Calculates profit/loss and money left after closing current position.
def calculate_profit(price_amount):
    print('\nYou spent {:.4} USD on this position.'.format(price_amount[2]))
    current_price = float(input("Please enter current price: "))
    profit = (current_price - price_amount[0]) * price_amount[1]
    print('Total profit (negative means loss): {:+.4f}'.format(profit))
    percentage = (current_price - price_amount[0]) / price_amount[0] * 100
    print('Total profit percentage: {:+.4f}%'.format(percentage))
    print('Your money will be {:.4f} USD after close.'.format(price_amount[2] + profit))


this_input = get_input()
this_average = calculate_average(this_input)
print('\nYour average entry price is: {:.4f} USD'.format(this_average[0]))

calculate_profit(this_average)

save = input("\nDo you want to save this as a new file? (y/n): ")
if save == 'y':
    save_to_file(this_input)

input('\nPress Enter to exit.')
