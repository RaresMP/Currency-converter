# Currency-converter

The script starts with the import statements for the csv and sys modules.

The csv_reader function is defined and takes a file parameter. 
The function reads the csv file with the specified filename and populates a dictionary file_list with the currency codes as keys and exchange rates as values.
If the file is not found, an error message is printed using sys.exit() function. 
If the file is found, it prompts the user to add a new currency by asking if they want to add a new currency or not. If the answer is "N", it breaks out of the loop. 
If the answer is "Y", it prompts the user to enter a new currency code and its exchange rate. The new currency is added to file_list. The function then returns the file_list dictionary.

The currency_converter function is defined and takes the following parameters: from_currency, to_currency, amount and exchange_rate. The function checks if both from_currency and to_currency are present in exchange_rate dictionary. 
If not, it prints an error message and returns None. If both currencies are present, the function retrieves their exchange rates from exchange_rate dictionary, calculates the converted amount and returns it.

The script calls the csv_reader function to read the csv file and stores the resulting dictionary in exchange_rate.

The script prompts the user to enter the amount, the currency to convert from and the currency to convert to.

The currency_converter function is called with the parameters from_currency, to_currency, amount and exchange_rate.
If the conversion is successful, the program prints the original amount, currency code and the converted amount and currency code to the console in the desired format.
