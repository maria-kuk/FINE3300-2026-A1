# FINE 3300 – Assignment 1: Exchange Rate Calculator

## Project Description

This project contains two Python programs that convert amounts between US dollars (USD) and Canadian dollars (CAD). The programs use exchange-rate data from a CSV file provided for FINE 3300 Assignment 1. The programs read the latest available exchange rate from the FXAUSDCAD column in the CSV file. The user enters an amount, the currency to convert from, and the currency to convert to. The result is displayed with a dollar sign, the currency code, and two decimal places.

## Program Versions

The repository contains two versions of the exchange-rate calculator. The original version was written for Part 1 of the assignment. The second version was generated using an AI model for Part 2. Both programs perform the same currency conversions, but they differ in how they read the CSV file and handle user input.

## Files
- exchange_rates.py – The original exchange rate calculator.
- ExchangeRatesAI.py – The AI-generated version created for Part 2 of the assignment.
- BankOfCanadaExchangeRate.2026.csv – The exchange-rate data file used by the programs.
- README.md – This file, which describes the project and explains how to run the programs.

## Requirements

- Python 3
- The CSV file listed above
- Visual Studio Code or another Python editor

## How to Run the Programs

1. Download or clone the repository to your computer.
2. Open the project folder in Visual Studio Code.
3. Make sure the Python files and CSV file are in the same folder.
4. Open the terminal in Visual Studio Code.
5. To run the original program, enter:

   python3 exchange_rates.py

6. Follow the prompts to enter the amount, starting currency (USD or CAD), and target currency (USD or CAD).

To run the AI-generated version, enter:

python3 ExchangeRatesAI.py

## Conversion Method

The programs use the USD/CAD exchange rate from the CSV file.

- **USD to CAD:** Multiply the USD amount by the exchange rate.
- **CAD to USD:** Divide the CAD amount by the exchange rate.
- **Same currency:** Return the original amount without converting it.
