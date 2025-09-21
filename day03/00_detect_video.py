import cv2

# fps 계산용
import time

from ultralytics import YOLO

from utils import Utils

model = YOLO('yolo11x.pt')
# model = YOLO('yolo11l.pt')
# model = YOLO('yolo11m.pt')
# model = YOLO('yolo11s.pt')
# model = YOLO('yolo11n.pt')

# video_file = "E:/[공부]/opencv/avocado.mp4"
video_file = "E:/[공부]/people.mp4"

output_path = "E:/[공부]/opencv/people_detect_x.mp4"
# output_path = "E:/[공부]/opencv/people_detect_l.mp4"
# output_path = "E:/[공부]/opencv/people_detect_m.mp4"
# output_path = "E:/[공부]/opencv/people_detect_s.mp4"
# output_path = "E:/[공부]/opencv/people_detect_n.mp4"

font_path = "C:/Windows/Fonts/NanumGothic.ttf"

# VideoCapture 객체 생성해 동영상 로딩 (웹캠도 가능)
cap = cv2.VideoCapture(video_file)

if cap.isOpened():

    # 원본 영상 프레임 추출
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 초 단위로 계산
    fream_time = 1.0 / fps

    # 원본 비디오의 너비
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # 원본 비디오의 높이
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 코덱, mp4v = mp4
    mp4 = cv2.VideoWriter_fourcc(*'mp4v')

    # VideoWriter 객체 생성
    # (저장경로, 코덱, (너비, 높이))
    out = cv2.VideoWriter(output_path, mp4, fps, (width, height))

    fps_time = time.time()

    while True:

        ret, img = cap.read()

        if not ret:

            break

        # 현재 시간
        current_time = time.time()

        # 객체 탐지
        results = model(img)

        if results[0].boxes is not None and len(results[0].boxes) > 0 :

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

        # 현재 시간 - 이전 시간
        calculate_time = current_time - fps_time

        # FPS 계산
        fps = 1 / calculate_time

        # 이전시간 = 현재시간
        fps_time = current_time

        fps_text = f'FPS: {fps:.2f}'

        img = Utils.text_pil(
            img,
            text=fps_text,
            position = (20, 20),
            font_path = font_path,
            font_size = 60,
            font_color = (0, 255, 0)
        )

        # 비디오 파일 작성
        out.write(img)

        cv2.imshow('YOLO11 Detect Video', img)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    out.release()

else :

    print("잘못된 경로")

cap.release()

cv2.destroyAllWindows()