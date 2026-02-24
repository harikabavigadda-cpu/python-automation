import json
def test_jk():
    data={"village":"seoul","name":"jk"}
    with open("jk.json","w")as file:
        json.dump(data,file,indent=4)
    assert data["village"]=="seoul"
    assert data["name"]=="jk"
print(test_jimin())
