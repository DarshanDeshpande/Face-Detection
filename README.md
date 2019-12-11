# Face-Detection
This is an extension to the face_recognition library by ageitgey.<br>
This was initially made for a topic for a hackathon where the goal was to make attendance logging more accurate.<br>

The recognize.py file contains a few functions which can help in formation of a list of people on which the model can be trained.
The output is received in the form of a list and accordingly if it recognizes the person, it can continue with the execution (in my case attendance logging).
The functions can be used for standalone purposes or can also be integrated with live video feed where using PIL, we can pull out frames at regular intervals which was the original intention behind the project.
