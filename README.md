# postalcodeareas-fi
Finnish postal code areas

This package provides Finnish postal code area boundary
coordinates and area center coordinates packaged into
Python dictionaries. Additionally, there are some
utilities to convert the data to KML or geojson.

## Installation

Install from PyPI. Alternatively, check out the source,
cd into the directory having the `flit.ini` file and run:

    flit install

## Building the data

Check out the source, cd to directory containing the
`rebuild.py` module, and run it. To use data from the
Google Fusion table created by Duukkis, you should
get an API key from Google as well. To use data provided
by Statistics Finland, using the Paavo API, no api key
is needed.

## Using the data

Just do:

    from postalcodeareas_fi.data import areas, centers
