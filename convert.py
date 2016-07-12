
import cv2
import numpy as np


for i in range(1,63):
    txt = open('./final/Sample0' + str(i).zfill(2) + '/text' + str(i) + '.txt', 'w')
    for j in range(1,1017):   #Fnt
        name = 'img0' + str(i).zfill(2) + '-0' + str(j).zfill(4)
        img = cv2.imread('./Text-Recognition/English/Fnt/Sample0' + str(i).zfill(2) + '/' + name + '.png',cv2.IMREAD_GRAYSCALE)
        n_name = 'img0' + str(i).zfill(2) + '_' + str(j)
        output = cv2.resize(img, (20,20), interpolation=cv2.INTER_AREA)
        for k in range(20):
            for l in range(20):
                txt.write(str(output[k][l]) + ',')
        cv2.imwrite('./final/Sample0' + str(i).zfill(2) + '/'+ n_name + '.png', output)
        txt.write('\n')
    tmp = j
    print tmp
    for j in range(1,56):   #Hnd
        name = 'img0' + str(i).zfill(2) + '-0' + str(j).zfill(2)
        img = cv2.imread('./Text-Recognition/English/Hnd/Img/Sample0' + str(i).zfill(2) + '/' + name + '.png',cv2.IMREAD_GRAYSCALE)
        n_name = 'img0' + str(i).zfill(2) + '_' + str(tmp+j)
        output = cv2.resize(img, (20,20), interpolation=cv2.INTER_AREA)
        for k in range(20):
            for l in range(20):
                txt.write(str(output[k][l]) + ',')
        cv2.imwrite('./final/Sample0' + str(i).zfill(2) + '/'+ n_name + '.png', output)
        txt.write('\n')
    tmp += j
    print tmp
    for j in range(1, 560):     #Good
        name = 'img0' + str(i).zfill(2) + '-0' + str(j).zfill(4)
        try:
            input = cv2.imread('./Text-Recognition/English/GoodImg/Bmp/Sample0' + str(i).zfill(2) + '/' + name + '.png',cv2.IMREAD_GRAYSCALE)
            output = cv2.resize(input, (20, 20), interpolation=cv2.INTER_AREA)
            n_name = 'img0' + str(i).zfill(2) + '_' + str(tmp + j)
            for k in range(20):
                for l in range(20):
                    txt.write(str(output[k][l]) + ',')
            cv2.imwrite('./final/Sample0' + str(i).zfill(2) + '/' + n_name + '.png', output)
            txt.write('\n')
        except:
            break
    tmp += (j-1)
    for j in range(1, 361):      #Bad
        name = 'img0' + str(i).zfill(2) + '-0' + str(j).zfill(4)
        try:
            input = cv2.imread('./Text-Recognition/English/BadImag/Bmp/Sample0' + str(i).zfill(2) + '/' + name + '.png',cv2.IMREAD_GRAYSCALE)
            output = cv2.resize(input, (20, 20), interpolation=cv2.INTER_AREA)
            n_name = 'img0' + str(i).zfill(2) + '_' + str(tmp + j)
            for k in range(20):
                for l in range(20):
                    txt.write(str(output[k][l]) + ',')
            cv2.imwrite('./final/Sample0' + str(i).zfill(2) + '/' + n_name + '.png', output)
            txt.write('\n')
        except:
            break

cv2.waitKey(0)