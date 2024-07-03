import os
import ctypes

import requests

import config as cfg







class APIManager:
    def __init__(self, *args, **kwargs):
        self.count_pages = str(kwargs.get('count_pages', cfg.DEFAULT_count_pages))
        self.page = str(kwargs.get('page', cfg.DEFAULT_page))

        self._project_link = kwargs.get('project_link', cfg.project_link)
        self.channel_url = kwargs.get('channel_url', cfg.channel_url).replace('_page_', self.page).replace('_count_pages_', self.count_pages)
        self.all_projects_url = kwargs.get('all_projects_url', cfg.all_projects_url).replace('_page_', self.page).replace('_count_pages_', self.count_pages)
        self.search_url = kwargs.get('search_url', cfg.search_url)

        self.search_data = kwargs.get('search_data', cfg.search_data)
        self.search_data['page'] = int(self.page)
        self.search_data['per_page'] = int(self.count_pages)
        self.search_data['value'] = []

        self.cookies = kwargs.get('cookies', cfg.cookies)
        self.headers = kwargs.get('header', cfg.headers)

    
    def format_project_link(self, project_id) -> str:
        return self._project_link.replace('_project_id_', str(project_id))
    

    def format_channel_url(self, channel_id) -> str:
        return self.channel_url.replace('_channel_id_', str(channel_id))


    @classmethod
    def _get_hash_ids(cls, data) -> list:
        hash_ids = []
        for item in data:
            project_id = item.get('hash_id', None)
            hash_ids.append(project_id)
        return hash_ids
    

    def get_projects_ids(self, channel_id, search_flag=False) -> list:
        response = self.get_response(channel_id=channel_id, search_flag=search_flag)

        if response.status_code != 200:
            raise Exception('Ошибка соединения. Проблема на стороне ArtStation')

        data = response.json().get('data', None)
        projects_ids = self._get_hash_ids(data)

        return projects_ids
    

    def get_response(self, search_flag, channel_id=None):
        '''
            Определение какой url будет задействован - 'Все/фильтр/категории'
        '''
        if search_flag:
            response = requests.get(
                self.search_url,
                cookies=self.cookies,
                headers=self.headers,
                json=self.search_data,
            )
            return response

        channel_url = self.format_channel_url(channel_id)
        response = requests.get(channel_url)
        return response
    


    


class ImageManager:
    def __init__(self, *args, **kwargs):
        self.height = kwargs.get('height', cfg.DEFAULT_height)
        self.width = kwargs.get('width', cfg.DEFAULT_width)
        self.session = kwargs.get('session', cfg.session)

        self._create_old_links()


    def get_project_obj(self, proj_link):
        response = self.session.get(proj_link)

        if response.status_code != 200:
            raise Exception('Ошибка соединения. Проблема на стороне ArtStation')
        
        data = response.json()['assets']
        return data
    

    def get_image_obj(self, obj):
        for item in obj:
            if item['asset_type'] == 'image':
                return item
    

    def get_size_image(self, image_obj) -> tuple:
        return image_obj['width'], image_obj['height']
    

    def get_image_url(self, image_obj) -> str:
        return image_obj['image_url']


    def validate_image(self, size, link_img) -> bool:
        size_condition =  (size[0] >= self.width) and (size[1] >= self.height)
        memory_condition = self.find_image(link_img)

        return size_condition and memory_condition
    

    @classmethod
    def _create_old_links(cls):
        try:
            with open(cfg.path_to_old_links, 'a') as f: pass
        except FileNotFoundError:
            with open(cfg.path_to_old_links, 'w') as f: pass
                

    def memorize_image(self, link_img):
        with open(cfg.path_to_old_links, 'a') as f:
            f.write(link_img + '\n')
      

    def find_image(self, link_img):
        with open(cfg.path_to_old_links, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i].replace('\n', '')

                if link_img == line:
                    return False
        return True



class FileManager:

    def upload_image(self, image_link):
        image_name = self._format_image_name(image_link)
        img_data = requests.get(image_link).content

        os.makedirs(cfg.path_to_images, exist_ok=True)
        with open(f'{cfg.path_to_images}/{image_name}', 'wb') as handler:
            handler.write(img_data)


    def set_image(self, image_link):
        image_name = self._format_image_name(image_link)
        image_path = os.path.abspath(f'{cfg.path_to_images}/{image_name}')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

        self._clear_directory(cfg.path_to_images)


    @classmethod
    def _clear_directory(cls, directory):
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                elif os.path.isdir(filepath):
                    os.rmdir(filepath)
            except Exception as e:
                print(f"Failed to delete {filepath}: {e}")


    @classmethod
    def _format_image_name(self, image_link):
        return image_link.split('/')[-1].split('?')[0]



if __name__ == '__main__':
    # Mock
    channel_id = 105
    proj_id = 7


    api = APIManager()
    project_ids = api.get_projects_ids(channel_id)

    image = ImageManager()
    proj_link = api.format_project_link(project_ids[proj_id])

    project_obj = image.get_project_obj(proj_link)
    image_obj = image.get_image_obj(project_obj)
    size = image.get_size_image(image_obj)
    image_url = image.get_image_url(image_obj)

    image_valid = image.validate_image(size, image_url)
    if image_valid:
        file = FileManager()
        file.upload_image(image_url)
        image.memorize_image(image_url)
        file.set_image(image_url)


    # print(image.validate_image(size, image_url))
    # image.memorize_image(image_url)
    # print(image.validate_image(size, image_url))

    # print('Size: ', size)
    # print('Project Object: ', project_obj)

    # https://www.artstation.com/projects/XgZRNn.json