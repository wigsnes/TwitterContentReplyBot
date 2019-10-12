import jsonpickle

fileI = "C:/Users/fredr/Documents/Repos/TwitterContentReplyBot/mock/usersMock.json"
fileO = "C:/Users/fredr/Documents/Repos/TwitterContentReplyBot/mock/usersMock2.json"

fi = open(fileI, mode="r", encoding="UTF-8")

D = jsonpickle.loads(fi.read())

for key, val in D.items():
    del val["_json"]
    del val["status"]["_json"]

fo = open(fileO, mode="w+", encoding="UTF-8")

fo.write(jsonpickle.encode(D, unpicklable=False))