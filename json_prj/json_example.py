#################################################
#                Import libs
#################################################
import json

#################################################
#                  common code
#################################################
people = {"name":"wangyt", "age":"24", "sex":"man", "isonly":True}
print(f"people type is {type(people)}")

#################################################
#               json dump function
#################################################
with open("people_json.json", "w+") as f:
    json.dump(people, f, indent=4)

#################################################
#               json dumps function
#################################################
people_str = json.dumps(people)
print(f"people str is {people_str}")
print(f"json_file type is {type(people_str)}")

#################################################
#               json load function
#################################################
with open("people_json.json", "r") as f:
    people_dict = json.load(f)
    print(f"people dict is {people_dict}")
    print(f"people dict type is {type(people_dict)}")

#################################################
#               json loads function
#################################################
people_dic = json.loads(people_str)
print(f"people dic is {people_dic}")
print(f"people dic type is {type(people_dic)}")