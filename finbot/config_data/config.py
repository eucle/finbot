from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class DatabaseConfig:
    db_name: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class RedisCongif:
    redisdb_host: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    redisdb: RedisCongif


def load_config(path: None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_id=int(env('ADMIN_ID')),
        ),
        db=DatabaseConfig(
            db_name=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
        ),
        redisdb=RedisCongif(
            redisdb_host=env('REDISDB_HOST'),
        ),
    )
