import json
import requests
import logging


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_new_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {
            'path': f'/{folder_name}'
        }
        response = requests.put(url=url, headers=headers, params=params)
        response.raise_for_status()
        logging.info("Create new folder on YaDisk for photos done")
        return

    def _create_info_file(self, image_list):
        with open('info.json', 'w', encoding='utf-8') as f:
            json.dump(image_list, f, ensure_ascii=False, indent=4)
        return

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        logging.info("Upload info.json done")
        return

    def upload_image_to_disk(self, folder_name, image_list):
        """ Upload photos to YaDisk + info.json in same dir"""
        logging.info("Start upload photos to YaDisk")
        if image_list is None:
            print('incorrect data list')
            return
        else:
            self.create_new_folder(folder_name)
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = self.get_headers()
            for image_dict in image_list:
                image_url = image_dict.pop("url")
                params = {
                        'path': f'/{folder_name}/{image_dict["file_name"]}',
                        'url': image_url
                }
                response = requests.post(url=url, headers=headers, params=params)
                response.raise_for_status()
            logging.info("DONE Upload photos to YaDisk")
            self._create_info_file(image_list)
            self.upload_file_to_disk(f'/{folder_name}/info.json', 'info.json')
            return

