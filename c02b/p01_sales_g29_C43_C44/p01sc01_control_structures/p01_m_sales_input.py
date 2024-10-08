import re
from datetime import datetime

def get_valid_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

def get_valid_year():
    while True:
        try:
            year = int(input("Year (2000-2999): "))
            if 2000 <= year <= 2999:
                return year
            else:
                print("Year must be between 2000 and 2999.")
        except ValueError:
            print("Invalid year. Please enter a numeric value.")

def get_valid_month():
    while True:
        try:
            month = int(input("Month (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Invalid month. Please enter a numeric value.")

def get_valid_day():
    while True:
        try:
            day = int(input("Day (1-28): "))
            if 1 <= day <= 28:
                return day
            else:
                print("Day must be between 1 and 28.")
        except ValueError:
            print("Invalid day. Please enter a numeric value.")

def get_valid_region():
    valid_regions = ['w', 'm', 'c', 'e']
    while True:
        region = input("Region ('w', 'm', 'c', 'e'): ").lower()
        if region in valid_regions:
            return region
        else:
            print(f"Region must be one of the following: {valid_regions}.")

def get_valid_date():
    while True:
        date_str = input("Date (yyyy-mm-dd): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if 2000 <= date.year <= 2999:
                return date
            else:
                print("Year of the date must be between 2000 and 2999.")
        except ValueError:
            print(f"{date_str} is not in a valid date format.")

def get_valid_filename():
    while True:
        filename = input("Enter name of file to import: ")
        if re.match(r'^sales_q\d_\d{4}_[wmce]\.csv$', filename):
            return filename
        else:
            print("Filename doesn't follow the expected format of 'sales_qn_yyyy_r.csv'.")

def main():
    amount = get_valid_amount()
    year = get_valid_year()
    month = get_valid_month()
    day = get_valid_day()
    region = get_valid_region()
    date = get_valid_date()
    filename = get_valid_filename()

    print(f"Date: {date.strftime('%Y-%m-%d')}, Amount: {amount}, Year: {year}, Month: {month}, Day: {day}, Region: {region}, Filename: {filename}")

if __name__ == "__main__":
    main()
