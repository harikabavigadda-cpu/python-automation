import json
def test_json3():
    data={"name":"latah","age":28,"section":"a","language":"python"}
    with open("hello.json","w")as file:
        json.dump(data,file,indent=4)
    assert data["language"] == "python"
    assert data ["section"] == "a"
    assert data["name"] == "latah"