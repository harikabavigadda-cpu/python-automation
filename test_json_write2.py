import json
def test_json_write2():
    data={"name":"hany","age":24}
    with open("honey.json","w")as file:
        json.dump(data, file, indent=4)
    assert data["name"] == "hany"
    assert data["age"] == 24