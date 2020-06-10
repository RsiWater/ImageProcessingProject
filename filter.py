import cv2
import numpy as np

def FilterED(inRGB,mid):
    reRGB=[]
    for i in range(len(inRGB)):
        reLine=[]
        for j in range(len(inRGB[0])):
            up = i-1
            down = i+1
            left = j-1
            right = j+1
            if up<0 or left<0: lu=0
            else: lu=inRGB[up][left]

            if up<0: u=0
            else: u=inRGB[up][j]

            if up<0 or right>=len(inRGB[0]): ru=0
            else: ru=inRGB[up][right]

            if left<0: l=0
            else: l=inRGB[i][left]

            if right>=len(inRGB[0]): r=0
            else: r=inRGB[i][right]

            if left<0 or down>=len(inRGB): ld=0
            else: ld = inRGB[down][left]

            if down>=len(inRGB): d=0
            else: d = inRGB[down][j]

            if right>=len(inRGB[0]) or down>=len(inRGB): rd=0
            else: rd=inRGB[down][right]

            re = mid*inRGB[i][j] - lu - u - ru - l - r - ld - d - rd
            if re<0: re=0
            if re>255: re=255
            reLine.append(re)
        reRGB.append(reLine)
    reRGB=np.array(reRGB)
    return reRGB

def embossFilter(inRGB):
    reRGB=[]
    for i in range(len(inRGB)):
        reLine=[]
        for j in range(len(inRGB[0])):
            up = i-1
            left = j-1

            if up<0 or left<0: lu=0
            else: lu=int(inRGB[up][left])

            re = inRGB[i][j] - lu
            if re<0: re=0
            if re>255: re=255
            reLine.append(re)
        reRGB.append(reLine)
    reRGB=np.array(reRGB)
    return reRGB

if __name__=='__main__':
    img_src = cv2.imread('patrick.jpg')
    B,G,R = cv2.split(img_src)
    R = embossFilter(R)
    G = embossFilter(G)
    B = embossFilter(B)
    img = cv2.merge([B,G,R])
    cv2.imwrite('emboss.png',img)

    B,G,R = cv2.split(img_src)
    R = FilterED(R,8)
    G = FilterED(G,8)
    B = FilterED(B,8)
    img = cv2.merge([B,G,R])
    cv2.imwrite('edge.png',img)

    B,G,R = cv2.split(img_src)
    R = FilterED(R,10)
    G = FilterED(G,10)
    B = FilterED(B,10)
    img = cv2.merge([B,G,R])
    cv2.imwrite('edgeE.png',img)

    B,G,R = cv2.split(img_src)
    R = FilterED(R,9)
    G = FilterED(G,9)
    B = FilterED(B,9)
    img = cv2.merge([B,G,R])
    cv2.imwrite('edgeEmore.png',img)