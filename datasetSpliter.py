import os

SRC = './forImgClassifyCompressed'
DST = './custom_dataset'

SRC_I = os.path.join(SRC, 'img')
DST_I = os.path.join(DST, 'images')
SRC_L = os.path.join(SRC, 'convertedLabels')
DST_L = os.path.join(DST, 'labels')

SRC_I0 = os.path.join(SRC_I, '0')
SRC_I1 = os.path.join(SRC_I, '1')
SRC_L0 = os.path.join(SRC_L, '0')
SRC_L1 = os.path.join(SRC_L, '1')

DST_I0 = os.path.join(DST_I, '0')
DST_I1 = os.path.join(DST_I, '1')
DST_L0 = os.path.join(DST_L, '0')
DST_L1 = os.path.join(DST_L, '1')

