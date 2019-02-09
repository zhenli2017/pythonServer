# -*- coding: utf-8 -*

# 导入Flask框架
from flask import Flask
# request 请求
from flask import request
# Logger日志打印
import logging
# Json解析
import json

# 初始化Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 初始化 Flask,默认端口是5000
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        logger.warning("POST")
    else:
        logger.warning("GET")
    return "{code=200,method=get}"


@app.route("/login", methods=["GET", "POST"])
def login():
    print logger.warning("fuck %s %s %s", "oooooo", "qq", "pp")
    loginMap = {"userName": "fuckTHD", "pwd": "123456"}
    return json.dumps(loginMap, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
