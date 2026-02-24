import json
def test_json_write2():
    data ={"name":"kate","age":23}
    with open("test.json","w")as file:
       json.dump(data,file,indent=4)
    assert data == {"name":"kate","age":23}