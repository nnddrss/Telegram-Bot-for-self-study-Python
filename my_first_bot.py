import telebot
from telebot import types
import sqlite3


bot = telebot.TeleBot('...', parse_mode=None) #instead of the ellipsis, enter the value of the bot token

@bot.message_handler(commands=['start','назад'])
def start_button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)   
    item1=types.KeyboardButton('Python')
    item2=types.KeyboardButton('Linux')
    item3=types.KeyboardButton('SQL')
    item4=types.KeyboardButton('Git')
    item5=types.KeyboardButton('Сайты с задачами, тренажеры')
    item6=types.KeyboardButton('Остальные полезные ресурсы')
    
    markup.add(item1, item2, item3)
    markup.add(item4, item5, item6)  
    
    bot.send_message(message.chat.id,'Выберите нужное',reply_markup=markup)
    

@bot.message_handler(content_types=['text'])
def start_button_message(message):
    if message.text == 'Python':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('Образовательные курсы. Python')
        item2=types.KeyboardButton('Книги по Python')
        item3=types.KeyboardButton('Python. Библиотеки, документация и т.д.')
        item4=types.KeyboardButton('/назад')
        
        markup.add(item1, item2)
        markup.add(item3, item4)
        
        bot.send_message(message.chat.id,'Выберите нужное',reply_markup=markup)
    
    
    elif message.text == 'Linux':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('Образовательные курсы. Linux')
        item2=types.KeyboardButton('Книги по Linux')
        item3=types.KeyboardButton('Linux. Библиотеки, документация и т.д.')
        item4=types.KeyboardButton('/назад')
        
        markup.add(item1, item2)
        markup.add(item3, item4)
        
        bot.send_message(message.chat.id,'Выберите нужное',reply_markup=markup)
    
    
    elif message.text == 'SQL':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('Образовательные курсы. SQL')
        item2=types.KeyboardButton('Книги по SQL')
        item3=types.KeyboardButton('SQL. Документация и т.д.')
        item4=types.KeyboardButton('/назад')
        
        markup.add(item1, item2)
        markup.add(item3, item4)
        
        bot.send_message(message.chat.id,'Выберите нужное',reply_markup=markup)
        
    
    elif message.text == 'Git':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('Образовательные курсы. Git')
        item2=types.KeyboardButton('Книги по Git')
        item3=types.KeyboardButton('Git. Документация и т.д.')
        item4=types.KeyboardButton('/назад')
        
        markup.add(item1, item2)
        markup.add(item3, item4)
        
        bot.send_message(message.chat.id,'Выберите нужное',reply_markup=markup)
        
            
    elif message.text == 'Сайты с задачами, тренажеры':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('codewars.com', url='https://www.codewars.com/dashboard'))
        markup.add(types.InlineKeyboardButton('Schoolw3.com', url='https://www.schoolsw3.com/python/exercise.php?filename=exercise_syntax1'))
        markup.add(types.InlineKeyboardButton('leetcode.com', url='https://leetcode.com/'))
        markup.add(types.InlineKeyboardButton('projecteuler.net', url='https://projecteuler.net/archives'))
        markup.add(types.InlineKeyboardButton('sql-academy.org', url='https://sql-academy.org/ru'))
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
    
    

    
    elif message.text == 'Остальные полезные ресурсы':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('НОУ ИНТУИТ', url='https://www.youtube.com/user/Intuitube/playlists'))
        markup.add(types.InlineKeyboardButton('Computer Science Center', url='https://www.youtube.com/c/CompscicenterRu/playlists'))
        markup.add(types.InlineKeyboardButton('Youtube-канал Разрабы', url='https://www.youtube.com/channel/UC-h5nFU9Qzo72dFW-fC_lkQ'))
        markup.add(types.InlineKeyboardButton('Бесплатные курсы от ЯП', url='https://practicum.yandex.ru/profile/backend-developer/'))
        
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
        
    elif message.text == 'Образовательные курсы. Python':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Selfedu', url='https://www.youtube.com/c/selfedu_rus/playlists'))
        markup.add(types.InlineKeyboardButton('Python программирование/Уроки для начинающих. Гоша Дударь ', url='https://www.youtube.com/watch?v=n0xtO0x81cg&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu'))
        markup.add(types.InlineKeyboardButton('Диджитализируй', url='https://www.youtube.com/c/%D0%94%D0%B8%D0%B4%D0%B6%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%B8%D1%80%D1%83%D0%B9/playlists'))
        markup.add(types.InlineKeyboardButton('PythonToday', url='https://www.youtube.com/c/PythonToday/playlists'))
        markup.add(types.InlineKeyboardButton('Олег Шпагин.Изучаем мир ИТ', url='https://www.youtube.com/channel/UCfxnN0xALQR6OtznIj35ypQ/playlists'))
        markup.add(types.InlineKeyboardButton('egoroff_channel', url='https://www.youtube.com/c/egoroffchannel/playlists'))
        markup.add(types.InlineKeyboardButton('Тимофей Хирьянов', url='https://www.youtube.com/c/%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B9%D0%A5%D0%B8%D1%80%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2/playlists'))
        markup.add(types.InlineKeyboardButton('Программирование. Создание игр, сайтов', url='https://www.youtube.com/channel/UC_aTa7Q7gFN5eaKKmGO8jXg/playlists'))
        markup.add(types.InlineKeyboardButton('Поколение Python": курс для начинающих. Stepic', url='https://stepik.org/course/58852/syllabus'))
        markup.add(types.InlineKeyboardButton('Уроки по Python для начинающих. PythonRu', url='https://pythonru.com/uroki/vvedenie-uroki-po-python-dlja-nachinajushhih'))
        markup.add(types.InlineKeyboardButton('Пишем ботов для Telegram на языке Python. MasterGroosha', url='https://mastergroosha.github.io/telegram-tutorial/'))
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
    
    elif message.text == 'Образовательные курсы. Linux':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Linux для Начинающих. Компьютерные секреты', url='https://www.youtube.com/watch?v=XvQVEVV46p4&list=PL874KddjzYd8d_A1mmUwxZ63MtJaSBXE1'))
        markup.add(types.InlineKeyboardButton('Linux для Начинающих. ADV-IT  ', url='https://www.youtube.com/watch?v=fAHpGshMCgQ&list=PLg5SS_4L6LYuE4z-3BgLYGkZrs-cF4Tep'))
        markup.add(types.InlineKeyboardButton('Уроки Linux для начинающих. Гоша Дударь', url='https://www.youtube.com/watch?v=fE1VG1gpXjU&list=PL0lO_mIqDDFUwVWvVitxG2oXA6a-Nq-Qq'))
        markup.add(types.InlineKeyboardButton('Основы командной строки. Хекслет', url='https://ru.hexlet.io/courses/cli-basics'))
        
                
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
    
    elif message.text == 'Образовательные курсы. SQL':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Практический курс по SQL для начинающих. EngineerSpock', url='https://www.youtube.com/watch?v=HVQNxdI6fqY&list=PLBheEHDcG7-k1Y_Uy04Dj2ylWhcfSfqoF'))
        markup.add(types.InlineKeyboardButton('Уроки SQL для начинающих. Гоша Дударь', url='https://www.youtube.com/watch?v=lapMmGGFS7k&list=PL0lO_mIqDDFVnLvR39VpEtphQ8bPJ-xR9'))
        markup.add(types.InlineKeyboardButton('Курс SQL Базы данных ORACLE. Prime Soft ', url='https://www.youtube.com/watch?v=Xktc0yHdQYw&list=PLv8UEsK35VB8ju8Vr9WeO71F7SCRofJis'))
        markup.add(types.InlineKeyboardButton('Базовый курс обучения SQL для начинающих. Максим Кухарь', url='https://www.youtube.com/watch?v=BYCU3XyKCzA&list=PLKl9v2TQvIkq4i_hZwZ1PmobxJSkIGwBf'))
        
                
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
    
    
    elif message.text == 'Образовательные курсы. Git':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Git для новичков. Loftblog', url='https://www.youtube.com/watch?v=PEKN8NtBDQ0&list=PLY4rE9dstrJyTdVJpv7FibSaXB4BHPInb'))
        markup.add(types.InlineKeyboardButton('Git и GitHub Курс Для Новичков. Владилен Минин', url='https://www.youtube.com/watch?v=zZBiln_2FhM&t=11s'))
        markup.add(types.InlineKeyboardButton('Git: курсJavaScript.ru', url='https://www.youtube.com/watch?v=W4hoc24K93E&list=PLDyvV36pndZFHXjXuwA_NywNrVQO0aQqb'))
        markup.add(types.InlineKeyboardButton('Уроки Git и GitHub. ITDoctor', url='https://www.youtube.com/watch?v=JdUzxh8miQw&list=PLuY6eeDuleIOMB2R_Kky05ZfiAx2_pbAH'))
        markup.add(types.InlineKeyboardButton('Введение в Git. Хекслет', url='https://ru.hexlet.io/courses/intro_to_git'))
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
        
    elif message.text == 'Книги по Python':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('(ru)Изучаем Питон. 4-е издание. Лутц', url='https://disk.yandex.ru/i/qaq4_ihgsAtG0Q'))
        markup.add(types.InlineKeyboardButton('(ru)Изучаем Питон. 5-е издание. Лутц', url='https://disk.yandex.ru/d/dExCTaz7ZxWyRg'))
        markup.add(types.InlineKeyboardButton('(ru)ООП в С. Lafore.R.', url='https://disk.yandex.ru/i/uaFm-17de3RGwQ'))
        markup.add(types.InlineKeyboardButton('(ru)Эффективное ООП. Лутц', url='https://disk.yandex.ru/i/BY_SjHPwYT5Sbg'))
        markup.add(types.InlineKeyboardButton('(ru)Программирование на Python для начинающих. Mike McGrath', url='https://disk.yandex.ru/i/0f6OH-jb06HKPw'))
        # markup.add(types.InlineKeyboardButton('', url=''))
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
    
    elif message.text == 'Книги по Linux':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('(en)Linux Pocket Guide. Daniel Barrett', url='https://disk.yandex.ru/i/vU1AcTWgVDzZFA'))
        markup.add(types.InlineKeyboardButton('(ru)Введение в Линукс. Гаррельс', url='https://disk.yandex.ru/i/VykiM6PtI6Atug'))
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
    
    elif message.text == 'Книги по SQL':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('(ru)SQL Полное руководство.3-е издание. Джеймс Грофф', url='https://disk.yandex.ru/i/Dh8aqDiMFEmUPg'))
        
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
    
    elif message.text == 'Книги по Git':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('(ru)Pro Git. Second edition. Scott Chacon', url='https://disk.yandex.ru/i/IoFLKrPJie6Vxg'))
        
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
        
    elif message.text == 'Python. Библиотеки, документация и т.д.':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('asyncio. Документация библиотеки', url='https://docs.python.org/3/library/asyncio.html'))
        markup.add(types.InlineKeyboardButton('aiogram. Документация библиотеки. Владилен Минин', url='https://docs.aiogram.dev/ru/latest/'))
        markup.add(types.InlineKeyboardButton('telebot. Документация библиотеки', url='https://pypi.org/project/pyTelegramBotAPI/'))
        markup.add(types.InlineKeyboardButton('Pandas. Документация библиотеки', url='https://pandas.pydata.org/docs/index.html'))
        markup.add(types.InlineKeyboardButton('NumPy. Документация библиотеки', url='https://numpy.org/doc/'))
        markup.add(types.InlineKeyboardButton('Pytest. Документация библиотеки', url='https://docs.pytest.org/en/7.1.x/contents.html'))
                
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        

    elif message.text == 'Linux. Библиотеки, документация и т.д.':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Пользовательская документация Ubuntu', url='https://help.ubuntu.ru/wiki/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F'))
                        
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
        
        
    elif message.text == 'SQL. Документация и т.д.':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Памятка/шпаргалка по SQL. Публикация из Хабр', url='https://habr.com/ru/post/564390/'))
        
                
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
    
    
    elif message.text == 'Git. Документация и т.д.':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Git. Документация', url='https://git-scm.com/book/ru/v2'))
        
                
        
        bot.send_message(message.chat.id,'Выберите...', reply_markup=markup)
    

bot.polling(none_stop=True, interval=0)