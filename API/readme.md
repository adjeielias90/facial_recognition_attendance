# Face Recognition API

## Python environment

**Python version:** `Python 3.6.8`
```

## Python dependencies

You can install all the dependencies with
```bash
$ pip3 install -r requirements.txt
```
  ### To install dependencies: https://pipenv-fork.readthedocs.io/en/latest/basics.html
```
Be carefull to have `CMake` installed before trying to install `face_recognition`. You can install it with
```bash
$ pip3 install CMake
```


## How to use it

There are two components in the backend: `app.py` and `get_name_from_camera_feed.py`.

* **app.py:** This is the API itself, it handle routes. You can run it with:
```bash
$ python3 app.py
```

* **recognition.py:** This is the algorithm that read the video feed and apply face recognition. You can run it
with:
```bash
$ python3 recognition.py`
```
By default it will select the camera of your computer, but you can change it to any video feed, by adjusting the value of `video_capture = VideoCapture(0)` 0 is the prinary webcam of your computer. You can also add multiple feeds.
