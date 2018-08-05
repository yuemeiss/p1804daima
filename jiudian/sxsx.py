import random
ll = [1]
while True:

    l = random.randint(2,10)
    if not l in ll:
        ll.append(l)

    if len(ll) == 6 :
        ll.sort()
        print(ll)
        break

