from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message

from db.database import create_db_entry, show_last_entries, delete_entry
from filters.filters import IsNumber
from keyboards.main_kb import create_main_kb
from lexicon.lexicon import LEX_CAT, LEX_PAY, LEX_SUBCAT, LEX_COMMANDS
from services.services import show_created_entry


class FSMRecordTransaction(StatesGroup):
    select_category = State()
    select_subcategory = State()
    select_payment_method = State()
    input_amount = State()


storage = MemoryStorage()

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def handle_start_command(message: Message, state: FSMContext):
    keyboard = create_main_kb(2, LEX_CAT)
    await message.answer(
        text='Выбери категорию расходов:',
        reply_markup=keyboard
    )
    await state.set_state(FSMRecordTransaction.select_category)


@router.callback_query(StateFilter(FSMRecordTransaction.select_category),
                       F.data.in_(LEX_CAT))
async def handle_category_selection(callback: CallbackQuery,
                                    state: FSMContext):
    await state.update_data(category=callback.data)
    keyboard = create_main_kb(2, LEX_SUBCAT, subcat=callback.data)
    await callback.message.answer(
        text='Выбери подкатегорию расходов:',
        reply_markup=keyboard
    )
    await state.set_state(FSMRecordTransaction.select_subcategory)


@router.callback_query(StateFilter(FSMRecordTransaction.select_subcategory),
                       F.data.in_({subcat for value in LEX_SUBCAT.values()
                                   for subcat in value.keys()}))
# @router.callback_query(StateFilter(FSMRecordTransaction.select_subcategory),
#                        F.data.in_({subcat[0] for value in LEX_SUBCAT.values()
#                                    for subcat in value}))
async def handle_subcategory_selection(callback: CallbackQuery,
                                       state: FSMContext):
    await state.update_data(subcategory=callback.data)
    keyboard = create_main_kb(2, LEX_PAY)
    await callback.message.answer(
        text='Выбери способ платежа:',
        reply_markup=keyboard
    )
    await state.set_state(FSMRecordTransaction.select_payment_method)


@router.callback_query(StateFilter(FSMRecordTransaction.select_payment_method),
                       F.data.in_(LEX_PAY))
async def handle_payment_method_selection(callback: CallbackQuery,
                                          state: FSMContext):
    await state.update_data(payment_method=callback.data)
    await callback.message.answer(
        text='Введи потраченную сумму:'
    )
    await state.set_state(FSMRecordTransaction.input_amount)


@router.message(StateFilter(FSMRecordTransaction.input_amount),
                IsNumber())
async def handle_transaction_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text, created_at=message.date)
    create_db_entry(await state.get_data())
    await message.answer(
        text=show_created_entry(await state.get_data())
    )
    await state.clear()


@router.message(Command(commands='last'))
async def handle_last_entries_command(message: Message):
    await message.answer(text=show_last_entries())


@router.message(Command(commands='delete'))
async def handle_delete_entry_command(message: Message):
    delete_information = delete_entry()
    await message.answer(text=delete_information)
