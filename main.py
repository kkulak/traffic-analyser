import time
import schedule
from db import DB
from rekognition_service import detect_labels
from serializer import serialize

def detect_and_store_labels(db, path):
    def __detect_and_store_labels():
        db.store(time.time(), detect_labels())
        serialize(db, path)
    return __detect_and_store_labels

if __name__ == '__main__':
    db = DB()
    schedule.every(1).minutes.do(detect_and_store_labels(db, 'data.txt'))

    while True:
        schedule.run_pending()
        time.sleep(1)