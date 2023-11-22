from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config_data.config import DatabaseConfig, load_config
from lexicon.lexicon import LEX_CAT, LEX_PAY, LEX_SUBCAT
from db.models import Base, Transaction


def create_db_entry(source):
    with Session(bind=engine) as session:
        transaction = Transaction(
            category=LEX_CAT[source['category']],
            subcategory=LEX_SUBCAT[source['category']][source['subcategory']],
            payment_method=LEX_PAY[source['payment_method']],
            amount=source['amount'],
            created_at=source['created_at'])

        session.add(transaction)
        session.commit()
        session.refresh(transaction)


def show_last_entries():
    string = '...\n'
    with Session(bind=engine) as session:
        entries = reversed(
            session.query(Transaction).order_by(
                Transaction.created_at.desc())[:5]
            )
        for entry in entries:
            string += (
                f"{entry.id}. {entry.category} > {entry.subcategory} > "
                f"{entry.payment_method} > {entry.amount}\n"
            )
    return string


def delete_entry():
    with Session(bind=engine) as session:
        entry = (
            session.query(Transaction).order_by(Transaction.id.desc()).first()
        )
        string = (
            "Запись успешно удалена:\n"
            f"{entry.id}. {entry.category} > {entry.subcategory} > "
            f"{entry.payment_method} > {entry.amount}\n"
        )
        session.delete(entry)
        session.commit()
        return string


db_config: DatabaseConfig = load_config().db
dsn = (
    f"postgresql+psycopg://{db_config.db_user}:{db_config.db_password}"
    f"@{db_config.db_host}/{db_config.db_name}"
)

engine = create_engine(dsn)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)
