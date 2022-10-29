# -*- codeing = utf-8 -*-
# @Time : 2022/8/19 8:46
# @Author : zzw
# @File : Increase_data.py
# @Software : PyCharm
import cv2
import os
import matplotlib.pyplot as plt

jpgs_path   = "datasets/JPEGImages"
count = os.listdir("./datasets/JPEGImages/")
for i in range(0, len(count)):
    print(count[i])
    plt.savefig('image/{}.jpg'.format(i))






