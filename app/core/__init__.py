from pathlib import Path

from pydantic import BaseSettings
from dotenv import load_dotenv


project_root = Path(__file__)

# go up the path until we are in the app dir
# where the env file should be
# this is needed as the cwd for the tests is app/tests
while project_root.name != 'app':
    project_root = project_root.parent


load_dotenv(project_root / '.env')


class Settings(BaseSettings):

    database_url: str = 'sqlite://'
    testing: bool = False
    secret: str
    first_superuser_email: str = None
    first_superuser_password: str = None


Config = Settings()
