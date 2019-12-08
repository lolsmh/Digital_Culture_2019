# -*- coding: utf-8 -*-
import math
from skimage.io import imread
import numpy as np
import collections

img = imread("obekt.jpg")
midimg = img[63:64, 0:128]  # выгружаем среднюю строку пикселей
midimg = 20 * (np.round(midimg / 20))  # производим квантование средней строки
midimgarr = midimg[0]  # так как мы имеем вложенный список, переводим его отдельно, для корректной работы метода counter
counter = collections.Counter(midimgarr)  # считаем встречаемость
print(counter)
