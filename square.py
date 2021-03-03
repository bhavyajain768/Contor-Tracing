import numpy as np

# Function to go left
def goLeft(pixel,backtrack):
    if(backtrack==pixel):
        return
    elif(backtrack[0]==pixel[0] and backtrack[1]<pixel[1]):
        return((pixel[0]-1,pixel[1]))
    elif(backtrack[0]==pixel[0] and backtrack[1]>pixel[1]):
        return((pixel[0]+1,pixel[1]))
    elif(backtrack[0]>pixel[0] and backtrack[1]==pixel[1]):
        return((pixel[0],pixel[1]-1))
    else:
        return((pixel[0],pixel[1]+1))

# Function to go right
def goRight(pixel,backtrack):
    if(backtrack==pixel):
        return
    elif(backtrack[0]==pixel[0] and backtrack[1]<pixel[1]):
        return((pixel[0]+1,pixel[1]))
    elif(backtrack[0]==pixel[0] and backtrack[1]>pixel[1]):
        return((pixel[0]-1,pixel[1]))
    elif(backtrack[0]>pixel[0] and backtrack[1]==pixel[1]):
        return((pixel[0],pixel[1]+1))
    else:
        return((pixel[0],pixel[1]-1))

def squareAlgo(img):
    time = 0
    i = 0
#Loops for finding a black pixel
    while(i<img.shape[0]):
        j = 0
        while(j<img.shape[1]):
            if(img[i,j,0]==0):
                time = time+1
                break
            j = j+1
        if(j<img.shape[1] and img[i,j,0]==0):
            time = time+1
            break
        i = i+1
    if (i==img.shape[0] and j==img.shape[1]):
        time = time+1
        return
    B = [(i,j)] #Set for contor pixels
    p = (i,j) #Current pixel
    if(j!=0):
        time = time+1
        c = (i,j-1) #Backtracker
    elif(j==0 and i!=0):
        time = time+2
        c = (i-1,j)
    else:
        time = time+2
        c = (1,0)
    c2 = c #For storing the pixel through which we entered (i,j)
    p,c = goLeft(p,c),p
    while(p != (i,j) or c != c2):
        if(img[p[0],p[1],0]==0):
            B.append(p)
            p,c = goLeft(p,c),p
        else:
            p,c = goRight(p,c),p
    return B
        
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
print(squareAlgo(data))