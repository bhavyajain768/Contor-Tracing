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
    while(ans[0]<0 or ans[1]<0 or ans[0]>=I or ans[1]>=J):
        a = nextClockwise(center,ans)
        ans = a[0]
        time = time+a[1]
    return (ans,time)


def pavilidisAlgo(img):
    time = 0
    i = 0
#Loops for finding a black pixel
    while(i<img.shape[0]):
        j = 0
        while(j<img.shape[1]):
            if(img[i,j,0]==0 and j>0 and img[i,j-1,0]!=0 and img[i-1,j,0]!=0):
                time = time+3
                break
            j = j+1
        if(j<img.shape[1] and img[i,j,0]==0 and j>0 and img[i,j-1,0]!=0 and img[i-1,j,0]!=0):
            time = time+3
            break
        i = i+1
    if (i==img.shape[0] and j==img.shape[1]):
        time = time+1
        return
    p = (i,j) #Current pixel
    B = [(i,j)] #Set for contor pixels
    c = (i,j-1) #Backtracker
    
    counter = 0
# This while loop is for doing clockwise rotations if p1,p2 and p3 are white
    while(counter<4):
 # If-else blocks for defining the position of p1,p2 and p3
        if(c[0]==p[0] and c[1]<p[1]):
            time = time+1
            p1 = (p[0]-1,p[1]+1)
            p2 = (p[0],p[1]+1)
            p3 = (p[0]+1,p[1]+1)
        elif(c[0]==p[0] and c[1]>p[1]):
            time = time+2
            p1 = (p[0]+1,p[1]-1)
            p2 = (p[0],p[1]-1)
            p3 = (p[0]-1,p[1]-1)
        elif(c[0]>p[0] and c[1]==p[1]):
            time = time+3
            p1 = (p[0]-1,p[1]-1)
            p2 = (p[0]-1,p[1])
            p3 = (p[0]-1,p[1]+1)
        else:
            time = time+3
            p1 = (p[0]+1,p[1]+1)
            p2 = (p[0]+1,p[1])
            p3 = (p[0]+1,p[1]-1)

        #If-else blocks for updating value of p and c
        if(img[p1[0],p1[1],0]==0):
            time = time+1
            B.append(p1)
            p,c = p1,p2
            break
        elif(img[p2[0],p2[1],0]==0):
            time = time+2
            B.append(p2)
            p,c = p2,p
            break
        elif(img[p3[0],p3[1],0]==0):
            time = time+3
            B.append(p3)
            if(c[0]==p[0] and c[1]<p[1]):
                time = time+1
                c = (p3[0],p3[1]-1)
            elif(c[0]==p[0] and c[1]>p[1]):
                time = time+2
                c = (p3[0],p3[1]+1)
            elif(c[0]>p[0] and c[1]==p[1]):
                time = time+3
                c = (p3[0]+1,p3[1])
            else:
                time = time+3
                c = (p3[0]-1,p3[1])
            p = p3
            break
        else:
            time = time+3
            a = nextClockwise(p,c,img.shape[0],img.shape[1])
            time = time+a[1]
            c = a[0]

        counter = counter+1
    # Case when there is an isolated pixel
    if(counter==4):
        return
    # Main while loop for traversing the image 
    while(p != (i,j)):
        counter = 0
# This while loop is for doing clockwise rotations if p1,p2 and p3 are white
        while(counter<4):
    # If-else blocks for defining the position of p1,p2 and p3
            if(c[0]==p[0] and c[1]<p[1]):
                time = time+1
                p1 = (p[0]-1,p[1]+1)
                p2 = (p[0],p[1]+1)
                p3 = (p[0]+1,p[1]+1)
            elif(c[0]==p[0] and c[1]>p[1]):
                time = time+2
                p1 = (p[0]+1,p[1]-1)
                p2 = (p[0],p[1]-1)
                p3 = (p[0]-1,p[1]-1)
            elif(c[0]>p[0] and c[1]==p[1]):
                time = time+3
                p1 = (p[0]-1,p[1]-1)
                p2 = (p[0]-1,p[1])
                p3 = (p[0]-1,p[1]+1)
            else:
                time = time+3
                p1 = (p[0]+1,p[1]+1)
                p2 = (p[0]+1,p[1])
                p3 = (p[0]+1,p[1]-1)

            #If-else blocks for updating value of p and c
            if(img[p1[0],p1[1],0]==0):
                time = time+1
                B.append(p1)
                p,c = p1,p2
                break
            elif(img[p2[0],p2[1],0]==0):
                time = time+2
                B.append(p2)
                p,c = p2,p
                break
            elif(img[p3[0],p3[1],0]==0):
                time = time+3
                B.append(p3)
                if(c[0]==p[0] and c[1]<p[1]):
                    time = time+1
                    c = (p3[0],p3[1]-1)
                elif(c[0]==p[0] and c[1]>p[1]):
                    time = time+2
                    c = (p3[0],p3[1]+1)
                elif(c[0]>p[0] and c[1]==p[1]):
                    time = time+3
                    c = (p3[0]+1,p3[1])
                else:
                    time = time+3
                    c = (p3[0]-1,p3[1])
                p = p3
                break
            else:
                time = time+3
                a = nextClockwise(p,c,img.shape[0],img.shape[1])
                time = time+a[1]
                c = a[0]
    
            counter = counter+1
        # Case when there is an isolated pixel
        if(counter==4):
            return
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
print(pavilidisAlgo(data))