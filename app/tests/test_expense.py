import json


def test_create(client, expense_data, access_headers):
    user, headers = access_headers
    resp = client.post(
        'expenses/new',
        json=json.loads(expense_data.json()),
        headers=headers
    )
    assert resp.status_code == 201
