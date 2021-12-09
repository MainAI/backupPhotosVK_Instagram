import logging
import requests


class VkPhotos:
    def __init__(self, token):
        self.token = token

    def get_list_photos(self, id_user, album, count):
        """
        Create result_list of dict key: file_name, size, url
        File_name = like count,if same exist than file_name = like count_date(unix)
        """
        logging.info("Start get list photos from user album Vk")
        url = 'https://api.vk.com/method/photos.get'  # METHOD?PARAMS&access_token=TOKEN&v=V
        params = {'owner_id': id_user,
                  'album_id': album,
                  'rev': 1,
                  'extended': 1,
                  'photo_sizes': 1,
                  'count': count,
                  'access_token': self.token,
                  'v': 5.131
                  }
        response = requests.get(url=url, params=params)
        data = response.json()
        if response.status_code != 200 and data.get('error') is not None:
            print(f'error_code: {data["error"]["error_code"]} \n'
                  f'error_msg: {data["error"]["error_msg"]}')
            return None

        elif response.status_code == 200 and data.get('error') is None:
            result_list = []
            temp_list = []
            for photos in data['response']['items']:
                if photos['likes']['count'] in temp_list:
                    file_name = f'{photos["likes"]["count"]}_{photos["date"]}.jpg'
                else:
                    file_name = f'{photos["likes"]["count"]}.jpg'
                    temp_list.append(photos["likes"]["count"])
                temp_dict = {'file_name': file_name,
                             'size': photos['sizes'][-1]['type'],
                             'url': photos['sizes'][-1]['url']
                             }
                result_list.append(temp_dict)
            logging.info("DONE Generate result_list Vk")
            return result_list




