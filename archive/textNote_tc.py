import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


# * 현재 생성은 모든 케이스를 확인할 수 없으므로 보관/삭제 기능 확인을 위한 세팅정도로 진행함
def creatNote_testSet(wd):
    print("creatNote_testSet xpath 생성 중")
    # text note 생성하기 위해 필요한 xpath
    xpath_notes_creat_btn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.ImageButton"
    xpath_notes_textnote_btn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.ImageButton[3]"
    xpath_edit_title = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText"
    xpath_edit_content = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText"
    xpath_edit_back_btn = "//android.widget.ImageButton[@content-desc=\"drawer open\"]"
    xpath_notes_1_title = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
    xpath_notes_1_content = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]"
    xpath_notes_1_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"

    # TEST 시작
    print("creatNote testSeting 시작")
    # notes 의 + 버튼 클릭
    create_btn = wd.find_element(By.XPATH, xpath_notes_creat_btn)
    create_btn.click()
    time.sleep(2)

    # notes 의 + 버튼에서 나타난 textnote 버튼 클릭
    textnote_btn = wd.find_element(By.XPATH, xpath_notes_textnote_btn)
    textnote_btn.click()
    time.sleep(2)

    # edit 의 title 클릭
    edit_title = wd.find_element(By.XPATH, xpath_edit_title)
    edit_title.click()
    time.sleep(2)

    # title 입력
    title_input = "Test Note Title"
    edit_title.send_keys(title_input)

    # edit 의 content 클릭
    edit_content = wd.find_element(By.XPATH, xpath_edit_content)
    edit_content.click()
    time.sleep(2)

    # content 입력
    content_input = "Test Note Content"
    edit_content.send_keys(content_input)

    # back 버튼 클릭
    edit_back_btn = wd.find_element(By.XPATH, xpath_edit_back_btn)
    edit_back_btn.click()
    time.sleep(2)

    # textnote 생성되었으면 test 시작
    print("testnote set 완료")


    #test 더미 생성 후 실행
    archive_test(wd)


# Archive TC
# Notes 화면 inspector
def archive_test(wd):
    print("achive_test 시작")
    xpath_notes_1_title = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
    xpath_notes_1_content = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]"
    xpath_notes_1_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"

    print("test result 생성")
    notes_1_title = wd.find_element(By.XPATH, xpath_notes_1_title)
    testresult_title = notes_1_title.text
    notes_1_content = wd.find_element(By.XPATH, xpath_notes_1_content)
    testresult_content = notes_1_content.text

    print(f"testresult_title : {notes_1_title.text}")
    print(f"testresult_content : {notes_1_content.text}")

    # 하단 메시지 확인
    # xpath(id) 저장 규칙 "xpath(id)_화면명_기능"
    id_undobar_undo_msg = "it.feio.android.omninotes.alpha:id/undobar_message"
    id_undobar_undo_btn = "it.feio.android.omninotes.alpha:id/undobar_button"

    # 사전조건1 : Text note 생성된 상태

    # *bounds 값으로 슬라이드 좌표 찍기

    # 오른쪽에서 왼쪽으로 슬라이드
    # 시작 지점 및 끝 지점 좌표
    y = 400  # 시작,종료 y 좌표 (화면의 중앙)

    start_x = 900  # 시작 x 좌표 (오른쪽에서 시작)
    end_x = 200  # 끝 x 좌표 (왼쪽으로 이동)
    duration = 800  # 밀리초 단위

    # TouchAction을 사용하여 슬라이드 동작 시뮬레이션
    action = TouchAction(wd)
    action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()
    time.sleep(2)

    # 슬라이드 후 하단 바 Undo 버튼 선택으로 보관 취소
    # 슬라이드 후 하단 바 N초 경과 후 보관 취소 사라짐

    #xpath
    xpath_hamberger = "//android.widget.ImageButton[@content-desc=\"drawer open\"]"
    xpath_h_archive = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.TextView"
    xpath_archive_top = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView"
    xpath_archive_1_title = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
    xpath_archive_1_content = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]"

    # 햄버거 버튼 선택
    print("햄버거 버튼 선택")
    hamberger = wd.find_element(By.XPATH, xpath_hamberger)
    hamberger.click()
    time.sleep(2)

    # Archive 버튼 선택
    print("Archive 버튼 선택")
    h_archive = wd.find_element(By.XPATH, xpath_h_archive)
    h_archive.click()
    time.sleep(2)

    # Archive 에 보관된 Note 확인
    print("결과 확인")
    archive_1_title = wd.find_element(By.XPATH, xpath_notes_1_title)
    result_title = archive_1_title.text
    archive_1_content = wd.find_element(By.XPATH, xpath_notes_1_content)
    result_content = archive_1_content.text

    print(result_title)
    print(result_content)

def trash_test(wd):
    xpath = "1"
    # Trash TC
    # 사전조건1 : Text note 생성된 상태
    # 사전조건2 : 보관함에서 삭제
    # 왼쪽에서 오른쪽으로 슬라이드
    # 슬라이드 후 하단 바 Undo 버튼 선택으로 삭제 취소
    # 슬라이드 후 하단 바 N초 경과 후 삭제 취소 사라짐

    # 햄버거 버튼 목록
    # Note 보관 시 Archive 가 목록에 나타나는지
    # Note 삭제 시 Trash 가 목록에 나타나는지

    # Archive 에 삭제한 Text note 확인

