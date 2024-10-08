# p01sc01_control_structures/p01beg_m_sales_input.py

def get_valid_amount():
    while True:
        amount = input("Amount: ")
        try:
            amount = float(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_year():
    while True:
        year = input("Year (2000-2999): ")
        try:
            year = int(year)
            if 2000 <= year <= 2999:
                return year
            else:
                print("Year must be between 2000 and 2999.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_month():
    while True:
        month = input("Month (1-12): ")
        try:
            month = int(month)
            if 1 <= month <= 12:
                return month
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_day():
    while True:
        day = input("Day (1-28): ")
        try:
            day = int(day)
            if 1 <= day <= 28:
                return day
            else:
                print("Day must be between 1 and 28.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_region():
    valid_regions = ('w', 'm', 'c', 'e')
    while True:
        region = input("Region ('w', 'm', 'c', 'e'): ").lower()
        if region in valid_regions:
            return region
        else:
            print(f"Region must be one of the following: {valid_regions}")

def main():
    amount = get_valid_amount()
    year = get_valid_year()
    month = get_valid_month()
    day = get_valid_day()
    region = get_valid_region()
    
    print(f"Amount: {amount}")
    print(f"Year: {year}")
    print(f"Month: {month}")
    print(f"Day: {day}")
    print(f"Region: {region}")

if __name__ == "__main__":
    main()
