from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta


def AtlasSiteReset(siteName,kullanıcı,sifre):
        
        #webdriver chrome yüklemesi , siteye giriş , sayfayı ekranı kaplatma , user name ve pass yerlerini bularak buralara giriş yapma ve login butonuna tıklama
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://armada.turktelekom.com.tr/maximo/webclient/login/login.jsp?appservauth=true")
        driver.maximize_window()
        sleep(1)
        username = driver.find_element(By.ID,"j_username")
        username.send_keys(kullanıcı)
        password = driver.find_element(By.ID,"j_password")
        password.send_keys(sifre)
        loginBtn = driver.find_element(By.ID,"loginbutton")
        loginBtn.click()
        sleep(5)

        #atlasa girdikten sonra wor sayfasına geçiş ve wor id yi bulma
        worBtn = driver.find_element(By.ID,"QuickInsert_WOR")
        worBtn.click()
        sleep(5)
        worid=driver.find_element(By.ID,"m93665d71-tb").get_attribute("value")
        
        #wor açılması için gerekli girişler
        description=driver.find_element(By.ID,"mcd42ce0b-tb")
        description.send_keys("Site Reset")

        Location=driver.find_element(By.ID,"m82410ac-tb")
        Location.send_keys(f"{siteName}")
        sleep(1)
        Location.send_keys(Keys.SPACE) #bazı manual grişler yazıldıktan sonra space bırakılınca register etmekte
        
        isTipi=driver.find_element(By.ID,"mc8f7970f-tb")
        isTipi.send_keys("RSMC \ SITE RESET")
        sleep(1)
        isTipi.send_keys(Keys.SPACE)

        detay = driver.find_element(By.ID,"m96cc4d77-ta")
        detay.send_keys(f"{siteName} sahasına site Reset uygulayabilir misiniz?" )

        atanacakGrup = driver.find_element(By.ID,"m293afb01-tb")
        atanacakGrup.send_keys("RSMC_ANKARA ")

        #tarih girişi , yapılacak iş için 30 dakika sonraya sonteslim tarihi veriliyor . 
        tarih = (datetime.now() + timedelta(minutes=30)).strftime("%d.%m.%Y %H:%M:%S")
        tarihAlanı = driver.find_element(By.ID , "m3156b48b-tb")
        tarihAlanı.send_keys(tarih)
        sleep(1)
        tarihAlanı.send_keys(Keys.SPACE)

        #herhalde girilen tarih register etsin diye başka bir alana tıklatmışım . çıkartılıp denenenebilir
        isPlani =  driver.find_element(By.ID , "m9fbb3235-tb")
        isPlani.click()

        #route edilip worID nin konsola bastırılması , 2. adım --> return ile WOR id alınıp buna göre mail attırılmaya çalışılacak 
        routeBtn = driver.find_element(By.ID,"ROUTEWF_WOR_-tbb_image")
        routeBtn.click()

        print(worid)


AtlasSiteReset("AN0606","burayakullanıcıID","BurayaŞifre")  


  





