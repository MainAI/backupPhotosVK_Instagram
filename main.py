import logging
from vkapi import VkPhotos
from ya_dsk import YandexDisk
from inst_photo import InsPhotos


def setup_for_vk_run(token):
    id_person = input('Введите id пользователя vk: ')
    id_album = input('Введите название альбома (profile, wall, saved): ').lower()
    count_photos = int(input('Введите количество резервируемых фотографий: '))
    token_yandex = input('Укажите token Yandex диска: ')
    vk = VkPhotos(token)
    yandex = YandexDisk(token_yandex)
    yandex.upload_image_to_disk(id_album, vk.get_list_photos(id_person, id_album, count_photos))
    return


def setup_for_ins_run(token):
    count = int(input('Введите количество резервируемых фотографий: '))
    token_yandex = input('Укажите token Yandex диска: ')
    ins = InsPhotos(token)
    yandex = YandexDisk(token_yandex)
    yandex.upload_image_to_disk('my_instagram_', ins.get_list_photos(count))
    return


def choice_way_run(token_vk, token_ins):
    choice_use = input('Введите название ресурса(VK, Instagram) для резервного копирования: ').lower()
    if choice_use == 'vk':
        setup_for_vk_run(token_vk)
    elif choice_use == 'instagram':
        setup_for_ins_run(token_ins)
    else:
        print('Ошибка')
        logging.error('Incorrect choice_use')
        return None
    return


if __name__ == '__main__':
    token_vk_user = ''  # Insert correct token before run API VK
    token_ins_user = ''  # Insert correct token before run API BASIC Instagram

    logging.basicConfig(filename="runtime.log", level=logging.INFO, filemode='w')
    logging.info("Program started")
    choice_way_run(token_vk_user, token_ins_user)
    logging.info("DONE!!!")
