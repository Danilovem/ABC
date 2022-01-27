from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_datas import pagination_callback
from keyboards.inline.pagination import get_page_keyboard, MAX_ITEMS_PER_PAGE
from loader import dp
from utils.db_api.db import DataBase
from utils.misc.pages import get_page

db = DataBase()


@dp.message_handler(Command("faq"))
async def pagination_answer(message: Message):
    text = get_page()
    await message.answer(text, reply_markup=get_page_keyboard(max_page=len(db.select_all_questions())))


@dp.callback_query_handler(pagination_callback.filter(page='current_page'))
async def current_page_error(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(pagination_callback.filter(key="question"))
async def show_chosen_page(call:CallbackQuery, callback_data: dict):

    current_page = int(callback_data.get("page"))
    text = get_page(page=current_page)
    markup = get_page_keyboard(max_page=len(db.select_all_questions()), page=current_page)

    await call.message.edit_text(text=text, reply_markup=markup)
