
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

f = open("failslog.txt", "r")
l = []
i=0
for line in f:
    if "http" in line:
        l.append(line.split(' ')[0])
        i +=1

for url in l:
    name = url.split(r'/')[-1]

    if download_image(save_path, url, name):
        f = open("failslog.txt", "a")
        f.write(f'{url} \n')
        f.close()