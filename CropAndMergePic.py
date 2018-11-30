# !/usr/bin/env python
# coding:utf-8

import numpy as np
import cv2
import os

class CropPic:
    def __init__(self):
        self.folder = ['rgb','gt','enet','dsnet']
        self.crop_width = 24
        self.crop_height = 12

    def image_cb(self,image_name,new_image):
        img = cv2.imread(image_name)
        img_shape = img.shape
        # img_new = img[self.crop_height:(img_shape[0] - self.crop_height),self.crop_width:(img_shape[1] - self.crop_width)]
        img_new = img[self.crop_height*2:(img_shape[0]),self.crop_width:(img_shape[1] - self.crop_width)]
        cv2.imwrite(new_image,img_new)

    def image_cb1(self,image_name,new_image):
        img = cv2.imread(image_name)
        img_shape = img.shape
        # img_new = img[self.crop_height:(img_shape[0] - self.crop_height),self.crop_width:(img_shape[1] - self.crop_width)]
        img_new = img[self.crop_height*2:(img_shape[0] - 250-250),274:(img_shape[1] - 274-500)]
        print img_new.shape
        cv2.imwrite(new_image,img_new)

    def run(self):
        os.mkdir('out_normal')
        for dir in self.folder:
            file_list = os.listdir(dir)
            for file in file_list:
                print "Handle: ",file
                self.image_cb(os.path.join(dir,file),os.path.join("out_normal",file))

        os.mkdir('out_special')
        for dir in self.folder:
            file_list = os.listdir(dir)
            for file in file_list:
                print "Handle: ",file
                self.image_cb1(os.path.join(dir,file),os.path.join("out_special",file))




# if __name__ == "__main__":
#     pipeLine = CropPic()
#     pipeLine.run()

from PIL import Image


folder = "out_normal"
root = folder
imageWidth = 1000
imageHeight = 500
files = os.listdir(folder)
cols = 4
rows = int(len(files)/cols)

target = Image.new("RGB",size=(imageWidth*cols,imageHeight*rows))

sorted_filelists = sorted(files,reverse=False)

for i in range(rows):
    left_y = imageHeight*i
    right_y = left_y + imageHeight
    rows_list = [sorted_filelists[i*cols+1],sorted_filelists[i*cols],sorted_filelists[i*cols+3],sorted_filelists[i*cols+2]]
    print rows_list
    for j in range(cols):
        left_x = imageWidth*j
        right_x = left_x + imageWidth
        img = Image.open(os.path.join(root,rows_list[j]))
        img.thumbnail((imageWidth,imageHeight))
        target.paste(img,(left_x,left_y,right_x,right_y))
target.save(os.path.join(root, "test.jpg"), "jpeg", quality=100, dpi=(600.0, 600.0))
target.save(os.path.join(root,"test.tiff"),"tiff",quality=100,dpi=(600.0,600.0))