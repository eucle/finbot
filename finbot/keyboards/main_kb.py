from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_main_kb(width: int,
                   lexicon: dict,
                   subcat=None) -> InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if type(list(lexicon.values())[0]) == str:
        for button, text in lexicon.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    else:
        for button, text in lexicon[subcat].items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()
