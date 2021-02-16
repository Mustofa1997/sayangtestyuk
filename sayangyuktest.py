import os
import telebot
from flask import Flask, request
# bot api token
TOKEN = '1606508013:AAHFrjbVKAJ4OA_v3EpuzVpRuwHGXvYy2Fs'
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


# fungsi untuk mengirim pesan
def sendMessage(message, text):
   bot.send_message(message.chat.id, text)
# method ini digunakan untuk menghandle command /start atau pada saat memulai bot
@bot.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Selamat datang Di Jejaka Tutorial Bot</b>\n"
   "Silahkan Ketik <b>hello</b> dan dapatkan balasan dari bot ini"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')
# method ini di gunakan untuk mengecek apakah text yang di kirimkan user berupa text atau string lainnya
@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
   if 'hello'in message.text.lower():
      sendMessage(message, 'Hai, {} Semoga Hari Mu Menyenangkan'.format(message.from_user.first_name))


# Bagian Server
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200
@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='<HEROKU Web URL>' + TOKEN)
   return "!", 200
if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
