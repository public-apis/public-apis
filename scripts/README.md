# glibc Public API Index — Scripts

This directory contains the validation, indexing, and testing scripts used to
maintain the **glibc Public API Index** (`README.md`).

```bash
scripts
├── build_index.py        # parse README.md -> site/data/index.json (static search index)
├── requirements.txt      # dependencies of the validate package
│
├── tests                 # unit tests for the validate package
│       test_validate_format.py
│       test_validate_links.py
│       test_helpers.py
│
└── validate              # validate package
        format.py         # 5-column table format checker
        links.py          # external link health checker
```

## Install dependencies

You must have [Python](https://www.python.org/) installed to use these scripts.

Install the validation package dependencies with [pip](https://pypi.org/project/pip/):

```bash
$ python -m pip install -r scripts/requirements.txt
```

## Run validations

To run format validation on `README.md`, being in the root directory of the
repository, run:

```bash
$ python scripts/validate/format.py README.md
```

To run link validation on `README.md`, being in the root directory of the
repository, run:

```bash
$ python scripts/validate/links.py README.md
```

As there are many links to check, this process can take some time. If your goal
is not to check whether the links are working, you can check only for duplicate
links (zero network). Run:

```bash
$ python scripts/validate/links.py README.md -odlc
```

*`-odlc` is an abbreviation of `--only_duplicate_links_checker`*

## Build the search index

`build_index.py` parses `README.md` (5-column tables) into a structured JSON
index consumed by the static search site under `site/`:

```bash
$ python scripts/build_index.py README.md site/data/index.json
```

## Running Tests

To run all tests it is necessary to change to the `scripts` directory:

```bash
$ cd scripts
```

then run:

```bash
$ python -m unittest discover tests/ --verbose
```

To run only the format tests, run:

```bash
$ python -m unittest discover tests/ --verbose --pattern "test_validate_format.py"
```

To run only the links tests, run:

```bash
$ python -m unittest discover tests/ --verbose --pattern "test_validate_links.py"
```
