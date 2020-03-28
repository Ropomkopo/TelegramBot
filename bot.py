#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
import telebot

bot = telebot.TeleBot('****************************')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(
        message.chat.id, 'Вибач, поки що розумію тільки кнопки')


bot.polling()
