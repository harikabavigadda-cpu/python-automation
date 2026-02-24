import requests

def test_json_practice():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    print(response.status_code)

    data = response.json()

    print(data["name"])