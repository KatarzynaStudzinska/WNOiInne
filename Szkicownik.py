import json

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

class klasa:
    def __init__(self):
        self.a = [1, 2, 3]
        self.tab = [[1, 2, 3], [8,8 ,8], [5, 4, 2]]
    def printuj(self):
        print( self.a)


classes = {'klasa':klasa}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

kon = klasa()
data = {"nos": 333, "k": kon, "obiekt": 333}


with open('dane.txt', 'w') as fp:
    json.dump(data, fp, default=serialize_instance)
'''
json_data = open('dane.txt').read()
data = json.loads(json_data, object_hook=unserialize_object)
konik = data["k"]
konik.printuj()'''

