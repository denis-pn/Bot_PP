
# -*- codecs: utf-8 -*-
import codecs
import telebot
import time
import fitz
import cv2
import pytesseract
import os

bot = telebot.TeleBot('1485841901:AAG-lVov-IBdK0mCm-CmqTg6kv3nfCZDBpI')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Помощь по документам и бланкам', 'Выяснение причин отказа и проблем с заявлениями')


keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard4.row('Бланк аренды земли', 'Бланк аренды квартиры', 'Бланк аренды нежилого помещения', "Назад")

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message.from_user.username, message.text)
    bot.send_message(message.chat.id, 'Здравствуйте, я помогу вам в ваших правовых вопросах, вы можете запросить бланки для заполнения, задать интересующий вас вопрос или приложить скан документа, по которому имеются у вас вопросы', reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        a = message.text.lower()
        text = a.split()
        print(text)
        f = codecs.open("C:\zhaba.txt", "r", "utf-8")
        fd = f.readlines(0)
        hash_ = 0
        hash = []
        i_1 = 0
        # print("1")
        while i_1 != len(fd):
            list1 = fd[i_1].split()

            i = 0
            while i != len(text) and hash_ == 0:
                if len(list1) == 1:
                    if text[i].lower() == list1[0]:
                        hash.append("Жалоба на Росреестр")
                        hash_ = 1
                if i + 1 != len(text) and len(list1) == 2:
                    if text[i].lower() == list1[0] and text[i + 1].lower() == list1[1]:
                        hash.append("Жалоба на Росреестр")
                        hash_ = 1
                i += 1
            i_1 += 1

        if hash_ == 1:
            bot.send_message(message.from_user.id, "Ваше сообщение расценено как жалоба на Росреестр, при наличии у вас ответа от Росрииестра, приложите данный документ")




        if message.text == "Помощь по документам и бланкам":
            bot.send_message(message.from_user.id, "Чем я могу вам помочь?")

        elif message.text == "Выяснение причин отказа и проблем с заявлениями":
            bot.send_message(message.from_user.id, "Укажите суть вашей проблемы или приложите скан уведомления?")



        # print(message.from_user.username, message.text)

        a = message.text.lower()

        text = a.split()
        f0 = codecs.open("C:\Pbaza\список.txt", "r", "utf-8")
        fd0 = f0.readlines(0)
        i_1 = 0
        doc = []
        text_ = []
        while i_1 != len(fd0) and len(doc) == 0:

            list0 = fd0[i_1].split()
            # print(list0)
            i_2 = 1
            ver = 0
            i = 0
            while i_2 != len(list0):
                # print(list0[i_2])
                i=0
                while i != len(text):
                    if text[i].lower() == list0[i_2]:
                        # print(text[i])
                        ver += 1
                    i += 1
                    # print(ver)
                if ver == (len(list0)-1):
                    doc.append(list0[0])
                    f_ = codecs.open("C:\Pbaza\{0}.txt".format(doc[0]), "r", "utf-8")
                    fd_ = f_.readlines()

                    if doc[0] == "4":
                        bot.send_message(message.chat.id, ' '.join(fd_), reply_markup=keyboard4)

                    else:

                        bot.send_message(message.chat.id, ' '.join(fd_))

                i_2 += 1
            i_1 += 1

        if message.text == "Бланк аренды земли":
            doc = open('C:/Аренда_земли.doc', 'rb')
            bot.send_document(message.from_user.id, doc)
            bot.send_document(message.from_user.id, "FILEID")
        elif message.text == "Бланк аренды квартиры":
            doc = open('C:/Аренда_квартиры.doc', 'rb')
            bot.send_document(message.from_user.id, doc)
            bot.send_document(message.from_user.id, "FILEID")
        elif message.text == "Бланк аренды нежилого помещения":
            doc = open('C:/Аренда_нежилого.doc', 'rb')
            bot.send_document(message.from_user.id, doc)
            bot.send_document(message.from_user.id, "FILEID")
        elif message.text.lower() == "назад":
            t = 0
            start_message(message)




        text = a.split()
        f0 = codecs.open("C:\helper\список.txt", "r", "utf-8")
        fd0 = f0.readlines(0)
        help_ = 0
        i_1 = 0
        doc = []
        text_ = []
        list0 = 0
        while i_1 != len(fd0):
            ver = 0

            list0 = fd0[i_1].split()
            print(list0)
            # print(list0)
            i_2 = 1
            ver = 0
            i = 0
            while i_2 != len(list0):
                # print(list0[i_2])
                i=0

                while i != len(text):
                    if text[i].lower() == list0[i_2]:
                        print(text[i],list0[i_2] )
                        # print(text[i])
                        ver += 1
                    i += 1

                    print(ver)

                print(len(list0))
                if ver == (len(list0)-1) and help_ == 0:
                    print("1111111111111")
                    f_ = codecs.open("C:\helper\{0}.txt".format(list0[0]), "r", "utf-8")
                    help_ = 1
                    fd_ = f_.readlines()
                    bot.send_message(message.chat.id, ' '.join(fd_))

                i_2 += 1
            i_1 += 1
        print("rjytw")



    except Exception as e:
        time.sleep(3)
        print(e)

@bot.message_handler(content_types=['document'])
def handle_file(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'C:/test/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        extension = 'C:/test/{0}'.format(message.document.file_name).split('.')[-1]
        print(extension)
        textik = []
        if extension == "pdf":
            # print("1111")
            pdf_document = fitz.open("C:/test/%s" % (message.document.file_name))
            for current_page in range(len(pdf_document)):
                for image in pdf_document.getPageImageList(current_page):
                    xref = image[0]
                    pix = fitz.Pixmap(pdf_document, xref)
                    if pix.n < 5:  # this is GRAY or RGB
                        pix.writePNG("C:/test/page%s-%s.png" % (current_page, xref))
                        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                        img = cv2.imread("C:/test/page%s-%s.png" % (current_page, xref))
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        config = r'--oem 3 --psm 6'
                        textik.append(pytesseract.image_to_string(img, lang='rus', config=config))
                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "C:/test/page%s-%s.png" % (current_page, xref))
                        os.remove(path)


                    else:  # CMYK: convert to RGB first
                        pix1 = fitz.Pixmap(fitz.csRGB, pix)
                        pix1.writePNG("C:/test/page%s-%s.png" % (current_page, xref))
                        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                        img = cv2.imread("C:/test/page%s-%s.png" % (current_page, xref))
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        config = r'--oem 3 --psm 6'
                        textik.append(pytesseract.image_to_string(img, lang='rus', config=config))
                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                            "C:/test/page%s-%s.png" % (current_page, xref))
                        os.remove(path)
                        pix1 = None
                    pix = None

        elif extension == "png":
            src = 'C:/test/12.png';
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)


            # os.rename('{0}', '12.png'.format(message.document.file_name))
            pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

            # img = cv2.imread("C:/test/Обращение.png")
            img = cv2.imread('C:/test/12.png')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            config = r'--oem 3 --psm 6'
            textik.append(pytesseract.image_to_string(img, lang='rus', config=config))
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                "C:/test/12.png")
            os.remove(path)


        print(len(textik))
        i111 = 0
        while i111 != len(textik):
            text = textik[i111].split()

            try:
                f = codecs.open("C:\zhaba.txt", "r", "utf-8")
                fd = f.readlines(0)
                hash_ = 0
                hash = []
                i_1 = 0
                # print("1")
                while i_1 != len(fd):
                    list1 = fd[i_1].split()

                    i = 0
                    while i != len(text) and hash_ == 0:
                        if len(list1) == 1:
                            if text[i] == list1[0]:
                                hash.append("Жалоба на Росреестр")
                                hash_ = 1
                        if i + 1 != len(text) and len(list1) == 2:
                            if text[i] == list1[0] and text[i + 1] == list1[1]:
                                hash.append("Жалоба на Росреестр")
                                hash_ = 1
                        i += 1
                    i_1 += 1

                if hash_ == 1:
                    bot.send_message(message.from_user.id, "Ваше сообщение расценено как жалоба на Росреестр, при наличии у вас ответа от Росрииестра, приложите данный документ")

                if message.text == "Помощь по документам и бланкам":
                    bot.send_message(message.from_user.id, "Чем я могу вам помочь?")

                elif message.text == "Выяснение причин отказа и проблем с заявлениями":
                    bot.send_message(message.from_user.id,
                                     "Укажите суть вашей проблемы или приложите скан уведомления?")

                print(message.from_user.username, message.text)

                f0 = codecs.open("C:\Pbaza\список.txt", "r", "utf-8")
                fd0 = f0.readlines(0)
                i_1 = 0
                doc = []
                text_ = []
                while i_1 != len(fd0) and len(doc) == 0:

                    list0 = fd0[i_1].split()
                    # print(list0)
                    i_2 = 1
                    ver = 0
                    i = 0
                    while i_2 != len(list0):
                        # print(list0[i_2])
                        i = 0
                        while i != len(text):
                            if text[i] == list0[i_2]:
                                # print(text[i])
                                ver += 1
                            i += 1
                            # print(ver)
                        if ver == (len(list0) - 1):
                            doc.append(list0[0])
                            f_ = codecs.open("C:\Pbaza\{0}.txt".format(doc[0]), "r", "utf-8")
                            fd_ = f_.readlines()

                            if doc[0] == "4":
                                bot.send_message(message.chat.id, ' '.join(fd_), reply_markup=keyboard4)

                            else:

                                bot.send_message(message.chat.id, ' '.join(fd_))

                        i_2 += 1
                    i_1 += 1

                if message.text == "Бланк аренды земли":
                    doc = open('C:/Аренда_земли.doc', 'rb')
                    bot.send_document(message.from_user.id, doc)
                    bot.send_document(message.from_user.id, "FILEID")
                elif message.text == "Бланк аренды квартиры":
                    doc = open('C:/Аренда_квартиры.doc', 'rb')
                    bot.send_document(message.from_user.id, doc)
                    bot.send_document(message.from_user.id, "FILEID")
                elif message.text == "Бланк аренды нежилого помещения":
                    doc = open('C:/Аренда_нежилого.doc', 'rb')
                    bot.send_document(message.from_user.id, doc)
                    bot.send_document(message.from_user.id, "FILEID")
                elif message.text == "Назад":
                    t = 0
                    start_message(message)


            except Exception as e:
                time.sleep(3)
                print(e)

            i111 += 1







    except Exception as e:
        print(e)
        # bot.reply_to(message, e)

bot.polling()