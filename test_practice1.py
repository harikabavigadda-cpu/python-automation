import json
def test_json_read2():
    data= {"name":"v","age" :30,"profession": "singer","country":"south korea"}
    with open("write.json","w")as file:
        json.dump(data ,file,indent=4)
        assert data["name"] == "v"
