from app import schemas


def test_create_user(client, user_data_factory):
    user_data = user_data_factory()
    resp = client.post(
        '/user/register',
        json=user_data.dict()
    )
    assert resp.status_code == 201


def test_user_exists(client, db_user_factory):
    user = db_user_factory()
    user_data = schemas.UserCreate(**user.__dict__)
    resp = client.post(
        '/user/register',
        json=user_data.dict()
    )
    assert resp.status_code == 409
    assert resp.json()['detail'] == 'A User with this email already exists'
