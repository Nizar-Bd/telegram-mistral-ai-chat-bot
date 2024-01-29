<img align="left" width="125" height="70" src="https://logos-world.net/wp-content/uploads/2021/03/Telegram-Logo.png" alt="Telegram Icon"><h1 style="text-align: center;">TELEGRAM CHATBOT AI ASSISTANT</h1>


<h3  align='center'> This repo will allow you to create your own Telegram Bot powered by <a href="https://mistral.ai/">Mistral AI</a> Large Language Model.</h3>

## Table of Contents
- [Prerequisites](#Prerequisites)
- [Token & Key](#Keys)
- [Installation](#Installation)
- [Usage](#Usage)

## Prerequisites
- **Python** 3.10.6
- **<a href="https://python-telegram-bot.org/">Python-Telegram-Bot</a>** 20.7
- **<a href='https://docs.mistral.ai/api/'>MistralAI</a>** 0.0.11

## Keys
- **Telegram Bot Token** (follow this <a href='https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token'>tutorial</a> to get one)
- **Mistral API Key** (follow this <a href=''>tutorial</a> to get one)

## Installation
**1. Clone the repository**
```bash
git clone https://github.com/Nizar-Bd/telegram-friend-bot.git

cd telegram-mistral-ai-chat-bot
```
**2. Install the prerequisites**
```bash
pip install -r requirements.txt
```
**3. Set your environment variables**

Copy your own token and key in environment variables called **TELEGRAM_TOKEN** and **MISTRAL_API_KEY**

## Usage

Now that everything is setup, lauch the program by writting in your terminal :
```bash
python telegram_bot/telegram_bot.py
```

Then find your bot on Telegram (depends on how you named it with @BotFather), press start and start talking with your bot!
