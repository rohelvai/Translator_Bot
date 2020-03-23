from translator import *


def controller(message, user_id, name):
    try:
        if message is None:
            return "Sorry. Don't know what happened. 😔😔😔"
        elif message[0] == '/':
            if message[1:] == 'start':
                return welcome(user_id, name)
            elif message[1:] == 'cl':
                return current_language(user_id)
            elif message[1:8] == 'changed':
                return language_change(user_id, message[9:])
            elif message[1:] == 'swap':
                return swap_language(user_id)
            elif message[1:] == 'reset':
                return reset(user_id)
            elif message[1:] == 'languages':
                return supported_languages()
            elif message[1:] == 'help':
                return get_help(name)
            else:
                return "Sorry. 😔😔😔 Wrong Command. 😔😔😔\n\n Send /help to get help about usage."
        else:
            return translate(user_id, message)
    except:
        return "Sorry. 😔😔😔 \nDon\'t know what happened. 😔😔😔"
