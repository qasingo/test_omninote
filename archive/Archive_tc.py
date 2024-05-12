from configuration.webDriver import get_element
from utils.xpath_archive import *     # xpath 변수 import
from utils.interaction_utils import Slide
import time
# # Archive 보관 기능 # #
# 사전조건. 노트 생성(생성할 노트 수량)
def run_test_preconditions(num_notes):
    for count in range(num_notes):
        time.sleep(1)
        # notes 의 + 버튼 클릭
        create_btn = get_element(xpath_notes_creat_btn)
        create_btn.click()
        time.sleep(2)

        # notes 의 + 버튼에서 나타난 textnote 버튼 클릭
        textnote_btn = get_element(xpath_notes_textnote_btn)
        textnote_btn.click()
        time.sleep(2)

        # edit 의 title 클릭
        edit_title = get_element(xpath_edit_title)
        edit_title.click()
        time.sleep(2)

        # title 입력
        title_input = f"Test Note Title {count}"
        edit_title.send_keys(title_input)

        # edit 의 content 클릭
        edit_content = get_element(xpath_edit_content)
        edit_content.click()
        time.sleep(2)

        # content 입력
        content_input = f"Test Note Content {count}"
        edit_content.send_keys(content_input)

        # back 버튼 클릭
        edit_back_btn = get_element(xpath_edit_back_btn)
        edit_back_btn.click()
        time.sleep(2)
        print(f"Note {count} created")
    time.sleep(2)


# test1) Notes 의 생성된 노트를 좌로 슬라이드
def test_archive_note_by_sliding_left():
    run_test_preconditions(1)
    Slide.temp_bounds_swipe_left()
    time.sleep(2)

# test2) 우로 슬라이드
def test_archive_note_by_sliding_right():
    run_test_preconditions(1)
    Slide.temp_bounds_swipe_right()
    time.sleep(2)

# test3) 노트 선택하여 :선택>Archive 선택
def test_archive_note_click_arcBtn():
    run_test_preconditions(1)
    notes_1_content = get_element(xpath_notes_1_content)
    notes_1_content.click()
# test4) 가장 하단에 있는 스크롤하여 나타나는 Note 슬라이드 삭제
# result - Notes 에서 사라짐
# result - Archive 로 이동 확인됨
#########################################################

# # Archive 복구 기능 # #
# 사전조건. 보관 기능 테스트 실행
# test1) Archive의 보관된 노트 선택하여 :선택>Restor from archive 선택
# result - Archive 에서 사라짐
# result - Notes 로 이동 확인됨
#########################################################