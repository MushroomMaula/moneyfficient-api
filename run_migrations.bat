echo %cd%
cd app
echo %cd%
set PYTHONPATH=.
cd ..
alembic revision --autogenerate
alembic upgrade head