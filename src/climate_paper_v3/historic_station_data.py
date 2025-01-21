"""
Classes that read and process historic climate station data.
"""
import csv
from io import StringIO
import logging
from pathlib import Path

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

logger = logging.getLogger(__name__)


class MetOfficeHistoricStationData:
    """
    Historic station data from Met Office files.
    """
    def __init__(self, data_file: Path) -> None:
        logger.info("Processing %s", data_file.name)
        self._data_file = data_file
        self.station_data = read_metoffice_file(data_file)
        self.station_name = get_station_name(data_file)

    def mean_maximum_temperature(self) -> float:
        mean_max_temp = self.station_data['tmax'].mean()
        logger.debug("Mean maximum temperature: %s", mean_max_temp)
        return mean_max_temp

    def plot_max_temp_png(self, work_dir: Path):
        """
        Generate a .png file in the working directory with a plot of max temp.
        """
        fig = self.plot_max_temp_figure()
        fig.savefig(f"{work_dir / self.station_name}.png", dpi=150)
        plt.close(fig)

    def plot_max_temp_figure(self) -> Figure:
        fig, ax = plt.subplots()
        ax = self.station_data['tmax'].plot(kind='line', ax=ax)
        ax.set_title(self.station_name)
        ax.set_xlabel('Year')
        ax.set_ylabel('Temperature degC')
        return fig
    
    def __repr__(self) -> str:
        return f"MetOfficeHistoricStationData for {self.station_name}"


# These functions do not depend on the internal data of the class.
# They can be defined as module-level functions or as static methods on the
# class.
def read_metoffice_file(data_file: Path) -> pd.DataFrame:
    """
    Read Met Office Historic Station data file into Pandas dataframe.
    """
    clean_pseudo_file = _preprocess_metoffice_file(data_file)

    # Define column names and missing value indicators
    column_names = ['year', 'month', 'tmax', 'tmin', 'frost_days', 'rain_mm', 'sun']
    missing_values = {'tmax': '---', 'tmin': '---', 'frost_days': '---', 'rain_mm': '---', 'sun': '---'}

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




def write_max_temps_csv_file(
    mean_max_temp_data: list[dict[str, float]], csv_file: Path
):
    """
    Use Python's inbuilt `csv` library to write data to csv file.
    """
    field_names = ["location", "max_temp"]

    # newline must be specified to stop Windows adding extra linebreaks
    with open(csv_file, "wt", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(mean_max_temp_data)
