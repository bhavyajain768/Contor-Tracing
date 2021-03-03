import numpy as np

#Function for getting next pixel of the current pixel in clocwise direction about the center pixel
def nextClockwise(center,current,I,J):
    time = 0
    if(center[0]<current[0] and center[1]==current[1]):
        time = time+1
        ans = (center[0],center[1]-1)
    elif(center[0]==current[0] and center[1]>current[1]):
        time = time+2
        ans = (center[0]-1,center[1])
    elif(center[0]>current[0] and center[1]==current[1]):
        time = time+3
        ans = (center[0],center[1]+1)
    else:
        time = time+3
        ans = (center[0]+1,center[1])
    
#A while loop for encountering corner cases
    while(ans[0]<(-0.5) or ans[1]<(-0.5) or ans[0]>=I or ans[1]>=J):
        a = nextClockwise(center,ans,I,J)
        ans = a[0]
        time = time+a[1]
    return (ans,time)

#To check if the line joining vertex 'a' and 'b' is a part of a black pixel in img
def isBlack(img,a,b):
    time = 0
    if (a==b):
        return False
    elif (a[0]==b[0] and a[1]<b[1]):
        time = time+1
        if (img[int(a[0]-0.5),int(a[1]+0.5),0]==0):
            time = time+1
            return (True,time)
        elif (img[int(a[0]+0.5),int(a[1]+0.5),0]==0):
            time = time+2
            return (True,time)
        else:
            time = time+2
            return (False,time)
    elif(a[0]==b[0] and a[1]>b[1]):
        time = time+2
        if (img[int(a[0]-0.5),int(a[1]-0.5),0]==0):
            time = time+1
            return (True,time)
        elif (img[int(a[0]+0.5),int(a[1]-0.5),0]==0):
            time = time+2
            return (True,time)
        else:
            time = time+2
            return (False,time)
    elif(a[0]>b[0] and a[1]==b[1]):
        time = time+3
        if (img[int(a[0]-0.5),int(a[1]-0.5),0]==0):
            time = time+1
            return (True,time)
        elif (img[int(a[0]-0.5),int(a[1]+0.5),0]==0):
            time = time+2
            return (True,time)
        else:
            time = time+2
            return (False,time)
    else:
        time = time+3
        if (img[int(a[0]+0.5),int(a[1]-0.5),0]==0):
            time = time+1
            return (True,time)
        elif (img[int(a[0]+0.5),int(a[1]+0.5),0]==0):
            time = time+2
            return (True,time)
        else:
            time = time+2
            return (False,time)

def vertex_following(img):
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
    B = [(i-0.5,j-0.5)] #Set for all the verticies
    p = (i-0.5,j-0.5) #Current vertex
    c = (i-0.5,j-1.5) #Pixel under consideration
    q = (c,time)

    while(c != (i-0.5,j-0.5)):
        x = isBlack(img,c,p)
        time = time+x[1]
        if(x[0]):
            B.append(c)
            q = nextClockwise(c,p,10.5,9.5)
            p,c = c,q[0]
            time = time+q[1]
        else:
            q = nextClockwise(p,c,10.5,9.5)
            c = q[0]
            time = time+q[1]
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
print(vertex_following(data))