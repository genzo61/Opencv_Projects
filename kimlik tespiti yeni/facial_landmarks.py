from PIL import Image,ImageDraw
import face_recognition
path = "1.jpg"
image = face_recognition.load_image_file(path)
landmarks = face_recognition.face_landmarks(image)
pılimage = Image.fromarray(image)
d = ImageDraw.Draw(pılimage)
for landmark in landmarks:
    for feature in landmark.keys():
        d.line(landmark[feature],width=3)
pılimage.show()