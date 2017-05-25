#!/bin/bash

node md2json.js ../README.md > ../json/api.json
cat ../json/api.json
