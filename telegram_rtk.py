import time
import schedule
from telegram import Bot
import asyncio


# Токен бота и ID чата
TOKEN = "7473927237:AAHRrI0-f8kPHuS5MhNeg9tkh5y9DecnTUQ"  # Замени на свой токен
CHAT_ID = "-4614478695"  # Замени на ID чата

bot = Bot(TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Привет! 🚀 Это тестовое сообщение!")
print("✅ Сообщение отправлено!")


def job():
    asyncio.run(send_message())


# Запланировать отправку в 9:00 утра
schedule.every().day.at("09:00").do(job)

print("Бот запущен. Ожидание времени отправки...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверяет расписание каждую минуту
