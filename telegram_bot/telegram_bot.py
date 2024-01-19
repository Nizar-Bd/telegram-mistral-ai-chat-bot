import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, Updater, filters
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


telegram_token = os.environ['TELEGRAM_TOKEN']

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-tiny"

client = MistralClient(api_key=api_key)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="""Hi, I am your new assistant powered by MistralAI.\n
                                           What can I do for you ?""")


async def mistral_ans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("query recieved, answer in process! ✅")
    messages = [ChatMessage(role="user", content=update.message.text)]
    chat_response = client.chat(model=model,messages=messages,)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=chat_response.choices[0].message.content)

if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), mistral_ans)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
