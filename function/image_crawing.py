#!/usr/bin/env python
# coding: utf-8

# In[30]:


#터미널 또는 concole을 통해 pip install selenium, pip install webdriver_manager 명령어로 설치


# In[117]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import time


# In[83]:


#미리 chromedriver를 설치후 로컬 폴더에 위치시킵니다. 버전 확인
#https://googlechromelabs.github.io/chrome-for-testing/#stable
link='C:\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(link)


# In[84]:


url3='https://pass.knto.or.kr/front/login/login?linkSiteApiId=B7c590PNxoifKD-4Pmhsww'
driver.get(url3)
#해당 라인까지 실행하면 로그인 화면이 뜹니다 수동으로 해주세요(자동은 되게 귀찮아요)


# In[ ]:


#또한 본격적으로 클롤링 하기 앞서 사이트에서 excel 또는 이미지 다운로드 버트을 한 번 클릭하여 다운로드 목적을 기재합시다.
#해당 사항을 전부 했다면 밑에 라인을 실행해주세요


# In[100]:


#excel 파일 다운, 다운 전에 배열을 200개씩 보기로 바꿔주세요

#262
#1047

time.sleep(20)


wait = WebDriverWait(driver, 40)
clicked_button = None
#시작 페이지
start_page=1
while True:

    
    
    try:
        print('try_download_click')
        time.sleep(4)
        image_button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-type4.btn-iconback.image')))
        if clicked_button != image_button_element:
            print('download_click')
            image_button_element.click()
            clicked_button = image_button_element
    except ElementNotInteractableException:
        print("Too fast, waiting for 10 seconds before trying again... in image")
        time.sleep(10)
        continue
        
    except ElementClickInterceptedException:
        print("Too fast, waiting for 10 seconds before trying again... in image")
        time.sleep(10)
        continue
        
    except TimeoutException:
        print("Timed out waiting for image button")
        continue
    

    
    time.sleep(8)
    try:
        # 클릭한 버튼이 이전에 클릭한 버튼과 같지 않은 경우에만 클릭
        next_button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.table-forward[name="next"]')))
        print('try_next_click')
        if clicked_button != next_button_element:
            print('next_click')
            next_button_element.click()
            # 클릭한 버튼 업데이트            
            clicked_button = next_button_element
            time.sleep(8)
    except ElementNotInteractableException:
        print("Too fast, waiting for 10 seconds before trying again... in next")
        time.sleep(10)
        continue
        
    except ElementClickInterceptedException:
        print("Too fast, waiting for 10 seconds before trying again... in next")
        time.sleep(10)
        continue
        
    except TimeoutException:
        print("Timed out waiting for next button")
        continue
    
    print(f'{start_page}done')
    if start_page== 262:
        
        break
    start_page+=1
    





