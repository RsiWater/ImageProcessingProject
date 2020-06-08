import cv2

def gray(v):
    vc = cv2.VideoCapture(v)
    fps = vc.get(cv2.CAP_PROP_FPS)
    frame_count = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
    video = []
    for idx in range(frame_count):   
        ret, frame = vc.read()
        if frame is not None:
            #print(idx)
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img_B = frame[:,:, 0]
            img_G = frame[:,:, 1]
            img_R = frame[:,:, 2]
            frame[:,:, 0]=img_B*0.114+img_G*0.587+img_R*0.299
            frame[:,:, 1]=img_B*0.114+img_G*0.587+img_R*0.299
            frame[:,:, 2]=img_B*0.114+img_G*0.587+img_R*0.299
            height, width,layers= frame.shape
            size = (width, height)
            video.append(frame)
    l=[video,fps,size]
    return l

def size_f(v,h_percent,w_percent):
    vc = cv2.VideoCapture(v)
    fps = vc.get(cv2.CAP_PROP_FPS)
    frame_count = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
    video = []
    for idx in range(frame_count):   
        ret, frame = vc.read()
        if frame is not None:
            frame=resize(frame,h_percent,w_percent)
            height, width,layers= frame.shape
            size = (width, height)
            video.append(frame)
    l=[video,fps,size]
    return l

def resize(img,h_percent,w_percent):
    height = img.shape[0]
    width = img.shape[1]
    h_percent=h_percent/100
    w_percent=w_percent/100
    height = height*h_percent
    width = width*w_percent
    img = cv2.resize(img,(int(width),int(height)))
    return img

def write_video(output,video,fps,size):
    out = cv2.VideoWriter(output,cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
    for i in range(len(video)):
        out.write(video[i])