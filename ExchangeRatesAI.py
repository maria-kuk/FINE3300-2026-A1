import csv
import os


class ExchangeRates:
    """Reads a Bank of Canada exchange-rate file and converts between USD and CAD."""

    def __init__(self, filename):
        # Build the full path to the CSV, assuming it sits in the same folder
        # as this Python file. This avoids "file not found" errors in VS Code.
        folder = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(folder, filename)

        # The rate we want is stored in this column of the CSV
        self.column_name = "FXAUSDCAD"

        # Read the file right away and store the latest USD/CAD rate.
        # This is the number of CAD that 1 USD buys.
        self.rate = self.get_latest_rate()

    def get_latest_rate(self):
        """Return the most recent USD/CAD rate found in the file."""
        with open(self.filepath, newline="", encoding="utf-8-sig") as file:
            rows = list(csv.reader(file))

        # Bank of Canada files can have extra info lines above the real table,
        # so search for the row that contains our column name (the header row).
        header_index = None
        for i, row in enumerate(rows):
            if self.column_name in row:
                header_index = i
                break

        if header_index is None:
            raise ValueError(f"Column '{self.column_name}' was not found in the file.")

        # Which position (column number) holds the exchange rate?
        col = rows[header_index].index(self.column_name)

        # Go through the data rows from the bottom up and take the first
        # row that has a real number. That is the latest available rate.
        for row in reversed(rows[header_index + 1:]):
            if len(row) > col and row[col].strip() != "":
                return float(row[col])

        raise ValueError("No exchange rate values were found in the file.")

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount between USD and CAD and return the result."""
        if from_currency == to_currency:
            # Same currency: nothing to convert
            return amount
        elif from_currency == "USD" and to_currency == "CAD":
            # The rate is CAD per 1 USD, so multiply
            return amount * self.rate
        else:
            # CAD to USD: divide by the rate
            return amount / self.rate


def get_amount():
    """Keep asking until the user enters a valid, non-negative number."""
    while True:
        text = input("Enter the amount to convert: ").replace(",", "").replace("$", "").strip()
        try:
            amount = float(text)
            if amount < 0:
                print("Please enter a positive amount.")
            else:
                return amount
        except ValueError:
            print("That's not a valid number. Please try again.")


def get_currency(prompt):
    """Keep asking until the user enters USD or CAD."""
    while True:
        currency = input(prompt).strip().upper()
        if currency in ("USD", "CAD"):
            return currency
        print("Please enter either USD or CAD.")


def main():
    # Create the ExchangeRates object using the CSV file
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
    print(f"Latest USD/CAD exchange rate: {rates.rate}\n")

    # Ask the user for the conversion details
    amount = get_amount()
    from_currency = get_currency("Convert from (USD or CAD): ")
    to_currency = get_currency("Convert to (USD or CAD): ")

    # Do the conversion
    result = rates.convert(amount, from_currency, to_currency)

    # Display both amounts: $, commas for thousands, 2 decimals, currency code
    print(f"\n${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


# This makes main() run only when you run this file directly
if __name__ == "__main__":
    main()
