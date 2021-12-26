import cv2
import glob
import numpy as np

# change this accordingly
videoPaths = glob.glob(
    'C:/Users/Dell/Desktop/DataSet/VID_20200222_194812_trim.mp4')


# for videoPath in videoPaths:
#     def actWriter(videoPath):
#         cap = cv2.VideoCapture(videoPath)
#         ret, frame = cap.read()
#         count = np.random.randint(1, high=9999)
#         ret = True
#         while ret:
#             cv2.imwrite('train/no_abnormal/noact%d.jpg' %
#                         count, frame)  # change this accordingly
#             ret, frame = cap.read()
#             count += np.random.randint(1, high=9999)

    # actWriter(videoPath)


def extractFrame():
    cap = cv2.VideoCapture(
        'D:/Amit/E-YIC/Tp2/VID_20200225_140002.mp4')  # vid name
    ret, frame = cap.read()
    count = 3824  # change after first itration
    ret = True
    while ret:
        cv2.imwrite('D:/Amit/E-YIC/Tp2/wave_label/wave (%d).jpg' %
                    count, frame)  # change this accordingly (frame write path)
        ret, frame = cap.read()
        count += 2
# extractFrame()

# extractFrame() #call this to extract frame


def reSize():
    imgPaths = glob.glob('D:/Amit/E-YIC/Tp2/wave_label/*.jpg')
    count = 1255
    for imgPath in imgPaths:
        img = cv2.imread(imgPath)
        img = cv2.resize(img, (600, 337))
        cv2.imwrite(
            'D:/Amit/E-YIC/Tp2/wave_label/wave/wave (%d).jpg' % count, img)
        count += 1
# reSize()
