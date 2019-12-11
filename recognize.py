import face_recognition
import pickle,os

known_encodings = []

unknown_image = face_recognition.load_image_file("D:\Facial Recognition\Pictures\Group\XYZ")
unknown_encodings = face_recognition.face_encodings(unknown_image)[0]

def build_list():
    global known_encodings
    known_encodings_address = "D:/Facial Recognition/Pictures/XYZ/"
    for filename in os.listdir(known_encodings_address):
        if filename.endswith('.jpg'):
            s = "".join((known_encodings_address,filename))
            image = face_recognition.load_image_file(s)
            encode = face_recognition.face_encodings(image)[0]
            known_encodings.append(encode)
            print("{} has been encoded".format(filename))
            s=""


def add_new_face(encoding):
    known_encodings.append(encoding)
    dump_list(known_encodings)


def dump_list(list):
    with open("Encodings.txt","wb")as f:
        pickle.dump(list,f)


def get_list():
    with open("Encodings.txt","rb")as f:
        global known_encodings
        known_encodings = pickle.load(f)


def predict(known_encodings,unknown_encodings):
    result = face_recognition.compare_faces(known_encodings,unknown_encodings,0.5)
    return result

get_list()
print(predict(known_encodings,unknown_encodings))


