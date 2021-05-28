# Flask Example Project

## Project Dependencies (install these)

- [Python](https://www.python.org/downloads/) (almost certainly already installed)
- [Pip](https://pip.pypa.io/en/stable/cli/pip_install/)
- [Docker](https://www.docker.com/get-started) (this is for the DB)

Once you've got these installed, we can build our container and run it

```
docker run \
  --name flask-postgres \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=flask_api \
  -e POSTGRES_USER=flask_user \
  -d postgres
```

Create yourself a virtual environment. If you're unfamiliar with virtual environments, you can think of it as a way to
install dependencies for the project without needing to install these python packages to the system.

```
python3 -m venv venv
```

Connect to that virtual env

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
flask db upgrade
```

## Running the project

Once you've got all the dependencies installed you can run the project via

```
flask run
```

By defualt the project runs at `localhost:5000`, but you can change the port by setting an alternate `PORT` environment
variable if you so choose.

If you're working in vscode, a configuration has been included to allow for debugging. Open up the VS Code Run and
Debug section and click `Debug API`.

## Working in the Project

This projet is built using

- [Python](https://www.python.org/downloads/) - Still the same as above
- [Express](https://flask.palletsprojects.com/en/1.1.x/) - REST framework
- [SqlAlchemy](https://www.sqlalchemy.org/) - Python ORM

### Common Flask_SqlAlchemy migration Commands

If the schema needs to be updated, you can do so by updating the models and running. It dumps these auto generated
migrations to `/migrations/versions`

```
flask db migrate -m "migration name"
```
