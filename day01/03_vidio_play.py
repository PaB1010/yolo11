# 동영상 파일 재생

import cv2

video_file = "E:/[공부]/avocado.mp4"

# 동영상 로딩 (웹캠도 가능)
cap = cv2.VideoCapture(video_file)

if cap.isOpened():

    while True:

        # 다음 프레임 읽기
        ret, img = cap.read()

        # 다음 프레임 있음
        if ret:

            # 화면에 표시
            cv2.imshow(video_file, img)

            # 25ms 지연
            cv2.waitKey(25)

        # 다음 프레임 없음
        else:
            break
else:
    print("잘못된 경로")

# 자원 해제
cap.release()

cv2.destroyAllWindows()