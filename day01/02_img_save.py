# 이미지 파일을 흑백으로 가공후 저장

import cv2

img_file = "C:/Users/mudod/Pictures/bee.webp"

save_img_file = "C:/Users/mudod/Pictures/bee_gray.webp"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

cv2.imshow(img_file, img)

# 이미지 저장 (저장할 경로, 대상 이미지)
cv2.imwrite(save_img_file, img)

cv2.waitKey()

cv2.destroyAllWindows()