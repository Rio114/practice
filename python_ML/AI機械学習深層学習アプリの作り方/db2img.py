import struct
from PIL import Image, ImageEnhance
import glob, os

outdir = 'png-etl1/'
if not os.path.exists(outdir): os.mkdir(outdir)

files = glob.glob('ETL1/*')
for fname in files:
    if fname == 'ETL1/ETL1INFO': continue
    print(fname)
    f = open(fname, 'rb')
    f.seek(0)
    while True:
        s = f.read(2052)
        if not s: break
        r = struct.unpack('>H2sHBs4sI4H4B2H2016sI', s)
        code_ascii = r[1]
        code_jis = r[3]
        iF = Image.frombytes('F', (64, 63), r[17], 'bit', 4)
        iP = iF.convert('L')

        dir = outdir + '/' + str(code_jis)
        if not os.path.exists(dir): os.mkdir(dir)
        fn = '{0:02x}-{1:02x}{2:04x}.png'.format(code_jis, r[0], r[2])
        fullpath = dir + '/' + fn
        if os.path.exists(fullpath): continue
        enhancer = ImageEnhance.Brightness(iP)
        iE = enhancer.enhance(16)
        iE.save(fullpath, 'PNG')
print('done.')