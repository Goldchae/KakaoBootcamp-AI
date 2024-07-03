import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청
url = 'https://ko.wikipedia.org/wiki/햄스터_(동음이의)'
response = requests.get(url)

# 2. 요청이 성공했는지 확인
if response.status_code == 200:
    # 3. BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.content, 'html.parser')

    # 4. 페이지 제목 추출
    title = soup.find('h1', id='firstHeading').text
    print(f"Title: {title}")

    # 5. 첫 번째 단락 추출
    first_paragraph = soup.find('p').text
    print(f"First paragraph: {first_paragraph}")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

# Title: 햄스터 (동음이의)
# First paragraph: 햄스터의 다른 뜻은 다음과 같다.