import pyowm
import telebot

# ---------- FREE API KEY examples ---------------------
owm = pyowm.OWM('b6bff2f5dc0afbc3112114c470e5b3ba')
# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot("1359590218:AAGnaTyoGaJ41TRlha1s1qafBz6vNt-OMo0")

mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"
    if temp < 10:
        answer += "Сейчас холодно, оденься потеплее."
    elif temp < 20:
        answer += "Сейчас норм погода."
    else:
        answer += "Сейчас жара"

	# bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
