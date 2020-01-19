from app.core import Config
from app import crud
from app.db.base import db_session
from app import schemas


def create_superuser(db):
    user = crud.user.get(Config.first_superuser_email, db)
    if not user:
        data = schemas.user.UserCreate(
            email=Config.first_superuser_email,
            password=Config.first_superuser_password,
            username=Config.first_superuser_username
        )
        user = crud.user.create(db, data)


if __name__ == '__main__':
    print('Creating superuser')
    create_superuser(db_session)
