import requests

def test_get_users():

    url = "https://reqres.in/api/users?page=2"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200

