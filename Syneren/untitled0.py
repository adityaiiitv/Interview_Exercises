import cv2
 
# to capture the video frame by frame
cap = cv2.VideoCapture('drop.avi')
 
# check if the feed is open
if (cap.isOpened() == False): 
  print("Error in reading video")
 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 10, (frame_width,frame_height))
 
fps = 15    # frames per sec
sec = 5     # total seconds
total = fps*sec # total frames
iter1 = 0   # iterator
while(iter1<total):
  iter1 = iter1 + 1
  ret, frame = cap.read()
 
  if ret == True: 
    out.write(frame)
    cv2.imshow('frame',frame)
 
cap.release()
out.release()
cv2.destroyAllWindows() 