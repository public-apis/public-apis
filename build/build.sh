#!/bin/bash

mkdir -p ../json
node md2json.js ../README.md > ../json/api.min.json
python -m json.tool ../json/api.min.json > ../json/api.json
cat ../json/api.json
