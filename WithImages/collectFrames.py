import cv2
import os
import time

IMAGE_PATH = "CollectedImages"

labels = ["hello"]
numberOfImages = 15

for label in labels:
    count = 0
    path = os.path.join(os.getcwd(), IMAGE_PATH, label)
    try:
        os.mkdir(path)
    except:
        pass
    cap = cv2.VideoCapture(1)
    print("Capturing images for {}".format(label))
    time.sleep(5)
    for imgNum in range(numberOfImages):
        ret, frame = cap.read()
        imageName = os.path.join(
            os.getcwd(), IMAGE_PATH, label, label+'.'+'{}.jpg'.format(count))
        # img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
        # edges = cv2.Canny(image=img_blur, threshold1=80, threshold2=180)
        # cv2.imwrite(imageName, edges)
        cv2.imshow("Capturing", frame)
        time.sleep(2)
        count = count+1

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

    cap.release()

# suyash
# hemil
# sujay
# bawa
# baje
# atharv
# suyash mom
# suyash dad
# hemil mom
# hemil dad
# pawan
# yash
