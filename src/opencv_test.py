import os
import cv2
import math
from matplotlib import pyplot as plt

dir_path = 'data/test_data'
max_num = 10

num_files = len(os.listdir(dir_path))
num_rows = math.floor(math.sqrt(max_num))
num_col = (max_num // num_rows) + 1

print(num_rows)
print(num_col)

index = 1

for filename in os.listdir(dir_path):
    if index < 10:
        print(filename)
        img = cv2.imread(dir_path + '/' + filename, 0)
        sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
        plt.subplot(num_rows, num_col, index), plt.imshow(sobely,cmap = 'gray')
        plt.title(filename), plt.xticks([]), plt.yticks([])
        index = index + 1

plt.show()
