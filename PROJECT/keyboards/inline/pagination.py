from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import pagination_callback

MAX_ITEMS_PER_PAGE = 5


def get_page_keyboard(max_page: int, key="question", page: int = 1):
    if max_page % MAX_ITEMS_PER_PAGE == 0:
        max_page = max_page // MAX_ITEMS_PER_PAGE
    else:
        max_page = max_page // MAX_ITEMS_PER_PAGE + 1

    first_page_text = "<<1"
    first_page = 1

    previous_page = page - 1
    previous_page_text = f"<{previous_page} "

    current_page_text = f" {page} "

    next_page = page + 1
    next_page_text = f" {next_page}>"

    markup = InlineKeyboardMarkup(row_width=5)

    markup.insert(
        InlineKeyboardButton(text=first_page_text, callback_data=pagination_callback.new(key=key, page=first_page)))

    if previous_page > 0:
        markup.insert(InlineKeyboardButton(text=previous_page_text,
                                           callback_data=pagination_callback.new(key=key, page=previous_page)))
    else:
        markup.insert(InlineKeyboardButton(text=" - ",
                                           callback_data=pagination_callback.new(key=key, page="current_page")))
    markup.insert(InlineKeyboardButton(text=current_page_text,
                                       callback_data=pagination_callback.new(key=key, page="current_page")))

    if next_page <= max_page:
        markup.insert(
            InlineKeyboardButton(text=next_page_text, callback_data=pagination_callback.new(key=key, page=next_page)))
    else:
        markup.insert(InlineKeyboardButton(text=" - ",
                                           callback_data=pagination_callback.new(key=key, page="current_page")))

    markup.insert(
        InlineKeyboardButton(text=f"{max_page}>>", callback_data=pagination_callback.new(key=key, page=max_page)))

    return markup

# def get_keyboard(array, page: int = 1):
#     markup = InlineKeyboardMarkup(row_width=1)
#     MAX_ITEMS_PER_PAGE = 5
#
#     first_item_index = (page - 1) * MAX_ITEMS_PER_PAGE
#     last_item_index = page * MAX_ITEMS_PER_PAGE
#
#     sliced_array = array[first_item_index:last_item_index]
#     item_buttons = []
#
#     for item in sliced_array:
#         item_buttons.append(
#             InlineKeyboardButton(text=f"{item[1]}", callback_data=show_question.new(question_id=item[0]))
#
#         )
#     pages_buttons = []
#     firs_page = 1
#     first_page_text = "<< 1"
#
#     current_page = page
#     current_page_text = f"-{current_page}-"
#
#     previous_page = page - 1
#     previous_page_text = f"<{previous_page}"
#
#     next_page = page + 1
#     next_page_text = f"{next_page}>"
#
#     if len(array) % MAX_ITEMS_PER_PAGE == 0:
#         max_page = len(array) // MAX_ITEMS_PER_PAGE
#     else:
#         max_page = len(array) // MAX_ITEMS_PER_PAGE + 1
#     max_page_text = f">> {max_page}"
#
#     pages_buttons.append(
#         InlineKeyboardButton(text=first_page_text, callback_data=pagination_callback.new(key="qq", page=firs_page))
#     )
#     if previous_page >= firs_page:
#         pages_buttons.append(
#             InlineKeyboardButton(text=previous_page_text, callback_data=pagination_callback.new(key="qq", page=previous_page))
#         )
#     else:
#         pages_buttons.append(
#             InlineKeyboardButton(text=" . ",
#                                  callback_data=pagination_callback.new(key="qq", page='current_page'))
#         )
#
#         pages_buttons.append(
#             InlineKeyboardButton(text=current_page_text, callback_data=pagination_callback.new(key="qq", page="current_page"))
#         )
#
#     if next_page <= max_page:
#         pages_buttons.append(
#             InlineKeyboardButton(text=next_page_text, callback_data=pagination_callback.new(key="qq", page=next_page))
#         )
#     else:
#         pages_buttons.append(
#             InlineKeyboardButton(text=" . ",
#                                  callback_data=pagination_callback.new(key="qq", page='current_page'))
#         )
#
#     pages_buttons.append(
#         InlineKeyboardButton(text=max_page_text, callback_data=pagination_callback.new(key="qq", page=max_page))
#     )
#
#     for i in item_buttons:
#         markup.insert(i)
#     markup.row(*pages_buttons)
#
#     return markup

# def get_keyboard1(array, page: int = 1):
#     markup = InlineKeyboardMarkup(row_width=1)
#     MAX_ITEMS_PER_PAGE = 5
#
#     first_item_index = (page - 1) * MAX_ITEMS_PER_PAGE
#     last_item_index = page * MAX_ITEMS_PER_PAGE
#
#     sliced_array = array[first_item_index:last_item_index]
#     item_buttons = []
#
#     for item in sliced_array:
#         item_buttons.append(
#             InlineKeyboardButton(text=f"{item[1]}", callback_data=show_question.new(question_id=item[0]))
#
#         )
#     pages_buttons = []
#     firs_page = 1
#     first_page_text = "<< 1"
#
#     previous_page = page - 1
#     previous_page_text = f"< {previous_page}"
#
#     next_page = page + 1
#     next_page_text = f"{next_page}>"
#
#     if len(array) % MAX_ITEMS_PER_PAGE == 0:
#         max_page = len(array) // MAX_ITEMS_PER_PAGE
#     else:
#         max_page = len(array) // MAX_ITEMS_PER_PAGE + 1
#     max_page_text = f">> {max_page}"
#
#     pages_buttons.append(
#         InlineKeyboardButton(text=first_page_text, callback_data=pagination_callback.new(key="qq", page=firs_page) )
#     )
#     if previous_page >= firs_page:
#         pages_buttons.append(
#             InlineKeyboardButton(text=previous_page_text, callback_data=pagination_callback.new(key="qq", page=previous_page))
#         )
#     else:
#         pages_buttons.append(
#             InlineKeyboardButton(text=" . ",
#                                  callback_data=pagination_callback.new(key="qq", page='current_page'))
#         )
#         pages_buttons.append(
#             InlineKeyboardButton(text=f" <{page}> ", callback_data="current_page")
#         )
#
#     if next_page <= max_page:
#         pages_buttons.append(
#             InlineKeyboardButton(text=next_page_text,callback_data=pagination_callback.new(key="qq", page=next_page))
#         )
#     else:
#         pages_buttons.append(
#             InlineKeyboardButton(text=" . ",
#                                  callback_data=pagination_callback.new(key="qq", page='current_page'))
#         )
#
#     pages_buttons.append(
#         InlineKeyboardButton(text=max_page_text,callback_data=pagination_callback.new(key="qq", page=max_page))
#     )
#
#     for i in item_buttons:
#         markup.insert()
#     markup.row(*pages_buttons)
#
#     return markup
