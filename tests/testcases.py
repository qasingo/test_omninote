from appium.webdriver.common.appiumby import By
from utils.interaction_utils import Slide
import time

# 기대 결과 값

# 인트로 화면 테스트 실행
def intro_test(wd):
    # Intro 화면 xpath
    text1_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.TextView[1]"
    text2_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.TextView[2]"
    button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageButton"

    # Intro 화면 테스트
    try:
        # Intro 첫 화면 슬라이드 확인
        Slide.swipe_right(wd)
        time.sleep(1)
        for intro_index in range(1, 7):  # Intro 화면은 총 6개
            # Intro 화면의 텍스트 확인
            text1_element = wd.find_element(By.XPATH, text1_xpath)
            text2_element = wd.find_element(By.XPATH, text2_xpath)

            print(f"Intro{intro_index} - Text1: {text1_element.text}")
            print(f"Intro{intro_index} - Text2: {text2_element.text}")

            # Intro 화면의 슬라이드
            Slide.swipe_left(wd)    # 슬라이드로 다음 화면 넘어가기
            time.sleep(1.5)

            if intro_index < 6:     # 마지막장이 아닌 경우
                Slide.swipe_right(wd)  # 슬라이드로 이전 화면 돌아가기
                time.sleep(1.5)

            # Intro 화면의 다음 버튼 클릭
            button_element = wd.find_element(By.XPATH, button_xpath)
            button_element.click()
            time.sleep(1)  # 다음 Intro로 넘어가는 동작 확인을 위해 1초 대기

    except Exception as e:
        print(f"에러 발생: {e}")