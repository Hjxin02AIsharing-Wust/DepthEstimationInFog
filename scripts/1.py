# from PIL import Image
# import numpy as np
# import skimage.transform
# img_file = Image.open('E:/datasets/ADD_data/oxford/oxford_processing_forADDS/day_val_451_gt/0000030525.png')
# depth_png = np.array(img_file,dtype=int)
# depth_gt = depth_png.astype(np.float) / 256.
#
# depth_gt = depth_gt[160:960-160,:]
# depth_gt = skimage.transform.resize(
#             depth_gt, (640,1280), order=0, preserve_range=True, mode='constant')
# print(depth_gt.shape)
import cv2
import scipy.io as scio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

dataFile = r'E:/datasets/depth_stereoscopic/test/berlin/berlin_000002_000019_depth_stereoscopic' # 单个的mat文件
data = scio.loadmat(dataFile)
print(type(data))
# print (data['data'])
# 由于导入的mat文件是structure类型的，所以需要取出需要的数据矩阵
a=data['depth_map']
# 取出需要的数据矩阵

# 数据矩阵转图片的函数
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im

new_im = MatrixToImage(a)
plt.imshow(a, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save('reggae.00041.bmp') # 保存图片
