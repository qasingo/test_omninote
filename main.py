from configuration import webDriver
from tests import testcases

# 테스트 웹 드라이버 호출
wd = webDriver.omniNotes()

#intro_test 진행
testcases.intro_test(wd)