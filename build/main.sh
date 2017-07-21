#!/bin/bash
CHECK_FILE=../README.md
echo "running format validation..."
./validate_format.rb $CHECK_FILE
if [[ $? != 0 ]]; then
    echo "format validation failed!"
    exit 1
else
    echo "format validation passed!"
fi

if [ "$TRAVIS_BRANCH" == "master" ]; then
    echo "running link validation..."
    ./validate_links.rb $CHECK_FILE
    if [[ $? != 0 ]]; then
        echo "link validation failed!"
        exit 1
    else
        echo "link validation passed!"
    fi
fi
