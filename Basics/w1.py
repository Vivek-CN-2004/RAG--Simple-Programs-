print("never give up")

import json

class Dictionary:

    def  store_data(self, name, role, goal):
        d = {}
        d['name'] = name
        d['role'] = role
        d['goal'] = goal
        return d
   
    
dd = Dictionary()
data = dd.store_data("Vivek", "AI Engineer", "Building RAG applications")
print(data['name'])
print(data['role'])
print(data['goal'])
print(data)
print("after converting to json")

json_data = json.dumps(data)
print(json_data)

