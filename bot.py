import telebot
from telebot import types
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import UseCurrentSession
import os
import shutil
import asyncio

bot = telebot.TeleBot("TOKEN", parse_mode='HTML')

def get_username(session_path):
    async def async_get_user():
        client = TelegramClient(session_path)
        await client.connect()
        me = await client.get_me()
        await client.disconnect()
        return me.username or me.first_name or str(me.id)
    return asyncio.run(async_get_user())

def create_tdata(session_name):
    async def async_create():
        try:
            client = TelegramClient(f"Session/{session_name}")
            await client.connect()
            tdesk = await client.ToTDesktop(flag=UseCurrentSession)
            username = await client.get_me()
            
            save_path = f"TData/{username.username}/tdata"
            tdesk.SaveTData(save_path)
            
            shutil.make_archive(
                f"TData/{username.username}/tdata",
                'zip',
                f"TData/{username.username}/tdata"
            )
            return username.username
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            await client.disconnect()
    
    return asyncio.run(async_create())

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Отправь сессию telethon (.session)</b>")

@bot.message_handler(content_types=['document'])
def handle_doc(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        name = message.document.file_name
        
        if not name.endswith('.session'):
            bot.reply_to(message, "🚫 Нужен .session файл!")
            return

        
        downloaded = bot.download_file(file_info.file_path)
        os.makedirs("Session", exist_ok=True)
        with open(f"Session/{name}", 'wb') as f:
            f.write(downloaded)

        
        username = create_tdata(name)
        if not username:
            raise Exception("Ошибка конвертации")

        
        zip_path = f"TData/{username}/tdata.zip"
        with open(zip_path, 'rb') as f:
            bot.send_document(
                message.chat.id, 
                f,
                caption=f"📁 tdata пользователя @{username}"
            )

        
        os.remove(f"Session/{name}")
        shutil.rmtree(f"TData/{username}")

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {str(e)}")
        if os.path.exists(f"Session/{name}"):
            os.remove(f"Session/{name}")

if __name__ == '__main__':
    os.makedirs("Session", exist_ok=True)
    os.makedirs("TData", exist_ok=True)
    bot.polling(none_stop=True)
