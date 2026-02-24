import json
def test_json():
    data = {"bts": "ot", "blackpink": "jin"}
    with open("kim.json", "w") as file:
        json.dump(data, file, indent=4)
    assert data ["bts"] == "ot"

