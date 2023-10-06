import cv2
video = cv2.VideoCapture("murderparty.mp4")
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
frame_width = int(video.get(3))
frame_height = int(video.get(4))
   
size = (frame_width, frame_height)
   
dow=cv2.VideoWriter('greymy.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),10,size,0)
while True:
    ret,frame=video.read()
    
    #dow.write(gray)
    #cv2.waitKey(0)
    #a=vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    #b=vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #print(a,b)
    if ret:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
        cv2.imshow('video',gray)
        dow.write(gray)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break

    
    
    

video.release()
dow.release()
cv2.destroyAllWindows()
