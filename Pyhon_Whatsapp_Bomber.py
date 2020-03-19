from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
while True:
    print("**********AGARTHA WHATSAPP SELENIUM DENEME************")
    print("**********WHATSAPP BOMBER************")

    try:
        name = input('Kullanici veya Grup Adi Yaz : ')
    except:
            print("Hata Olustu")
            name = input('Kullanici veya Grup Adi Yaz : ')
    try:
        msg = input('Mesajini Yaz : ')
    except:
        print("Bir hata oluþtu")
        msg = input('Mesajini Yaz : ')
    try:
        count = int(input('Kaç Adet Gönderilsin : '))
    except: 
        print("Hata Olustu")
        count = int(input('Kaç Adet Gönderilsin : '))
        
    input('Göndermek icin Basiniz')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
