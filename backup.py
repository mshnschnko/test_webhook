from dotenv import load_dotenv
import os
import platform
import yadisk

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

YA_TOKEN = os.environ.get("YA_TOKEN")
y = yadisk.YaDisk(token=YA_TOKEN)

USERS_STORAGE_FOLDER = "tg_storage/users_files/"
REMOTE_BACKUP_FOLDER = "tg_storage/files_backup/"
LOCAL_STORAGE = "storage"
LOCAL_BACKUP_FOLDER = "./storage/backup/"
LOCAL_TEMP_FOLDER = "./storage/temp/"


try:
    # y.download("/tg_storage/", "./storage/backup/")
    for i in list(y.listdir(USERS_STORAGE_FOLDER)):
        dir_name = i['name']
        for j in list(y.listdir(f"{USERS_STORAGE_FOLDER}{dir_name}/")):
            file_name = j['name']
            try:
                os.mkdir(f'{LOCAL_BACKUP_FOLDER}{dir_name}')
            except:
                pass
            y.download(f'{USERS_STORAGE_FOLDER}{dir_name}/{file_name}', f'{LOCAL_BACKUP_FOLDER}{dir_name}/{file_name}')
    print(platform.system())
    if platform.system() == 'Windows':
        os.system(f'powershell Compress-Archive -Force "{os.path.join(".", LOCAL_STORAGE, "backup")}"\
                    {os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")}')
    elif platform.system() == 'Linux':
        os.system(f'zip -rF "{os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")} {os.path.join(".", LOCAL_STORAGE, "backup")}"')
    y.upload(f'{os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")}', f'{REMOTE_BACKUP_FOLDER}backup.zip', overwrite=True)
    if os.path.isfile(os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")):
                os.remove(os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip"))
except Exception as ex:
    print(ex)