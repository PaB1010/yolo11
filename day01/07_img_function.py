# 이미지 텍스트 삽입 공통 함수화

import cv2

import numpy as np

from PIL import ImageFont, ImageDraw, Image

# 텍스트 함수
def text_pil(img, text, position, font_path, font_size, font_color) :

    # OpenCV IMG ->  Pillow IMG 객체 변환
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Pillow로 텍스트 그리기
    draw = ImageDraw.Draw(img_pil)

    font = ImageFont.truetype(font_path, font_size)

    draw.text(position, text, font=font, fill=font_color)

    # Pillow IMG 객체 -> OpenCV IMG 변환
    img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    return img_cv

# 텍스트 + 박스 함수
def text_box_pil(img, text, box_start, box_end, box_color, box_bold, font_path, font_size, font_color) :

    cv2.rectangle(img, box_start, box_end, box_color, box_bold)

    # OpenCV IMG ->  Pillow IMG 객체 변환
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Pillow로 텍스트 그리기
    draw = ImageDraw.Draw(img_pil)

    font = ImageFont.truetype(font_path, font_size)

    text_x = box_start[0]

    # padding 5
    text_y = box_start[1] - font_size - 5

    # 박스 벗어날 경우 위치 고정
    if text_y < 0:
        text_y = box_start[1] + 5

    draw.text((text_x, text_y), text, font=font, fill=font_color)

    # Pillow IMG 객체 -> OpenCV IMG 변환
    img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    return img_cv

img_file = "C:/Users/mudod/Pictures/bee.webp"

img = cv2.imread(img_file)

font_path = "C:/Windows/Fonts/NanumGothic.ttf"

# img = text_box_pil(img, "텍스트1", (50, 50), font_path, 32, (255, 255, 255))
# img = text_box_pil(img, "텍스트2", (50, 100), font_path, 64, (152,177, 203))

img = text_box_pil(
    img,
    "텍스트박스1",
    (50, 50),
    (350, 100),
    (0, 0, 0),
3,
    font_path,
    32,
    (255, 255, 255))

cv2.imshow("텍스트 이미지", img)

cv2.waitKey()

cv2.destroyAllWindows()