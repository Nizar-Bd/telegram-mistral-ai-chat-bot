import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, Updater, filters
import os
from nlpmodel import  *

peeplet_token = os.getenv('TELEGRAM_TOKEN')
print(peeplet_token)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Salut beau gosse 👋, qu'est ce que je peux faire pour toi ?")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    print("query recieved, answer in process! ✅")
    bot_reply = answer_query(pipe, user_query)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_reply)

if __name__ == '__main__':
    application = ApplicationBuilder().token(peeplet_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    pipe = load_model("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    print("model loaded ready to work ✅")


    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), caps)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
