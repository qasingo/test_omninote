from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.app_package = 'it.feio.android.omninotes'
options.app_activity = 'it.feio.android.omninotes.MainActivity'
options.auto_grant_permissions = True

def omniNotes():
  driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
  print("실행 완료")
  time.sleep(10)
  return driver