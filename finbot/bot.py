import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import TgBot, load_config
from handlers import user_handlers
from keyboards.set_menu import set_main_menu


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    bot_config: TgBot = load_config().tg_bot

    bot: Bot = Bot(token=bot_config.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
