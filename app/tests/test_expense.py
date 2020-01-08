import json


def test_create(client, expense_data_factory, access_headers):
    user, headers = access_headers
    expense = expense_data_factory()
    resp = client.post(
        'expenses/new',
        json=json.loads(expense.json()),
        headers=headers
    )
    assert resp.status_code == 201


def test_get_by_id(client, db_expense_factory, access_headers):
    user, headers = access_headers
    expense = db_expense_factory(1, user).pop()
    resp = client.get(
        f'expenses/{expense.id}',
        headers=headers
    )

    assert resp.status_code == 200


def test_get_by_id_access_denied(client, db_expense_factory, access_headers, db_user_factory):
    user, headers = access_headers
    expense = db_expense_factory(1, db_user_factory()).pop()
    resp = client.get(
        f'expenses/{expense.id}',
        headers=headers
    )

    assert resp.status_code == 401


def test_get_all(client, access_headers, db_expense_factory):
    user, headers = access_headers
    expenses = db_expense_factory(10, user)
    resp = client.get(
        'expenses/',
        headers=headers
    )
    data = resp.json()['data']
    assert len(data) == 10
    assert all(original.id == r['id'] for original, r in zip(expenses, data))
