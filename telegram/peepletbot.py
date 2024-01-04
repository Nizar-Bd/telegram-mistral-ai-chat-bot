import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

peeplet_token = os.getenv('TELEGRAM_TOKEN')
print(peeplet_token)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Salut beau gosse 👋, qu'est ce que je peux faire pour toi ?")

if __name__ == '__main__':
    application = ApplicationBuilder().token(peeplet_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

# async
