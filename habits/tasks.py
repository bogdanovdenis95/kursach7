import asyncio
import telegram
from celery import shared_task
from decouple import config
from .models import Habit


@shared_task
def send_telegram_notification(habit_id):
    habit = Habit.objects.get(id=habit_id)
    bot_token = config('TELEGRAM_BOT_TOKEN')
    chats_id = config('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=bot_token)

    async def send_message():
        message = f"Напоминание: {habit.action} в {habit.time} в {habit.location}."
        await bot.send_message(chat_id=chats_id, text=message)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message())
