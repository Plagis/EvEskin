# Project Tile: EvE marketing Skin Calculator

# Definitions for Skin Calulation

import requests

# constants for conversion and tax
PLEX_TO_ISK = 5350000
SALES_TAX = 5000000
MULTIPLIER = 2
BONUS_RATE = 1.20
API_URL = "https://janice.e-351.com/api/rest/v2/markets"
API_KEY = "iCwfwg6pdQzQwxTQtuPZX2iKBJFuErr5"


# Function to calculate plex amount
def convert_plex_to_isk(plex_amount):
    isk_amount = plex_amount * PLEX_TO_ISK
    return isk_amount

# Function to calculate final amount
def calculate_final_amount(isk_amount):
    doubled_amount = isk_amount * MULTIPLIER
    final_amount = doubled_amount * BONUS_RATE
    return final_amount

# Function to substract ccp sales tax
def subtract_ccp_sales_tax(final_amount):
    sell_amount = final_amount - SALES_TAX
    return sell_amount



def main():
    try:
        plex_amount = float(input("Enter the amount of PLEX: "))
        isk_amount = convert_plex_to_isk(plex_amount)
        final_amount = calculate_final_amount(isk_amount)
        sell_amount = subtract_ccp_sales_tax(final_amount)
        print(f"The final ISK amount after conversion, doubling, and adding 20%, then subtracting ccp sales tax is: {sell_amount:,.2f} ISK")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
