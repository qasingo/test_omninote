from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.app = r'C:/Workspace/QA/Appium_omniNote/apk/TEST-OmniNotes-alphaDebug-6.3.2.apk'
options.auto_grant_permissions = True

# *개선해볼 내용 : {디바이스 환경:디바이스 이름} 딕셔너리 형태로 생성
# 디바이스 환경
d = 'd'             # 디바이스
avd = 'avd'         # 안드로이드가상디바이스

# deviceName
d_s9 = '228818e4410b7ece'
# avd Name
avd_px3 = 'Pixel_3_API_31'


# 디바이스 환경 및 디바이스 대상 지정하여 실행
def config_omniNotes_wd(deviceEnvironment, testDevice):
  # 디바이스 환경이 실제환경인지 가상환경인지 확인
  if deviceEnvironment == 'd':
    options.device_name = testDevice
  elif deviceEnvironment == 'avd':
    options.avd = testDevice

  driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
  print("실행 완료")
  time.sleep(10)
  return driver

# 테스트 웹 드라이버 호출
# 테스트 실행할 디바이스 환경/디바이스 이름 입력
wd = config_omniNotes_wd(avd, avd_px3)

# wd 가 있는 곳에서만 함수 자동완성이 되어 해당 웹드라이버에 함수 생성함
# xpath 를 통해 element 를 찾아 반환
def get_element(xpath):
  element = wd.find_element(By.XPATH, xpath)
  return element

# xpath와 attribute를 입력해 attribute value 값을 찾아 반환 (안됨)
def get_attribute_value(xpath, attribute):
  element = wd.find_element(By.XPATH, xpath)
  # attribute_value = element.
  # return attribute_value
