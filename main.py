# coding=utf-8
import time

import schedule

from db import DB
from fetch_images import take_snapshot_from_camera
from rekognition_service import detect_labels_for
from serializer import serialize


def detect_and_store_labels(db, path, camera_name):
    def __detect_and_store_labels():
        db.store(time.time(), detect_labels_for(take_snapshot_from_camera(camera_name)))
        serialize(db, path)

    return __detect_and_store_labels


if __name__ == '__main__':
    db = DB()
    schedule.every(1).minutes.do(detect_and_store_labels(db, 'data.txt', u'Węzeł Modlnica'))

    while True:
        schedule.run_pending()
        time.sleep(1)
