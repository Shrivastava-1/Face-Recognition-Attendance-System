import cv2
import numpy as np
import face_recognition
import os
import pickle
import csv
from datetime import datetime

path = 'Images'

images = []
classNames = []

for img_name in os.listdir(path):
    img = cv2.imread(f'{path}/{img_name}')
    images.append(img)
    classNames.append(os.path.splitext(img_name)[0])

print("Students Enrollment :", classNames)

# Function to find encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encodeList.append(encodings[0])
    return encodeList

encodeListKnown = findEncodings(images)
print("Encodings loaded:", len(encodeListKnown))

# Save encodings to a file
with open('encodings.pickle', 'wb') as f:
    pickle.dump((encodeListKnown, classNames), f)

# Initialize webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Generate CSV file name based on current date
current_date = datetime.now().strftime('%d-%m-%Y')
csv_filename = f'Attendance_{current_date}.csv'

# Initialize CSV file
with open(csv_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['"Enrollment Number"', '"Time"', '"Date"'])

# Function to mark attendance
def markAttendance(name):
    with open(csv_filename, 'r+') as f:
        data = f.readlines()
        name_list = [line.split(',')[0] for line in data]
        if name not in name_list:
            now = datetime.now()
            time_string = now.strftime('%H:%M:%S')
            current_date = datetime.now().strftime("%d-%m-%Y")
            f.write(f'\n{name},{time_string},{current_date}')

while True:
    success, img = cap.read()
    if not success:
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(imgS)
    face_encodings = face_recognition.face_encodings(imgS, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(encodeListKnown, face_encoding)
        face_distances = face_recognition.face_distance(encodeListKnown, face_encoding)

        if len(face_distances) > 0:
            match_index = np.argmin(face_distances)

            if matches[match_index]:
                name = classNames[match_index].upper()
                markAttendance(name)
                y1, x2, y2, x1 = face_location
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
