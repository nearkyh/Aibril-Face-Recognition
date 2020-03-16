import os
import requests
import base64
import json
from PIL import Image


class SK_FRS:

    def __init__(self, api_key):
        self.api_key = api_key

    # ============================== #
    #          관심 인물 등록
    # ============================== #
    def registConcernPerson(self, fname, mname=None, lname=None, gender=None, concernType="GENERAL",
                            remarks=None, nationality=None, birthday=None, _type="ADD",
                            img=None, imgFormat="jpg", imgW="150", imgH="150", imgRemark=None):
        _url = "https://visionai.skcc.com/frs/investigation/concern-person"
        _headers = {                                            # 필수 여부 / 설명
            "Content-Type": "application/json; charset=utf-8",  # Y / 속성
            "api-key": self.api_key,                            # Y / 서비스 인증(aibril에서 key 발급)
        }
        _body = {                                               # 필수 여부 / 설명
            "fname": fname,                                     # Y / 이름의 첫번째 글자(영문)
            "mname": mname,                                     # N / 이름의 두번째 글자(영문)
            "lname": lname,                                     # N / 이름의 세번째 글자(영문)
            "gender": gender,                                   # N / 성별 코드 (M:남성, W:여성, U:알수없음)
            "concernType": concernType,                         # Y / 사람 유형 (GENERAL:일반, BLACK:블랙리스트, WHITE:화이트리스트)
            "remarks": remarks,                                 # N / 별도로 등록할 정보 입력
            "nationality": nationality,                         # N / 국적 코드(한국:KR, 미국:US, 일본:JP 등..)
            "birthday": birthday,                               # N / 생년월일 8자리 (YYYYMMDD 형식)
            "type": _type,                                      # Y / 사람 등록 여부
            "imgList": [                                        # Y / 얼굴 이미지 데이터(리스트로 저장)
                {
                    "img": img,                                 # base64로 인코딩된 이미지 데이터
                    "imgFormat": imgFormat,                     # 이미지 확장자 (*jpg 형식만 가능)
                    "imgW": imgW,                               # 이미지 가로 크기 (150px 이상)
                    "imgH": imgH,                               # 이미지 세로 크기 (150px 이상)
                    "imgRemark": ""                             # 이미지에 대한 설명
                }
            ]
        }
        return requests.post(url=_url, headers=_headers, data=json.dumps(_body))

    # ============================== #
    #          관심 인물 삭제
    # ============================== #
    def deleteConcernPerson(self, personId):
        _url = "https://visionai.skcc.com/frs/investigation/concern-person/delete/{}".format(personId)
        _headers = {
            "Content-Type": "application/json; charset=utf-8",
            "api-key": self.api_key,
        }
        return requests.post(url=_url, headers=_headers)

    # ============================== #
    #        관심 인물 사진 삭제
    # ============================== #
    def deleteConcernFace(self, faceId):
        _url = "https://visionai.skcc.com/frs/investigation/concern-face/delete/{}".format(faceId)
        _headers = {
            "Content-Type": "application/json; charset=utf-8",
            "api-key": self.api_key,
        }
        return requests.post(url=_url, headers=_headers)

    # ============================== #
    #          관심 인물 조회
    # ============================== #
    def getConcernPerson(self, personId):
        _url = "https://visionai.skcc.com/frs/investigation/concern-person?personId={}".format(personId)
        _headers = {
            "Content-Type": "application/json; charset=utf-8",
            "api-key": self.api_key,
        }
        return requests.get(url=_url, headers=_headers)

    # ============================== #
    #        관심 인물 정보 변경
    # ============================== #
    def modifyConcernPerson(self, personId, fname, mname=None, lname=None, gender=None, concernType=None,
                            remarks=None, nationality=None, birthday=None, _type="MODIFY",
                            img=None, imgFormat="jpg", imgW="150", imgH="150", imgRemark=None):
        _url = "https://visionai.skcc.com/frs/investigation/concern-person/{}".format(personId)
        _headers = {
            "Content-Type": "application/json; charset=utf-8",
            "api-key": self.api_key,
        }
        _body = {
            "fname": fname,
            "mname": mname,
            "lname": lname,
            "gender": gender,
            "concernType": concernType,
            "remarks": remarks,
            "nationality": nationality,
            "birthday": birthday,
            "type": _type,
            "imgList": [
                {
                    "img": img,
                    "imgFormat": imgFormat,
                    "imgW": imgW,
                    "imgH": imgH,
                    "imgRemark": imgRemark
                }
            ]
        }
        return requests.post(url=_url, headers=_headers, data=json.dumps(_body))

    # ============================== #
    #      관심 인물 사진 추가 등록
    # ============================== #
    def registConcernFace(self, personId, img=None, imgFormat="jpg", imgW="150", imgH="150", imgRemark=None):
        _url = "https://visionai.skcc.com/frs/investigation/concern-face"
        _headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }
        _body = {
            "personId": personId,
            "imgList": [
                {
                    "img": img,
                    "imgFormat": imgFormat,
                    "imgW": imgW,
                    "imgH": imgH,
                    "imgRemark": imgRemark
                }
            ]
        }
        return requests.post(url=_url, headers=_headers, data=json.dumps(_body))

    # ============================== #
    #        전체 관심 인물 조회
    # ============================== #
    def getAllConcernPersonInfo(self):
        _url = "https://visionai.skcc.com/frs/investigation/all-concern-person"
        _headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }
        return requests.get(url=_url, headers=_headers)

    # ============================== #
    #       이미지 간편 분석 요청
    # ============================== #
    def startLiveImage(self, imageFile):
        _url = "https://visionai.skcc.com/frs/ondemand/image/start-image"
        _headers = {
            # "Content-Type": "multipart/form-data; boundary=ebf9f03029db4c2799ae16b5428b06bd",
            "api-key": self.api_key,
        }
        print(imageFile)
        imageFile = open(imageFile, 'rb')
        _files = {"imageFile": imageFile}
        return requests.post(url=_url, headers=_headers, files=_files)

    # ============================== #
    #       얼굴 이미지 유사도 측정
    # ============================== #
    def compareImage(self, sourceFile, targetFile):
        _url = "https://visionai.skcc.com/frs/ondemand/image/compare-image"
        _headers = {
            # "Content-Type": "multipart/form-data",
            "api-key": self.api_key,
        }
        print(sourceFile)
        print(targetFile)
        sourceFile = open(sourceFile, 'rb')
        targetFile = open(targetFile, 'rb')
        _files = {
            "sourceFile": "{}".format(sourceFile),
            "targetFile": "{}".format(targetFile)
        }
        return requests.post(url=_url, headers=_headers, files=_files)

