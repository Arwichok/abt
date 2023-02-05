from .factory import create_dp, create_bot
from ..util import config


create_dp()\
    .run_polling(
        create_bot(
            token=config.TELEGRAM_BOT_TOKEN
        )
    )
