import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import bot_callback
from keyboards.inline.choice_buttons import choice, choice1, helpME, menu, TicketMenu, Check_list, Ticket_filling, \
    AmIHelpedYou, ForMembers, ForMembers1, Ticket_filling1, Autumn, Autumn1, Autumn2, ForMembers2, Spring,  \
    program, prog_lang
from loader import dp

'''___________________________________________________________
Реакция на команду "/start"
'''


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text='''Привет! Меня зовут Роберт и я помогу Вам узнать, что такое международная мобильность в ВШЭ.
\nУже что-то знаете про мобильность?''', reply_markup=choice)

'''___________________________________________________________
Сценарий 4: "Викторина" 
'''


@dp.callback_query_handler(bot_callback.filter(action='yes'))
async def push_yes(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Отлично! Есть ли у Вас вопросы по теме международной мобильности?', reply_markup=choice1)
    callback_data = call.data

    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='no'))
async def push_no(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Хорошо. Держите ссылку для ознакомления с ней!\n
Если я понадоблюсь Вам в следующий раз, нажмите на кнопку\nhttps://www.youtube.com/watch?v=HJ0xBYo6hbs''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='net'))
async def push_no(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Хорошо. Нажмите на кнопку ниже, если я Вам вдруг понадоблюсь! :)', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='da'))
async def push_yes(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Напишите команду "faq"(/faq), чтобы посмотеть ответы на частозадаваемые вопросы.\n
Если же вашего вопроса не оказалось в данной базе ответов, напишите ваш вопрос на почту ЦМСМ(studyabroad@hse.ru)\n
Когда я понадоблюсь Вам в следующий раз, нажмите на кнопку ниже''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")



'''___________________________________________________________
Сценарий 1: узнать список документов для подачи заявки на мобильность
'''


@dp.callback_query_handler(bot_callback.filter(action='3'))
async def on_thr_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Напишите команду "faq"(/faq), чтобы посмотеть ответы на частозадаваемые вопросы.\n
Если же вашего вопроса не оказалось в данной базе ответов, напишите ваш вопрос на почту ЦМСМ(studyabroad@hse.ru)\n
Когда я понадоблюсь Вам в следующий раз, нажмите на кнопку ниже''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='1'))
async def on_fr_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''1. Посмотреть гайд\n2. Список документов\n3. Составление ИУП\n4. Назад''', reply_markup=TicketMenu)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='guide'))
async def guide(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''В этом гайде ты узнаешь, как подать заявку на Международную мобильность в НИУ ВШЭ
\nhttps://www.youtube.com/watch?v=zEwqrW81nKk
\nМогу помочь Вам заполнить заявку поэтапно! Нажмите на один из вариантов ответа ниже ''', reply_markup=Check_list)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='doc_list'))
async def document_list(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Вот, держи список документов нужных для подачи заявки на международную мобильность! 
- Заявленине на конкурс
- Смета планируемых расходов
- Мотивационное письмо на английском языке
- Специальный ИУП
- Подтверждение уровня языка(например, TOEFL/IELTS)
- Рекомендательное письмо на английском языке в свободной форме (опционально)
Для получения более точной информации Вы можете ознакомиться с информацией на сайте:https://studyabroad.hse.ru/documents''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='fo'))
async def on_fo_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='ISP'))
async def ISP(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Для того, чтобы составить ИУП на поездку в зарубежный ВУЗ вам необходимо:
\n1) Посмотреть на сайте зарубежного ВУЗа предметы, которые соответствуют выбранным Вами учебным дисциплинам на период вашей мобильности
\n2) Составить список предметов и обратиться к менеджеру учебной программы для составления ИУП (https://studyabroad.hse.ru/mirror/pubs/share/445159084)
\n3) Получить одобрение специального ИУПа от Академического руководителя образовательной программы
Расскажите, помогла ли Вам данная информация?(кнопки ниже)''', reply_markup=AmIHelpedYou)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='yyr'))
async def YouHelpedMe(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text="Спасибо за ответ! Если Вам будет нужна моя помощь, нажмите на кнопку ниже", reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='nyrn'))
async def YouRNHelpedMe(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text="Спасибо за ответ! Если Вам будет нужна моя помощь, нажмите на кнопку ниже", reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='yft'))
async def FillingTicket(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Первое, что вам необходимо сделать - подготовить все документы.
\nИх список можете посмотеть, пройдя по пути "Главное меню" -> "Подать заявку" -> "Список документов"
\nНажмите на кнопку "Я сделал", когда этап будет пройден или "Главное меню", чтобы вызвать главное меню''', reply_markup=Ticket_filling)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='nft'))
async def WithoutFillingTicket(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text="Когда я понадоблюсь Вам в следующий раз, нажмите на эту кнопку", reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")

'''___________________________________________________________
Помощь в заполнении заявки
'''


@dp.callback_query_handler(bot_callback.filter(action='tido'))
async def ticket_document(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''После того, как Вы собрали все документы, Вам необходимо заполнить заявку на мобильность
\nДля её заполнения можете воспользоваться подсказкой:
\nhttp://surl.li/aovfn''', reply_markup=Ticket_filling1)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='toLMS'))
async def to_LMS(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Последний шаг: вам необходимо отправить свою заявку в Ваш LMS.
\n Ссылка на LMS: https://lms.hse.ru/
\nНажмите кнопку, чтобы вызвать главное меню''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")

'''___________________________________________________________
Сценарий 6
'''


@dp.callback_query_handler(bot_callback.filter(action='4'))
async def on_fo_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text="Что бы Вы хотели узнать?", reply_markup=ForMembers)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='check'))
async def chek_list(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Отъезжая на мобильноссть, первое, что Вам будет необходимо сделать - заполнить чек-лист
Выберите сезон, в который Вы собираетесь поехать на Международную мобильность:''', reply_markup=ForMembers1)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='delay'))
async def on_fr_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='''Перенос мобильности можно совершить, если Вы по какой-то причине не можете поехать на мобильность в данный момент.\n
Перенос можно оформить только один раз.\nЕсли вы решили перенести мобильность:
1) Согласуйте возможность переноса с учебным офисом Вашей программы
2) Свяжитесь с ЦМСМ для согласования условий переноса мобильности (необходимо предоставить согласование от учебного офиса о возможности переноса)
3) Ожидайте ответ от ЦМСМ. Он согласует перенос с университетом-партнером и ответит Вам.\nЕсли Вам понадобится моя помощь, нажмите на кнопку ниже''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='autumn'))
async def if_autumn(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='''А вот и чек-лист для осенней мобильности! Кстати, еще вам необходимо посетить ориентационную сессию!
Это обязательно необходимо сделать с 20 по 30 апреля.
     https://studyabroad.hse.ru/mirror/pubs/share/438382746.pdf''', reply_markup=Autumn)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='atmNext'))
