# Christopher Villarreal
# October 8, 2025
# Module 11.2 - Recursive Functions
# Purpose:  This program demonstrates two approaches (recursive and non-recursive)
#           to printing the numbers 1 through n. The user input will be validated to avoid a 0 or negative integer.
#           The program will then display clear output messages for each.

def main():
    # Ask user for positive integer
    n = int(input("Enter a positive integer: "))
    # Loop until value is 1 or more
    while n <= 0:
        print("Error: Please enter a number greater than 0.")
        n = int(input("Enter a positive integer: "))

    # Ask user what method they would like to do
    selected_option = input("What method would you like to do? 'Recursive' or 'Non-recursive' or 'both'? ")

    # Exit program safely per user's choice
    if selected_option.lower() == 'quit' or selected_option.lower() == 'stop':
        print("Goodbye")

    elif selected_option.lower() == "recursive":
        recursive_print(1,n)

    elif selected_option.lower() == "non-recursive":
        non_recursive_print(n)

    elif selected_option.lower() == "both":
        # Call recursive and non-recursive functions with lines separation
        print("\n=== Starting Recursive Function ===")
        recursive_print(1, n)
        print("=== Ending Recursive Function ===\n")

        print("=== Starting Non-Recursive Function ===")
        non_recursive_print(n)
        print("=== Ending Non-Recursive Function ===")

    else:
        print("Sorry, that is not a valid option.")
        return


# Recursive function
# Explanation: This function will print numbers from 1 up to the user's input, defined as n, using recursion.
# It will call itself, increasing the current number each time, up until the base case (current > n) is reached.
def recursive_print(current, n):
    if current > n:
        print(f"Shrimps reached case {n}. Now closing all open cases...")
        return  # Base case: stop recursion
    print(f"The shrimps are opening case #{current}")
    recursive_print(current + 1, n)  # Recursive call
    print(f"The shrimps are closing case #{current}")


# Non-recursive function
# Explanation: This function prints numbers from 1 up to n using a simple for loop.
# This does NOT call itself making it iterative rather than recursive.
def non_recursive_print(n):
    for i in range(1, n + 1):
        print(f"The shrimps have printed out #{i}.")


# Run the main function
if __name__ == "__main__":
    main()