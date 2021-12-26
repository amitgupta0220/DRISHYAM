import cv2
import glob
import numpy as np

# change this accordingly
# videoPaths = glob.glob(
#     'C:/Users/Dell/Desktop/DataSet/VID_20200222_194812_trim.mp4')


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
        'D:/Amit/Projects/Final year/Drishyam/ACTIONS/how/VID_20200225_140002.mp4')  # vid name
    ret, frame = cap.read()
    count = 0  # change after first itration
    ret = True
    while ret:
        cv2.imwrite('D:/Amit/Projects/Final year/Drishyam/ACTIONS/how/how_label/how_label (%d).jpg' %
                    count, frame)  # change this accordingly (frame write path)
        ret, frame = cap.read()
        count += 1

# extractFrame() #call this to extract frame


def reSize():
    imgPaths = glob.glob(
        'D:/Amit/Projects/Final year/Drishyam/ACTIONS/how/how_label/*.jpg')
    count = 0
    for imgPath in imgPaths:
        img = cv2.imread(imgPath)
        img = cv2.resize(img, (640, 480))
        cv2.imwrite(
            'D:/Amit/Projects/Final year/Drishyam/ACTIONS/how/how_label/how_label (%d).jpg' % count, img)
        count += 1


reSize()

# video record
# save in respective action ka folder
# extract frames according to count and change it accordingly
# after extracting all frames then resize it(check order of images first)
# then labelling
