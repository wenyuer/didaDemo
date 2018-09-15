from flask import Flask, request
from flask_cors import CORS
import time, json, random
app = Flask(__name__)
CORS(app)


@app.route("/dida/allfrontcate.do")
def allFrontCate():
    with open("1.json") as f:
        return json.dumps(json.load(f))


@app.route("/dida/loadsource.do")
def loadSource():
    with open("2.json") as f:
        return json.dumps(json.load(f))


@app.route("/dida/merge.do")
def merge():
    time.sleep(5)
    with open("3.json") as f:
        return json.dumps(json.load(f))


@app.route("/dida/mergebyrawdata.do", methods=['POST'])
def mergeByRawData():
    time.sleep(5)
    print request.get_json()
    with open("3.json") as f:
        return json.dumps(json.load(f))
