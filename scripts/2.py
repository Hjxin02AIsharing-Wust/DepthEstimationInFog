import cv2
import scipy.io as sio
import numpy as np
# mat_data = sio.loadmat(r'E:/datasets/depth_stereoscopic/test/berlin/berlin_000002_000019_depth_stereoscopic')
# # # #直接输出mat文件的内容
# # # #输出mat数据的key
# mat_data=mat_data['depth_map']
# x = np.array(mat_data)
# print(x)
from PIL import Image
import numpy as np
import skimage.transform
img_file = Image.open('test/0004._disp.jpeg')
img_file2=Image.open('test/2.png')
y1=img_file.convert('L')
y1= np.array(y1)
y2=np.array(img_file2)
print(y1)
print(y2)
# img_file2=Image.open('test/0004_ADD_MyModel_0_disp.jpeg')
# y2=np.array(img_file2)
# y1=y1.reshape(2048,1024)
# depth_gt = depth_png.astype(np.float) / 256.
#
# depth_gt = depth_gt[160:960-160,:]
# y1= skimage.transform.resize(
#              y1, (1024,2048), order=0, preserve_range=True, mode='constant')
# print(y1.shape)
# print((1280, 640)[::-1])
def compute_errors(gt, pred):
    """Computation of error metrics between predicted and ground truth depths
    """
    thresh = np.maximum((gt / pred), (pred / gt))
    a1 = (thresh < 1.25     ).mean()
    a2 = (thresh < 1.25 ** 2).mean()
    a3 = (thresh < 1.25 ** 3).mean()

    rmse = (gt - pred) ** 2
    rmse = np.sqrt(rmse.mean())

    rmse_log = (np.log(gt) - np.log(pred)) ** 2
    rmse_log = np.sqrt(rmse_log.mean())

    abs_rel = np.mean(np.abs(gt - pred) / gt)

    sq_rel = np.mean(((gt - pred) ** 2) / gt)

    return print("\n  " + ("{:>8} | " * 7).format(abs_rel, sq_rel, rmse, rmse_log, a1, a2, a3))

compute_errors(y2, y1)