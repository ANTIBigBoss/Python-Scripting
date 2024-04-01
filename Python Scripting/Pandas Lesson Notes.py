import pandas as pd

# Creating a Series with default index
grades = pd.Series([87, 100, 94])
print("Grades Series:")
print(grades)

# Creating a Series with floating values and a custom index
floating = pd.Series(98.6, range(3))
print("\nFloating Series:")
print(floating)

# Series methods used in statistical analysis
print("\nSeries Statistical Methods:")
print("Count:", grades.count())
print("Mean:", grades.mean())
print("Min:", grades.min())
print("Max:", grades.max())
print("Standard Deviation:", grades.std())

# Describing a Series, which shows a summary of statistics
print("\nDescribe Series:")
print(grades.describe())

# Creating Series with custom indices
arduinoUNO = pd.Series([14, 6, 3], index=['digital', 'analog', 'timers'])
print("\nArduino UNO Series with custom indices:")
print(arduinoUNO)

# Dictionary initializers for Series
arduinoUNO_dict = pd.Series({'digital': 14, 'analog': 6, 'timers': 3})
print("\nArduino UNO Series created from a dictionary:")
print(arduinoUNO_dict)

# Accessing elements in a Series
print("\nAccessing elements in Arduino UNO Series:")
print("Analog:", arduinoUNO['analog'])
print("Digital:", arduinoUNO.digital)

# Creating a DataFrame from a dictionary
grades_dict = {
    'Wally': [87, 96, 70],
    'Eva': [100, 87, 90],
    'Sam': [94, 77, 90],
    'Katie': [100, 81, 82],
    'Bob': [83, 65, 85]
}
grades_df = pd.DataFrame(grades_dict)

print("\nDataFrame created from dictionary:")
print(grades_df)

# Setting custom index for the DataFrame
grades_df.index = ['Test1', 'Test2', 'Test3']
print("\nDataFrame with custom index:")
print(grades_df)

# Exercise 1: Creating a DataFrame from a dictionary and counting values greater than 50
n_dict = {
    'A': [56, 29, 83],
    'B': [71, 63, 60],
    'C': [13, 34, 71]
}
n = pd.DataFrame(n_dict)
n.index = ['1', '2', '3']
print("\nExercise 1 DataFrame:")
print(n)
print('Number of values greater than 50:', n[n > 50].count().sum())

# Exercise 2: Creating a DataFrame from a dictionary representing a table of generators
generator_dict = {
    '1st generator': [122.5, 122.7, 123.0],
    '2nd generator': [120.2, 127.0, 125.1],
    '3rd generator': [121.7, 124.9, 126.0],
    '4th generator': [122.9, 123.8, 126.7],
    '5th generator': [121.5, 124.7, 122.6]
}
generator_df = pd.DataFrame(generator_dict, index=['Measurement 1', 'Measurement 2', 'Measurement 3'])
print("\nExercise 2 DataFrame:")
print(generator_df)
print(generator_df)

# Print a Series of voltages for Generator 2
print("\nGenerator 2 Voltages:")
print(generator_df['2nd generator'])

# Calculate and print the mean voltage for Generator 3
generator3_mean = generator_df['3rd generator'].mean()
print("\nGenerator 3 Mean Voltage:", generator3_mean, "Volts")

# Find and print the maximum voltage and the corresponding generator
max_voltage = generator_df.max().max()
max_gen = generator_df.idxmax(axis=1)[generator_df.max(axis=1) == max_voltage].index[0]
print("\nMaximum Voltage:", max_voltage, "Volts @", max_gen)

# Exercise 3: Creating a DataFrame for a table of city populations
cities_dict = {
    'city': ['Bombay', 'Calcutta', 'Delhi', 'Dhaka', 'Jakarta', 'Lagos', 'Mexico City', 'New York', 'Sao Paulo', 'Tokyo'],
    'country': ['India', 'India', 'India', 'Bangladesh', 'Indonesia', 'Nigeria', 'Mexico', 'USA', 'Brazil', 'Japan'],
    'pop2005': [18.2, 14.3, 15.1, 12.4, 13.0, 11.0, 19.0, 18.5, 18.2, 35.2],
    'pop2015': [22.6, 16.8, 20.9, 17.9, 17.5, 17.0, 20.6, 19.7, 20.0, 36.2]
}

cities_df = pd.DataFrame(cities_dict)
print("\nExercise 3 DataFrame:")
print(cities_df)

# Using describe() to get a summary of the population statistics from exercise 3
pop_stats = cities_df.describe()
print("\nPopulation Statistics:")
print(pop_stats)
