from selenium import webdriver
import time


def elements_exist(bro, val):
    try:
        bro.find_element(by="xpath", value=val)
        return False
    except:
        return True


browser = webdriver.Chrome()
browser.get("https://dazi.kukuw.com/")
time.sleep(3)
browser.find_element(by="id", value="name").click()
time.sleep(1)
browser.find_element(by="id", value="new_username").send_keys("Reaebot")
time.sleep(1)
browser.find_element(by="link text", value="修改").click()
time.sleep(1)
browser.find_element(by="id", value="radio_group2").click()
time.sleep(1)
browser.find_element(by="name", value="group_num").send_keys("W8HM2")
time.sleep(1)
browser.find_element(by="name", value="start_button").click()
Now_Line = 0
while 1:
    if elements_exist(browser, '//*[@id="i_' + str(Now_Line) + '"]/div/span'):
        break
    Text = browser.find_element(by="xpath", value='//*[@id="i_' + str(Now_Line) + '"]/div/span').text
    browser.find_element(by="xpath", value='//*[@id="i_'+ str(Now_Line) + '"]/input[2]').send_keys(Text + ' ')
    Now_Line += 1
