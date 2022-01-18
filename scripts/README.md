# Public APIs Scripts

This directory contains all validation and testing scripts used by Public APIs.

```bash
scripts
│   github_pull_request.sh  # used to validate changes of a pull request
│   requirements.txt  # contains dependencies of validate package
│
├───tests  # contains all unit tests from the validate package
│       test_validate_format.py
│       test_validate_links.py
│
└───validate  # validate package
        format.py
        links.py
```

## Install dependencies

You must have [python](https://www.python.org/) installed to use these scripts.

it is also necessary to install the validation package dependencies, use [pip package manager](https://pypi.org/project/pip/) for this:

```bash
$ python -m pip install -r scripts/requirements.txt
```

## Run validations

To run format validation on the `README.md` file, being in the root directory of public-apis, run:

```bash
$ python scripts/validate/format.py README.md
```

To run link validation on the `README.md` file, being in the root directory of public-apis, run:

```bash
$ python scripts/validate/links.py README.md
```

As there are many links to check, this process can take some time. If your goal is not to check if the links are working, you can only check for duplicate links. Run:

```bash
$ python scripts/validate/links.py README.md -odlc
```

*`-odlc` is an abbreviation of `--only_duplicate_links_checker`*

## Running Tests

To run all tests it is necessary to change to the scripts directory:

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
