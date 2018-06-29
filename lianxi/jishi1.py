class DogDzb(object):
    __instance = None
    def __init__(self):
        pass
    def __new__(cls,*k):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
kity = DogDzb()
kity1 = DogDzb()
print(id(kity))
print(id(kity1))
