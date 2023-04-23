from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
import os
import platform
import yadisk


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
# from config import TOKEN

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

YA_TOKEN = os.environ.get("YA_TOKEN")
y = yadisk.YaDisk(token=YA_TOKEN)

BOT_OWNER_ID = os.environ.get("BOT_OWNER_ID")

USERS_STORAGE_FOLDER = "tg_storage/users_files/"
REMOTE_BACKUP_FOLDER = "tg_storage/files_backup/"
LOCAL_STORAGE = "storage"
LOCAL_BACKUP_FOLDER = "./storage/backup/"
LOCAL_TEMP_FOLDER = "./storage/temp/"

@dp.message_handler(lambda message: message.from_id==int(BOT_OWNER_ID), commands=["backup_storage"])
async def backup_handler(msg: types.Message):
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
        print(os.getcwd())
        if platform.system() == 'Windows':
            os.system(f'powershell Compress-Archive -Force "{os.path.join(".", LOCAL_STORAGE, "backup")}"\
                       {os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")}')
        elif platform.system() == 'Linux':
            os.system(f'zip -rF "{os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")} {os.path.join(".", LOCAL_STORAGE, "backup")}"')
        y.upload(f'{os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")}', f'{REMOTE_BACKUP_FOLDER}backup.zip', overwrite=True)
        if os.path.isfile(os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip")):
                    os.remove(os.path.join(".", LOCAL_STORAGE, "temp", "backup.zip"))
    except Exception as ex:
        await msg.answer(ex)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message_handler(lambda message: not message.text.startswith("/backup_storage"), content_types=["text", "document", "photo", "video", "audio"])
async def echo_message(msg: types.Message):
    if msg.text is not None:
        await bot.send_message(msg.from_user.id, msg.text)
    if msg.document is not None:
        await msg.document.download(destination=LOCAL_TEMP_FOLDER+msg.document.file_name)
        filename = msg.document.file_name
        print("Token is actual" if y.check_token() else "Please, update token")
        try:
            y.mkdir(f"{USERS_STORAGE_FOLDER}{msg.from_id}")
        except:
            pass
        try:
            y.upload(f"{LOCAL_TEMP_FOLDER}{filename}", f"{USERS_STORAGE_FOLDER}{msg.from_id}/{filename}", overwrite=True)
            if os.path.isfile(os.path.join(LOCAL_TEMP_FOLDER, filename)):
                    os.remove(os.path.join(LOCAL_TEMP_FOLDER, filename))
            msg.answer("Файл успешно загружен")
        except Exception as ex:
            await msg.answer(ex)

def backup():
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


if __name__ == '__main__':
    backup()
    executor.start_polling(dp)