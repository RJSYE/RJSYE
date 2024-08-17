import base64
import sqlite3
from bs4 import BeautifulSoup
import requests
import os

# SQLite 데이터베이스 파일에 연결
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# 테이블 생성 (존재하지 않으면 생성)
c.execute('''
CREATE TABLE IF NOT EXISTS youtube_comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT,
    response TEXT
)
''')
auth_token = "918658b0-cc4b-4304-a8ca-8ac850c16ed7" 
# YouTube API 키와 비디오 ID


def get_comment(video_id,key,lange):
# YouTube API로부터 댓글 데이터 가져오기
    url = f'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={key}'
    start = lange[0]
    end = lange[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching YouTube comments: {e}")
        conn.close()
        return


    # 댓글 데이터 처리 및 API 요청
    for i in range(start, min(end, len(data.get('items', [])))):
        comment = data['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']
        print(f"Comment: {comment}")
        data2 = {"document": comment}
        
        headers = {
            "Content-Type": "application/json",
            "x-auth-token": "918658b0-cc4b-4304-a8ca-8ac850c16ed7"
        }

        try:
            response2 = requests.post("https://api.matgim.ai/54edkvw2hn/api-keyword-slang",headers=headers, json=data2)
            response2.raise_for_status()
            response2_json = response2.json()
            print(response2_json)
        except requests.RequestException as e:
            print(f"댓글 포스팅중 오류 발생: {e}")
            continue

        # "category":"vulgarism" 형식이 발견될 때만 처리
        if ('result' in response2_json and 
            'data' in response2_json['result']):
            
            results = response2_json['result']['data']
            print(f"Results: {results}")
            
            if isinstance(results, list):
                vulgarism_detected = False  # 비속어 감지를 위한 플래그
                for result in results:
                    category = result.get('category')
                    print(f"Category: {category}")
                    if category == 'vulgarism':
                        text = result.get('text', 'No text provided')  # 비속어 텍스트 가져오기
                        print(f"발견된 비속어: {text}")
                        
                        # 댓글과 API 응답 데이터를 데이터베이스에 저장
                        c.execute('INSERT INTO youtube_comments (comment, response) VALUES (?, ?)', (comment, text))
                        vulgarism_detected = True
                        break  # 비속어를 찾으면 루프를 종료
                
                if not vulgarism_detected:
                    print("댓글에서 비속어가 발견되지 않았습니다.")
            else:
                print("결과가 리스트가 아니거나 비었습니다.")
        else:
            print("API 응답에서 유효한 구조가 발견되지 않았습니다.")
def youtube_search(query,amount):
    api_key = "AIzaSyAVnteL9JlOKZwa0cUk52PgpuqVYi7rZZQ"
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": amount,
        "key": api_key
    }
    
    response = requests.get(url, params=params)
    print(response.text)
    if response.status_code == 200:
        results = response.json()
        for item in results['items']:
            print(f"Title: {item['snippet']['title']}")
            print(f"Channel: {item['snippet']['channelTitle']}")
            print(f"Description: {item['snippet']['description']}")
            print(f"URL: https://www.youtube.com/watch?v={item['id']['videoId']}")
            get_comment(item['id']['videoId'],"AIzaSyAVnteL9JlOKZwa0cUk52PgpuqVYi7rZZQ",(3,5))
    else:
        print("Error:", response.status_code, response.text)

# 예시 검색어로 검색
youtube_search("욕 배틀",5)
# 변경사항 저장
conn.commit()

# 연결 종료
conn.close()
