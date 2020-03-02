import pytest
from tests.utils import fake


# @pytest.mark.skip
def test_to_xtf(client):
    data = fake.methods()
    print(data)
    url = "api/docs/methods/trans/to_xtf"
    res = client.post(url, json=data)
    assert res.status_code == 200


# @pytest.mark.skip
def test_to_xhx(client):
    data = fake.methods()
    url = "api/docs/methods/trans/to_xhx"
    res = client.post(url, json=data)
    assert res.status_code == 200


# @pytest.mark.skip
def test_market(client):
    data = fake.market()
    res = client.post("api/docs/market/shop?pag=1", json=data)
    assert res.status_code == 200


