import json
def test_json():
    data = {"bts": "ot", "blackpink": "jin","country":"seoul"}
    with open("kim.json", "w") as file:
        json.dump(data, file, indent=4)
    assert data ["bts"] == "ot"
    assert data ["blackpink"] == "jin"
    assert data ["country"] == "seoul"

