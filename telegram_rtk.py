import time
import schedule
from telegram import Bot

print(telegram.__version__)

# Токен бота и ID чата
TOKEN = "7473927237:AAHRrI0-f8kPHuS5MhNeg9tkh5y9DecnTUQ"  # Замени на свой токен
CHAT_ID = "-4614478695"  # Замени на ID чата

bot = Bot(TOKEN)


def send_message():
    try:
        bot.send_message(
            chat_id=CHAT_ID, text="Привет! Это автоматическое сообщение 🚀")
        print("✅ Сообщение отправлено!")
    except Exception as e:
        print(f"❌ Ошибка отправки сообщения: {e}")


# Отправка каждые 5 минут
schedule.every(5).minutes.do(send_message)

while True:
    schedule.run_pending()
    print("🔄 Ожидание...")
    time.sleep(60)
