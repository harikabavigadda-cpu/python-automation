import json
def test_json():
    data ={"name":"chiku","age":23,"section":"a",}
    with open("write.json","w")as file:
        json.dump(data ,file,indent=4)
    assert data ["age"] == 23