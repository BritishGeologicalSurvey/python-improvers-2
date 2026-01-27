"""
Tests for historic station data classes.
"""
from textwrap import dedent

from .historic_station_data import MetOfficeHistoricStationData


def test_met_office_historic_station_data(tmp_path):
    # Arrange
    test_file = tmp_path / "teststationdata.txt"
    contents = dedent("""
    Yeovilton
    Location: 355100E 123200N, Lat 51.006 Lon -2.641, 20 metres amsl
    Estimated data is marked with a * after the value.
    Missing data (more than 2 days missing in month) is marked by  ---.
    Sunshine data taken from an automatic Kipp & Zonen sensor marked with a #, otherwise sunshine data taken from a Campbell Stokes recorder.
    yyyy  mm   tmax    tmin      af    rain     sun
                degC    degC    days      mm   hours
    1964   9    1.0     8.8       0    37.4     ---
    1964  10    2.0     4.2       5    77.8     ---
    1964  11    3.0     4.7       3    45.5     ---
    1964  12    4.0     0.1      17    65.1     ---
    1965   1    5.0     0.8      14    74.6     ---
    """).strip()  # noqa
    test_file.write_text(contents)

    # Act
    met_office_data = MetOfficeHistoricStationData(test_file)

    # Assert
    assert met_office_data.station_name == "teststation"
    assert met_office_data.mean_maximum_temperature() == 3.0
