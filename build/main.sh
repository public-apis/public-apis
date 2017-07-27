#!/bin/bash

FORMAT_FILE=../README.md
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo "running on $TRAVIS_BRANCH branch"
    LINK_FILE=../README.md
else
    echo "running on Pull Request #$TRAVIS_PULL_REQUEST"
    DIFF_URL="https://patch-diff.githubusercontent.com/raw/toddmotto/public-apis/pull/$TRAVIS_PULL_REQUEST.diff"
    curl $DIFF_URL > diff.txt
    echo "------- BEGIN DIFF -------"
    cat diff.txt
    echo "-------- END DIFF --------"
    cat diff.txt | egrep "\+" > additions.txt
    echo "------ BEGIN ADDITIONS -----"
    cat additions.txt
    echo "------- END ADDITIONS ------"
    LINK_FILE=additions.txt
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
