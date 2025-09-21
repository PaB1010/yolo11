import cv2

import numpy as np

from ultralytics import YOLO

from utils import Utils

# YOLO11 모델
model = YOLO('yolo11x-seg.pt')

img_path = 'C:/Users/mudod/Pictures/cars.jpg'

# model()사용시 이미지 경로만 있어도 자동으로 이미지 로딩하지만
# Utils.text_mask_pil 함수 사용 위해 이미지 로딩
img = cv2.imread(img_path)

font_path = "C:/Windows/Fonts/NanumGothic.ttf"

# Detect - 객체 탐지 추론
# model() = 단축버전으로 conf, iou, verbose 기본값 사용
# conf = 신뢰도, 낮을수록 신뢰도 낮은 후보도 표시, 기본값 = 0.25
# iou = IoU 임계값, 낮을수록 중복 박스 허용, 기본값 = 0.7
# verbose = 상세 로그 출력 여부, 기본값 = True
results = model.predict(img, conf=0.25, iou=0.7, verbose=True)

if img is not None and len(results) > 0:

    # 박스정보, 마스크정보 모두
    results_list = zip(results[0].boxes, results[0].masks.xy)

    for box, segment in results_list :
        # 탐지된 객체 정보 추출
        # 1. 좌표 추출
        # 2. 신뢰도 추출
        # 3. 객체 id 추출 및 변환

        # 1. 좌표 추출 S #

        # 텍스트
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        text_start = (x1, y1)

        # 마스크
        points = np.int32([segment])

        # 1. 좌표 추출 E #

        # 2. 신뢰도 추출 S #

        conf = float(box.conf[0])

        # 2. 신뢰도 추출 E #

        # 3. 객체 id 추출 및 변환 S #

        cls_id = int(box.cls[0])

        # 클래스ID를 클래스명으로 변환
        class_name = model.names[cls_id]

        # 3. 객체 id 추출 및 변환 E #

        # f-string 사용
        # conf는 소수점 2자리까지
        label = f'{class_name}({cls_id}) : {conf:.2f}'

        img = Utils.text_mask_pil(
            img,
            text=label,
            points=points,
            mask_color=(203, 177, 152),
            opacity=0.5,
            text_start=text_start,
            font_path=font_path,
            font_size=25,
            font_color=(255, 255, 255)
        )

    cv2.imshow('YOLO11 Segment Utils', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    if img is None:

        print("잘못된 이미지 경로")

    else:

        print("탐지 객체 없음")