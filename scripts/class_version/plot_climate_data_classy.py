"""
Script to generate figures for climate paper.

Run with `python climate_paper_figs.py`.
"""
import csv
import logging
from pathlib import Path

from historic_station_data import MetOfficeHistoricStationData

logger = logging.getLogger("climate_paper")
WORK_DIR = Path(__file__).parent.parent.parent / "work"
DATA_DIR = Path(__file__).parent.parent.parent / "data"

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
        try:
            met_office_data = MetOfficeHistoricStationData(data_file)
        except Exception:
            logger.exception("Failed to read %s", data_file)
            continue

        mean_max_temps.append(
            {
                "location": met_office_data.station_name,
                "max_temp": met_office_data.mean_maximum_temperature(),
            }
        )
        met_office_data.plot_max_temp_png(work_dir)

    csv_file = work_dir / "max_temps.csv"
    write_max_temps_csv_file(mean_max_temps, csv_file)


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


if __name__ == "__main__":
    # This message is not displayed when module is imported.
    print(f"{__file__} is being run as a script!")

    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s - %(levelname)s: %(message)s",
    )

    WORK_DIR.mkdir(exist_ok=True)
    plot_climate_paper_figs_and_csv(DATA_DIR, WORK_DIR)
