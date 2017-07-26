from difflib import SequenceMatcher

import vkapi
import commands
from command_system import command_list, required_fields, Response


user_orders = {}


def command_processor(user_id, moderator_id, token, command, text):
    user_data = user_orders.setdefault(user_id, {})
    if command == commands.Ready:
        for required_field, required_command in required_fields.items():
            if required_field not in user_data:
                return Response(required_command.required_msg, '', '')

        message = 'Поступил новый заказ от пользователя %s:\n\n%s' % (
            'https://vk.com/id%s' % user_id,
            '\n'.join(
                '%s: %s' % (
                    key,
                    ', '.join(value) if isinstance(value, list) else value
                ) for key, value in user_data.items()
            )
        )
        vkapi.send_message(moderator_id, token, message, '')

        del user_orders[user_id]

    response = command.process(text)
    if hasattr(command, 'field'):
        if hasattr(command, 'multiple') and command.multiple:
            user_data.setdefault(command.field, []).append(response.data)
        else:
            user_data[command.field] = response.data
    return response


def get_answer(user_id, moderator_id, token, body):
    ratio = 0
    text = ''
    command = None
    for c in command_list:
        ratios = []
        for key in c.keys:
            body_prefix = body[:len(key)].lower()
            body_suffix = body[len(key):]
            key_ratio = SequenceMatcher(None, body_prefix, key).ratio()
            ratios.append((key_ratio, body_suffix))
        max_ratio, max_ratio_text = max(ratios, key=lambda x: x[0])
        if max_ratio > ratio:
            ratio = max_ratio
            text = max_ratio_text
            command = c
    if ratio > 0.5:
        response = command_processor(user_id, moderator_id, token, command, text)
        return response.message, response.attachment
    message = "Введи 'меню' для вывода меню, 'заказ' для добавления товара в корзину, 'телефон' для указания номера телефона, 'адрес' для указания адреса и 'оформить' для оформления заказа"
    return message, ''


def create_answer(data, token, moderator_id):
    user_id = data['user_id']
    message, attachment = get_answer(user_id, moderator_id, token, data['body'])
    vkapi.send_message(user_id, token, message, attachment)
