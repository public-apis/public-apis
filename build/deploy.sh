#!/bin/bash

set -o errexit -o nounset

rev=$(git rev-parse --short HEAD)

mkdir deploy
cd deploy

git init
git config --global user.name $GH_USER
git config --global user.email $GH_EMAIL

git remote add upstream "https://$GH_TOKEN@github.com/toddmotto/public-apis.git"
git fetch upstream
git reset upstream/master

mv ../../json .

git add json/
git commit -m "rebuild JSON at ${rev}" -m "[ci skip]"
git push upstream HEAD:master

