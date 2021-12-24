import cv2
import os
import time

IMAGE_PATH = "CollectedImages"

labels = ["hello"]
numberOfImages = 15

for label in labels:
    path = os.path.join(os.getcwd(), IMAGE_PATH, label)
    os.mkdir(path)
    cap = cv2.VideoCapture(0)
    print("Capturing images for {}".format(label))
    time.sleep(5)
    for imgNum in range(numberOfImages):
        ret, frame = cap.read()
        imageName = os.path.join(
            os.getcwd(), IMAGE_PATH, label, label+'.'+'{}.jpg'.format(count))
        cv2.imwrite(imageName, frame)
        cv2.imshow("Capturing", frame)
        time.sleep(2)
        count = count+1

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

    cap.release()
