# Project setup

The [pipenv](https://docs.pipenv.org) tool is using as a dependencies management tool

```bash
pipenv shell
python manage.py runserver
```

# Other

## Pipenv commands

```bash
# activate the virtual environment
pipenv shell

# install deps
pipenv sync


# install dev deps
pipenv sync --dev


# install new dependency
pipenv istall requests
pipenv istall --dev httpx

# lock dependencies. Update the Pipfile.lock
pipenv lock
```
