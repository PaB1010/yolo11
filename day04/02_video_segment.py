import cv2

import numpy as np

from ultralytics import YOLO

from utils import Utils

# YOLO11 모델
model = YOLO('yolo11x-seg.pt')

video_file = "E:/study/people.mp4"

output_path = "E:/study/opencv/people_segment_x.mp4"

font_path = "C:/Windows/Fonts/NanumGothic.ttf"

cap = cv2.VideoCapture(video_file)

if cap.isOpened():

    # 원본 영상 프레임 추출
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 원본 비디오의 너비
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # 원본 비디오의 높이
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 코덱, mp4v = mp4
    mp4 = cv2.VideoWriter_fourcc(*'mp4v')

    # VideoWriter 객체 생성
    # (저장경로, 코덱, (너비, 높이))
    out = cv2.VideoWriter(output_path, mp4, fps, (width, height))

    while True:

        ret, frame = cap.read()

        if not ret:

            break

        results = model.predict(frame)

        if results[0].boxes is not None and len(results[0].boxes) > 0 :

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
                    frame,
                    text=label,
                    points=points,
                    mask_color=(203, 177, 152),
                    opacity=0.5,
                    text_start=text_start,
                    font_path=font_path,
                    font_size=25,
                    font_color=(255, 255, 255)
                )

        out.write(img)

        cv2.imshow('YOLO11 Video Segment Utils', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()

else:

    print("탐지 객체 없음")

cap.release()

cv2.destroyAllWindows()