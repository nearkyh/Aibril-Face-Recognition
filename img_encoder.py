import base64
import os

# capture = cv2.VideoCapture(0)
#
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
# while True:
#     ret, frame = capture.read()
#
#     cv2.imshow("VideoFrame", frame)
#
#     if cv2.waitKey(1) > 0: break
#
# capture.release()
# cv2.destroyAllWindows()

img_path = os.path.join('face_images', 'yonghan-kim')
img_list = os.listdir(img_path)
img_data = []
for img in img_list:
    img = os.path.join(img_path, img)
    with open(img, 'rb') as f:
        img_b64 = base64.b64encode(f.read())
        img_data.append(img_b64)

_data = {                                               # 필수 여부 / 설명
    "Content-Type": "application/json; charset=utf-8",  # Y / 속성
    "api-key": "input api key",                         # Y / 서비스 인증(aibril에서 key 발급)
    "fname": "kim",                                     # Y / 이름의 첫번째 글자(영문)
    "mname": "yong",                                    # N / 이름의 두번째 글자(영문)
    "lname": "han",                                     # N / 이름의 세번째 글자(영문)
    "gender": "M",                                      # N / 성별 코드 (M:남성, W:여성, U:알수없음)
    "concernType": "WHITE",                             # Y / 사람 유형 (GENERAL:일반, BLACK:블랙리스트, WHITE:화이트리스트)
    "remarks": "",                                      # N / 별도로 등록할 정보 입력
    "nationality": "KR",                                # N / 국적 코드(한국:KR, 미국:US, 일본:JP 등..)
    "birthday": "19920924",                             # N / 생년월일 8자리 (YYYYMMDD 형식)
    "type": "ADD",                                      # Y / 사람 등록 여부
    "imgList": []
}

for i in range(len(img_data)):
    img = str(img_data[i]).split("'")[1]
    update_img = {
        "img": img,
        "imgFormat": "jpg",
        "imgW": "200",
        "imgH": "200"
    }
    _data['imgList'].append(update_img)

print(_data['imgList'])
