[![tests](https://github.com/yavv951/api_tests_store/actions/workflows/tests.yml/badge.svg)](https://github.com/yavv951/api_tests_store/actions/workflows/tests.yml)
# Python Project REST API Store Testing

This is a tutorial project that shows how to implement api tests in Python

The project uses:
1. Python
2. Requests
3. Allure for reports
4. CI (GitHub actions)


Testing application (write with Flask):

git: https://github.com/yavv951/api_tests_store

url: https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/


### How to start

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```

and add pre-commit
```
pre-commit install
```

### Run all tests

```python
pytest
```
