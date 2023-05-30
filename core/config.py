from dataclasses import dataclass

from environs import Env


@dataclass
class Bot:
    bot_token: str
    admin_id: int


@dataclass
class Config:
    bot: Bot


def get_config(path: str):
    env = Env()
    env.read_env(path=path)

    return Config(
        bot=Bot(
            bot_token=env.str('TOKEN'),
            admin_id=env.int('ADMIN_ID')

        )
    )


config = get_config('.env')
