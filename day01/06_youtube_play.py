# 유튜브 동영상 재생
# yt_dlp = 유튜브 페이지 url을 OpenCV가 직접 읽을 수 있는 실제 동영상 스트리밍 주소로 바꿔주는 원리

import cv2
import yt_dlp

def get_best_video(youtube_url) :

    # 최고 화질
    ydl_opts = {'format' : 'best'}

    try :
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            # download :
            #   True : 실제로 파일 저장
            #   False : 정보만 가져옴
            info = ydl.extract_info(youtube_url, download=False)

            return info ['url']

    except Exception as e :

        print(e)

        return None

# 유튜브 영상
youtube_url = "https://youtu.be/pAGodJ2n8b0"

# 스트리밍 영상
# youtube_url = "https://youtu.be/yNc5W-Bjpcw"

streaming_url = get_best_video(youtube_url)

if streaming_url :

    cap = cv2.VideoCapture(streaming_url)

    if cap.isOpened():

        while True:

            # 다음 프레임 읽기
            ret, img = cap.read()

            # 다음 프레임 없음
            if not ret:

                break

            # 다음 프레임 있음

            # 사이즈 변경
            # dsize = 사이즈 절대값 변경
            # fx = 사이즈 비율 변경
            img = cv2.resize(img , dsize=(0,0), fx=0.5, fy=0.5)
            
            # 사각형 박스
            cv2.rectangle(img, (310, 170), (10, 10), (190, 190, 255), 2)

            # 화면에 표시
            cv2.imshow('Youtube', img)

            # 25ms 지연, q 입력시 반복 종료
            if  cv2.waitKey(25) & 0xFF == ord('q') :
                break
    else:
        print("잘못된 유튜브 경로")

# 자원 해제
cap.release()

cv2.destroyAllWindows()