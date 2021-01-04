import datetime
import pyautogui
from selenium import webdriver
import os
import time

tc = 'TCBURAYA'
passwd = 'PAROLABURAYA'

os.system("cls")
def check_ders_input(ders_time):
	if len(ders_time) == 1: 
		if ders_time[0] < 24 and ders_time[0] >= 0:
			return True
	if len(ders_time) == 2: 
		if ders_time[0] < 24 and ders_time[0] >= 0 and \
		   ders_time[1] < 60 and ders_time[1] >= 0:
			return True
	elif len(ders_time) == 3: 
		if ders_time[0] < 24 and ders_time[0] >= 0 and \
		   ders_time[1] < 60 and ders_time[1] >= 0 and \
		   ders_time[2] < 60 and ders_time[2] >= 0:
			return True
	return False

print("ORNEK : 18:30:00")
while True:
	ders_input = input("Dersiniz ne zaman basliyor ? : ")
	try:
		ders_time = [int(n) for n in ders_input.split(":")]
		if check_ders_input(ders_time):
			break
		else:
			raise ValueError
	except ValueError:
		print("HATA: LUTFEN DERS SAATINI DAGRU GIRIR SS:DD")


seconds_hms = [3600, 60, 1]
ders_seconds = sum([a*b for a,b in zip(seconds_hms[:len(ders_time)], ders_time)])

now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

time_diff_seconds = ders_seconds - current_time_seconds

if time_diff_seconds < 0:
	time_diff_seconds += 86400 

print("Dersinizin baslamasina kalan sure %s" % datetime.timedelta(seconds=time_diff_seconds))

time.sleep(time_diff_seconds)


print("Derse Basladi")

os.system("cls")
os.system("canliDersOtomasyonProgramim")

tarayıcı=webdriver.Chrome()

hedef=tarayıcı.get("https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp")
time.sleep(4)
username=tarayıcı.find_element_by_name("tckn")
password=tarayıcı.find_element_by_name("password")
giriş_buton=tarayıcı.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/button')
time.sleep(3)
username.send_keys(tc)
password.send_keys(passwd)
giriş_buton.click()
time.sleep(5)
bassme=tarayıcı.find_element_by_xpath('//*[@id="joinMeeting"]')
bassme.click()
time.sleep(70)
bassme2=tarayıcı.find_element_by_xpath('//*[@id="join"]')
bassme2.click()
time.sleep(10)
pyautogui.click(#BURAYA)


