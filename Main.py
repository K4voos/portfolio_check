def get_input():
    entry_history = {}

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
    #     total_amount += buy_amount
    #     ave += buy_price * buy_amount
    # ave /= total_amount
    # return ave


def calculate_average(dictionary):
    total_amount = 0
    ave = 0
    for key in dictionary:
        ave += key * dictionary[key]
        total_amount += dictionary[key]
    ave /= total_amount
    return ave


this_average = calculate_average(get_input())
print('\nYour average entry price is: {} dollars.'.format(this_average))

# input('\nPress Enter to exit.')
