import requests
import config as cfg



# APIManager:
#     - Ссылки на каналы;
#     - Ссылки на проекты;
#     - Ссылки на картинки;


# ImageManager:
#     - Сохранение картинки в "наличии";
#     - Поиск картинки в "наличии";
#     - Получение размера(ширины и высоты изображения)
#     - Решение о валидности изображения (размер/наличие);


# FileManager:
#     - Скачивание картинки;
#     - Установка картинки в к-ве рабочего стола;


# UserInput:
#     - Запрос исходной папки;
#     - Запрос интервала;
#     - Запрос фильтров;
#     - На основе введённых штук создаётся конфиг;



# if __name__ == '__main__':
    # Выбор пользователю: Конфигурация/парсить
    # Если парсить: проверяется конфиг, если там достаточно данных - запуск парсингла/интервала или в ручную
    # Если конфигурация, то: UserInput

# Подумать о замене некоторых частей программы на другие
# Подумать о расширении/добавления функционала




class Url:
    def __init__(self, *args, **kwargs):
        self.count_pages = kwargs.get('count_pages', cfg.DEFAULT_count_pages)
        self.page = kwargs.get('count_pages', cfg.DEFAULT_page)
        self.project_link = f'https://www.artstation.com/projects/_project_id_.json'
        self.channel_url = f'https://www.artstation.com/api/v2/community/channels/projects.json?channel_id=_channel_id_&page={self.page}&sorting=trending&dimension=all&per_page={self.count_pages}'
        self.all_project_url = f'https://www.artstation.com/api/v2/neighborhoods/projects/community.json?page={self.page}&per_page={self.count_pages}'

    
    def format_channel_url(self, channel_id):
        self.channel_url = self.channel_url.replace('_channel_id_', str(channel_id))

    def format_project_url(self, _project_id_):
        self.project_link = self.project_link.replace('_project_id_', str(_project_id_))

    def get_hash_id(self, data):
        hash_ids = []
        for item in data:
            project_id = item.get('hash_id', None)
            hash_ids.append(project_id)
        return hash_ids


    def get_projects_ids(self, channel_id):
        self.format_channel_url(channel_id)
        response = requests.get(self.channel_url)

        if response.status_code != 200:
            raise Exception('Ошибка соединения. Проблема на стороне ArtStation')

        data = response.json().get('data', None)
        projects_ids = self.get_hash_id(data)

        return projects_ids
        

    # def get_project_link(self, channel_id):



class Image(Url):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.height = kwargs.get('height', cfg.DEFAULT_height)
        self.width = kwargs.get('width', cfg.DEFAULT_width)

    def get_hash_ids(self):
        print(self.get_projects_ids(105))


a = Image()
a.get_hash_ids()