from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


@dataclass
class DB_Info:
    pg_dsn: str


def load_config(path: None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'))
        )


def load_db_info(path: None = None) -> DB_Info:
    env = Env()
    env.read_env(path)
    return DB_Info(pg_dsn=env('POSTGRES_DSN'))
