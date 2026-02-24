import json
def test_py():
    data = {"name" : "heyyy","k" : "jk"}
    with open("jk.json", "w")as file:
        json.dump(data, file, indent=4)
    assert data ["name"]=="heyyy"





