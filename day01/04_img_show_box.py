# 이미지에 박스, 텍스트 추가후 저장

import cv2

img_file = "C:/Users/mudod/Pictures/bee.webp"

save_img_file = "C:/Users/mudod/Pictures/bee_box.webp"

img = cv2.imread(img_file)

if img is not None:

    # 사각 박스
    # (이미지, 시작점좌표, 끝점좌표, 색상(BGR), 두께)
    cv2.rectangle(img, (550, 750), (50, 50), (152, 177, 203), 3)

    # 텍스트 추가
    # (이미지, 텍스트, 시작점좌표, 폰트, 크기, 색상(BGR), 두께)
    cv2.putText(img, 'brown box', (350, 750), cv2.FONT_ITALIC, 1, (0, 0, 0), 2)

    cv2.imshow(img_file, img)

    cv2.imwrite(save_img_file, img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

else:

    print("잘못된 경로")