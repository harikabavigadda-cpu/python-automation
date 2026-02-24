import json

def test_write_json():
    data = {
        "name": "Harika",
        "age": 28,
        "skills": ["Python", "Selenium"]
    }

    # Write to file
    with open("harika.json", "w") as file:
        json.dump(data, file, indent=4)

    # Optional: check key values
    assert data["name"] == "Harika"
    assert "Python" in data["skills"]
