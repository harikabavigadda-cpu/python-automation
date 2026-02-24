import json
def test_kim_w():
    data={"village":"seoul","name":"kim","age":29}
    with open("kim.json","w")as file:
         json.dump(data,file,indent=4)
    assert data ["village"] == "seoul"