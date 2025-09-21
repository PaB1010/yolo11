import cv2

from ultralytics import YOLO

model = YOLO('yolo11n.pt')

img_path = 'C:/Users/mudod/Pictures/cars.jpg'
# img_path = 'C:/Users/mudod/Pictures/bee.webp'

# Detect - 객체 탐지
# 경로를 넣으면 이미지 로딩도 자동으로 됨
# cv2.imread(img_path)할 필요 없어짐
results = model(img_path)

# Box + Text 그려진 이미지 반환
frame = results[0].plot()

# 결과 이미지를 화면에 표시
cv2.imshow("YOLO11 Detect Plot", frame)

cv2.waitKey(0)

cv2.destroyAllWindows()