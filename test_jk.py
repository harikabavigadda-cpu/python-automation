import json
def test_json():
    data ={"name":"jk","country":"sk","age":29}
    with open("kim.json","w")as file:
      json.dump(data,file,indent=4)
    assert data["name"] == "jk"
    assert data["country"] == "sk"

