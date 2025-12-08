#! /bin/bash

# This shell script can be used on a Linux system to download the latest
# versions of the weather data.

# Data are taken from the Met Office's Historic station data page.
# https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data

# Note that some files then require manual alteration of the header to ensure
# that the read data start on line 8.  This involves concatenating location data
# where it is spread across multiple rows.  `braemardata.txt` is an example.

# Change to script directory
cd "$(dirname "$0")";

wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/aberporthdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/armaghdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/ballypatrickdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/bradforddata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/braemardata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/cambornedata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/cambridgedata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/cardiffdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/chivenordata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/cwmystwythdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/dunstaffnagedata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/durhamdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/eastbournedata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/eskdalemuirdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/hurndata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/lerwickdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/leucharsdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/lowestoftdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/manstondata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/nairndata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/newtonriggdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/paisleydata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/ringwaydata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/rossonwyedata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/shawburydata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/sheffielddata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/southamptondata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/stornowaydata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/suttonboningtondata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/tireedata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/valleydata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/waddingtondata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/whitbydata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/wickairportdata.txt"
wget "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/yeoviltondata.txt"