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
# 1) 기사 본문 태그 추출하기
selector = soup.select('#dic_area')

if not selector :   # 선택한 태그가 없으면
    print('크롤링 실패')
    sys.exit(0)

#print(selector)
print('-' * 20)

# 2) 불필요한 부분 제거/치환
item = selector[0]

# <strong> 태그 제거
for target in item.find_all('strong') :
    target.extract()

#print(item)
print('-' * 20)

# <span> 태그 제거
for target in item.select('span.end_photo_org') :
    target.extract()

print(item)
print('-' * 20)

# <br> 태그를 줄넘김 문자로 변경
for target in item.find_all('br') :
    target.replace_with('\n')
    
print(item)
print('-' * 20)    

# 3) 최종 텍스트 추출
result = item.text
print(result)
print('-' * 20)

# 앞뒤 공백 제거
result = result.strip()
print(result)
print('-' * 20)

# 4) 파일로 저장
with open('네이버뉴스.txt', 'w', 
          encoding='utf-8') as f:
    f.write(result)
    print('저장 성공')
 







