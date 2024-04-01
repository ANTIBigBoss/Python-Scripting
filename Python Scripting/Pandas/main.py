import pandas as pd
import matplotlib.pyplot as plt


# I decided functions and a main menu was a simpler way to view each graph required and could fit everything into one .py file
# Function for Q1 a) Plot a bar graph depicting the highest mark of each student
def highest_marks(grades):

    # Had to put plt.close() in because it kept generating an extra figure for each menu choice
    plt.close()
    highest_marks = grades.max()
    plt.figure(figsize=(12, 8))
    highest_marks.plot(kind='bar', color='skyblue')
    plt.title('Highest Mark of Each Student')
    plt.xlabel('Students')
    plt.ylabel('Marks')
    plt.show()


# Function for Q1 b) Plot a bar graph showing the lowest mark in each test
def lowest_marks(grades):
    plt.close()
    lowest_marks = grades.min(axis=1)
    plt.figure(figsize=(12, 8))
    lowest_marks.plot(kind='bar', color='lightgreen')
    plt.title('Lowest Mark in Each Test')
    plt.xlabel('Tests')
    plt.ylabel('Marks')
    plt.show()


# Function for Q2 a) Plot a bar graph depicting movies with their IMDB score greater than or equal to 8
def movie_scores(movies):
    plt.close()  # Close any existing figures
    high_score_movies = movies[movies['IMDB'] >= 8]
    fig, ax = plt.subplots(figsize=(12, 8))  # Create a new figure and a new axes.
    high_score_movies.plot(x='Title', y='IMDB', kind='bar', color='orange', legend=False, ax=ax)
    ax.set_title('Movies with IMDB Score Greater or Equal to 8')
    ax.set_xlabel('Movie Title')
    ax.set_ylabel('IMDB Score')
    # Had to get creative to stop the movie titles from cropping
    ax.tick_params(axis='x', rotation=60, labelright=True)  # Rotate the x-axis labels to 60 degrees and align them to the right
    plt.subplots_adjust(bottom=0.4)  # Adjust the bottom margin
    plt.show()


# Function for Q2 b) Plot a bar graph showing movies from the 70s with their IMDB score
def movies70s(movies):
    plt.close()  # Close any existing figures
    movies_70s = movies[movies['Year'].between(1970, 1979)]
    fig, ax = plt.subplots(figsize=(14, 8))  # Create a new figure and a new axes.
    movies_70s.plot(x='Title', y='IMDB', kind='bar', color='purple', legend=False, ax=ax)
    ax.set_title('Movies from the 70s with IMDB Score')
    ax.set_xlabel('Movie Title')
    ax.set_ylabel('IMDB Score')
    plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels to 45 degrees and align them to the right
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin
    plt.show()


# Function for Q2 c) Plot a bar graph displaying movies of the director John Carpenter with the IMDB score
def john_carpenter_movies(movies):
    plt.close()  # Close any existing figures
    carpenter_movies = movies[movies['Director'] == 'John Carpenter']
    fig, ax = plt.subplots(figsize=(14, 8))  # Create a new figure and a new axes.
    carpenter_movies.plot(x='Title', y='IMDB', kind='bar', color='teal', legend=False, ax=ax)
    ax.set_title('Movies of John Carpenter with IMDB Score')
    ax.set_xlabel('Movie Title')
    ax.set_ylabel('IMDB Score')
    plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels to 45 degrees and align them to the right
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin
    plt.show()


# Main menu function to loop between all the graphs in the assignments
def main_menu():
    grades_csv = pd.read_csv('grades.csv')
    movies_csv = pd.read_csv('movies.csv')
    while True:
        print("\nMenu:")
        print("1. Plot a bar graph depicting the highest mark of each student")
        print("2. Plot a bar graph showing the lowest mark in each test")
        print("3. Plot a bar graph depicting movies with their IMDB score greater than or equal to 8")
        print("4. Plot a bar graph showing movies from the 70s with their IMDB score")
        print("5. Plot a bar graph displaying movies of the director John Carpenter with the IMDB score")
        print("0. Exit")
        choice = input("Enter your choice (0, 1, 2, 3, 4, 5): ")

        if choice == '1':
            highest_marks(grades_csv)
        elif choice == '2':
            lowest_marks(grades_csv)
        elif choice == '3':
            movie_scores(movies_csv)
        elif choice == '4':
            movies70s(movies_csv)
        elif choice == '5':
            john_carpenter_movies(movies_csv)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
