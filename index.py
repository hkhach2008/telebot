import telebot
import pandas as pd
import time
import os

bot = telebot.TeleBot('5533441609:AAHb3RQe3WPynitgDfDFvNtZ2c_D7devVoA')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello {message.from_user.first_name} {message.from_user.last_name}\n<b>sent me your data</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
@bot.message_handler(content_types=['document'])
def get_user_doc(message):
    bot.send_message(message.chat.id, 'Wait for answer')
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    milliseconds = int(round(time.time() * 1000))
    file_extension = os.path.splitext(message.document.file_name)[1]
    src = './files/data/' + str(milliseconds) + file_extension
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    list1 = []
    list2 = []
    list3 = []
    with open(src, 'r') as file:
      res = file.readlines()
    for i in range(0, len(res)):
      res[i] = res[i].replace('\n', '')
      res[i] = res[i].split(' - ')
    for i in range(len(res)):
        list1.append(res[i][0])
        list2.append(res[i][1])
        list3.append(res[i][2])

    df = pd.DataFrame({'name': list1,
                    'surname': list2,
                    'count': list3})
    df.to_excel('./files/excel/grqi_goxy_gox_chi.xlsx')
    fl = open('./files/excel/grqi_goxy_gox_chi.xlsx', 'rb')
    bot.send_document(message.chat.id, fl)

bot.polling()