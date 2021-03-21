def average_entry_price():
    total_amount = 0
    average = 0
    while True:
        entry_amount = float(input("How many shares have you bought? (-1 to skip): "))
        if entry_amount == -1:
            break
        total_amount += entry_amount
        entry_price = float(input("At what price you've bought your shares? "))
        average += entry_price * entry_amount
    average /= total_amount
    return average


this_average = average_entry_price()
print('\nYour average entry price is: {} dollars.'.format(this_average))

input('\nPress Enter to exit.')
