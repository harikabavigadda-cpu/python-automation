import json

def test_write_json_file():
    data = {"name": "Kavya", "age": 25}
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)

    # Optional check
    assert data["name"] == "Kavya"
