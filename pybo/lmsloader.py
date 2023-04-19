# 필요한 라이브러리 로드
# 크롬 드라이버 다운로드 >https://sites.google.com/chromium.org/driver/
# 셀레니움 설치 > anaconda prompt 에서 pip3 install selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import re  # html 처리 관련 - 검색, 분할 등
# from bs4 import BeautifulSoup
import m3u8_To_MP4  # m3u8 변환
import os  # 동영상 저장, 이름짓기
import os.path


def Lmsloader(id, password):
    basedir = 'C:/joljak'
    os.chdir(basedir)

    # 크롬드라이버 실행 파트
    dr = webdriver.Chrome("C:/windows/chromedriver.exe")
    dr.set_window_size(414, 800)  # 브라우저 크기 414*800으로 고정
    dr.get('https://lms.kau.ac.kr/login.php')  # LMS 접속
    time.sleep(0.5)  # 반초 대기

    # LMS창에서 로그인 진행
    id_box = dr.find_element(By.CSS_SELECTOR, "#input-username")  # 아이디 입력창
    password_box = dr.find_element(By.CSS_SELECTOR, "#input-password")  # 비밀번호 입력창
    login_button = dr.find_element(By.CSS_SELECTOR,
                                   '#region-main > div > div > div > div.col-loginbox > div:nth-child(1) > div.col-login.col-login-person > form > div.submitform > input')  # 로그인 버튼

    # 동작 제어
    ID = id
    PW = password

    act = ActionChains(dr)  # 동작 명령어 지정
    act.send_keys_to_element(id_box, ID).send_keys_to_element(password_box, PW).click(login_button).perform()
    time.sleep(1)

    titles = dr.find_elements(By.CLASS_NAME, 'course-title')
    titlelist = []

    for title in titles:
        tt = title.text
        ttsp = re.split('\n', tt)
        titlelist.append(ttsp[0])

    # course_link 라는 클래스 네임으로 참조되는 것 > 각 강의 타이틀 누르면 연결되는 URL. course_link의 href="https://~~~~" 이다.
    divs = dr.find_elements(By.CLASS_NAME, 'course_link')
    time.sleep(0.5)

    for i in range(len(titlelist)):
        viewlist = []
        linklist = []
        namelist = []

        try:
            os.mkdir(titlelist[i])
        except:
            pass

        newdir = basedir + '/' + titlelist[i]
        os.chdir(newdir)
        url = divs[i].get_attribute('href')
        exctlink = 'window.open("' + url + '");'
        dr.execute_script(exctlink)  # 주소대로 새 탭으로 열기
        new_tab_handle = dr.window_handles[-1]  # 새 창에서 강의 url로 이동
        dr.switch_to.window(new_tab_handle)
        time.sleep(0.5)

        insts = dr.find_elements(By.CLASS_NAME, "activityinstance")
        for inst in insts:
            icon = inst.find_element(By.CLASS_NAME, "activityicon")
            alt = icon.get_attribute("alt")
            if alt == '동영상':
                name = inst.find_element(By.CLASS_NAME, "instancename")
                tt = name.text
                ttlist = re.split("\n", tt)
                namelist.append(ttlist[0])

        html = dr.page_source
        view = re.findall(
            'https://lms.kau.ac.kr/mod/vod/view.php(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            html)
        viewlist.extend(view)
        viewerlist = []

        # viewlist 안의 url들에대해 각각 view > viewer로 수정한다. 이러면 동영상으로 직접 엑세스한다. (얼럿창 제어 위함)
        for v in viewlist:
            tmp = re.split('view', v)
            viewerlist.append(tmp[0] + 'viewer' + tmp[1])

        for v in viewerlist:
            tmp = 'window.open("' + v + '");'
            dr.execute_script(tmp)
            new_tab_handle = dr.window_handles[-1]  # 새 창에서 강의 url로 이동
            dr.switch_to.window(new_tab_handle)
            time.sleep(0.4)
            try:
                Alert(dr).accept()
            except:
                pass
            time.sleep(0.1)
            txt = dr.find_element(By.XPATH, "/html/head/script[3]").get_attribute('innerText')
            m3u8URL = re.findall(
                'https://fcbjngaswqol4996171(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                txt)
            linklist.extend(m3u8URL)
            dr.close()  # 강의동영상 창 닫기
            dr.switch_to.window(dr.window_handles[-1])  # 다시 이전 창(강의창, 동영상 목록)으로 이동

        for ii in range(len(linklist)):
            if __name__ == '__main__':
                print('m3u8download try...')
                m3u8_To_MP4.multithread_download(linklist[ii])
                try:
                    os.rename('m3u8_To_MP4.mp4', namelist[ii] + '.mp4')
                except:
                    os.remove('m3u8_To_MP4.mp4')
        dr.close()
        dr.switch_to.window(dr.window_handles[-1])  # 다시 이전 창(강의창, 동영상 목록)으로 이동
        time.sleep(0.1)
        os.chdir(basedir)

    dr.close()

Lmsloader('2015124164','2741427aoa!')
