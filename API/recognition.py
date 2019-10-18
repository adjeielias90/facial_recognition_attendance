import face_recognition
import numpy as np
import cv2, queue, threading, time
import requests, os, re

# bufferless VideoCapture
class VideoCapture:
    def __init__(self, name):
        self.cap = cv2.VideoCapture(name)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

    # read frames as soon as they are available, keeping only most recent one
    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()   # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()

# Select the webcam of the computer
# video_capture = VideoCapture('https://stream-eu1-charlie.dropcam.com:443/nexus_aac/b85a6ec812c045cd921f4164e8e7ecc0/playlist.m3u8?public=GqJifk6U25')
video_capture = VideoCapture(0)