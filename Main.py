from csv import reader, writer
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
            try:
                buy_amount = float(input("How many shares have you bought? (-1 to skip): "))
            except:
                print("In this step you must enter the amount of shares you've bought")
                continue
            if buy_amount == -1:
                break
            try:
                buy_price = float(input("At what price you've bought your shares? "))
            except:
                print("\nIn this step you must have entered the the price in which you have bought some shares.")
                print("Let's start from the beginning of this round.")
                continue
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
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('File not found!')
        entry = get_input()
        return entry

    csv_reader = reader(f)
    next(csv_reader)
    for line in csv_reader:
        entry[float(line[0])] = float(line[1])
        print("Prince: ", line[0])
        print("Amount: ", line[1])
    f.close()

    return entry


# Saves the existing price-amount dictionary to a .SVC file.
def save_to_file(dictionary):
    save = input("\nDo you want to save this as a new file? (y/n): ")
    if save == 'y':
        file_name = filedialog.asksaveasfilename(initialdir="/", title="Select File",
                                                 filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        if not file_name == '' and '.csv' not in file_name:
            file_name += '.csv'
        try:
            f = open(file_name, "w", newline="")
        except FileNotFoundError:
            save_to_file(this_input)
            return False
        csv_writer = writer(f)
        csv_writer.writerow(("price", "amount"))
        for price, amount in dictionary.items():
            csv_writer.writerow((price, amount))
        f.close()
        print('File saved successfully.')
    elif save == 'n':
        return False
    else:
        print('Please enter only "y" or "n"!')
        save_to_file(this_input)


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
    print('\nYou have spent ${:.4} on this position.'.format(price_amount[2]))
    current_price = float(input("Please enter current price: "))
    profit = (current_price - price_amount[0]) * price_amount[1]
    print('Total profit (negative means loss): ${:+.4f}'.format(profit))
    percentage = (current_price - price_amount[0]) / price_amount[0] * 100
    print('Total profit percentage: {:+.4f}%'.format(percentage))
    print('Your money will be ${:.4f} after close.'.format(price_amount[2] + profit))


this_input = get_input()
this_average = calculate_average(this_input)
print('\nYour average entry price is: ${:.4f}'.format(this_average[0]))

calculate_profit(this_average)

save_to_file(this_input)

input('\nPress Enter to exit.')
