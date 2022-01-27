from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import bot_callback

choice = InlineKeyboardMarkup(row_width=2)
choice1 = InlineKeyboardMarkup(row_width=2)
helpME = InlineKeyboardMarkup(row_width=1)
menu = InlineKeyboardMarkup(row_width=3)
TicketMenu = InlineKeyboardMarkup(row_width=2)
Check_list = InlineKeyboardMarkup(row_width=2)
Ticket_filling = InlineKeyboardMarkup(row_width=1)
Ticket_filling1 = InlineKeyboardMarkup(row_width=1)
AmIHelpedYou = InlineKeyboardMarkup(row_width=2)
ForMembers = InlineKeyboardMarkup(row_width=2)
ForMembers1 = InlineKeyboardMarkup(row_width=2)
Autumn = InlineKeyboardMarkup(row_width=1)
Autumn1 = InlineKeyboardMarkup(row_width=2)
Autumn2 = InlineKeyboardMarkup(row_width=1)
ForMembers2 = InlineKeyboardMarkup(row_width=1)
Spring = InlineKeyboardMarkup(row_width=1)
program = InlineKeyboardMarkup(row_width=2)
prog_lang = InlineKeyboardMarkup(row_width=3)


#Сценарий 4

yes_button = InlineKeyboardButton(text="Да", callback_data=bot_callback.new(action="yes"))
choice.insert(yes_button)

no_button = InlineKeyboardButton(text="Нет", callback_data=bot_callback.new(action="no"))
choice.insert(no_button)

yes_button1 = InlineKeyboardButton(text="Да", callback_data=bot_callback.new(action="da"))
choice1.insert(yes_button1)

no_button1 = InlineKeyboardButton(text="Нет", callback_data=bot_callback.new(action="net"))
choice1.insert(no_button1)

#----------------------------------------------------------------------------------------------
#Сценарий 2

help_button = InlineKeyboardButton(text="Роберт, мне нужна твоя помощь", callback_data=bot_callback.new(action="help"))
helpME.insert(help_button)

#----------------------------------------------------------------------------------------------
#Main Menu

fr_button = InlineKeyboardButton(text="1", callback_data=bot_callback.new(action="1"))
menu.insert(fr_button)

sc_button = InlineKeyboardButton(text="2", callback_data=bot_callback.new(action="2"))
menu.insert(sc_button)

thr_button = InlineKeyboardButton(text="3", callback_data=bot_callback.new(action="3"))
menu.insert(thr_button)

fourth_button = InlineKeyboardButton(text="4", callback_data=bot_callback.new(action="4"))
menu.insert(fourth_button)

fth_button = InlineKeyboardButton(text="5", callback_data=bot_callback.new(action="5"))
menu.insert(fth_button)
#----------------------------------------------------------------------------------------------
#Menu Сценарий 1

Guide = InlineKeyboardButton(text="1", callback_data=bot_callback.new(action="guide"))
TicketMenu.insert(Guide)

doc_list = InlineKeyboardButton(text="2", callback_data=bot_callback.new(action="doc_list"))
TicketMenu.insert(doc_list)

ISP = InlineKeyboardButton(text="3", callback_data=bot_callback.new(action="ISP"))
TicketMenu.insert(ISP)

back = InlineKeyboardButton(text="4", callback_data=bot_callback.new(action="back"))
TicketMenu.insert(back)

#----------------------------------------------------------------------------------------------
#Сценарий 3: совместное заполнение заявки

yes_for_ticket = InlineKeyboardButton(text="Да, пожалуйста", callback_data=bot_callback.new(action="yft"))
Check_list.insert(yes_for_ticket)

no_for_ticket = InlineKeyboardButton(text="Нет, не надо", callback_data=bot_callback.new(action="nft"))
Check_list.insert(no_for_ticket)

ticket_documents = InlineKeyboardButton(text="Я сделал", callback_data=bot_callback.new(action="tido"))
Ticket_filling.insert(ticket_documents)

main_menu = InlineKeyboardButton(text="Главное меню", action="help")
Ticket_filling.insert(main_menu)

final_step = InlineKeyboardButton(text="Я сделал", callback_data=bot_callback.new(action="toLMS"))
Ticket_filling1.insert(final_step)
Ticket_filling1.insert(main_menu)

#----------------------------------------------------------------------------------------------
#Сценарий 7: совместное заполнение заявки

yesYouAre = InlineKeyboardButton(text="Да", callback_data=bot_callback.new(action="yyr"))
AmIHelpedYou.insert(yesYouAre)

noYouNot = InlineKeyboardButton(text="Нет", callback_data=bot_callback.new(action="nyrn"))
AmIHelpedYou.insert(noYouNot)

#----------------------------------------------------------------------------------------------
#Сценарий 6

check_list = InlineKeyboardButton(text="Чек-лист перед отъездом", callback_data=bot_callback.new(action="check"))
ForMembers.insert(check_list)

delay = InlineKeyboardButton(text="Перенос мобильности", callback_data=bot_callback.new(action="delay"))
ForMembers.insert(delay)

autumn = InlineKeyboardButton(text="Осенью", callback_data=bot_callback.new(action="autumn"))
ForMembers1.insert(autumn)

spring = InlineKeyboardButton(text="Весной", callback_data=bot_callback.new(action="spring"))
ForMembers1.insert(spring)

atmNext = InlineKeyboardButton(text="Далее", callback_data=bot_callback.new(action="atmNext"))
Autumn.insert(atmNext)

atmOL = InlineKeyboardButton(text="Онлайн формат", callback_data=bot_callback.new(action="atmOn"))
Autumn1.insert(atmOL)

atmOf = InlineKeyboardButton(text="Выезд в другую страну", callback_data=bot_callback.new(action="atmOf"))
Autumn1.insert(atmOf)

atf = InlineKeyboardButton(text="Далее", callback_data=bot_callback.new(action="atmF"))
Autumn2.insert(atf)
ISP1 = InlineKeyboardButton(text="про ИУП", callback_data=bot_callback.new(action="PoIS"))
Autumn2.insert(ISP1)
ForMembers2.insert(atf)

Spring.insert(atmNext)

#----------------------------------------------------------------------------------------------
#Сценарий 5

levelBach = InlineKeyboardButton(text="Бакалавриат", callback_data=bot_callback.new(action="Bach"))
program.insert(levelBach)
levelMag = InlineKeyboardButton(text="Магистратура", callback_data=bot_callback.new(action="Mag"))
program.insert(levelMag)

eng = InlineKeyboardButton(text="Английский", callback_data=bot_callback.new(action="Eng"))
prog_lang.insert(eng)
fr = InlineKeyboardButton(text="Французский", callback_data=bot_callback.new(action="French"))
prog_lang.insert(fr)
ger = InlineKeyboardButton(text="Немецкий", callback_data=bot_callback.new(action="Ger"))
prog_lang.insert(ger)
span = InlineKeyboardButton(text="Испанский", callback_data=bot_callback.new(action="Span"))
prog_lang.insert(span)

