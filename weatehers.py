from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import time
 
options = Options()
options.add_argument('--headless')  # 창 없이 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
 
# webdriver-manager로 ChromeDriver 자동 설치 및 경로 지정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
 
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
driver.get(url)
time.sleep(3)  # JS 로딩 시간 기다림
 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
 
rank = 1
results = soup.findAll('span', 'item_title')
 
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
 
with open("rankresult.txt", "a", encoding='utf-8') as search_rank_file:
    for result in results:
        text = result.get_text()
        search_rank_file.write(f"{rank}위: {text}\n")
        print(f"{rank}위 : {text}")
        rank += 1
 
driver.quit()
 
 
 
 
#설치 명령어
#pip install selenium webdriver-manager beautifulsoup4