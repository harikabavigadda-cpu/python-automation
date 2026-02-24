import json

def test_read_json():
    with open("harika.json", "r") as file:
        data = json.load(file)  # Read JSON → Python dict

    # Check values
    assert data["age"] == 28
    assert "Selenium" in data["skills"]

    # Optional: print to console
    print(json.dumps(data, indent=4))


