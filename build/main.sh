#!/bin/bash

FORMAT_FILE=../README.md
echo "running format validation..."
./validate_format.py $FORMAT_FILE
if [[ $? != 0 ]]; then
    echo "format validation failed!"
    exit 1
fi
echo "format validation passed!"
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo "running on $TRAVIS_BRANCH branch - skipping Pull Request logic"
    exit 0
fi

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

echo "running link validation..."
./validate_links.py $LINK_FILE
if [[ $? != 0 ]]; then
    echo "link validation failed!"
    exit 1
else
    echo "link validation passed!"
fi
