import telebot
from os import environ

API_KEY = environ['TEL_API_KEY']

bot = telebot.TeleBot(API_KEY)


def get_starting_keyboard():
    starting_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    starting_keyboard.row('Major\'s Accredited Certification', 'Learning Resources')

    return starting_keyboard


def get_learning_resources_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('CS111 Python', 'CS112 Java')
    keyboard.row('SE 342 Software Architecture', 'SE 323 Modeling and Design')
    keyboard.row('Back to start!')
    return keyboard


def start_boolean(message):
    return message.text.lower() == 'back to start!'


@bot.message_handler(commands=['start'])
@bot.message_handler(func=start_boolean)
def start(message):
    keyboard = get_starting_keyboard()
    rsp = "Hi There!!"
    bot.send_message(message.chat.id, rsp, reply_markup=keyboard)


def certifications_boolean(message):
    return message.text.lower() == 'major\'s accredited certification'


@bot.message_handler(func=certifications_boolean)
def certifications(message):
    bot.send_message(message.chat.id, "To be added 😁")


def resources_boolean(message):
    return message.text.lower() == 'learning resources'


@bot.message_handler(func=resources_boolean)
def resources(message):
    keyboard = get_learning_resources_keyboard()
    bot.send_message(message.chat.id, "Here You go!", reply_markup=keyboard)


def python_resources_boolean(message):
    return message.text.lower() == 'cs111 python'


@bot.message_handler(func=python_resources_boolean)
def python_resources(message):
    resp = '''CS111 Python:

English:
        
https://youtu.be/_uQrJ0TkZlc

https://www.w3schools.com/python/

عربي:
https://satr.codes/paths/OTZExaETAH/view
    '''
    keyboard = get_learning_resources_keyboard()
    bot.send_message(message.chat.id, resp, reply_markup=keyboard)


def java_resources_boolean(message):
    return message.text.lower() == 'cs112 java'


@bot.message_handler(func=java_resources_boolean)
def java_resources(message):
    resp = '''CS112 Java:

https://youtu.be/eIrMbAQSU34

https://www.w3schools.com/java/
    '''
    keyboard = get_learning_resources_keyboard()
    bot.send_message(message.chat.id, resp, reply_markup=keyboard)


def soft_arch_resources_boolean(message):
    return message.text.lower() == 'se 342 software architecture'


@bot.message_handler(func=soft_arch_resources_boolean)
def soft_arch_resources(message):
    resp = '''SE 342 Software Architecture:

https://www.developertoarchitect.com/lessons/

https://www.w3schools.com/java/\n
'''
    keyboard = get_learning_resources_keyboard()
    bot.send_message(message.chat.id, resp, reply_markup=keyboard)


def modeling_resources_boolean(message):
    return message.text.lower() == 'se 323 modeling and design'


@bot.message_handler(func=modeling_resources_boolean)
def modeling_resources(message):
    resp = '''SE 323 Modeling and Design:

https://youtu.be/NU_1StN5Tkk
    '''
    keyboard = get_learning_resources_keyboard()
    bot.send_message(message.chat.id, resp, reply_markup=keyboard)


# For Administrators' Debugging
def message_id_boolean(message):
    return message.from_user.username.lower() == 'kasehomar'


@bot.message_handler(func=message_id_boolean)
def message_id(message):
    bot.reply_to(message, str(message.message_id))


bot.polling()
