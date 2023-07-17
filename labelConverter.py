import json, os

PATH = './forImgClassifyCompressed/labels'
PATH_STORE = './forImgClassifyCompressed/convertedLabels'
PATH0 = os.path.join(PATH, '0')
PATH1 = os.path.join(PATH, '1')
PATH_STORE0 = os.path.join(PATH_STORE, '0')
PATH_STORE1 = os.path.join(PATH_STORE, '1')

PATHS = [PATH1, PATH0]
PATHS_STORE = [PATH_STORE1, PATH_STORE0]

HEIGHT_IN = 1024
WIDTH_IN = 1920
HEIGHT_OUT = 120
WIDTH_OUT = 160
HRATIO = HEIGHT_OUT / HEIGHT_IN
WRATIO = WIDTH_OUT / WIDTH_IN

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
                        centerX = int((x0 + x1) / 2 * WRATIO)
                        centerY = int((y0 + y1) / 2 * HRATIO)
                        bW = int(abs(x1 - x0) * WRATIO)
                        bH = int(abs(y1 - y0) * HRATIO)
                        ff.write('1' + ' ' +
                                 str(centerX) + ' ' +
                                 str(centerY) + ' ' +
                                 str(bW) + ' ' +
                                 str(bH) + '\n')

