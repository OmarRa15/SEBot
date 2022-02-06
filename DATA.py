import telebot
from os import environ
API_KEY = environ['TEL_API_KEY']

bot = telebot.TeleBot(API_KEY)
