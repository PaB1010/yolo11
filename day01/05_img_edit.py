# 다양한 이미지 가공

import cv2

img_file = "C:/Users/mudod/Pictures/bee.webp"

img = cv2.imread(img_file)

if img is not None:

    # 흑백
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('흑백 이미지', gray_img)

    # 크기 조절
    # (이미지, (너비, 높이))
    resized_img = cv2.resize(img, (300, 200))

    cv2.imshow('작은 이미지', resized_img)

    # 블러 적용
    # (이미지, (너비, 높이), 표준편차)
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

    cv2.imshow('흐린 이미지', blurred_img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    print("잘못된 경로")