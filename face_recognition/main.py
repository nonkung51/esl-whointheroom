import face_recognition
# from picamera import PiCamera
from time import sleep
import requests

# camera = PiCamera()
URL = "https://warm-lake-39502.herokuapp.com/people"

# Load the known people faces
biden_image = face_recognition.load_image_file("img\\biden.jpg")
obama_image = face_recognition.load_image_file("img\\obama.jpg")
nonthakon_image = face_recognition.load_image_file("img\\nonthakon.jpg")

#encoding people faces
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
nonthakon_face_encoding = face_recognition.face_encodings(nonthakon_image)[0]

#make a list of people faces encoding
known_faces = [
    biden_face_encoding,
    obama_face_encoding,
    nonthakon_face_encoding
]

#list of people name TODO: change to id
people_names = [
    "Joe Biden",
    "Barack Obama",
    "Nonthakon Jitchiranant"
]

#capture picture from pi camera save as a file
#encoding the picture from camera
#make a results list then loop in it if the idex is True send request to update the database

while(True):
    # camera.start_preview()
    # camera.capture('/home/pi/Desktop/image.jpg')
    # camera.stop_preview()
    # unknown_image = face_recognition.load_image_file("/home/pi/Desktop/image.jpg")
    unknown_image = face_recognition.load_image_file("img\\stranger.jpg")
    try:
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

        for i in range(len(people_names)):
            if(results[i]):
                print(people_names[i])
                r = requests.put(url = URL, data = {'name': people_names[i]})

        if (True not in results):
            # send a request there's stranger
            print("Found no one")
            r = requests.put(url = URL, data = {'name': 'unknown' })
        
        sleep(5)
    except Exception as e:
        print(e)
        
        sleep(5)