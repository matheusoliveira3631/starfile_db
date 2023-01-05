from flask import Blueprint
from flask import request

from .controllers import fileController

app = Blueprint("app", __name__)

@app.route("/file", methods = ["POST"])
def fileUpload():
    return fileController().fileUpload(request)

@app.route("/file/<string:fileId>/")
def fileDownload(fileId):
    return fileController().fileDownload(fileId)

