import os, random, shutil


TEST_RATIO = 0.1
VAL_RATIO = 0.1

SRC = './forImgClassifyCompressed'
# SRC = './forImgClassify'
DST = './custom_dataset'

SRC_I = os.path.join(SRC, 'img')
DST_I = os.path.join(DST, 'images')
SRC_L = os.path.join(SRC, 'convertedLabels')
DST_L = os.path.join(DST, 'labels')

SRC_I0 = os.path.join(SRC_I, '0')
SRC_I1 = os.path.join(SRC_I, '1')
SRC_L0 = os.path.join(SRC_L, '0')
SRC_L1 = os.path.join(SRC_L, '1')

DST_ITRAIN = os.path.join(DST_I, 'train')
DST_LTRAIN = os.path.join(DST_L, 'train')
DST_ITEST = os.path.join(DST_I, 'test')
DST_LTEST = os.path.join(DST_L, 'test')
DST_IVAL = os.path.join(DST_I, 'val')
DST_LVAL = os.path.join(DST_L, 'val')

if not os.path.isdir(DST):
    os.mkdir(DST)
if not os.path.isdir(DST_I):
    os.mkdir(DST_I)
if not os.path.isdir(DST_L):
    os.mkdir(DST_L)
if not os.path.isdir(DST_ITRAIN):
    os.mkdir(DST_ITRAIN)
if not os.path.isdir(DST_LTRAIN):
    os.mkdir(DST_LTRAIN)
if not os.path.isdir(DST_ITEST):
    os.mkdir(DST_ITEST)
if not os.path.isdir(DST_LTEST):
    os.mkdir(DST_LTEST)
if not os.path.isdir(DST_IVAL):
    os.mkdir(DST_IVAL)
if not os.path.isdir(DST_LVAL):
    os.mkdir(DST_LVAL)


img0_list = os.listdir(SRC_I0)
img1_list = os.listdir(SRC_I1)
label0_list = os.listdir(SRC_L0)
label1_list = os.listdir(SRC_L1)
img0_list.sort()
img1_list.sort()
label0_list.sort()
label1_list.sort()

rdnList = list(range(len(img0_list)))
random.shuffle(rdnList)

idx = 0
for i in range(int(len(img0_list) * TEST_RATIO)):
    ii = rdnList[idx]
    idx += 1
    src_i0 = os.path.join(SRC_I0, img0_list[ii])
    src_l0 = os.path.join(SRC_L0, label0_list[ii])
    src_i1 = os.path.join(SRC_I1, img1_list[ii])
    src_l1 = os.path.join(SRC_L1, label1_list[ii])
    dst_i0 = os.path.join(DST_ITEST, img0_list[ii])
    dst_l0 = os.path.join(DST_LTEST, label0_list[ii])
    dst_i1 = os.path.join(DST_ITEST, img1_list[ii])
    dst_l1 = os.path.join(DST_LTEST, label1_list[ii])
    dst_l0 = dst_l0[:-4] + 'txt'
    dst_l1 = dst_l1[:-4] + 'txt'
    shutil.copy(src_i0, dst_i0)
    shutil.copy(src_l0, dst_l0)
    shutil.copy(src_i1, dst_i1)
    shutil.copy(src_l1, dst_l1)
    # print(src_l0, dst_l0)
    # print(src_l1, dst_l1)
    # print(src_i1, dst_i1)
    # print(src_i0, dst_i0)

for i in range(int(len(img0_list) * VAL_RATIO)):
    ii = rdnList[idx]
    idx += 1
    src_i0 = os.path.join(SRC_I0, img0_list[ii])
    src_l0 = os.path.join(SRC_L0, label0_list[ii])
    src_i1 = os.path.join(SRC_I1, img1_list[ii])
    src_l1 = os.path.join(SRC_L1, label1_list[ii])
    dst_i0 = os.path.join(DST_IVAL, img0_list[ii])
    dst_l0 = os.path.join(DST_LVAL, label0_list[ii])
    dst_i1 = os.path.join(DST_IVAL, img1_list[ii])
    dst_l1 = os.path.join(DST_LVAL, label1_list[ii])
    dst_l0 = dst_l0[:-4] + 'txt'
    dst_l1 = dst_l1[:-4] + 'txt'
    shutil.copy(src_i0, dst_i0)
    shutil.copy(src_l0, dst_l0)
    shutil.copy(src_i1, dst_i1)
    shutil.copy(src_l1, dst_l1)
    # print(src_l0, dst_l0)
    # print(src_l1, dst_l1)
    # print(src_i1, dst_i1)
    # print(src_i0, dst_i0)

for i in range(idx, len(img0_list)):
    ii = rdnList[idx]
    idx += 1
    src_i0 = os.path.join(SRC_I0, img0_list[ii])
    src_l0 = os.path.join(SRC_L0, label0_list[ii])
    src_i1 = os.path.join(SRC_I1, img1_list[ii])
    src_l1 = os.path.join(SRC_L1, label1_list[ii])
    dst_i0 = os.path.join(DST_ITRAIN, img0_list[ii])
    dst_l0 = os.path.join(DST_LTRAIN, label0_list[ii])
    dst_i1 = os.path.join(DST_ITRAIN, img1_list[ii])
    dst_l1 = os.path.join(DST_LTRAIN, label1_list[ii])
    dst_l0 = dst_l0[:-4] + 'txt'
    dst_l1 = dst_l1[:-4] + 'txt'
    shutil.copy(src_i0, dst_i0)
    shutil.copy(src_l0, dst_l0)
    shutil.copy(src_i1, dst_i1)
    shutil.copy(src_l1, dst_l1)
    # print(src_l0, dst_l0)
    # print(src_l1, dst_l1)
    # print(src_i1, dst_i1)
    # print(src_i0, dst_i0)