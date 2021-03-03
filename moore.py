import numpy as np

#Function for getting next pixel of the current pixel in clocwise direction about the center pixel
def nextClockwise(center,current,I,J):
    time = 0
    if(center[0]<current[0] and center[1]<current[1]):
        ans = (current[0],current[1]-1)
        time = time+1
    elif(center[0]<current[0] and center[1]==current[1]):
        time = time+2
        ans = (current[0],current[1]-1)
    elif(center[0]<current[0] and center[1]>current[1]):
        time = time+3
        ans = (current[0]-1,current[1])
    elif(center[0]==current[0] and center[1]>current[1]):
        time = time+4
        ans = (current[0]-1,current[1])
    elif(center[0]>current[0] and center[1]>current[1]):
        time = time+5
        ans = (current[0],current[1]+1)
    elif(center[0]>current[0] and center[1]==current[1]):
        time = time+6
        ans = (current[0],current[1]+1)
    elif(center[0]>current[0] and center[1]<current[1]):
        time = time+7
        ans = (current[0]+1,current[1])
    else:
        time = time+7
        ans = (current[0]+1,current[1])
    
#A while loop for encountering corner cases
    while(ans[0]<0 or ans[1]<0 or ans[0]>=I or ans[1]>=J):
        a = nextClockwise(center,ans,I,J)
        ans = a[0]
        time = time+a[1]
    return (ans,time)


def mooreAlgo(img):
    time = 0
    i = 0
#Loops for finding a black pixel
    while(i<img.shape[0]):
        j = 0
        while(j<img.shape[1]):
            if(img[i,j,0]==0 and j>0 and img[i,j-1,0]!=0):
                time = time+2
                break
            j = j+1
        if(j<img.shape[1] and img[i,j,0]==0 and j>0 and img[i,j-1,0]!=0):
            time = time+2
            break
        i = i+1
    if (i==img.shape[0] and j==img.shape[1]):
        time = time+1
        return
    B = [(i,j)] #Set for contor pixels
    p = (i,j) #Current pixel
    c = (i,j-1) #Pixel under consideration
    b = p #A backtracker for the clockwise movement of c
    q = (c,time)
    while(c != (i,j) or b != (i,j-1)):
        if(img[c[0],c[1],0]==0):
            time = time+1
            B.append(c)
            p = c
            c = b
        else:
            b = c
            q = nextClockwise(p,c,img.shape[0],img.shape[1])
            c,time = q[0],time+q[1]+1
    return time

w, h = 11, 10
data = np.zeros((w, h, 3), dtype=np.uint8)
data[0:11, 0:10] = [255,255,225] #White background
data[1,7:9] = [0,0,0]
data[2,7:9] = [0,0,0]
data[3,3:7] = [0,0,0]
data[4,2:7] = [0,0,0]
data[5,1:7] = [0,0,0]
data[6,2:7] = [0,0,0]
data[7,3:7] = [0,0,0]
data[8,7:9] = [0,0,0]
data[9,7:9] = [0,0,0]
print(mooreAlgo(data))
