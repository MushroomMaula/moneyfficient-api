@echo off
cd app
set PYTHONPATH=.
echo %PYTHONPATH%
cd ..
alembic upgrade head

pipenv run python app\db\inital_data.py