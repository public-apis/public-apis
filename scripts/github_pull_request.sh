#!/usr/bin/env bash

set -e

# Argument validation
if [ $# -ne 3 ]; then
    echo "Usage: $0 <github-repo> <pull-number> <filename>"
    exit 1
fi

# Assign variables
GITHUB_REPOSITORY="$1"
GITHUB_PULL_REQUEST="$2"
FILENAME="$3"

# Move to root of project
cd "$GITHUB_WORKSPACE"

# Determine files
FILENAME="$( realpath "${FILENAME}" )"

# Skip if build number could not be determined
if [ -z "$GITHUB_REPOSITORY" -o -z "$GITHUB_PULL_REQUEST" ]; then
    echo "No pull request and/or repository is provided"
    exit 1
fi

# Pull changes on PR
echo "running on Pull Request #$GITHUB_PULL_REQUEST"

# Trick the URL validator python script into not seeing this as a URL
DUMMY_SCHEME="https"
DIFF_URL="$DUMMY_SCHEME://patch-diff.githubusercontent.com/raw/$GITHUB_REPOSITORY/pull/$GITHUB_PULL_REQUEST.diff"
curl -L "$DIFF_URL" -o diff.txt

# Construct diff
echo "------- BEGIN DIFF -------"
cat diff.txt
echo "-------- END DIFF --------"
cat diff.txt | egrep "\+" > additions.txt

echo "------ BEGIN ADDITIONS -----"
cat additions.txt
echo "------- END ADDITIONS ------"
LINK_FILE=additions.txt

# Validate links
echo "Running link validation on additions..."
python scripts/validate/links.py "$LINK_FILE"

# Vebosity
if [[ $? != 0 ]]; then
    echo "link validation failed on additions!"
    exit 1
else
    echo "link validation passed on additions!"
fi
