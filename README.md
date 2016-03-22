# Flask Boilerplate

This repository contains example minimal Flask application structure that includes:

* SQLAlchemy
* Alembic
* Celery
* py.test

## Installation

Firstly clone the repository and create virtualenv. Then install requirements:

`$ pip install -r requirements.txt`

Before running the application make sure that your local PostgreSQL server is up. The create the databases:

```
CREATE DATABASE flask_example;
CREATE DATABASE flask_example_test;
```

Now you can create tables using Alembic:

`./manage.py db upgrade`

Finally you can run the application:

`./manage.py runserver`

or play in Python REPL:

`./manage.py shell`

In order to run unit tests in py.test you can invoke:

`./manage.py test`


## Contribution

We are happy to see your way of scaffolding Flask applications. Feel free to submit an issue with your ideas or comments.
