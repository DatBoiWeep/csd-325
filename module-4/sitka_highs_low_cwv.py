# Christopher Villarreal
# November 7, 2025
# Module 4.2 Assignment
# Purpose of this program:
# Asks user what data they would like to view from a .csv file containing high and low temps.
# Then visual display the data into a chart with respective colors for high/low temps.
# Program will continue to run until user requests to exit.


import csv, sys
from datetime import datetime

from matplotlib import pyplot as plt

def main():
    filename = 'sitka_weather_2018_simple.csv'

    print("Welcome to the Data Center for the Weather in SITKA AIRPORT, AK US")
    print("Would you like to view 'Highs' or 'Lows'?")
    print("You can also say Quit / Exit to leave the program.")

    # Program will loop until user quits.
    while True:
        selection = input("> ").strip().lower()

        # Safely allow program to exit upon user request
        if selection == "quit" or selection == "exit":
            print("Now exiting the program, goodbye!")
            sys.exit(0)

        # Data will be prepared to output high temps
        elif selection == "highs":
            print("Please allow a moment for us to load the requested data.")
            color = "red"
            title = "Daily high temperatures - 2018"
            generate_data(selection, color, title, filename)

        # Data will be prepared to output low temps
        elif selection == "lows":
            print("Please allow a moment for us to load the requested data.")
            color = "blue"
            title = "Daily low temperatures - 2018"
            generate_data(selection, color, title, filename)

        else:
            print("Not a valid selection. Please try again.")
            print("Please enter 'highs', 'lows', or 'quit'.")

# Function's purpose is to generate and fill the provided that to form a visual plot
# Depending on user's selection, it will provide the highs or lows, along with changes to color and text.
def generate_data(selection, color, title, filename):
    # Preset row selection for retrieving temperature data 'High' / 'Low'
    if selection == "highs":
        s_row = 5
    elif selection == "lows":
        s_row = 6

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and either High/Low temperatures from this file.
        dates, data = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            temp = int(row[s_row])
            data.append(temp)

    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, data, c = color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    print(f"Success! Now showing {selection} values for Sitka!")

if __name__ == "__main__":
    main()