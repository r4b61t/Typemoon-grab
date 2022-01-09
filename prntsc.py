from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import requests
import io
from PIL import Image

save_path = "C:\\Users\\chaya\\Documents\\selenium\\Type_moon\\pics\\"

ser = Service("C:\\Users\\chaya\\Documents\\selenium\\Type_moon\\geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=ser, options=op)
def download_image(save_path,url,name):
    try:
        img_content = requests.get(url).content
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file)
        img = img.convert('RGB')
        file_path = save_path + name

        with open(file_path, 'wb') as f:
            img.save(f,'JPEG')
        print(f'success')
    except Exception as e:
        try:
            print(f'failed, retrying')
            img_content = requests.get(url).content
            img_file = io.BytesIO(img_content)
            img = Image.open(img_file)
            img = img.convert('RGB')
            file_path = save_path + name
            with open(file_path, 'wb') as f:
                img.save(f,'JPEG')
            print('second attempt success')
        except:
            print('second attempt failed, moving on')
            return True
for j in range(124,154):
    url = f'http://browse.minitokyo.net/gallery?tid=311&order=id&index=3&page={j}'

    driver.get(url)

    for i in range(1,50):
        try:
            thumb = driver.find_element(By.XPATH,
                        f'//*[@id="content"]/ul/li[{i}]/a/img')

            thumb_url = thumb.get_attribute('src')
            print(thumb_url)
            full = thumb_url.replace("thumbs", "downloads")
            print(full)
            name = full.split(r'/')[-1]
            # driver.get(full)

            if download_image(save_path, full, name):
                f = open("failslog.txt", "a")
                f.write(f'{full} \n')
                f.close()
        except Exception as e:
            if e.__class__.__name__ == 'NoSuchElementException':
                print('next page')
                f = open("failslog.txt", "a")
                f.write(f'page no.{j} done.\n')
                f.close()
                break
        if i == 3:
            f = open("failslog.txt", "a")
            f.write(f'page no.{j} has more 50(?) pictures.\n')
            f.close()
driver.quit()

#selenium.common.exceptions.TimeoutException: