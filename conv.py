
import os
import glob
from PIL import Image
from pathlib import Path

# 元画像が入ったディレクトリ
p = Path('/Users/arimachishun/work/star_form/datasets/試合時')
src_img_list = list(p.glob('*.JPG'))

# トリミングのサイズ(ピクセル)

for i, src_img in enumerate(src_img_list):

    # 画像読み込み
    img = Image.open(src_img)

    img = img.convert('RGB')
    img.save('/Users/arimachishun/work/star_form/datasets/試合時/convert' + str(i) + ".jpg",quality=100)
