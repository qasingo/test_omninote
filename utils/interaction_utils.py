from appium.webdriver.common.touch_action import TouchAction
from configuration.webDriver import wd, get_element


class Touch:
    # 터치 1회
    def tap_by_element(xpath):
        element = get_element(xpath)
        action = TouchAction(wd)
        action.tap(element).perform()

    # 더블 터치 1회
    def double_tap_by_element(xpath):
        element = get_element(xpath)
        action = TouchAction(wd)
        action.tap(element).wait(100).tap(element).perform()  # 간격을 100ms로 설정하여 더블탭 시뮬레이션

    # 롱 터치 1회
    def long_press_by_element(xpath, duration=1000):
        element = get_element(xpath)
        action = TouchAction(wd)
        action.long_press(element, duration=duration).release().perform()


class Slide:
    # 전체 화면 오른쪽에서 왼쪽으로 슬라이드
    def window_swipe_left():
        size = wd.get_window_size()
        start_x = size['width'] * 0.8
        end_x = size['width'] * 0.2
        y = size['height'] * 0.5
        duration = 800  # 밀리초 단위

        action = TouchAction()
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()

    # 전체 화면 왼쪽에서 오른쪽으로 슬라이드
    def window_swipe_right():
        size = wd.get_window_size()
        start_x = size['width'] * 0.2
        end_x = size['width'] * 0.8
        y = size['height'] * 0.5
        duration = 800  # 밀리초 단위

        action = TouchAction(wd)
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()

    # element 의 att_bounds 기준으로 오른쪽에서 왼쪽으로 슬라이드
    def bounds_swipe_left(bounds):
        start_x = bounds[1][0]
        end_x =  bounds[0][0]
        y = (bounds[0][1] + bounds[1][1]) * 0.5
        duration = 800  # 밀리초 단위
        action = TouchAction(wd)
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()

    # element 의 att_bounds 기준으로 왼쪽에서 오른쪽으로 슬라이드
    def bounds_swipe_right(bounds):
        start_x = bounds[0][0]
        end_x =  bounds[1][0]
        y = (bounds[0][1] + bounds[1][1]) * 0.5
        duration = 800  # 밀리초 단위
        action = TouchAction(wd)
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()

    def temp_bounds_swipe_left():
        y = 400                      # 시작,종료 y 좌표 (화면의 중앙)
        start_x = 900                # 시작 x 좌표 (오른쪽에서 시작)
        end_x = 200                  # 끝 x 좌표 (왼쪽으로 이동)
        duration = 800               # 밀리초 단위
        action = TouchAction(wd)     # TouchAction을 사용하여 슬라이드 동작 시뮬레이션
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()
    
    def temp_bounds_swipe_right():
        y = 900                      # 시작,종료 y 좌표 (화면의 중앙)
        start_x = 400                # 시작 x 좌표 (왼쪽에서 시작)
        end_x = 200                  # 끝 x 좌표 (오른쪽으로 이동)
        duration = 800               # 밀리초 단위
        action = TouchAction(wd)     # TouchAction을 사용하여 슬라이드 동작 시뮬레이션
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()