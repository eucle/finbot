import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from config_data.config import TgBot, load_config
from handlers import user_handlers
from keyboards.set_menu import set_main_menu


async def main():
    logger.info("Bot started.")

    bot_config: TgBot = load_config().tg_bot

    bot: Bot = Bot(token=bot_config.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=user_handlers.storage)

    await set_main_menu(bot)
    logger.info("Main menu set.")

    dp.include_router(user_handlers.router)
    logger.info("Handlers are ready.")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
