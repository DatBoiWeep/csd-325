# Christopher Villarreal
# October 26, 2025
# Module 1.3 Assignment
# Purpose: Process the input from user, defined as x, and print the countdown until 0 is reached.

def main():
    # Ask user for number of bottles
    bottles = int(input("Enter the number of bottles: "))

    # Run code block until count reaches 1
    while bottles > 0:
        beer_on_wall(bottles)
        bottles -= 1
        pass_around(bottles)

    print("Time to buy more bottles of beer.")

# Verse 1
def beer_on_wall(x):
    pluralized = plural(x)
    print(f"{x} {pluralized} of beer on the wall, {x} {pluralized} of beer.")

# Verse 2
def pass_around(x):
    pluralized = plural(x)
    print(f"Take one down and pass it around, {x} {pluralized} of beer on the wall.")

# Check to the number of bottles to modify the words in the song
def plural(count):
    if count > 1 or count == 0:
        return "bottles"
    else:
        return "bottle"

# Call main function
if __name__ == "__main__":
    main()