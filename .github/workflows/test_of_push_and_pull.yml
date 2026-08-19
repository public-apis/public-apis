name: "Tests of push & pull"

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

env:
  FILENAME: README.md

jobs:
  tests:
    name: 'Validate README.md changes'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: python -m pip install -r scripts/requirements.txt

      - name: Validate Markdown format
        run: python scripts/validate/format.py ${FILENAME}

      - name: Validate pull request changes
        run: scripts/github_pull_request.sh ${{ github.repository }} ${{ github.event.pull_request.number }} ${FILENAME}
        if: github.event_name == 'pull_request'

      - name: Checking if push changes are duplicated
        run: python scripts/validate/links.py ${FILENAME} --only_duplicate_links_checker
        if: github.event_name == 'push'
