import requests
from bs4 import BeautifulSoup

# AI Hub 페이지 URL
url = 'https://www.aihub.or.kr/'

# 웹 페이지 요청
response = requests.get(url)
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.content, 'html.parser')

# 인기 데이터 TOP3 섹션 찾기
top3_section = soup.find('div', class_='secR')

# 각 데이터 항목 추출
data_list = top3_section.find_all('div', class_='list')

# 데이터 제목 추출
titles = []
for data in data_list:
    title = data.find('h3').get_text(strip=True)
    clean_title = title.split(']')[-1].strip()
    titles.append(clean_title)

# 추출한 데이터 출력
for idx, title in enumerate(titles, start=1):
    print(f"TOP {idx}: {title}")


# TOP 1: 객체 간 관계성 인지용 한국형 비전 데이터
# TOP 2: 손∙팔 협조에 의한 파지-조작 동작 데이터
# TOP 3: 상용 자율주행차 야간 자동차 전용도로 데이터