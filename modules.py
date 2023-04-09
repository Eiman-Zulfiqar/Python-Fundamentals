# import datetime
# from datetime import date
# import time
# today = date.today()
# timestamp =time.time()

# print(today)
# print(timestamp)

from camelcase import CamelCase

c = CamelCase()

print(c.hump('hello there world'))

import validator
from validator import validate_email #now we can use this function

email = 'test test.com'

if validate_email(email):
    print('email valid')
else:
    print('inavlid')