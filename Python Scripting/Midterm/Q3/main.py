import pandas as pd
import matplotlib.pyplot as plt


def highest_marks(grades):

    plt.close()
    highest_marks = grades.max()
    plt.figure(figsize=(12, 8))
    highest_marks.plot(kind='bar', color='skyblue')
    plt.title('Highest Mark of Each Student')
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.show()


def lowest_marks(grades):
    plt.close()
    lowest_marks = grades.min(axis=1)
    plt.figure(figsize=(12, 8))
    lowest_marks.plot(kind='bar', color='lightgreen')
    plt.title('Lowest Mark in Each Test')
    plt.xlabel('Tests')
    plt.ylabel('Marks')
    plt.show()


def main_menu():
    grades_csv = pd.read_csv('grades.csv')
    while True:
        print("\nMenu:")
        print("1. Plot a bar graph depicting the highest mark of each student")
        print("2. Plot a bar graph showing the lowest mark in each test")
        print("0. Exit")
        choice = input("Enter your choice (0, 1, 2):")

        if choice == '1':
            highest_marks(grades_csv)
        elif choice == '2':
            lowest_marks(grades_csv)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()