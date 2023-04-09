#json is commonly used with data in apis

import json

#sample

userJSON = '{"first_name": "john", "last_name": "doe", "age": 30}'

#parse to dict
user = json.loads(userJSON)

print(user)
