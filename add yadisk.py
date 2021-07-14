from pprint import pprint
import requests


class YaUploader:

    def __init__(self, file_path: str):    # класс создается с путем к файлу
        self.file_path = file_path

    def upload(self, disk_file_path, filename):
        # метод в классе по загрузке файла. Объект создается с параметрами путь и имя. В итоге запись на яндекс диск по указанным параметрам
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Accept': 'application/json', 'Authorization': TOKEN}
        params = {"path": disk_file_path, "overwrite": "true"}  # путь, по которому нужно загрузить файл
        response = requests.get(upload_url, headers=headers, params=params)  # запрашиваем ссылку для загрузки
        put_url = response.json().get('href')  # вынимаем url
        response = requests.put(put_url, data=open(filename, 'rb'), headers=headers) # записываем на диск
        if response.status_code == 201:
            pprint("Success")
        else:
            pprint('думай')


ya = YaUploader(file_path=r'''D:\Study\Pycharm\Netology\11. Работа с библиотекой requests, http запросы\дз\new_file2.txt''')

ya.upload('/Netology/new_file2.txt', 'new_file2.txt')
