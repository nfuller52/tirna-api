# Tirna

## Local Setup

### API

#### Prerequisites

- [Python 3.12.1](https://www.python.org/downloads/)
- [Postgres 16]()
- [Pipenv](https://github.com/pypa/pipenv?tab=readme-ov-file#installation)

#### Initial Setup

_All commands are run from the `./api` directory._

1. Install dependencies

```sh
pipenv install
```

2. Start the virtual environment

```sh
pipenv shell
```

3. Create the development db

```sh
createdb tirna_api_development
```

4. Migrate the database

```sh
python manage.py migrate
```

---
### Web

#### Prerequisites

- [NodeJS 20.x (20.11.0)](https://nodejs.org/en/download)
- [pnpm >= 8.15.1](https://pnpm.io/installation)
- [Tirna API](https://github.com/nfuller52/tirna)

#### Initial Setup

_All commands are run from the `./web` directory._

1. Download dependencies

```sh
pnpm install
```