async def if_autumn1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text="Как Вы учавствуете в мобильности? Выбирете вариант ниже", reply_markup=Autumn1)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='atmOn'))
async def if_autumn2(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''За две недели до начала обучения Вам будет необходимо предоставить в учебный офис ряд документов:
1) Заявление на мобильность с пометкой, что Вы учавствуете в программе онлайн(Заявление: https://studyabroad.hse.ru/mirror/pubs/share/495275937
Как его заполнить:https://studyabroad.hse.ru/mirror/pubs/share/437447099)
2) Письмо-приглашение от вуза-партнера
3) ИУП на период мобильности, который Вы составляете с учебным офисом(конкретнее можете прочитать про составление ИУП, нажав на кнопку ниже) 
4) На почту Цента международной студенческой мобильности (studyabroad@hse.ru) не обходмо прислать решение по формату обучения в принимающем университете''',
reply_markup=Autumn2)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='PoIS'))
async def ISP(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='''Для того, чтобы составить ИУП на поездку в зарубежный ВУЗ вам необходимо:
\n1) Посмотреть на сайте зарубежного ВУЗа предметы, которые соответствуют выбранным Вами учебным дисциплинам на период вашей мобильности
\n2) Составить список предметов и обратиться к менеджеру учебной программы для составления ИУП (https://studyabroad.hse.ru/mirror/pubs/share/445159084)
\n3) Получить одобрение специального ИУПа от Академического руководителя образовательной программы''', reply_markup=ForMembers2)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='atmOf'))
async def ISP(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Не меннее, чем за четыре недели до выезда Вам необходимо предоставить в учебный офис:
1) Заявляение на исходящую мобильность с физическим выездом(Заявление: https://studyabroad.hse.ru/mirror/pubs/share/495275917
Как его заполнить: https://studyabroad.hse.ru/mirror/pubs/share/437447147)
2) Согласие студента на осуществление мобильности(Заявляение: https://studyabroad.hse.ru/mirror/pubs/share/440221939
Как его заполнить: https://studyabroad.hse.ru/mirror/pubs/share/437447166)
3) Приглашение от принимающего университета
4) ИУП на период мобильности(подробнее можно узнать, нажав на кнопочку ниже)
5) На почту Цента международной студенческой мобильности (studyabroad@hse.ru) не обходмо прислать решение по формату обучения в принимающем университете,
а так же согласие студента на осуществление мобильности(документ и его заполнение в пункте 2)''', reply_markup=Autumn2)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='atmF'))
async def for_members2(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='''Следующие шаги:
1) Пройти регистрационные процедуры в принимающем вузе.
Информацию о принимающих процедурах можно получить:
    - Из переписки с принимающим вузом;
    - У координатора принимающего вуза
    - из факт-листа принимающего университета(универ можно найти тут: https://studyabroad.hse.ru/catalogue/)
    - воспользовавшись поиском в Интернете

2) Решите визовые вопросы: (напоминание: Подача заявлений на визу происходит не ранее 3 месяцев и не позднее 1 месяца до предполагаемой даты выезда)
    - загран паспорт действителен не меннее 2-х лет после начала мобильности
    - Уточните в посольстве/ консульстве/ визовом центре требования по точным срокам действия паспорта для оформления визы в страну принимающего университета

3) Сверьтесь еще раз с чек-листом(смотрите сообщения выше)

4) Изучите рекомендации МИД РФ для выезжающих за рубеж, информация для граждан РФ по странам(http://www.kdmid.ru/docs.aspx?rg=all)
Если Вам понадобится моя помощь, нажмите на кнопку ниже''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='spring'))
async def spring(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''А вот и чек-лист для весенней мобильности!\nКстати, еще вам необходимо посетить ориентационную сессию!
Это обязательно необходимо сделать с 10 по 20 ноября.
https://studyabroad.hse.ru/mirror/pubs/share/438382796.pdf''', reply_markup=Spring)
    callback_data = call.data
    logging.info(f"{callback_data=}")

