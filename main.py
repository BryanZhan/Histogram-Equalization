import cv2
import numpy as np


img = cv2.imread('mp2.jpg',0)
img1 = cv2.equalizeHist(img)
cv2.imshow('img1.jpg',img1)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf1 = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf1[img]
cv2.imshow('img2.jpg', img2)
cv2.waitKey(0)

