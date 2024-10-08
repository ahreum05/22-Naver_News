import requests
import sys
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/003/0012577249'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent, 'Referer': None}

r = requests.get(url, headers=headers)

if r.status_code != 200 :
    print('[ERROR] %s' %r.status_code)
    sys.exit(0)
    
#print(r.text)
print('-' * 20)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(r.text, 'html.parser')
# 기사 본문 태그 추출하기
selector = soup.select('#dic_area')

if not selector :   # 선택한 태그가 없으면
    print('크롤링 실패')
    sys.exit(0)

print(selector)
print('-' * 20)





