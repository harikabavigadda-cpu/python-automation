import json
def test_jk():
    data={"village":"seoul","name":"jk","age":25,"gender":"male"}
    with open("jk.json","w")as file:
        json.dump(data,file,indent=4)
    assert data["village"]=="seoul"
    assert data["name"]=="jk"
    assert data["age"]==25
    assert data["gender"]=="male"
print(test_jimin())

