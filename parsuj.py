def parsuj(data):
    slownik = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    x = slownik.get(data[0])
    y = slownik.get(data[1])
    print "Awiva"
    return [x, y]

