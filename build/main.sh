#!/bin/bash

echo "running format validation..."
./validate.rb ../README.md

if [[ $? != 0 ]]; then
    echo "format validation failed!"
    exit $?
else
    echo "format validation passed!"
fi

if [ "$TRAVIS_BRANCH" == "master" ]; then
    echo "running link validation..."
    awesome_bot ../README.md --allow-ssl --allow 403,302
fi
