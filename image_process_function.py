import cv2
from filter import FilterED
from filter import embossFilter

def get_video(v):
    vc = cv2.VideoCapture(v)
    fps = vc.get(cv2.CAP_PROP_FPS)
    frame_count = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
    video=[]
    for i in range(frame_count):
        ret, frame = vc.read()
        if frame is not None:
            video.append(frame)
    return(video,fps)

def fpsDrop(frames,fps):
    reframes=[]
    for i in range(0,len(frames),int(fps)):
        reframes.append(frames[i])
    return reframes,1

def grey(frames):
    modify_frames=[]
    for i in range(len(frames)):
        img_B = frames[i][:,:, 0]
        img_G = frames[i][:,:, 1]
        img_R = frames[i][:,:, 2]
        frames[i][:,:, 0]=img_B*0.114+img_G*0.587+img_R*0.299
        frames[i][:,:, 1]=img_B*0.114+img_G*0.587+img_R*0.299
        frames[i][:,:, 2]=img_B*0.114+img_G*0.587+img_R*0.299
        modify_frames.append(frames[i])
    return modify_frames

def findEdge(frames): #邊緣提取濾鏡
    modify_frames=[]
    for frame in frames:
        B,G,R = cv2.split(frame)
        R = FilterED(R,8)
        G = FilterED(G,8)
        B = FilterED(B,8)
        img = cv2.merge([B,G,R])
        modify_frames.append(img)
    return modify_frames

def edgeEnhance(frames): #邊緣增強濾鏡
    modify_frames=[]
    for frame in frames:
        B,G,R = cv2.split(frame)
        R = FilterED(R,10)
        G = FilterED(G,10)
        B = FilterED(B,10)
        img = cv2.merge([B,G,R])
        modify_frames.append(img)
    return modify_frames

def edgeEnMore(frames):
    modify_frames=[]
    for frame in frames:
        B,G,R = cv2.split(frame)
        R = FilterED(R,9)
        G = FilterED(G,9)
        B = FilterED(B,9)
        img = cv2.merge([B,G,R])
        modify_frames.append(img)
    return modify_frames

def emboss(frames): #浮雕濾鏡
    modify_frames=[]
    for frame in frames:
        B,G,R = cv2.split(frame)
        R = embossFilter(R)
        G = embossFilter(G)
        B = embossFilter(B)
        img = cv2.merge([B,G,R])
        modify_frames.append(img)
    return modify_frames

def color(frames,b,g,r):  #blue:(b:0.587,g:0.299,r:0.114),green:(b:0.114,g:0.587,r:0.229),red:(b:0.114,g:0.114,r:0.887),purple:(b:0.299,g:0.114,r:0.587),yellow(b:0.005,g:0.499,r:0.888)
    modify_frames=[]
    for i in range(len(frames)):
        img_B = frames[i][:,:, 0]
        img_G = frames[i][:,:, 1]
        img_R = frames[i][:,:, 2]
        frames[i][:,:, 0]=img_B*b
        frames[i][:,:, 1]=img_G*g
        frames[i][:,:, 2]=img_R*r
        modify_frames.append(frames[i])
    return modify_frames

def size(frames,h_percent,w_percent):
    modify_frames=[]
    for i in range(len(frames)):
        frames[i]=resize(frames[i],h_percent,w_percent)
        modify_frames.append(frames[i])
    return modify_frames


def write_video(output,frames,fps):
    height, width,layers= frames[0].shape
    size = (width, height)
    out = cv2.VideoWriter(output,cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
    for i in range(len(frames)):
        out.write(frames[i])


def resize(img,h_percent,w_percent):
    height = img.shape[0]
    width = img.shape[1]
    h_percent=h_percent/100
    w_percent=w_percent/100
    height = height*h_percent
    width = width*w_percent
    img = cv2.resize(img,(int(width),int(height)))
    return img

def get_image(i):
    img=cv2.imread(i)
    return [img]

def write_image(output,image):
    cv2.imwrite(output,image[0])