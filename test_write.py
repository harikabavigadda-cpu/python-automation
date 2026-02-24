import json
def test_json_write():
    data={"name":"hany","age":24}
    with open("test.json","w")as file:
        json.dump(data, file, indent=4)