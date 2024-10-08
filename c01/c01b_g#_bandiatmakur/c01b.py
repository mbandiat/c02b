def display_message():
    message = """
    This Find Interest application will ask user to specify the amount
    of a principal, an interest rate, and the number of years.
    The application calculates and displays the simple interest
    for the given amount at the specified interest for a specified number
    of years.
    """
    print(message)

def calculate_simple_interest(principal, rate, time):
    # Simple interest formula
    interest = principal * (rate / 100) * time
    return interest

def calculate_compounded_interest(principal, rate, time):
    # Compounded monthly interest formula: A = P(1 + r/n)^(nt)
    # where n is 12 (compounded monthly), t is time in years
    amount = principal * (1 + (rate / 100) / 12) ** (12 * time)
    return amount

def main():
    display_message()

    # Ask for inputs
    principal = int(input("Enter the amount of loan (e.g. 1500 for $1,500): "))
    rate = float(input("Enter the annual interest rate (e.g. 3.25 for 3.25%): "))
    time = int(input("Enter the number of years (e.g. 3 for 3 years): "))

    # Calculate simple interest
    simple_interest = calculate_simple_interest(principal, rate, time)
    
    # Display simple interest result
    print(f"\nThe simple interest on a loan of ${principal} at {rate}% yearly interest rate "
          f"for {time} years is ${simple_interest:.2f}.")

    # Calculate compounded monthly interest
    compounded_interest = calculate_compounded_interest(principal, rate, time)

    # Display compounded interest result
    print(f"The monthly compounded interest on a loan of ${principal} at {rate}% yearly interest rate "
          f"for {time} years is ${compounded_interest:.2f}.")

if __name__ == "__main__":
    main()
