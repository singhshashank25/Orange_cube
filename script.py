import json
print("I'm running here :/")

obj = {
    1:'dfv',
    2:'ffghgjgjhgjg'
}
with open("xyz.json", "w") as fp:
    json_string =  json.dump(obj,fp)