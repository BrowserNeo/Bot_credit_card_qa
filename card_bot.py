# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='<<<INSERT TOKEN>>>'
, parse_mode='html') # создание бота

faker = Faker() # утилита для генерации номеров кредитных карт

# объект клавиаутры
card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)
# второй ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text=' \n юхууу... кого я вижу \n ...... ' + message.from_user.first_name + ' ' + message.from_user.last_name + ' !!!     🤝    привет!\n \n сгенерировать тебе номер тестовой банковской карты?\n \nВыбери тип:', # текст сообщения
        reply_markup=card_type_keybaord,
    )


# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):

    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    elif message.text == 'JCB':
        card_type = 'jcb'
    else:
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
        bot.send_message(
            chat_id=message.chat.id,
            text='Прости, но я не понимаю тебя :(',
        )
        return

    # card_type может принимать одно из зачений ['maestro', 'mastercard', 'visa13', 'visa16', 'visa19',
    # 'amex', 'discover', 'diners', 'jcb15', 'jcb16']
    card_number = faker.credit_card_number(card_type)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Готово! Тестовая карта {card_type}:'        
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=f'\n<code>{card_number}</code>'
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='\n ...обращайся еще, а то скучновато здесь одному...'
    )


# главная функция программы
def main():
    # запускаем бота
    bot.infinity_polling()


if __name__ == '__main__':
    main() 
    
   
