from environs import Env


env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN")
TELEGRAM_SECRET = env("TELEGRAM_SECRET")

