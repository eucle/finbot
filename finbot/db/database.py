from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config_data.config import DB_Info, load_db_info
from lexicon.lexicon import LEX_CAT, LEX_SUBCAT, LEX_PAY
from db.models import Base, Transaction


def create_db_entry(source):
    # Создаем саму сессию БД
    with Session(bind=engine) as session:
        # создаем объект Transaction для добавления в БД
        transaction = Transaction(
            category=LEX_CAT[source['category']],
            subcategory=LEX_SUBCAT[source['category']][source['subcategory']],
            payment_method=LEX_PAY[source['payment_method']],
            amount=source['amount'],
            created_at=source['created_at'])

        session.add(transaction)      # добавляем в БД
        session.commit()              # сохраняем изменения
        session.refresh(transaction)  # обновляем состояние объекта


def show_last_entries():
    string = '...\n'
    with Session(bind=engine) as session:
        entries = reversed(
            session.query(Transaction).order_by(Transaction.id.desc())[:5])
        for entry in entries:
            string += (
                f"{entry.id}. {entry.category} > {entry.subcategory} > "
                f"{entry.payment_method} > {entry.amount}\n")
    return string


def delete_entry():
    with Session(bind=engine) as session:
        entry = session.query(Transaction).order_by(Transaction.id.desc()
                                                    ).first()
        string = (
            "Запись успешно удалена:\n"
            f"{entry.id}. {entry.category} > {entry.subcategory} > "
            f"{entry.payment_method} > {entry.amount}\n")

        session.delete(entry)
        session.commit()
        return string


db_info: DB_Info = load_db_info()

engine = create_engine(db_info.pg_dsn)
# engine = create_engine("postgresql+psycopg://postgres:1709Mirus%40@postgres:5432/finbot_db")

Session = sessionmaker(bind=engine)

# Создаем таблицу в БД
Base.metadata.create_all(bind=engine)
