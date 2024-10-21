from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory # , page_num=10
img_path = './CA0001.pdf'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    if res:
        for line in res:
            print(line)

# 產生純文字檔
all_text = ""
for page in range(len(result)):
    res = result[page]
    if res:
        txts = [line[1][0] for line in res]
        txts_joined = ' '.join(txts)
    all_text += f"Page {page + 1}:\n{txts_joined}\n\n"

# Save the extracted text to a file
with open('paddleOCR_output.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)

# 显示结果
import fitz
from PIL import Image
import cv2
import numpy as np
imgs = []

# 繪圖前先載入原始圖
with fitz.open(img_path) as pdf:
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        mat = fitz.Matrix(2, 2)
        pm = page.get_pixmap(matrix=mat, alpha=False)
        # if width or height > 2000 pixels, don't enlarge the image
        if pm.width > 2000 or pm.height > 2000:
            pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

        img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        imgs.append(img)

# 開始繪圖
for idx in range(len(result)):
    res = result[idx]
    image = imgs[idx]
    if res:
        boxes = [line[0] for line in res]
        txts = [line[1][0] for line in res]
        scores = [line[1][1] for line in res]
    else:
        boxes = []
        txts = []
        scores = []
    im_show = draw_ocr(image, boxes, txts, scores, font_path='NotoSansTC-VariableFont_wght.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result_page_{}.jpg'.format(idx))