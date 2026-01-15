from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config import DB


def new_session_maker(
    db_config: DB,
) -> sessionmaker[Session]:
    database_uri = f"postgresql://{db_config.USER}:{db_config.PASSWORD}@{db_config.HOST}:{db_config.PORT}/{db_config.NAME}"

    engine = create_engine(
        database_uri,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )
    return sessionmaker(
        engine, class_=Session, autoflush=False, expire_on_commit=False
    )
