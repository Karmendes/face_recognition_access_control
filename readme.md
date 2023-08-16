# Facial Recognition for Access Control Project

This is a facial recognition project developed for access control purposes, utilizing a series of interconnected modules. The system can capture camera images, identify faces, perform facial recognition, apply entry rules, record access events, and even control automatic door opening. Communication between modules is facilitated using RabbitMQ, and the entire project is implemented in Python.

## Modules

The project consists of the following modules:

**filmmaker**: This module is responsible for capturing camera feeds, obtaining frames for further processing.

**headcut**: The module performs face detection on the frames captured by the camera, determining the presence of faces.

**severiner**: severiner is responsible for facial recognition. It uses the faces detected by the HeadCutter to compare against faces registered in the system and determine the individual's identity.

**buildingconcierge**: This module applies access rules based on information obtained by Severiner. If the facial recognition is positive and meets predefined rules, BuildingConcierge controls door opening and records the access event.

**moses**: The moses module is responsible for physical control, automatically opening the door according to instructions from BuildingConcierge.

**imigrationofficer**: imigrationofficer handles the registration of new faces in the system. It receives captured images from the camera, performs face detection, and stores the faces in the database for later use in facial recognition.