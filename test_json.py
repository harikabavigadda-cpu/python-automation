import json
def test_json():
    data={"name":"kim","age":29,"profession":"singer","country":"south korea"}
    with open("kim.json","w")as file:
          json.dump(data,file,indent=4)
    assert data["country"] == "south korea"