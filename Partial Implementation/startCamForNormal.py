# importing libraries
import cv2
cap = cv2.VideoCapture('./Partial Implementation/scene2-camera1.mov')
if (cap.isOpened()== False): 
  print("Error opening video  file")
# Read until video is completed
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # resized = cv2.resize(frame,(256,256))
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
    median = cv2.medianBlur(img_gray,5)
    scharrx_filter = cv2.Scharr(img_gray, ddepth=-1, dx=1, dy=0, scale=1, borderType=cv2.BORDER_DEFAULT)
    # sobelxy = cv2.Sobel(src=median, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=15) 
    edges1 = cv2.Laplacian(img_blur, ddepth=-1, ksize=5, scale=1, borderType=cv2.BORDER_DEFAULT)                # >>><<<
    edges = cv2.Laplacian(median, ddepth=-1, ksize=5, scale=1, borderType=cv2.BORDER_DEFAULT)
    edges2 = cv2.Laplacian(scharrx_filter, ddepth=-1, ksize=5, scale=1, borderType=cv2.BORDER_DEFAULT)
    # edges = cv2.Canny(image=img_gray, threshold1=80, threshold2=180)            # >>><<<                                              
    # edges1 = cv2.Canny(image=median, threshold1=80, threshold2=180)
    # edges2 = cv2.Canny(image=scharrx_filter, threshold1=80, threshold2=180)
    cv2.imshow('Frame', edges)
    cv2.imshow('Frame2', edges1)
    cv2.imshow('Frame3', edges2)
    # cv2.imshow('Frame3', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break
cap.release()
cv2.destroyAllWindows()

# GUI
# resize and gray scale
# conclusion gaussian > median blur > bilateral filter
# edge detection ke liye canny > Laplacian