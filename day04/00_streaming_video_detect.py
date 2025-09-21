# 스트리밍 영상 객체 탐지

import cv2
from ultralytics import YOLO
from utils import Utils

model = YOLO('yolo11x.pt')

# 스트리밍 영상
youtube_url = "https://youtu.be/P4F2dxSEDLE"

streaming_url = Utils.get_best_video(youtube_url)

output_path = "E:/[공부]/opencv/muhan_x.mp4"

font_path = "C:/Windows/Fonts/NanumGothic.ttf"

if streaming_url:

    cap = cv2.VideoCapture(streaming_url)

    if cap.isOpened():

        # 원본 비디오의 너비
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        # 원본 비디오의 높이
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 코덱, mp4v = mp4
        mp4 = cv2.VideoWriter_fourcc(*'mp4v')

        # VideoWriter 객체 생성
        # (저장경로, 코덱, (너비, 높이))
        out = cv2.VideoWriter(output_path, mp4, 25.0, (width, height))

        while True:

            # 다음 프레임 읽기
            ret, img = cap.read()

            # 다음 프레임 없음
            if not ret:

                break

            # 객체 탐지
            results = model.predict(img)

            if results[0].boxes is not None and len(results[0].boxes) > 0:

                # 탐지된 객체의 정보
                boxes = results[0].boxes

                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    conf = float(box.conf[0])

                    cls_id = int(box.cls[0])

                    class_name = model.names[cls_id]

                    label = f'{class_name}({cls_id}) : {conf:.2f}'

                    img = Utils.text_box_pil(
                        img,
                        text=label,
                        box_start=(x1, y1),
                        box_end=(x2, y2),
                        box_color=(203, 177, 152),
                        box_bold=4,
                        font_path=font_path,
                        font_size=25,
                        font_color=(255, 255, 255)
                    )

            # 비디오 파일 작성
            out.write(img)

            # 화면에 표시
            cv2.imshow('Youtube Streaming Detect', img)

            # 1ms 지연, q 입력시 반복 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out.release()

    else:
        print("잘못된 유튜브 경로")

    # 자원 해제
    cap.release()

    cv2.destroyAllWindows()