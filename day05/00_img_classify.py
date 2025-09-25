import cv2

from ultralytics import YOLO

from utils import Utils

# YOLO11 모델
model = YOLO('yolo11x-cls.pt')

img_path = 'C:/Users/admin/Pictures/사과.jpg'
# img_path = 'C:/Users/mudod/Pictures/bee.webp'

# model()사용시 이미지 경로만 있어도 자동으로 이미지 로딩하지만
# Utils.texT_box_pil 함수 사용 위해 이미지 로딩
img = cv2.imread(img_path)

font_path = "C:/Windows/Fonts/NanumGothic.ttf"

# model() = 단축버전으로 conf, iou, verbose 기본값 사용
# conf = 신뢰도, 낮을수록 신뢰도 낮은 후보도 표시, 기본값 = 0.25
# iou = IoU 임계값, 낮을수록 중복 박스 허용, 기본값 = 0.7
# verbose = 상세 로그 출력 여부, 기본값 = True
results = model.predict(img, conf=0.25, iou=0.7, verbose=True)

if img is not None and len(results) > 0:

    # result[0] = 탐지결과
    boxes = results[0].boxes

    for box in boxes:
        # 탐지된 객체 정보 추출
        # 1. 좌표 추출
        # 2. 신뢰도 추출
        # 3. 객체 id 추출 및 변환

        # 1. 좌표 추출 S #

        # box.xyxy = 바운딩 박스 좌표
        # [0] = box.xyxy는 2차원 배열이라서 첫번째 요소인 리스트만 가져오기 위함
        # [좌측상단x, 좌측상단y, 우측하단x, 우측하단y]
        # map(int, [xyxy]) = 모든 항목 int 적용
        # 즉 객체 좌표를 모두 가져와 정수로 변환
        x1, y1, x2, y2 = map(int, box.xyxy[0])

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

    cv2.imshow('YOLO11 Detect Utils', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    if img is None:

        print("잘못된 이미지 경로")

    else:

        print("탐지 객체 없음")