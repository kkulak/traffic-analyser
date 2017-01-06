import time
from db import DB
from rekognition_service import detect_labels
from serializer import serialize

if __name__ == '__main__':
    
    print detect_labels()
    #db = DB()
    #db.store(time.time(), detect_labels())

    #serialize(db)