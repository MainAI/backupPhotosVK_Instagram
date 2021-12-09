## backupPhotosVK_Instagram to Yandex Disk
#### *Backup the required number of photos:*
1. From VK. 
1. From Instagram. 

#### *Description VK use:*  
From the selected user_id, album_name, count_photos copied max size photos to the "album_name" folder on Yandex Disk.   
No need to create "album_name" folder on Yandex Disk in advance.  
Name: "count_like.jpg", if same "count_like_date.jpg".  

#### *Description Instagram use:*  
From your profile copied the selected count_photos photos to the "my_instagram_" folder on Yandex Disk.  
Name: "id_photo.jpg".  

#### *For all output* info.json *file. Example:*
```json
[
    {
        "file_name": "name.jpg",
        "size": "size"
    }
]
```

#### *Before use insert your token for VK API and  API Instagram Basic Display inside main.py:*
```python
if __name__ == '__main__':
    token_vk_user = ''  # Insert correct token before run API VK
    token_ins_user = ''  # Insert correct token before run API BASIC Instagram
```
