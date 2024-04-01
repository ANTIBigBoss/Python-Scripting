import pandas as pd

generator_dict = {
    'gen1': [122.5, 122.7, 123.0],
    'gen2': [120.2, 127.0, 125.1],
    'gen3': [121.7, 124.9, 126.0],
    'gen4': [122.9, 123.8, 126.7],
    'gen5': [121.5, 124.7, 122.6]
}
generator_df = pd.DataFrame(generator_dict, index=['Volt 1', 'Volt 2', 'Volt 3'])
print(generator_df)

print("\nGenerator 2 Voltages:")
print(generator_df['gen2'])

generator3_mean = generator_df['gen3'].mean()
print("\nGenerator 3 Mean Voltage: {:.1f} Volts".format(generator3_mean))

max_voltage = generator_df.max().max()
max_gen_col = generator_df.idxmax(axis=0)[generator_df.max(axis=0) == max_voltage].index[0]
max_gen_row = generator_df.max(axis=1).idxmax()
max_gen_name = 'Generator ' + max_gen_col.replace('gen', '')

print("\nMaximum Voltage: {:.1f} Volts @ {} {}".format(max_voltage, max_gen_name, max_gen_row))