'''
curl -H 'Content-type: multipart/form-data' \
-H 'api-key: input api key' \
-F 'imageFile=/home/soosang/sk-aibril-face-recognition/face_images/yonghan-kim/yonghan_2.jpg' \
-X POST https://visionai.skcc.com/frs/ondemand/image/start-image

'''

# 로컬에 저장된 이미지
# img_path = os.path.join('face_images', 'yonghan-kim')
# img_list = os.listdir(img_path)
# img_data = []
# img_size = []
# for img in img_list:
#     img = os.path.join(img_path, img)
#     with open(img, 'rb') as f:
#         img_b64 = base64.b64encode(f.read())
#         img_data.append(img_b64)
#
#     im = Image.open(img)
#     img_size.append(im.size)
#
# image = str(img_data[0]).split("'")[1]
# img_width = img_size[0][0]
# img_height = img_size[0][1]


if __name__ == '__main__':

    abs_path = os.path.dirname(os.path.abspath(__file__))

    sk_frs = SK_FRS(api_key='input api key')

    # ============================== #
    #          관심 인물 등록
    # ============================== #
    img_path = os.path.join('face_images', 'yonghan-kim')
    img_list = os.listdir(img_path)
    index = 0
    img_file = os.path.join(img_path, img_list[index])
    with open(img_file, 'rb') as f:
        img_b64 = base64.b64encode(f.read())
    img = str(img_b64).split("'")[1]
    im = Image.open(img_file)
    img_width = im.size[0]
    img_height = im.size[1]
    response = sk_frs.registConcernPerson(fname='Kim', img=img, imgH=str(img_height), imgW=str(img_width))
    print("[관심 인물 등록]")
    print(response.text)

    # ============================== #
    #          관심 인물 삭제
    # ============================== #
    # response = sk_frs.deleteConcernPerson(personId=2927)
    # print(response.text)

    # ============================== #
    #        관심 인물 사진 삭제
    # ============================== #
    # response = sk_frs.deleteConcernFace(faceId=1922)
    # print(response.text)

    # ============================== #
    #          관심 인물 조회
    # ============================== #
    # response = sk_frs.getConcernPerson(personId=2928)
    # print(response.text)

    # ============================== #
    #        관심 인물 정보 변경
    # ============================== #

    # ============================== #
    #      관심 인물 사진 추가 등록
    # ============================== #
    # response = sk_frs.registConcernFace(personId=2907, img=img, imgH=str(img_height), imgW=str(img_width))
    # print(response.text)

    # ============================== #
    #        전체 관심 인물 조회
    # ============================== #
    print("[전체 관심 인물 조회]")
    response = sk_frs.getAllConcernPersonInfo()
    print(response.text)

    # ============================== #
    #       이미지 간편 분석 요청
    # ============================== #
    print("[이미지 간편 분석 요청]")
    response = sk_frs.startLiveImage(imageFile=os.path.join(abs_path + '/' + img_path, img_list[0]))
    print(response.text)

    # ============================== #
    #       얼굴 이미지 유사도 측정
    # ============================== #
    print("[얼굴 이미지 유사도 측정]")
    response = sk_frs.compareImage(sourceFile=os.path.join(abs_path + '/' + img_path, img_list[0]),
                                   targetFile=os.path.join(abs_path + '/' + img_path, img_list[2]))
    print(response.text)

    try:
        pass
    except Exception as e:
        pass
