
# Session2TDataBot 🔄

Телеграм-бот для конвертации сессий Telethon (.session) в TData-архивы с именем пользователя.

## ⚙️ Установка

1. Установите зависимости:
```bash
pip install pyTelegramBotAPI opentele telethon 
```

2. Получите токен бота:
- Напишите [@BotFather](https://t.me/BotFather) в Telegram
- Создайте нового бота командой `/newbot`
- Скопируйте полученный токен

3. Вставьте токен в код:
```python
bot = telebot.TeleBot("ВАШ_ТОКЕН_ЗДЕСЬ", parse_mode='HTML')  # в 9 строке bot.py
```

## 🚀 Запуск
```bash
python bot.py
```

## 📌 Использование
1. Отправьте боту файл `.session`
2. Получите ZIP-архив `tdata` с подписью:
```
📁 tdata пользователя @username
```

## 🔧 Особенности
- Автоопределение username из сессии
- Самоочистка временных файлов
- Поддержка сессий с 2FA
- Обработка ошибок

## 📚 Зависимости
- `pyTelegramBotAPI` → работа с Telegram API
- `opentele` → конвертация сессий
- `telethon` → чтение .session файлов

## 👤 Разработчик 
[@worpli](https://t.me/worpli)

## 🌟 Вдохновение
Проект основан на [session_to_tdata](https://github.com/woidead/session_to_tdata) от @woidead

> ⚠️ Бот не хранит ваши данные. Используйте только свои сессии!
```
