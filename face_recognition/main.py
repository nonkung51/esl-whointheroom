import face_recognition
import picamera
import numpy as np
import requests

camera = picamera.PiCamera()
camera.resolution = (800, 800)
output = np.empty((800, 800, 3), dtype=np.uint8)

URL = "https://warm-lake-39502.herokuapp.com/update_people"

print("Loading known face image(s)")
nonthakon_image = face_recognition.load_image_file("img/nonthakon.jpg")
nonthakon_face_encoding = face_recognition.face_encodings(nonthakon_image)[0]
nonthakon2_image = face_recognition.load_image_file("img/nonthakon_test.jpg")
nonthakon2_face_encoding = face_recognition.face_encodings(nonthakon2_image)[0]
pbeer_image = face_recognition.load_image_file("img/pbeer.jpg")
pbeer_face_encoding = face_recognition.face_encodings(pbeer_image)[0]
prayuth_image = face_recognition.load_image_file("img/prayuth.jpg")
prayuth_face_encoding = face_recognition.face_encodings(prayuth_image)[0]

known_faces = [
    nonthakon_face_encoding,
    nonthakon2_face_encoding,
    pbeer_face_encoding,
    prayuth_face_encoding
]

# Initialize some variables
face_locations = []
face_encodings = []

names = [
    "Non",
    "Non",
    "P'Beer",
    "Uncle Prayuth",
    "Stranger",
]

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = ""

        for match in matches:
            if match:
                name = names[matches.index(match)]
                r = requests.post(url = URL, data = {'name': names[matches.index(match)]})
                
        if True not in matches:
            #print("Stranger!")
            r = requests.post(url = URL, data = {'name': names[5]})
        else:
            print("I see someone named {}!".format(name))


