import matplotlib.pyplot as plt
import numpy as np


def plot_simple_line():
    plt.plot([1, 0.25, 0.5, 2, 3, 3.75, 3.5])
    plt.show()


def plot_line_with_labels():
    plt.plot([0, 1, 2, 3, 4, 5, 6], [0, 2, 6, 14, 30, 43, 75])
    plt.ylabel('Speed', fontsize=12)
    plt.xlabel('Time', fontsize=12)
    plt.title('Speed v Time')
    plt.plot([0, 1, 2, 3, 4, 5, 6], [0, 2, 6, 14, 30, 43, 75], 'bo-')  # Blue circles and solid line
    plt.show()


def plot_sine_function():
    time = np.arange(-20, 20, 0.1)
    amplitude = np.sin(time) / time
    plt.title('Sinc Function')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.plot(time, amplitude, 'b')  # Blue line
    plt.show()


def plot_bar_chart():
    labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
    index = [1, 2, 3, 4, 5]  # Provides locations on the x-axis
    sizes = [45, 10, 15, 30, 22]
    plt.bar(index, sizes, tick_label=labels)
    plt.ylabel('Usage')
    plt.xlabel('Programming Languages')
    plt.show()


def plot_stacked_bar_chart():
    labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
    index = [1, 2, 3, 4, 5]
    web_usage = [20, 2, 10, 14, 22]
    data_science_usage = [15, 8, 15, 2, 10]
    games_usage = [10, 1, 5, 5, 4]

    plt.bar(index, web_usage, tick_label=labels, label='Web')
    plt.bar(index, data_science_usage, bottom=web_usage, label='Data Science')
    web_and_games_usage = [web_usage[i] + data_science_usage[i] for i in range(len(web_usage))]
    plt.bar(index, games_usage, bottom=web_and_games_usage, label='Games')

    plt.ylabel('Usage')
    plt.xlabel('Programming Languages')
    plt.legend()
    plt.show()


def plot_grouped_bar_chart():
    BAR_WIDTH = 0.35

    team_a_results = [60, 75, 56, 62, 58]
    team_b_results = [55, 68, 80, 73, 55]
    index_team_a = [1, 2, 3, 4, 5]
    index_team_b = [i + BAR_WIDTH for i in index_team_a]

    ticks = [i + BAR_WIDTH / 2 for i in index_team_a]
    tick_labels = ['Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5']

    plt.bar(index_team_a, team_a_results, BAR_WIDTH, color='b', label='Team A')
    plt.bar(index_team_b, team_b_results, BAR_WIDTH, color='r', label='Team B')

    plt.xlabel('Labs')
    plt.ylabel('Scores')
    plt.title('Scores by Lab')
    plt.xticks(ticks, tick_labels)
    plt.legend()
    plt.show()


def display_menu():
    while True:
        print("\nChoose a plot to display:")
        print("1: Simple Line Plot")
        print("2: Line Plot with Labels")
        print("3: Sine Function Plot")
        print("4: Bar Chart")
        print("5: Stacked Bar Chart")
        print("6: Grouped Bar Chart")
        print("0: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            plot_simple_line()
        elif choice == "2":
            plot_line_with_labels()
        elif choice == "3":
            plot_sine_function()
        elif choice == "4":
            plot_bar_chart()
        elif choice == "5":
            plot_stacked_bar_chart()
        elif choice == "6":
            plot_grouped_bar_chart()
        elif choice == "0":
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")


# Run the menu
display_menu()
