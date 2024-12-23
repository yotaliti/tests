import requests
import time


class TestYDCreateFolder:

    def setup_method(self) -> None:
        self.header {
            'Authorization':
        }

    def test_create_folder(self):
        url = 'https://api.nasa.gov/planetary/apod'
        params = {
            'api_key': 'xAV7ZrQf0yCNVFKcCa87ujS38lXMiI4mgmpREBBd',
            'date': '2024-06-05'
        }
        response = requests.get(url, params=params)
        url_image = response.json()['url']
        file_name = url_image.split('/')[-1]

        params = {
            'path': 'Image'
        }
        create_folder = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                     params=params,
                                     headers=self.headers
                                     )
        time.sleep(2)

        upload_image = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload?'
                                     f'path=Image%2F{file_name}&'
                                     f'url=https%3A%2F%2Fapod.nasa.gov%2Fapod%2Fimage%2F2406%2F{file_name}',
                                     headers=self.headers)
        time.sleep(2)

        folder_exists = requests.get('https://cloud-api.yandex.net/v1/disk/resources/last-uploaded',
                                params=params,
                                headers=self.headers,
                                )
        result = folder_exists.json()['items'][0]['path'].split('/')[1]

        assert folder_exists.status_code == 200
        assert result == 'Image'
