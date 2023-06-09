import os
import telebot
from dotenv import load_dotenv
from news import get_articles_by_category
load_dotenv()

bot_token= os.getenv('BOT_TOKEN')

bot=telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Klk miop, que ace?")
    
@bot.message_handler(commands=['news'])
def news_handler(message):
    text = "What category do you want?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_news)
    
def fetch_news(message):
    news = get_articles_by_category(message.text)
    for i in range(len(news)):
        data = news[i]
        text_message = f'**New:** {data["title"]}\n**Url:** {data["url"]}'
        bot.send_message(message.chat.id, text_message)
    
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.send_message(message.chat.id, message.chat.first_name)
#     bot.send_message(message.chat.id, message.text)
    
bot.infinity_polling()