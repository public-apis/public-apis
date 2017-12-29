#!/bin/bash

# create json directory if not already present
mkdir -p ../json
# parse API README and print (minified) JSON to stdout, redirect to /json
./md2json.py ../README.md > ../json/entries.min.json
# beautify the previously created JSON file, redirect to /json
python -m json.tool ../json/entries.min.json > ../json/entries.json
