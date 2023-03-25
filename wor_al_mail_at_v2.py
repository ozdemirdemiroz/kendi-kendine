
import tkinter as tk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import win32com.client as win32

siteNamelist=[]
#siteNamelist=["AN0001","AN0002"]
worid_alinan=""
worIDlist=[]

def AtlasSiteReset(sahaListesi,kullanıcı,sifre):
        
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
        
        
        for sahaAdi in sahaListesi:
                sleep(5)
                #wor açılması için gerekli girişler
                description=driver.find_element(By.ID,"mcd42ce0b-tb")
                description.send_keys("Site Reset")

                Location=driver.find_element(By.ID,"m82410ac-tb")
                Location.send_keys(f"{sahaAdi}")
                sleep(1)
                Location.send_keys(Keys.SPACE) #bazı manual grişler yazıldıktan sonra space bırakılınca register etmekte
                sleep(1)
                isTipi=driver.find_element(By.ID,"mc8f7970f-tb")
                isTipi.send_keys("CNRO \ KART ILAVE")
                sleep(1)
                isTipi.send_keys(Keys.SPACE)

                detay = driver.find_element(By.ID,"m96cc4d77-ta")
                #detay.send_keys(f"{sahaAdi} sahasına site Reset uygulayabilir misiniz?" )
                detay.send_keys("RECEJT Edilebilir" )

                atanacakGrup = driver.find_element(By.ID,"m293afb01-tb")
                atanacakGrup.send_keys("MS OMC ")

                #tarih girişi , yapılacak iş için 30 dakika sonraya sonteslim tarihi veriliyor . 
                tarih = (datetime.now() + timedelta(minutes=30)).strftime("%d.%m.%Y %H:%M:%S")
                tarihAlanı = driver.find_element(By.ID , "m3156b48b-tb")
                tarihAlanı.send_keys(tarih)
                sleep(1)
                tarihAlanı.send_keys(Keys.SPACE)



                #herhalde girilen tarih register etsin diye başka bir alana tıklatmışım . çıkartılıp denenenebilir
                isPlani =  driver.find_element(By.ID , "m9fbb3235-tb")
                isPlani.click()

                worid_alinan=driver.find_element(By.ID,"m93665d71-tb").get_attribute("value")
                worIDlist.append(worid_alinan)
                
                #route edilip worID nin konsola bastırılması , 2. adım --> return ile WOR id alınıp buna göre mail attırılmaya çalışılacak 
                routeBtn = driver.find_element(By.ID,"ROUTEWF_WOR_-tbb_image")
                routeBtn.click()
                sleep(5)

                newWorBtn=driver.find_element(By.ID, "toolactions_INSERT-tbb_image")
                newWorBtn.click()


def sendMail(siteName,worid):
    try:
        outlook = win32.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.Display()
        #sleep(2)
        mail.Subject = f"{siteName} Site Reset"
        message = f"{siteName} sahasına site Reset uygulayabilir misiniz? WOR: {worid}"
        mail.HTMLBody ="Merhaba" +"<br><br><br>"+  message + mail.HTMLBody
        mail.To = "ozdemir.demiroz@gmail.com "

        mail.Send()
    except Exception as e:
        print(f"Error sending email: {e}")


# düğme tıklama
def button_click():
    siteNamelist = Sahalar.get("1.0", "end-1c").split()  # get the text input from the text area
    
    #burya ATLAS WOR ALMA fonksiyonu , Return ile wor listesi döndürecek
    # for i in siteNamelist:
    #  AtlasSiteReset(i,"29102446","ejBztS5PyvL28E3")
    #  print(worIDlist)
    AtlasSiteReset(siteNamelist,Atlas_user.get("1.0", "end-1c"),atlas_sifre.get("1.0", "end-1c"))
    print(worIDlist)
    for i in siteNamelist:
     sendMail(i,worIDlist[siteNamelist.index(i)])
  

# tkinter ana Pencere
AnaPencere = tk.Tk()
AnaPencere.title("Site Reset Tool")

# text giriş alanı
Sahalar = tk.Text(AnaPencere, height=5, width=30)
Sahalar.pack()

#user
Atlas_user_label=tk.Label(AnaPencere,text="Atlas User Name")
Atlas_user=tk.Entry(AnaPencere, width=20)
Atlas_user_label.pack()
Atlas_user.pack()

#pass
Atlas_sifre_label=tk.Label(AnaPencere,text="Atlas Şifre")
atlas_sifre=tk.Entry(AnaPencere,show="*" , width=20)
Atlas_sifre_label.pack()
atlas_sifre.pack()
# düğme
button = tk.Button(AnaPencere, text="Wor al ve mail at", command=button_click)
button.pack()


AnaPencere.mainloop()