import numpy as np
from scipy.spatial import KDTree
import requests
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
'''
    구글 geolocation API로 좌표 리턴
'''
def get_pos(address):
    params = {
        'address': address,
        'sensor': 'false',
        'key': '' # 구글 geolocation API key 입력
    }
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    result = res['results'][0]
    return result['geometry']['location']['lat'], result['geometry']['location']['lng']

'''
    내 위치 (기업은행 본점)
'''
from_address_name = ['기업은행 본점']
from_address = ['서울특별시 중구 명동 을지로 79']
lat, lng = get_pos(from_address[0]) # 내 위치 위도, 경도 가져옴
from_lat = [lat] # 내 위치 위도
from_lng = [lng] # 내 위치 경도

'''
    주변 위치 정보 
'''
neighbor_address_name = ['을지면옥', 'IBK시스템', '왕비집(명동2호점)', '충무로족발', '탑골공원']
neighbor_address = ['서울특별시 중구 을지로동 161'
                  , '서울특별시 중구 충무로2가 62-7'
                  , '서울특별시 중구 명동1가 명동9길 13'
                  , '서울특별시 중구 필동 퇴계로27길 41'
                  , '서울특별시 종로구 종로2가 종로 99']
neighbor_lat = []
neighbor_lng = []
for neighbor in neighbor_address:
    lat, lng = get_pos(neighbor) # 주변 위치 위도, 경도 가져옴
    neighbor_lat.append(lat) # 주변위치 위도
    neighbor_lng.append(lng) # 주변위치 경도

# KDTree알고리즘으로 거리정보 및 가까운 순으로 index를 가져옴 (k는 가져올 갯수)
latlng_s = np.vstack([neighbor_lat, neighbor_lng]).T
dist_idx = [KDTree(latlng_s).query(coords, k=5) for coords in zip(from_lat, from_lng)]

# 가까운 거리를 가져옴
for from_idx, (distance, index) in enumerate(dist_idx):
    for i in range(len(distance)):
        d = distance[i]
        nm = neighbor_address_name[index[i]]
        print('`' + from_address_name[from_idx] + '`으로부터 ' + str(i + 1) + '번째로 가까운 곳: ' + nm + ', 거리값: ' + str(d))
