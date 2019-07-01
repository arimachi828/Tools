import os
import glob
from PIL import Image
from pathlib import Path

# 元画像が入ったディレクトリ
p = Path('/Users/arimachishun/Desktop/pokemon_datasets_cat_30/115')
src_img_list = list(p.glob('*.jpg'))

# トリミングのサイズ(ピクセル)

for i, src_img in enumerate(src_img_list):

    # 画像読み込み
    img = Image.open(src_img)

    # トリミング
    img_crop = img.crop((30, 130, 820, 720))

    # トリミングした画像を保存
    img_crop.save('/Users/arimachishun/Desktop/pokemon_datasets_cat_30/115/after_data' + str(i) + '.jpg', 'JPEG', quality=100, optimize=True)
