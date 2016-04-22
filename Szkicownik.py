from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import parse

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = { 'k':[10, 10, 10], 'p': 10}
e = dict_to_xml('stock', s)
print tostring(e)
k = e.findtext('k')
print k

fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
fo.write(tostring(e))
fo.close()
fo = open("foo.txt", "r")
m = fo.read()
print m.find('k') + 9
# Close opend file
fo.close()

#doc = parse(tostring(e))
