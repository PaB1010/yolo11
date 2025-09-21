# 이미지 파일을 화면에 표시

import cv2

img_file = "C:/Users/mudod/Pictures/bee.webp"

# imread(경로) = 이미지 로딩
img = cv2.imread(img_file)

if img is not None:

    # 이미지 표시
    cv2.imshow('IMG', img)

    # 키보드 입력 대기
    cv2.waitKey()

    # 모든 창 닫음
    cv2.destroyAllWindows()

else:
    
    print('잘못된 이미지 경로')