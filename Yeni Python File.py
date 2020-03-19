from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
while True:
    print("**********AGARTHA WHATSAPP SELENIUM DENEME************")
    print("**********WHATSAPP BOMBER************")

    try:
        name = input('Kullanýcý veya Grup Adý Yaz : ')
    except:
            print("Hata Oluþtu")
            name = input('Kullanýcý veya Grup Adý Yaz : ')
    try:
        msg = input('Mesajýný Yaz : ')
    except:
        print("Bir hata oluþtu")
        msg = input('Mesajýný Yaz : ')
    try:
        count = int(input('Kaç Adet Gönderilsin : '))
    except: 
        print("Hata Oluþtu")
        count = int(input('Kaç Adet Gönderilsin : '))
        
    input('Göndermek Ýçin Basýnýz')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()