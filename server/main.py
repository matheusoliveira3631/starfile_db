from flask import Blueprint
from flask import request

from .controllers import fileController

app = Blueprint("app", __name__)

@app.route("/file", methods = ["POST"])
def fileUpload():
    return fileController().fileUpload(request)

@app.route("/download/")
def fileDownload():
    fileId = request.args.get("id", type=str)
    print(fileId)
    return fileController().fileDownload(fileId)

