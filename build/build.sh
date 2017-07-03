#!/bin/bash

# create json directory if not already present
mkdir -p ../json
# parse API README and print (minified) JSON to stdout, redirect to /json
node md2json.js ../README.md > ../json/entries.min.json
# beautify the previously created JSON file, redirect to /json
python -m json.tool ../json/entries.min.json > ../json/entries.json
# print out pretty JSON (useful for debugging, checking for new entries, etc)
cat ../json/entries.json
