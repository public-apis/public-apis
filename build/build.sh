#!/bin/bash

mkdir -p ../json
node md2json.js ../README.md > ../json/api.json
cat ../json/api.json
ls -l ..
ls -l ../json
