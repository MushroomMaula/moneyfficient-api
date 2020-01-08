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
