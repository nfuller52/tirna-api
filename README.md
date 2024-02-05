# Tirna

## Local Setup

### Prerequisites

- [Python 3.12.1](https://www.python.org/downloads/)
- [Postgres 16]()
- [Pipenv](https://github.com/pypa/pipenv?tab=readme-ov-file#installation)

### Initial Setup

_All commands are run from the `./api` directory._

1. Start the virtual environment

```sh
pipenv shell
```

2. Install dependencies

```sh
pipenv install
```

3. Create the development db

```sh
createdb tirna_development
```

4. Migrate the database

```sh
python manage.py migrate
```
