import json
def test_kim_w():
    data={"village":"seoul","name":"kim","age":29,"city":"hyd"}
    with open("kim.json","w")as file:
         json.dump(data,file,indent=4)
    assert data ["village"] == "seoul"
    assert data ["name"] == "kim"
    assert data ["age"] == 29
    assert data ["city"] == "hyd"
    assert data ["village"] == "seoul"