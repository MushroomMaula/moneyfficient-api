from faker import Faker
from faker.providers import python, internet, date_time


fake = Faker()
fake.add_provider(python)
fake.add_provider(internet)
fake.add_provider(date_time)


def random_string():
    return fake.pystr()


def random_float():
    return fake.pyfloat(positive=True)
