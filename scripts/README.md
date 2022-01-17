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

*Note that it is necessary to have [python](https://www.python.org/) installed.*
