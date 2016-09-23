[![Build Status](https://travis-ci.org/sunscrapers/flask-boilerplate.svg?branch=master)](https://travis-ci.org/sunscrapers/flask-boilerplate)

# Flask Boilerplate

This repository contains a sample minimal Flask application structure that includes:

* SQLAlchemy
* Alembic
* Celery
* py.test

It runs on both Python 2.7 and 3.5.

## Installation

First, clone the repository and create a virtualenv. Then install the requirements:

`$ pip install -r requirements.txt`

Before running the application make sure that your local PostgreSQL server is up. Then create the databases:

```
CREATE DATABASE flask_example;
CREATE DATABASE flask_example_test;
```

Now you can create the tables using Alembic:

`./manage.py db upgrade`

Finally you can run the application:

`./manage.py runserver`

or play in the Python REPL:

`./manage.py shell`

In order to run unit tests in py.test invoke:

`./manage.py test`


## Contribution

We are happy to see your way of scaffolding Flask applications. Feel free to submit an issue with your ideas or comments.
