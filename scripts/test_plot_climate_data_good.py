"""
Tests for plot_climate_data_good.py
"""
from pathlib import Path

import pandas as pd
import pytest

from plot_climate_data_good import (
    calculate_mean_maximum_temperature,
    get_station_name,
    read_metoffice_file,
)


def test_get_station_name():
    # Arrange
    test_data_file = Path("someplacedata.txt")
    expected_name = "someplace"

    # Act
    station_name = get_station_name(test_data_file)

    # Assert
    assert station_name == expected_name


def test_read_met_office_file():
    # Arrange
    test_data_file = Path(__file__).parent / "exampledata.txt"

    # Act
    data = read_metoffice_file(test_data_file)

    # Assert
    assert isinstance(data, pd.DataFrame)
    assert data.index.name == 'date'
    assert data.columns.to_list() == ['tmax', 'tmin', 'frost_days', 'rain_mm', 'sun']


def test_calculate_mean_maximum_temperature():
    # Arrange
    test_data_file = Path(__file__).parent / "exampledata.txt"

    # Act
    data = read_metoffice_file(test_data_file)
    mean_max_temp = calculate_mean_maximum_temperature(data)

    # Assert
    assert mean_max_temp == pytest.approx(12.35, abs=0.01)
