dict = {"Sean" : {"age": 25, "gender": "male"}, "Mariposa": {"age": 22, "gender": "female"}, "Omar": {"age": 100, "gender": "male"}}

for name in dict:
    print(name + " is " + str(dict[name]["age"]) + " years old. And their gender is " + dict[name]["gender"] + ".")