"""
FINE 3300 - Assignment 1
Currency Exchange Rate Calculator
"""

import csv

class ExchangeRates:
    def __init__(self, filename):
        # Store the name of the exchange rate file
        self.__filename = filename

        # Open the CSV file and read its contents
        with open(self.__filename, "r", encoding="utf-8-sig", newline="") as file:
            # Read each row using the column names as keys
            reader = csv.DictReader(file)
            rows = list(reader)

        # Search from the last row to find the latest available rate
        for row in reversed(rows):
            rate = row["FXAUSDCAD"].strip()

            if rate != "":
                self.__exchange_rate = float(rate)
                break

    def exchange_rate(self):
        return self.__exchange_rate

    def convert(self, amount, from_currency, to_currency):
        # If both currencies are the same, no conversion is needed
        if from_currency == to_currency:
            return amount
        # Multiply by the rate to convert USD to CAD
        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.__exchange_rate
        # Divide by the rate to convert CAD to USD
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.__exchange_rate

 # Ask the user for the amount to convert and currencies
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (USD/CAD): ").upper()
to_currency = input("Enter the currency to convert to (USD/CAD): ").upper()

# Create the object and convert the amount
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
converted_amount = rates.convert(amount, from_currency, to_currency)

# Display the result to two decimal places, with commas for thousands and the currency code
print(f"${amount:,.2f} {from_currency} = ${converted_amount:,.2f} {to_currency}")