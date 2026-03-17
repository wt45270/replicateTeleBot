from aiogram.utils import executor
from create_bot import dp, bot, dev_mode
from handlers import client, other


async def on_startup(_):
    print('Bot Online')


client.register_handlers_client(dp)
if dev_mode:
    other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
export TELEGRAM_BOT_API_TOKEN="8594216185:AAF4_o5wZdNNioVVbdRvO3Ee3Wn6gXG9NJ8"
export REPLICATE_API_TOKEN="你的r8_002s5xIvy7Thw6CsSgbF9Zn4rAuwsOx2QoHeb"

