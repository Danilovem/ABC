from keyboards.inline.pagination import MAX_ITEMS_PER_PAGE
from utils.db_api.db import DataBase
db = DataBase()
alq = db.select_all_questions()


def get_page(page: int = 1):
    first_item_index = (page - 1) * MAX_ITEMS_PER_PAGE
    last_item_index = page * MAX_ITEMS_PER_PAGE

    items = ''

    for i in alq[first_item_index:last_item_index]:
        for j in i[1:3]:
            items += j+'\n'
        items += "\n"

    return items
