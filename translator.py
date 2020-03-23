import requests
import dic
from googletrans import Translator


# Filing _ START
f1 = open('user.txt', 'r')
f2 = open('src.txt', 'r')
f3 = open('dest.txt', 'r')
f4 = open('langList.txt', 'r')
user = f1.read().split()
src = f2.read().split()
dest = f3.read().split()
langList = f4.read()
f1.close()
f2.close()
f3.close()
f4.close()
# Filing _ END


# File Modify Function _ START
def filing():
    f1 = open('user.txt', 'w')
    f2 = open('src.txt', 'w')
    f3 = open('dest.txt', 'w')
    for item in user:
        f1.write("%s\n" % item)
    for item in src:
        f2.write("%s\n" % item)
    for item in dest:
        f3.write("%s\n" % item)
    f1.close()
    f2.close()
    f3.close()
# File Modify Function _ END


# Encoding Function _ START
def encode(text):
    text = text.title()
    if text == 'Bangla':
        return 'bn'
    for name, code in dic.dic.items():
        if name == text:
            return code
    else:
        return 'wrong'
# Encoding Function _ END


# Encoding Function _ START
def decode(text):
    if text == 'auto':
        return 'Any (Auto Detect)'
    for name, code in dic.dic.items():
        if code == text:
            return name
# Encoding Function _ END


# Translating Function _ START
def translator(text, index):
    if src[index] == 'auto':
        return Translator().translate(text, dest[index]).text
    else:
        return Translator().translate(text, dest[index], src[index]).text
# Translating Function _ END


# Commands _ START
def welcome(user_id, name):
    user_id = str(user_id)
    message = 'Hi, {name}. 😉😉😉 \n\nWelcome to TranslatorBot.\n\n' \
                  'Send any sentence to translate.\n\n' \
                  'Send /admin to chat with admin.\n' \
                  'Send /help to get help.\n' \
                  '\n\n\n' \
                  'A translator bot by Rohel (V--1.0.0).\n\n' \
                  '--------------------\n' \
                  'Admin --> Rohel\n' \
                  'Creator --> Rohel\n--------------------\n\n' \
                  'Contact ::->\n' \
                  '--> FB: http://facebook.com/null.rohel/\n' \
                  '--> Telegram: http://t.me/nullrohel\n' \
                  '' \
                  '\nBest of luck. Any feedback is much appreciated.'.format(name=name)

    if user_id not in user:
        user.append(user_id)
        src.append('auto')
        dest.append('en')
        filing()

    return message + '\n\n\nCurrent translation: \n\n' + 'From: %s\nTo: %s' \
           % (decode(src[user.index(str(user_id))]), decode(dest[user.index(str(user_id))]))


def current_language(user_id):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    return 'Current translation: \n\n' + 'From: %s\nTo: %s' \
           % (decode(src[user.index(str(user_id))]), decode(dest[user.index(str(user_id))]))


def language_change(user_id, message):
    if user_id in user:
        try:
            message = message.split('-')
            print(message)

            if encode(message[0]) != 'wrong' and encode(message[1]) != 'auto' and encode(message[1]) != 'wrong':
                src[user.index(str(user_id))] = encode(message[0])
                dest[user.index(str(user_id))] = encode(message[1])
                text = "Success! 😍😍😍"
                filing()
            else:
                text = 'Sorry. 😔😔😔 Check format and supported languages.' \
                       '(Auto detect can\'t be destination language)'
            return text + '\n\nCurrent translation: \n\n' + 'From: %s\nTo: %s' \
                   % (decode(src[user.index(str(user_id))]), decode(dest[user.index(str(user_id))]))
        except Exception as e:
            print(e)
            return "Sorry. 😔😔😔 Something wrong happened.\n" \
                   "Try sending /start once more or " \
                   "check format and supported languages."
    else:
        return 'Sorry. 😔😔😔\nTry sending /start once more.'


def swap_language(user_id):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    try:
        if src[user.index(str(user_id))] == 'auto':
            return 'Sorry. Language swap not possible. Auto detect can\'t be selected as destination language.'
        temp = src[user.index(str(user_id))]
        src[user.index(str(user_id))] = dest[user.index(str(user_id))]
        dest[user.index(str(user_id))] = temp
        filing()
        return 'Success! 😍😍😍\n\nCurrent translation: \n\n' \
               'From: %s\nTo: %s' % (decode(src[user.index(str(user_id))]),
                                     decode(dest[user.index(str(user_id))]))
    except:
        return 'Sorry. 😔😔😔 Something isn\'t right.' \
               'Try sending /start once more.'


def reset(user_id):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    try:
        src[user.index(str(user_id))] = 'auto'
        dest[user.index(str(user_id))] = 'en'
        filing()
        return 'Success! 😍😍😍\n\nCurrent translation: \n\n\n' \
               'From: %s\nTo: %s' % (decode(src[user.index(str(user_id))]),
                                     decode(dest[user.index(str(user_id))]))
    except:
        return 'Sorry. 😔😔😔 Something isn\'t right.' \
               'Try sending /start once more.'


def supported_languages():
    return langList


def get_help(name):
    return 'Welcome {name}. 😍😍😍\n\n' \
           'Send \'/admin\' to chat with admin.\n' \
           'Send \'/cl\' to get current translation languages.\n' \
           'Send \'/languages\' to see total supported languages.\n' \
           'Send \'/swipe\' to swipe current languages.\n' \
           'Send \'/reset\' to set auto as source language and ' \
           'English as destination Language.\n' \
           'Send \'/changed FromLanguage-ToLanguage\'\n' \
           'Example: To translate english to bangla, simply send,\n\n' \
           '/changed english-bangla\n\n' \
           'To auto detect your language, send \'auto\' as source/FromLanguage.\n\n' \
           'A translator bot by Rohel (V--1.0.0).\n\n' \
           '--------------------\n' \
           'Admin --> Rohel\n' \
           'Creator --> Rohel\n--------------------\n\n' \
           'For further help, contact me:\n\n' \
           '--> FB: http://facebook.com/null.rohel/\n' \
           '--> Telegram: http://t.me/nullrohel\n' \
           '' \
           '\n\nBest of luck. Any feedback is much appreciated.'.format(name=name)
# Commands _ END


def translate(user_id, message):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    try:
        return translator(message, user.index(str(user_id)))
    except:
        return 'Sorry. 😔😔😔 Something isn\'t right.' \
               'Try sending /start once more or change languages or reset languages by sending /reset.'
