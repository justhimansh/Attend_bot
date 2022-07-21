from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1
})


driver = webdriver.Chrome(chrome_options=opt)
driver.maximize_window()

driver.get('http://canvas.aut.ac.nz/')

username_field = driver.find_element_by_id('username')
username_field.click()
username_field.send_keys('[ENTER YOUR USERNAME HERE]')

password_field = driver.find_element_by_id('password')
password_field.click()
password_field.send_keys('[ENTER YOUR PASS HERE]')

login_btn = driver.find_element_by_class_name('form-button')
login_btn.click()

calender = driver.find_element_by_id('global_nav_calendar_link').click()

agenda = driver.find_element_by_id('agenda').click()

time.sleep(5)

lecture = driver.find_element_by_xpath("//span[contains(@class,'group_course_10963') and contains(text(), 'COMP700 Session 2')]").click()

clickOnLec = driver.find_element_by_link_text('Join COMP700 Session (Microsoft Teams Meeting)').click()

time.sleep(2)


teamsBrowser = driver.find_element_by_xpath('/html[@class="ltr uiv2"]/body/div[@id="launcherApp"]/div[@id="rootViewV2"]/div[@class="modernViewContainer"]/div[@id="container"]/div[@class="modernViewRenderer"]/div[@id="buttonsbox"]/button[@class="btn primary"][2]').click()

time.sleep(5)

onteams = driver.find_element_by_id('username')
onteams.click()
onteams.send_keys('Himansh')

time.sleep(2)
mute = driver.find_element_by_css_selector('[track-summary="Toggle microphone OFF in meeting pre join screen"]').click()
cover = driver.find_element_by_css_selector('[track-summary="Toggle camera OFF in meeting pre join screen"]').click()
time.sleep(2)
joinclassnow = driver.find_element_by_css_selector('[track-summary="join meeting from pre-join screen"]').click()
