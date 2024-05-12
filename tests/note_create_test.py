from configuration.webDriver import get_element
from utils.xpath_archive import *
import time


# notes 화면 에서 우측 하단 + 버튼 클릭
def test_notes_plus_click():
    create_btn = get_element(xpath_notes_creat_btn)
    create_btn.click()
    print("test")
    time.sleep(2)

# notes 화면 + 버튼 클릭 > textnote 버튼 클릭
def test_notes_plus_textnote_click():
    textnote_btn = get_element(xpath_notes_textnote_btn)
    textnote_btn.click()
    time.sleep(2)

# edit 화면의 title 영역 클릭
def test_edit_title_click():
    edit_title = get_element(xpath_edit_title)
    edit_title.click()
    time.sleep(2)

# edit 화면의 title 에 text 입력
def test_edit_title_input(input):
    edit_title = get_element(xpath_edit_title)
    title_input = input
    edit_title.send_keys(title_input)
    time.sleep(2)

# edit 화면의 content 영역 클릭
def test_edit_content_click():
    edit_title = get_element(xpath_edit_content)
    edit_title.click()
    time.sleep(2)

# edit 화면의 content 에 text 입력
def test_edit_content_input(input):
    edit_title = get_element(xpath_edit_content)
    title_input = input
    edit_title.send_keys(title_input)
    time.sleep(2)

def test_edit_back_click():
    edit_back_btn = get_element(xpath_edit_back_btn)
    edit_back_btn.click()
    time.sleep(2)
