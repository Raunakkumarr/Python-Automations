import schedule
from selenium import webdriver
import time
import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
  })

url = 'https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
gmail_username = '019neb409@sxc.edu.np'
gmail_password = 'Me@24/01'

def job():
    print("It's class time !!")
    driver = webdriver.Chrome(options=opt, executable_path=r'C:\Users\DELL\chromedriver\chromedriver.exe')
    driver.maximize_window()
    driver.get(url)

    driver.implicitly_wait(60)
    driver.find_element_by_id('identifierId').send_keys(gmail_username)
    driver.find_element_by_id('identifierNext').click()

    driver.implicitly_wait(60)
    driver.find_element_by_name('password').send_keys(gmail_password)
    driver.find_element_by_id('passwordNext').click()
    driver.implicitly_wait(60)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[5]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div[2]/div/span/a/div').click()
    time.sleep(7)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(30)
    keyboard.press_and_release('ctrl+w')
    print("1st Class Attended !!")
    driver.get('https://classroom.google.com')
    driver.implicitly_wait(60)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[5]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div[2]/div/span/a').click()

schedule.every().day.at("14:33").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
