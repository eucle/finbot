from lexicon.lexicon import LEX_CAT, LEX_PAY, LEX_SUBCAT


def show_created_entry(source):
    _string = (
      f"Операция выполнена:\nКатегория: {LEX_CAT[source['category']]}\n"
      f"Подкатегория: {LEX_SUBCAT[source['category']][source['subcategory']]}\n"
      f"Способ платежа: {LEX_PAY[source['payment_method']]}\n"
      f"Сумма: {source['amount']}\n"
      f"Дата: {source['created_at']}\n"
    )

    return _string
