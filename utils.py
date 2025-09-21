import cv2

import numpy as np

from PIL import ImageFont, ImageDraw, Image

class Utils :

    # OpenCV IMG ->  Pillow IMG 객체 변환
    @staticmethod
    def to_pil(img) :

        pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        draw = ImageDraw.Draw(pil)

        return pil, draw

    # Pillow IMG 객체 -> OpenCV IMG 변환
    @staticmethod
    def to_opencv(pil) :

        return cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)

    # 텍스트 함수
    @staticmethod
    def text_pil(img, text, position, font_path, font_size, font_color) :

        # OpenCV IMG ->  Pillow IMG 객체 변환
        img_pil, draw = Utils.to_pil(img)

        font = ImageFont.truetype(font_path, font_size)

        # Pillow로 텍스트 그리기
        draw.text(position, text, font=font, fill=font_color)

        # Pillow IMG 객체 -> OpenCV IMG 변환
        img_cv = Utils.to_opencv(img_pil)

        return img_cv

    # 텍스트 + 박스 함수
    @staticmethod
    def text_box_pil(img, text, box_start, box_end, box_color, box_bold, font_path, font_size, font_color) :

        copy_img = img.copy()

        cv2.rectangle(copy_img, box_start, box_end, box_color, box_bold)

        # Pillow로 텍스트 그리기
        img_pil, draw = Utils.to_pil(copy_img)

        font = ImageFont.truetype(font_path, font_size)

        text_x = box_start[0]

        # padding 5
        text_y = box_start[1] - font_size - 5

        # 박스 벗어날 경우 위치 고정
        if text_y < 0:
            text_y = box_start[1] + 5

        draw.text((text_x, text_y), text, font=font, fill=font_color)

        # Pillow IMG 객체 -> OpenCV IMG 변환
        img_cv = Utils.to_opencv(img_pil)

        return img_cv