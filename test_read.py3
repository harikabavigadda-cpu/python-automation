def test_write_json_file():  # ✅ Must start with test_
    data = {"name": "Kavya", "age": 25}
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)

    # Optional assertion
    assert data["name"] == "Kavya"
