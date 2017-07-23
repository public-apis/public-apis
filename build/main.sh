#!/bin/bash
FORMAT_FILE=../README.md
if [ "$TRAVIS_PULL_REQUEST" != "false" ]; then
    echo "running on Pull Request #$TRAVIS_PULL_REQUEST"
    git show | egrep "\+" > additions.txt
    echo "--ADDITIONS--"
    cat additions.txt
    LINK_FILE=additions.txt
else
    echo "running on $TRAVIS_BRANCH branch"
    LINK_FILE=../README.md
fi

echo "running format validation..."
./validate_format.rb $FORMAT_FILE
if [[ $? != 0 ]]; then
    echo "format validation failed!"
    exit 1
else
    echo "format validation passed!"
fi

echo "running link validation..."
./validate_links.rb $LINK_FILE
if [[ $? != 0 ]]; then
    echo "link validation failed!"
    exit 1
else
    echo "link validation passed!"
fi
