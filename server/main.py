from flask import Flask, request
from flask_cors import CORS
import time, json, random
app = Flask(__name__)
CORS(app)

POOL = []
id = 0
for i in range(6):
    with open('testitem/%d' % i) as f:
        for line in f:
            POOL.append({
                "type": str(i),
                "id": id,
                "image": line.strip()
            })
            id += 1


@app.route("/items")
def getItems():
    type = request.args['type']
    data = []
    while len(data) < 6:
        item = POOL[random.randint(0, len(POOL) - 1)]
        if type == item["type"] and item not in data:
            data.append(item)
    return json.dumps(data)


@app.route("/collocation")
def getCollocation():
    items = []
    types = []
    if 'itemId' in request.args:
        item = POOL[int(request.args['itemId'])]
        items.append(item)
        types.append(item['type'])
    while len(items) < 4:
        item = POOL[random.randint(0, len(POOL) - 1)]
        if item["type"] not in types and item not in items:
            items.append(item)
            types.append(item['type'])
    result = []
    for item in items:
        result.append({
            "id": item["id"],
            "image": item["image"],
            "w": random.randint(150, 200),
            "h": random.randint(150, 200),
            "x": random.randint(0, 300),
            "y": random.randint(0, 300)
        })
    return json.dumps(result)


@app.route("/position", methods=['POST'])
def submitPosition():
    print request.get_json()
    return 'https://cn.vuejs.org/images/logo.png'


@app.route("/dida/allfrontcate.do")
def allFrontCate():
    with open("1.json") as f:
        return json.dumps(json.load(f))


@app.route("/dida/loadsource.do")
def loadSource():
    with open("2.json") as f:
        return json.dumps(json.load(f))
