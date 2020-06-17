#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Program name : naver_utils
# Explain : 네이버 관련 유용한 함수들 모음
# Version : 1.0
# Developer : GoodFriend
# LastUpdate : 2020. 06. 17

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


###########################################
# 네이버 로그인 함수
def naver_login(nid, npw):
    login_url = 'https://nid.naver.com/nidlogin.login'

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(login_url)

    # id, pw 입력할 곳을 찾습니다.
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    time.sleep(0.5)

    # id 입력
    pyperclip.copy(nid)
    tag_id.click()
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(0.5)

    # pw 입력
    pyperclip.copy(npw)
    tag_pw.click()
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(0.5)

    # 로그인 버튼 클릭
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    time.sleep(3)

    if "네이버 : 로그인" in driver.title:  # 로그인 실패
        print(nid + " 계정에 로그인 실패하였습니다.")
        driver.quit()
        return False
    else:
        print(nid + " 계정에 로그인하였습니다.")
        driver.quit()
        return True
    # end if
