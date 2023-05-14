import sys
import csv

# Function to read a CSV file and store the currency codes and exchange rates as a dictionary
def csv_reader(file):
    file_list = {}
    try:
        with open(file, newline="") as csv_file:
            csv_read = csv.DictReader(csv_file)
            for row in csv_read:
                file_list[row["Currency"].upper()] = float(row["Value"])
    # Handling file not found errors with OSError
    except OSError:
        sys.exit("Error: File not found!")
    # Adding new currency exchange rates if requested by the user
    else:
        while True:
            add_currency = input("Do you want to add new currency?: (Y/N) ").upper()
            if add_currency == "N":
                break
            elif add_currency == "Y":
                currency_code = input("Enter the new currency code: ").upper()
                exchange_rate = float(input("Enter the new currency code exchange rate: "))
                file_list[currency_code] = exchange_rate
            else:
                print("Invalid input! Try 'Y' or 'N'.")
    # Returning the dictionary of currency codes and exchange rates
    return file_list

# Function to convert from one currency to another
def currency_converter(from_currency, to_currency, exchange_rate, amount):
    # Checking if the exchange rate is available for the input currency codes
    if from_currency not in exchange_rate:
        print(f"Exchange rate not found for currency code : {from_currency}")
        return None
    if to_currency not in exchange_rate:
        print(f"Exchange rate not found for currency code : {to_currency}")
        return None
    # Converting the amount using the exchange rates
    from_exchange_rate = exchange_rate[from_currency]
    to_exchange_rate = exchange_rate[to_currency]
    converted_amount = amount * (float(to_exchange_rate) / float(from_exchange_rate))
    # Returning the converted amount
    return converted_amount

# Calling the csv_reader function to read the CSV file and store the exchange rates
exchange_rates = csv_reader('file_path')

# Getting the input for the amount, currency to convert from, and currency to convert to
amount_exchange = float(input("Enter the amount you want to convert: "))
from_currency_exchanges = input("Enter the currency you want to convert from: ").upper()
to_currency_exchanges = input("Enter the currency you want to convert to: ").upper()

# Calling the currency_converter function to convert the amount
convert_amount = currency_converter(from_currency_exchanges, to_currency_exchanges, exchange_rates, amount_exchange)

# Print result if conversion is successful
if convert_amount is not None:
    print(f"{amount_exchange:.2f} {from_currency_exchanges} = {convert_amount:.2f} {to_currency_exchanges}")
