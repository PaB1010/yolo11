# 이미지 파일을 흑백으로 화면에 표시

import cv2

img_file = "C:/Users/mudod/Pictures/bee.webp"

# # imread(경로, cv2.IMREAD_GRAYSCALE) = 흑백으로 이미지 로딩
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:

  cv2.imshow('IMG', img)

  cv2.waitKey()

  cv2.destroyAllWindows()

else:

    print('잘못된 이미지 경로')