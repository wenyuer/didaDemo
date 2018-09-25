#encoding=utf-8
from flask import Flask, request
from flask_cors import CORS
import time, json, random
app = Flask(__name__)
CORS(app)

error = {
    "success": False,
    "errorCode": "DAPEI_ALGO_FAIL",
    "position": "119-138",
    "errorMsg": u"算法生成搭配失败！"
}


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
    time.sleep(1)
    if random.random() <= 0.3:
        return json.dumps(error)
    with open("3.json") as f:
        return json.dumps(json.load(f))


@app.route("/dida/mergebyrawdata.do", methods=["POST"])
def mergeByRawData():
    print request.get_data()
    time.sleep(1)
    if random.random() <= 0.3:
        return json.dumps(error)
    with open("4.json") as f:
        return json.dumps(json.load(f))
