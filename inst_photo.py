import logging
import requests


class InsPhotos:
    def __init__(self, token):
        self.token = token

    def get_list_photos(self, count):
        """
        Work only for your media
        Create result_list of dict key: file_name, size, url
        File_name = ID media
        """
        logging.info("Start get list photos from user album Instagram")
        url = 'https://graph.instagram.com/me/media'
        params = {'limit': count,
                  'fields': ['id', 'media_url'],
                  'access_token': self.token,
                  }
        response = requests.get(url=url, params=params)
        if response.status_code != 200:
            print(f'Error code: {response.status_code}')
            return None

        elif response.status_code == 200:
            data = response.json()
            result_list = []
            for photos in data['data']:
                file_name = f'{photos["id"]}.jpg'
                temp_dict = {'file_name': file_name,
                             'size': 'unknown',
                             'url': photos['media_url']
                             }
                result_list.append(temp_dict)
            logging.info("DONE Generate result_list Instagram")
            return result_list



