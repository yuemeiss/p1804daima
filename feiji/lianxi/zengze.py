import re
ret=re.match('1[^0-8]\d{10}$','17622234524').group()
print(ret)




