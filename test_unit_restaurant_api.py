'''API testing file'''
from api import *

# test payloads
payload_restaurant_id = {
    "id": 1
}


def test_get_restaurant():
    with app.app_context():
        response = get_restaurant_by_id(payload_restaurant_id.get('id'))
        assert response.status_code == 200
