from aiogram import Dispatcher, Bot


def create_dp() -> Dispatcher:
    return Dispatcher()
    
    
def create_bot(token: str) -> Bot:
    return Bot(token=token)
