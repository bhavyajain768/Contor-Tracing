from PIL import Image
import numpy as np

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
img = Image.fromarray(data, 'RGB')
print(data.shape[1])