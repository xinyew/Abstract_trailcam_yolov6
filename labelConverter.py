import json, os

PATH = './forImgClassifyCompressed/labels'
PATH_STORE = './forImgClassifyCompressed/convertedLabels'

# PATH = './forImgClassify/labels'
# PATH_STORE = './forImgClassify/convertedLabels'

PATH0 = os.path.join(PATH, '0')
PATH1 = os.path.join(PATH, '1')
PATH_STORE0 = os.path.join(PATH_STORE, '0')
PATH_STORE1 = os.path.join(PATH_STORE, '1')

PATHS = [PATH1, PATH0]
PATHS_STORE = [PATH_STORE1, PATH_STORE0]

HEIGHT_OUT = 120
WIDTH_OUT = 160
HEIGHT_IN = 1024
WIDTH_IN = 1920

if not os.path.isdir(PATH_STORE):
    os.mkdir(PATH_STORE)
if not os.path.isdir(PATH_STORE0):
    os.mkdir(PATH_STORE0)
if not os.path.isdir(PATH_STORE1):
    os.mkdir(PATH_STORE1)


for i in range(len(PATHS)):
    p = PATHS[i]
    p_wrt = PATHS_STORE[i]
    for pp in os.listdir(p):
        d = os.path.join(p, pp)
        d_wrt = os.path.join(p_wrt, pp)
        with open(d) as f:
            j = json.loads(f.read())
            with open(d_wrt, 'w+') as ff:
                for c in j['children']:
                    if c['identity'] == 'pedestrian':
                        x0 = c['x0']
                        x1 = c['x1']
                        y0 = c['y0']
                        y1 = c['y1']
                        centerX = round((x0 + x1) / (2 * WIDTH_IN), 5)
                        centerY = round((y0 + y1) / (2 * HEIGHT_IN), 5)
                        bW = round(abs(x1 - x0) / WIDTH_IN, 5)
                        bH = round(abs(y1 - y0) / HEIGHT_IN, 5)
                        if centerX <= 0:
                            print(centerX)
                        if centerY <= 0:
                            print(centerY)
                        if bW <= 0:
                            print(bW)
                        if bH <= 0:
                            print(bH)
                        ff.write('0' + ' ' +
                                 str(centerX) + ' ' +
                                 str(centerY) + ' ' +
                                 str(bW) + ' ' +
                                 str(bH) + '\n')

