import telebot
import feedparser

bot_token ='YOUR_TELEGRAM_BOT_TOKEN_HERE'
channel_id = '@YOUR_TELEGRAM_CHANNEL_NAME_HERE'

bot= telebot.TeleBot(token=bot_token)

def send_latest_news():
    feed = feedparser.parse("YOUR_RSS_FEED_URL_HERE")

    # Get the latest news from the RSS feed
    latest_news = feed.entries[0]
    title = latest_news.title
    summary = latest_news.summary
    link = latest_news.link

    # Send the latest news to the Telegram channel
    message = f"{title}\n{summary}\n{link}"
    bot.send_message(channel_id, message)

# Set up a scheduled job to run every hour
import schedule
import time

schedule.every().hour.do(send_latest_news)

while True:
    schedule.run_pending()
    time.sleep(1)
