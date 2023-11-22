LEX_CAT: dict[str, str] = {
    'auto': 'Автомобиль',
    'entertainment': 'Развлечения',
    'household': 'Хозяйство',
    'kids': 'Дети',
    'personal_expenditure': 'Личные расходы',
    'pet': 'Кот',
    'transport': 'Транспорт',
}

LEX_SUBCAT: dict[str, dict] = {
    'auto': {
        'car_repair': 'Ремонт авто',
        'car_insurance': 'Страхование авто',
        'petrol': 'Бензин',
        'tyre_fitting': 'Шиномонтаж',
        'car_wash': 'Мойка',
        'parking': 'Парковка',
        'car_tax': 'Налог на авто',
        'toll_road': 'Платная дорога',
    },
    'entertainment': {
        'cinema': 'Кинотеатр',
        'restaurant': 'Ресторан, кафе',
        'gifts': 'Подарки',
    },
    'household': {
        'food': 'Продукты',
        'goods': 'Промтовары',
        'family_expenses': 'Семейные траты',
        'appliances': 'Техника',
        'house_payments': 'Платежи за квартиру',
        'house_insurance': 'Страхование квартиры',
        'internet': 'Интернет',
        'pharmacy': 'Аптека',
        'house_tax': 'Налог на квартиру',
        'house_repair': 'Домашний ремонт',
    },
    'kids': {
        'strolls': 'Прогулки, игровые',
        'kids_clothing_shoes': 'Одежда, обувь детские',
        'kids_classes': 'Занятия, кружки',
        'toys_books': 'Игрушки, книги',
        'kids_ medicine': 'Медуслуги детские',
    },
    'personal_expenditure': {
        'phone': 'Телефон',
        'other_taxes': 'Налоги другие',
        'personal_clothing_shoes': 'Одежда, обувь личные',
        'hairdressing': 'Парикмахерская',
        'personal_ medicine': 'Медуслуги личные',
        'parents': 'Родители',
        'sites': 'Сайты',
    },
    'pet': {
        'pet_food': 'Корм',
        'pet_medicine': 'Ветклиника',
        'pet_vacation': 'Передержка',
    },
    'transport': {
        'taxi': 'Такси',
        'subway_bus': 'Метро, автобус',
    }

    }

LEX_PAY: dict[str, str] = {
    'cash': 'Наличные',
    'tin_credcard': 'Тинькофф кред.',
    'tin_debtcard': 'Тинькофф дебет.',
    'vtb_debtcard': 'ВТБ дебет.',
    'sber_debtcard': 'Сбер дебет.',
}

LEX_COMMANDS: dict[str, str] = {
    '/start': 'Добавить операцию',
    '/last': 'Показать 5 последних',
    '/delete': 'Удалить последнюю',
}
