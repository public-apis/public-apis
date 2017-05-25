#!/bin/bash

set -o errexit -o nounset

if [ "$TRAVIS_BRANCH" != "master" ]
then
  echo "This commit was made against $TRAVIS_BRANCH and not master! No deploy!"
  exit 0
fi

rev=$(git rev-parse --short HEAD)

mkdir deploy
cd deploy

git init
git config --global user.name "Travis CI"
git config --global user.email "build@travis.org"

git remote add upstream "https://$GH_TOKEN@github.com/davemachado/public-apis.git"
git fetch upstream
git reset upstream/master

mv ../../json .

git add json/
git commit -m "rebuild JSON at ${rev}"
git push upstream HEAD:master

