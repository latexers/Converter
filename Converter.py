import cv2
import scipy.io as scio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
# 数据矩阵转图片的函数
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im

if __name__ == '__main__':
    path = r'C:\Users\DE\Downloads\NPC_Renew_Data_1'
    IDs = os.listdir(path)
    for id in IDs:
        idPath = path + '\\' + id
        print(idPath)
        labelFiles = os.listdir(idPath)
        print(labelFiles)
        for label in labelFiles:
            filePath = idPath + '\\' + label
            if os.path.isfile(filePath):
                (filename, extension) = os.path.splitext(label)
                pngDir = idPath + '\\' + filename
                if not os.path.exists(pngDir):
                    os.makedirs(pngDir)
                data = scio.loadmat(filePath)
                print(data.keys())
                seg = list(data.keys())[-1]
                data = data[seg]
                x, y, z = data.shape
                for i in range(0,z):
                    binaryimg = np.uint8(data[:,:,i]>0)
                    img = binaryimg*255
                    new_img = Image.fromarray(img, 'L')
                    name = pngDir + '\\' + str(i) + '.png'
                    new_img.save(name)
                    print(name)
                # print('It is a file')

        # Labels = os.listdir(r'C:\Users\DE\Downloads\NPC_Renew_Data_2' + '\\'+id)
        # print(Labels)
    # dataFile = r'10100990_T2_Label_1.mat'
    # data = scio.loadmat(dataFile)
    # print(type(data))
    # # print(data)
    # a = data['seg1']
    # print(type(a))
    # x,y,z = a.shape
    # print(a.shape)
    # print(a[:,:,1].shape)
    # for i in range(0,36):
    #     b = a[:,:,i] * 255
    #     new_im = Image.fromarray(b, 'L')
    #     name = str(i) + '.png'
    #     new_im.save(name)
    # # for i in range(0,z):
    # #     print(i)

        # print(type(a[::i]))
        # b = a[::i].astype('float64')
        # print(b.shape)
        # new_im = Image.fromarray(b,'L')
        # new_im.save(i + ".png")
        # print(a[::i])
    # new_im = MatrixToImage(a)
    # plt.imshow(a, cmap=plt.cm.gray, interpolation='nearest')
    # new_im.show()
    # new_im.save('reggae.00041.bmp')  # 保存图片
    # print("Finished!")