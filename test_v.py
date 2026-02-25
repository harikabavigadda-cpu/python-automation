import json
def test_python_json_read2():
    data={"name":"tejuu","age":29,"country":"india","language":"telugu"}
    with open("teju.json","w")as file:
        json.dump(data,file,indent=4)
    assert data ["name"]=="tejuu"
    assert data["age"]==29
    assert data["country"]=="india"
    assert data["language"]=="telugu"
