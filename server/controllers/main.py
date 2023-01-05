import os 
import random

from flask import request
from flask import Response
from flask import send_file
from flask.templating import render_template
from flask.globals import current_app
from werkzeug.utils import secure_filename
from tinydb import TinyDB, Query

from database import Database

class fileController():
    def __init__(self):
        db_name=current_app.config['DB_NAME']
        tndb = TinyDB(f'{db_name}.json')
        self.db = Database(tndb)
        pass

    def fileUpload(self,request) -> None:
        try:
            file = request.files['file']
            filename = secure_filename(file.filename)
            fileId = self.fileRegister(filename)
            filePath=os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(filePath):
                pass
            else:
                file.save(filePath)
            
            return fileId
        except EnvironmentError as err:
            print(err)
            return render_template('error.html')

    def fileRegister(self, filename):
        random_range = lambda n : str(random.randint(10**(n-1), (10**n)-1))
        file_id=random_range(10)
        id_list=self.db.listIds()
        while file_id in id_list:
            file_id=random_range(10)
        
        self.db.fileRegistration(filename, file_id)
        return file_id
    
    def fileDownload(self, fileId):
        query = Query()
        print(fileId)
        fileName = self.db.getFileName(query, fileId)
        filePath=os.path.join(current_app.config['UPLOAD_FOLDER'], fileName)
        return send_file(filePath, as_attachment=True)


