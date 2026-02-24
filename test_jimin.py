import json
def test_jimin():
    data={"name":"jimin","age":"34"}
    with open("jimin.json","w")as file:
        json.dump(data,file,indent=4)
    assert data ["name"]=="jimin"
    assert data ["age"]=="34"

