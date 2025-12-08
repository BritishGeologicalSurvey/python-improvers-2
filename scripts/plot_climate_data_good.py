"""
Script to generate figures for climate paper.

Run with `python climate_paper_figs.py`.
"""
import csv
from io import StringIO
import logging
from pathlib import Path

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

logger = logging.getLogger("climate_paper")
DATA_DIR = Path(__file__).parent.parent / "data"
RESULTS_DIR = Path(__file__).parent.parent / "results"

# This message is used to demonstrate that code is run when module is imported.
print(f"Hello from {__file__} body!")


def plot_climate_paper_figs_and_csv(data_dir: Path, work_dir: Path) -> None:
    """
    Read files from data_dir and plot graphs of daily maximum temperature and
    a .csv file of mean maximum temperatures.  Output files are stored in
    work_dir.
    """
    mean_max_temps = []  # store for mean max temp data

    for data_file in data_dir.glob("*data.txt"):
        logger.info("Processing %s", data_file.name)

        try:
            station_data = read_metoffice_file(data_file)
        except Exception:
            logger.exception("Failed to read %s", data_file)
            continue

        station_name = get_station_name(data_file)

        plot_max_temp_png(station_data, station_name)
        max_mean_temp = calculate_mean_maximum_temperature(station_data)
        mean_max_temps.append({"location": station_name, "max_temp": max_mean_temp})

    csv_file = RESULTS_DIR / "max_temps.csv"
    write_max_temps_csv_file(mean_max_temps, csv_file)


def read_metoffice_file(data_file: Path) -> pd.DataFrame:
    """
    Read Met Office Historic Station data file into Pandas dataframe.
    """
    clean_pseudo_file = _preprocess_metoffice_file(data_file)

    # Define column names and missing value indicators
    column_names = ['year', 'month', 'tmax', 'tmin', 'frost_days', 'rain_mm', 'sun']
    missing_values = {
        'tmax': '---',
        'tmin': '---',
        'frost_days': '---',
        'rain_mm': '---',
        'sun': '---'
    }

    # Read the cleaned lines, skipping the first lines of metadata
    # and the "provisional" data from the end of the file.
    df = pd.read_csv(
        clean_pseudo_file,
        sep=r"\s+",
        skiprows=7,
        names=column_names,
        na_values=missing_values,
        on_bad_lines="skip",
    )

    # Create an index with the dates
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    df.set_index('date', inplace=True)
    df.drop(columns=['year', 'month'], inplace=True)

    # Some data values have '*' or '#' appended to them.
    # Force these to numeric values, returning NaN if it isn't possible.
    for column in column_names[2:]:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    logger.debug("%s rows loaded", len(df))

    return df


def get_station_name(data_file: Path) -> str:
    return data_file.name.replace("data.txt", "")


def calculate_mean_maximum_temperature(station_data: pd.DataFrame) -> float:
    mean_max_temp = station_data['tmax'].mean()
    logger.debug("Mean maximum temperature: %s", mean_max_temp)
    return mean_max_temp


def plot_max_temp_png(station_data: pd.DataFrame, station_name: str, work_dir: Path = RESULTS_DIR):
    """
    Generate a .png file in the working directory with a plot of max temp.
    """
    fig = plot_max_temp_figure(station_data, station_name)
    fig.savefig(f"{work_dir / station_name}.png", dpi=150)
    plt.close(fig)


def plot_max_temp_figure(station_data: pd.DataFrame, station_name: str) -> Figure:
    fig, ax = plt.subplots()
    ax = station_data['tmax'].plot(kind='line', ax=ax)
    ax.set_title(station_name)
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature degC')
    return fig


def write_max_temps_csv_file(
    mean_max_temp_data: list[dict[str, float]], csv_file: Path
):
    """
    Use Python's inbuilt `csv` library to write data to csv file.
    """
    logger.info("Writing CSV data to %s", csv_file)
    field_names = ["location", "max_temp"]

    # newline must be specified to stop Windows adding extra linebreaks
    with open(csv_file, "wt", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(mean_max_temp_data)


def _preprocess_metoffice_file(data_file: Path) -> StringIO:
    """
    Create file-like StringIO object containing cleaned version of original
    file.  Removes "Station closed" lines e.g. from cwmystwythdata.txt.
    """
    logger.debug("Preprocessing %s", data_file)

    clean_lines = []
    with open(data_file, "r") as input_file:
        clean_lines = [
            line for line in input_file if "site closed" not in line.casefold()
        ]

    return StringIO("".join(clean_lines))


if __name__ == "__main__":
    # This message is not displayed when module is imported.
    print(f"{__file__} is being run as a script!")

    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s - %(levelname)s: %(message)s",
    )

    RESULTS_DIR.mkdir(exist_ok=True)
    plot_climate_paper_figs_and_csv(DATA_DIR, RESULTS_DIR)
