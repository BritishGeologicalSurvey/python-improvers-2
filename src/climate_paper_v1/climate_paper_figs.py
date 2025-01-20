from io import StringIO
import os
import pandas as pd

def ProcessFile(filename):
    print(filename)
    if not filename.endswith('.txt'):
        # Ignore non-data files
        return

    # Define column names and missing value indicators
    column_names = ['year', 'month', 'tmax', 'tmin', 'frost_days', 'rain_mm', 'sun']
    missing_values = {'tmax': '---', 'tmin': '---', 'frost_days': '---', 'rain_mm': '---', 'sun': '---'}

    # Create pseudo-file that has removed the Site closed lines from
    # any files that have it e.g. cwmystwythdata.txt.
    cleaned_lines = []
    with open('data/' + filename, 'r') as file:
        for line in file:
            if 'site closed' not in line.casefold():  # Skip lines containing 'Site closed'
                cleaned_lines.append(line)
    cleaned_pseudo_file = StringIO(''.join(cleaned_lines))

    # Read the cleaned lines, skipping the first lines of metadata
    # and the "provisional" data from the end of the file.
    df = pd.read_csv(cleaned_pseudo_file, sep='\s+', skiprows=8,
                    names=column_names, na_values=missing_values,
                    on_bad_lines='warn')

    # Create an index with the dates
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    df.set_index('date', inplace=True)
    df.drop(columns=['year', 'month'], inplace=True)

    # Some data values have '*' or '#' appended to them.
    # Force these to numeric values, returning NaN if it isn't possible.
    for column in column_names[2:]:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    max_temps_file.write(f"{filename.replace("data.txt", "")},{df['tmax'].mean()}\n")

max_temps_file = open('max_temps.csv', 'wt')
max_temps_file.write("location,max_temp\n")

for filename in os.listdir('data'):
    ProcessFile(filename)

max_temps_file.close()
