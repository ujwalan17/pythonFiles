import json
data=open("jsonformatter.json","r")
d=data.read()
v=json.loads(d)
print(v["products"][0]["cost"])
print(type(v))
with open("ex.txt","w+") as f:
    json.dump(v,f)
# with open("jsonformatter.json","r") as f:
#     d = f.read()
#     r = json.loads(d)
#     print(type(r))
#     print(type(d))

            


