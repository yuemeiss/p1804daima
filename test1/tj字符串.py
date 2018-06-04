q = 'hello word god is allways busy'
l = ''
for i in q:
    if not i in l :
        l=l + i + ":" + str(q.count(i)) + " "
print(l)
for i in ''.join(q.split()):
    if i + ":" + str(q.count(i)) not in l:
        l += (i + ":" + str(q.count(i)) + " ")
print(l)
