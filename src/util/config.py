import logging

import environs


env = environs.Env()
env.read_env()


DEV = env.bool("DEV", False)

DOMAIN = env("DOMAIN", "")
PORT = env.int("PORT", 8000)
HOST = env("HOST", "localhost")

DETA_PATH = env("DETA_PATH", None)
DETA_RUNTIME = env("DETA_RUNTIME", False)
DETA_PROJECT_KEY = env("DETA_PROJECT_KEY", None)

TELEGRAM_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN")
TELEGRAM_SECRET = env("TELEGRAM_SECRET")
TELEGRAM_WEBHOOK_PATH = env("TELEGRAM_WEBHOOK", "/bot_wh")
SKIP_TELEGRAM_UPDATES = env.bool("SKIP_TELEGRAM_UPDATES", False)

if DETA_RUNTIME:
    DOMAIN = f"{DETA_PATH}.deta.dev"

WEBHOOK_URL = f"https://{DOMAIN}{TELEGRAM_WEBHOOK_PATH}"


if DEV:
    logging.basicConfig(level=logging.DEBUG)
    with open(".env.dist", "w") as f:
        f.writelines(sorted([f"{k}=\n" for k in env.dump()]))
else:
    logging.basicConfig(level=logging.WARNING)
