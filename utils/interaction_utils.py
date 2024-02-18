from appium.webdriver.common.touch_action import TouchAction
import time

class Touch:
    # 터치 1회
    def tap_by_xpath(wd, xpath):
        element = wd.find_element_by_xpath(xpath)
        action = TouchAction(wd)
        action.tap(element).perform()

    # 더블 터치 1회
    def double_tap_by_xpath(wd, xpath):
        element = wd.find_element_by_xpath(xpath)
        action = TouchAction(wd)
        action.tap(element).wait(100).tap(element).perform()  # 간격을 100ms로 설정하여 더블탭 시뮬레이션

    # 롱 터치 1회
    def long_press_by_xpath(wd, xpath, duration=1000):
        element = wd.find_element_by_xpath(xpath)
        action = TouchAction(wd)
        action.long_press(element, duration=duration).release().perform()


class Slide:
    # 오른쪽에서 왼쪽으로 슬라이드
    def swipe_left(wd):
        size = wd.get_window_size()
        start_x = size['width'] * 0.8
        end_x = size['width'] * 0.2
        y = size['height'] * 0.5
        duration = 800  # 밀리초 단위

        action = TouchAction(wd)
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()

    # 왼쪽에서 오른쪽으로 슬라이드
    def swipe_right(wd):
        size = wd.get_window_size()
        start_x = size['width'] * 0.2
        end_x = size['width'] * 0.8
        y = size['height'] * 0.5
        duration = 800  # 밀리초 단위

        action = TouchAction(wd)
        action.press(x=start_x, y=y).wait(duration).move_to(x=end_x, y=y).release().perform()
