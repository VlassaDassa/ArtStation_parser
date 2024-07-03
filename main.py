import requests
from requests_html import HTMLSession
import ctypes
import os



per_page = 30
page = 2
image_name = 'image.jpg'
url = f'https://www.artstation.com/api/v2/community/channels/projects.json?channel_id=85&page={page}&sorting=trending&dimension=all&per_page={per_page}'

session = HTMLSession()

def get_project_link(url, index):
    response = requests.get(url)
    data = response.json()
    hash_id = data['data'][index]['hash_id']
    return f'https://www.artstation.com/projects/{hash_id}.json' 


def get_images_array(proj_link):
    response = session.get(proj_link)
    data = response.json()
    return data['assets']

def get_image_link(images):
    for image in images:
        type_condition = image['asset_type'] == 'image'
        size_condition = image['width'] >= 1920 and image['height'] >= 1080
        proportions_condition = int(image['width'] / image['height']) >= 1.7

        if (type_condition and size_condition and proportions_condition):
            return image['image_url']
        

def memorize_link(image_link):
    with open('old_links.txt', 'a') as f:
        f.write(image_link + '\n')


def find_link(image_link):
    with open('old_links.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].replace('\n', '')

            if image_link == line:
                return True
    return False


def save_image(image_link):
    img_data = requests.get(image_link).content
    with open(image_name, 'wb') as handler:
        handler.write(img_data)


def set_image():
    image_path = os.path.abspath(image_name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


            
if __name__ == '__main__':
    set_image()
    for index in range(1, per_page):
        proj_link = get_project_link(url, index)
        images = get_images_array(proj_link)
        image_link = get_image_link(images)

        if (image_link) and not find_link(image_link):
            memorize_link(image_link)
            save_image(image_link)
            set_image()
            break
            


    
    
    
    