'''___________________________________________________________
Сценарий 5: подбор программы    
'''


@dp.callback_query_handler(bot_callback.filter(action='5'))
async def prog_Find(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Попробую помочь Вам подобрать программу на мобильность!
Выбирите интересующий Вас уровень образования(кнопки ниже)''', reply_markup=program)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='Bach'))
async def prog_Find6(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Инструкция по поиску на сайте:
1) Зайдите на сайт https://studyabroad.hse.ru/catalogue
2) Нажмите ctrl+f или command+f(MacOs)
3) В окошко, которое появилось в верхнем правом углу, напишите Bachelor 
Сейчас нужно выбрать интересующий Вас язык обучения
Нажмите на кнопку ниже для выбора(можно только одну за раз)''', reply_markup=prog_lang)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='Mag'))
async def prog_Find1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Инструкция по поиску на сайте:
1) Зайдите на сайт https://studyabroad.hse.ru/catalogue
2) Нажмите ctrl+f или command+f(MacOs)
3) В окошко, которое появилось в верхнем правом углу, напишите Master 
Сейчас нужно выбрать интересующий Вас язык обучения
Нажмите на кнопку ниже для выбора(можно только одну за раз)''', reply_markup=prog_lang)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='Eng'))
async def prog_Find2(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Нажимая на кнопки "назад" и "далее" на окошке в правом верхнем углу выбирите программу,
у которой языком преподавания является Английский(English)
Введите команду "FoS"(/Fos), чтобы найти программы по интересующей Вас научной области''',reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='French'))
async def prog_Find3(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.edit_text(text='''Нажимая на кнопки "назад" и "далее" на окошке в правом верхнем углу выбирите программу,
у которой языком преподавания является Французский(French)
Введите команду "FoS"(/Fos), чтобы найти программы по интересующей Вас научной области''', reply_markup=helpME)

    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='Ger'))
async def prog_Find4(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Нажимая на кнопки "назад" и "далее" на окошке в правом верхнем углу выбирите программу,
у которой языком преподавания является Немецкий(Germany)
Введите команду "FoS"(/Fos), чтобы найти программы по интересующей Вас научной области''', reply_markup=helpME)

    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='Span'))
async def prog_Find5(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Нажимая на кнопки "назад" и "далее" на окошке в правом верхнем углу выбирите программу,
    у которой языком преподавания является Испанский(Spanish)
    Введите команду "FoS"(/Fos), чтобы найти программы по интересующей Вас научной области''', reply_markup=helpME)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.message_handler(Command("FoS"))
async def sphere(message: Message):
    await message.answer(text='''Введите в поисковик на сайте название области из представленного списка:
Architecture, Area Studies, Arts, Asian Studies, Brain Sciences, Business, Civics,	
Communication, Computer	Sciences, Creativity, Culture, Design, Economics, Education,
Energy,	Engineering, English & American Studies, Environmental Studies, Ethnology,	
Film, Finance, German Literature & Linguistics,	Globalization, Government, History,	
Humanities, Information	Systems	in Business, Innovation, International Relations, IT,	
Journalism,	Languages, Law,	Life Science Technologies, Linguistics,	Literature,	Logistics,	
Management,	Marketing, Maths, Media	Studies, Natural Resources,	Philosophy,	Physics,	
Political Science, Psychology, Public Policy, Science, Semiotics, Slavonic Studies,	Social	
Sciences, Sociology, Statistics, Studies in Sport & Health Sciences, Technology, Urban Studies''', reply_markup=helpME)


'''___________________________________________________________
Главное Меню бота
'''


@dp.callback_query_handler(bot_callback.filter(action='help'))
async def push_yes(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text='''Привет! Выберите нужный Вам раздел:\n1. Подать заявку
2. Получить стипендию\n3. Задать вопрос\n4. Для участников\n5. Подбор программ на мобильность''', reply_markup=menu)
    callback_data = call.data
    logging.info(f"{callback_data=}")


@dp.callback_query_handler(bot_callback.filter(action='back'))
async def push_yes(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='''Привет! Выберите нужный Вам раздел:\n1. Подать заявку
2. Получить стипендию\n3. Задать вопрос\n4. Для участников\n5. Подбор программ на мобильность''', reply_markup=menu)
    callback_data = call.data
    logging.info(f"{callback_data=}")
