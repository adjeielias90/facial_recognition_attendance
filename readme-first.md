# Late Checker

## Description

**Late Checker** is a web app with a deep learning AI to automate attendance recording.
It will detect every face that comes in the range of the camera and compare it with the all the already known faces
in the system. The system automatically updates the arrival or departure time in the database.
At the end you get for every day and every employee a *record* with:
* Name
* Date
* Arrival time
* Arrival picture
* Departure time
* Departure picture
* Is he late?
* Has he left early?

## Features

* You can see the video feed that record people that leave or come in the room.
* You can search for an employee to check the time of his time of arrival and departure.
* You can check the keep a screenshot of every arrival or departure.
* You can add an employee in the system with a single picture.
* You can delete an employee of the system.
* You can fastly see the 5 last employee detected by the camera.


## How does it work?

The camera feed is first fed to a model will detect it, if there are any faces on it and where.
A second model will make the match with all the known faces that are in the system.
When the model has extracted all the information from each frame, it is sent it to the API.
The API will then send the data to the database to persist it.

The web app will send request to the API. The API will take information asked in the DB and send it to the front-end.
The front-end will display all the data and allow you to seek for individual data.


## Which technologies?

* **Front-end:** *ReactJs*
* **Back-end API:** *Python Flask*
* **AI model:** [Face_recognition](https://github.com/ageitgey/face_recognition)
* **Installation and environment setup:** *Bash*
* **Database**: *PostgreSQL*


## More details
* [Back-end details](API/README.md)
* [Front-end details](frontend/face-attendance/README.md)

