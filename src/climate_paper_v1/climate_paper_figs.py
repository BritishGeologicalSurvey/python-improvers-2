from io import StringIO
import matplotlib.pyplot as plt
import os
data_Dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
work_Dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'work')

try:
    os.mkdir(work_Dir)
except FileExistsError:
    pass

if not os.path.exists(data_Dir):
    os.mkdir(data_Dir)

import csv

def ProcessFile(filename):
    print(filename)
    if filename.endswith('.txt') is False:
        # Ignore non-data files
        return

    # Define column names and missing value indicators
    columnNames = ['year', 'month', 'tmax', 'tmin', 'frost_days', 'rain_mm', 'sun']
    mvs = {'tmax': '---', 'tmin': '---', 'frost_days': '---', 'rain_mm': '---', 'sun': '---'}

    # Create pseudo-file that has removed the Site closed lines from
    # any files that have it e.g. cwmystwythdata.txt.
    clean = []
    with open(os.path.join(data_Dir, filename), 'r') as file:
        for lines in file:
            if 'site closed' not in lines.casefold():  # Skip lines containing 'Site closed'
                clean += [lines]
    cleaned_pseudo_file = StringIO(''.join(clean))

    # Read the cleaned lines, skipping the first lines of metadata
    # and the "provisional" data from the end of the file.
    import pandas as pd
    df = pd.read_csv(cleaned_pseudo_file, sep='\s+', skiprows=8, names=columnNames, na_values=mvs, on_bad_lines='warn')
    print(len(df))

    # Create an index with the dates
    df['date'] = pd.to_datetime(df[['year', 'month']]
                                      .assign(day=1))
    df.set_index('date', inplace=True)
    df.drop(columns=['year', 'month'], inplace=True)

    # Some data values have '*' or '#' appended to them.
    # Force these to numeric values, returning NaN if it isn't possible.
    for c in columnNames[2:]:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    
    f .write(f"{filename.replace("data.txt", "")},{df['tmax'].mean()}\n")
    ax = df['tmax'].plot(kind='line')
    ax.set_title(filename.replace('data.txt', ''))
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature degC')
    ax.get_figure().savefig(os.path.join(work_Dir, filename.replace('data.txt', '.png',
                                                        )), dpi=90)
    plt.close()
f = open(os.path.join(work_Dir, 'max_temps.csv'), 'wt')
f .write("location,max_temp\n")

for filename in os.listdir(os.path.join(os.path.dirname(work_Dir), 'data')):
    ProcessFile(filename)

f.close()