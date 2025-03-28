# from telebot import TeleBot, types
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message, Chat
# from test import TOKEN
#
# bot = TeleBot(TOKEN)
# file_path = 'C:/Users/Anaconda/PycharmProjects/Zerocoder/dist/listbox_contents.txt'  # указываем файл с данными и путь
# bot.state = {}  # Инициализация состояния
#
# def load_file():  # загружает значения из файла listbox_contents.txt
#     if file_path:  # если он корректно указан
#         list_box = []  # создаем список перед загрузкой нового содержимого
#         with open(file_path, 'r', encoding='cp1251', errors='ignore') as file:  # Открываем файл и читаем его содержимое
#             for line in file:
#                 list_box.append(line.strip())  # Добавляем строку в Listbox
#     return list_box  # возвращаем заполненный из файла список
#
# def save_file(items):  # Функция для сохранения списка в файл
#     with open(file_path, 'w', encoding='cp1251') as file:
#         for item in items:
#             file.write(item + '\n')  # Записываем каждый элемент в новую строку
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     items = load_file()  # присваиваем переменной список, загруженный из файла
#     bot.reply_to(message, 'Привет! Я ТГ-бот, я буду помогать тебе с твоими задачами и целями! \nУдалять выполненные и ставить новые')
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("Добавить задачу"))  # Добавляем кнопку для добавления новой задачи
#     for item in items:  # перебор элементов списка
#         markup.add(KeyboardButton(item))  # создаются кнопки в виде элементов списка
#     bot.send_message(message.chat.id, "Выберите решенную задачу и ее можно будет удалить. Либо добавьте новую:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     items = load_file()  # присваиваем переменной список, загруженный из файла
#
#     if message.text in items:  # Если выбрана задача для удаления
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
#         bot.send_message(message.chat.id, f'Вы выбрали: {message.text}. Вы уверены, что хотите удалить эту задачу?',
#                          reply_markup=markup)
#         bot.last_selected_item = message.text  # Сохраняем выбранный ответ в атрибуте
#
#     elif message.text == "Да":  # если выбрал по кнопке ДА - удаляем из списка
#         if hasattr(bot, 'last_selected_item'):  # если мы получили в бот атрибут 'last_selected_item'
#             item_to_remove = bot.last_selected_item
#             items.remove(item_to_remove)
#             bot.send_message(message.chat.id, f'Была удалена задача: "{item_to_remove}".')
#             del bot.last_selected_item
#             save_file(items)  # Сохраняем изменения в файл
#             send_welcome(message)  # Обновляем список задач в боте
#
#     elif message.text == "Добавить задачу":  # Обработка нажатия кнопки "Добавить задачу"
#         bot.send_message(message.chat.id, "Введите описание новой задачи:")
#         bot.state[message.from_user.id] = "waiting_for_task"  # Устанавливаем состояние ожидания новой задачи
#
#     elif message.from_user.id in bot.state and bot.state[message.from_user.id] == "waiting_for_task":
#         new_task = message.text
#         items.append(new_task)  # Добавляем новую задачу в список
#         save_file(items)  # Сохраняем изменения в файл
#         bot.send_message(message.chat.id, f'Задача "{new_task}" добавлена.')  # Подтверждение добавления
#         del bot.state[message.from_user.id]  # Удаляем состояние после добавления
#
# # Не забудьте добавить обработчик для запуска бота
# bot.polling()


# @bot.message_handler(func=lambda message: True)
# def handle_message(message): # message.text: Досмотреть видео по Jango - то что выбрал тользователь с виртуальной клавиатуры
#     items = load_file()  # присваеваем пременной список, загруженый из файла
#     print('message.text:',message.text)
#     print('items:', items)
#     if message.text in items: # например:   items: ['Досмотреть видео по Jango', 'Посмотреть книгу по Jango', 'Сделать Anki по Tkinter', 'Посмотреть допзанятие по парсингу и Pandas', 'Посмотреть видео о Linux и парсингу']
#         # Запрашиваем подтверждение удаления, создается клавиатура ДА - НЕТ на месте предидущей клавы
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
#         bot.send_message(message.chat.id, f'Вы выбрали: {message.text}. Вы уверены, что хотите удалить эту задачу?',
#                          reply_markup=markup)
#
#         # Сохраняем выбранный ответ в атрибуте для дальнейшего использования
#         bot.last_selected_item = message.text # message.text: Досмотреть видео по Jango - то что выбрал тользователь с виртуальной клавиатуры
#     elif message.text == "Да": # если он выбрал ДА - удаляем из списка
#         if hasattr(bot, 'last_selected_item'): # если мы получили в бот атрибут 'last_selected_item'
#             item_to_remove = bot.last_selected_item # присваеваем его имя пременной
#             items.remove(item_to_remove) # и удаляем этот элемент из списка items
#             bot.send_message(message.chat.id, f'Была удалена задача: "{item_to_remove}".') # оптавляем об этом информацию в чат-бот
#             del bot.last_selected_item  # Удаляем после этого и сам атрибут после использования, очишаеи поле атрибуда для дальнейшей работы
#             send_welcome(message)  # Обновляем список задач в боте через сообщение
#             print('message:', message)
#
#             with open(file_path, 'w', encoding='cp1251') as file:
#                 for item in items:
#                     file.write(item + '\n')  # Записываем каждый элемент в новую строку
#
#         else: # если атрибут отсутствует - отправляем в чат сообщение:
#             bot.send_message(message.chat.id, 'Нет выбранной задачи для удаления.')
#     elif message.text == "Нет": # если он выбрал НЕТ - отправляем в чат сообщение:
#         bot.send_message(message.chat.id, 'Удаление отменено.')
#     else: # в остальных случаях - отправляем в чат сообщение:
#         bot.send_message(message.chat.id, 'Пожалуйста, выберите задачу из списка для удаления.')
#         send_welcome(message) # Вызываем обработчик для отправки "/start" в чат-бот (авто-обновления списка задач)
