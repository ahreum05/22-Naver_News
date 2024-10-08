import requests
import sys
from bs4 import BeautifulSoup

url = 'https://v.daum.net/v/20240530160143261'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
headers = {'User-agent':user_agent,'Referer':None}

r = requests.get(url, headers=headers)

if r.status_code != 200:
    print('[ERROR] %s' %r.status_code)
    sys.exit()

#print(r.text)
#print('-'*30)

# 기사 본문 태그 추출하기
soup = BeautifulSoup(r.text,'html.parser')

selector = soup.select('section[dmcf-sid="7FpYKisdqI"]')

# 선택된 태그가 없으면
if not selector:
    print('크롤링 실패')
    sys.exit(0)
    
# print(selector)
#print('-'*30)

# 불필요한 부분 제거/치환
item = selector[0]

# 태그 제거
for target in item.find_all('figure'):
    target.extract()

#print(item)
#print('-'*30)

# 최종 텍스트 추출
result = item.text
#print(result)
#print('-'*30)

# 양쪽 공백문자 제거
result = result.strip()
print(result)
print('-'*30)

# 파일 저장
with open('다음뉴스.txt', 'w', 
          encoding='utf-8') as f:
    f.write(result)
    print('저장완료')

