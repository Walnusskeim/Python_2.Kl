'''
Erster Telegram Bot
QrKid. Er kann QR-Code erstellen.
Maximilian
15.05.2023
'''

import telebot
import csv
import os
import yfinance as yf
import time


file = open("telegrambot.txt", "r")
token = file.read()
file.close()

bot = telebot.TeleBot(token , parse_mode=None)



def get_stock_price(name):
	tickers = [name]
	for ticker in tickers:
		ticker_yahoo = yf.Ticker(ticker)
		data = ticker_yahoo.history()
		print(data)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	user_message = str(message).lower()
	bot.reply_to(message, "Hallo, ich bin QrKid. Ich kann QR-Codes erstellen. Sende mir einen Link, welcher mit "
						  "'https://' oder mit 'www.'beginnt, und ich erstelle dir einen QR-Code. \nSchreibe '/exit', um den Befehl zu beenden.")

#############################################################################################################


	def link_check(message):
		link = str(message.text).lower()
		if link.startswith("https://") or link.startswith("www."):
			return "a"

		elif link == "/exit":
			return "b"

		else:
			return "c"

	@bot.message_handler(func=link_check)
	def send_qr(message):
		result = link_check(message)
		if result == "a":
			bot.reply_to(message, "Ich habe deinen Link erhalten. Ich erstelle dir nun einen QR-Code.")
			time.sleep(1)
			bot.send_photo(message.chat.id, "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + message.text)
		elif result == "b":
			bot.reply_to(message, "Ich habe den Befehl abgebrochen.")
		elif result == "c":
			bot.reply_to(message, "Das ist kein Link. Versuche es nochmal.")

#############################################################################################################



@bot.message_handler(commands=['stockspls'])
def define_stock(message):
	bot.reply_to(message,"Gib mr den Namen eines Unternehmens, das Kürzel oder die ISIN, und ich gebe dir den aktuellen Aktienkurs.")
	name = str(message.text).lower()

	def stock_check(name):
		stock = str(name.text).lower()
		if len(stock) == 10:
			real_stock = stock
			return real_stock
		else:
			pass

	@bot.message_handler(func=stock_check)
	def send_stock(name):
		final = stock_check(name)
		final_stock = yf.Ticker(final)
		data = final_stock.info
		print(data)




bot.infinity_polling()
