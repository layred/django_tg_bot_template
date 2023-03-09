# Пропишите markup клавиатур для ботов здесь
from telebot.types import (InlineKeyboardButton, InlineKeyboardMarkup,  # noqa
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


class Markups:

    def __init__(self) -> None:
        pass

    def _remove(self):
        return ReplyKeyboardRemove()

    def register(self) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(KeyboardButton('👤 Отправить контакт 👤', request_contact=True))
        return markup

    def welcome(self) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(KeyboardButton('Меню'))
        return markup
