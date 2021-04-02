import csv
from tkinter import filedialog


def get_input():
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

    for key in entry:
        print("Prince: ", key)
        print("Amount: ", entry[key])
    return entry


def save_to_file(dictionary):
    file_name = filedialog.asksaveasfilename(initialdir="/", title="Select File",
                                             filetypes=(("SCV files", "*.csv"), ("all files", "*.*")))
    if '.csv' not in file_name:
        file_name += '.csv'
    f = open(file_name, "w", newline="")
    writer = csv.writer(f)
    writer.writerow(("price", "amount"))
    for key in dictionary:
        writer.writerow((key, dictionary[key]))
    f.close()
    print('File saved successfully.')


def calculate_average(dictionary):
    total_amount = 0
    ave = 0
    for key in dictionary:
        ave += key * dictionary[key]
        total_amount += dictionary[key]
    ave /= total_amount
    return ave


this_input = get_input()
current_price = float(input("Please enter current price: "))
this_average = calculate_average(this_input)

print('\nYour average entry price is: {} dollars.'.format(this_average))

total_profit = current_price - this_average
print(f'Total profit = {total_profit}')

percentage = (current_price - this_average) / this_average * 100
print(f'Total profit percentage: {percentage}')

save = input("Do you want to save this as a new file? (y/n): ")
if save == 'y':
    save_to_file(this_input)

input('\nPress Enter to exit.')
