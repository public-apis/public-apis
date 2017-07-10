#!/bin/bash

if [ "$TRAVIS_BRANCH" == "master" ]
then
    awesome_bot README.md --allow-ssl --allow 403,302
fi

./validate.rb ../README.md
