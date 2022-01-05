# for test
from selenium.webdriver import Edge
from time import sleep
import time

 # import時注意瀏覽器開頭大小寫

driver = Edge('./msedgedriver.exe')
# url = 'https://www.google.com.tw/'http://127.0.0.1:5000/register.html
url = 'http://127.0.0.1:5000/register.html'


driver.get(url)

username = Edge.find_element()

# //*[@id="username_r"]
# //*[@id="password_r"]
# //*[@id="email"]
# //*[@id="sex"]
# //*[@id="age"]
# //*[@id="area"]
# //*[@id="career"]
# //*[@id="submit_r"]
