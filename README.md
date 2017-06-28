# postalcodeareas-fi

This package provides Finnish postal code area boundary
coordinates and area center coordinates packaged into
Python dictionaries. Additionally, there are some
utilities to convert the data to KML or geojson.

The data when fetched and built is about 15MB so you
may want to instead store it into a database though.

## Installation

Install from PyPI. Alternatively, check out the source,
cd into the directory having the `flit.ini` file and run:

    flit install

## Building the data

Check out the source, cd to directory containing the
`rebuild.py` module, and run it:

    python rebuild.py --help

Then use the (re)builder script as instructed. To use
data from the Google Fusion table created by Duukkis, you
should get an API key from Google as well. To use data
provided by Statistics Finland, using the Paavo API, no
api key is needed.

## Using the data

After building the data, just do:

    from postalcodeareas_fi.data import areas, centers
