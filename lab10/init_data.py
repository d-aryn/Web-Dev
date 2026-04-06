import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

def populate():

    Product.objects.all().delete()
    Category.objects.all().delete()

    categories_data = [
        {'id': 1, 'name': 'Боксерская экипировка'},
        {'id': 2, 'name': 'MMA и единоборства'},
        {'id': 3, 'name': 'Футбол и активный спорт'},
        {'id': 4, 'name': 'Каратэ и боевые искусства'},
    ]

    category_objects = {}
    for cat in categories_data:
        c = Category.objects.create(id=cat['id'], name=cat['name'])
        category_objects[cat['id']] = c
        print(f"Категория создана: {c.name}")

    products_data = [
        # Категория 1
        {'name': 'Боксерки Venum', 'price': 15000, 'desc': 'Лёгкие и удобные боксерки...', 'cat_id': 1},
        {'name': 'Боксерские перчатки IBA', 'price': 17764, 'desc': 'Фирменные перчатки...', 'cat_id': 1},
        {'name': 'Шлем для бокса Wesing', 'price': 14500, 'desc': 'Защитный шлем...', 'cat_id': 1},
        {'name': 'Скакалка для бокса', 'price': 6500, 'desc': 'Профессиональная скакалка...', 'cat_id': 1},
        {'name': 'Боксерский бинт', 'price': 2500, 'desc': 'Эластичные бинты...', 'cat_id': 1},
        # Категория 2
        {'name': 'Перчатки для MMA', 'price': 5999, 'desc': 'Открытые перчатки...', 'cat_id': 2},
        {'name': 'Рашгард Green', 'price': 18000, 'desc': 'Спортивный рашгард...', 'cat_id': 2},
        {'name': 'Накладки на голень', 'price': 1894, 'desc': 'Щитки для защиты...', 'cat_id': 2},
        {'name': 'Шлем для спарринга', 'price': 21500, 'desc': 'Усиленный шлем...', 'cat_id': 2},
        {'name': 'Майка для единоборств', 'price': 9000, 'desc': 'Спортивная майка...', 'cat_id': 2},
        # Категория 3
        {'name': 'Футбольная форма Manchester City', 'price': 14500, 'desc': 'Домашняя форма...', 'cat_id': 3},
        {'name': 'Футбольные бутсы', 'price': 22994, 'desc': 'Лёгкие бутсы...', 'cat_id': 3},
        {'name': 'Футбольный мяч', 'price': 8900, 'desc': 'Универсальный мяч...', 'cat_id': 3},
        {'name': 'Гетры футбольные', 'price': 3500, 'desc': 'Удобные и эластичные...', 'cat_id': 3},
        {'name': 'Щитки футбольные', 'price': 4200, 'desc': 'Защитные щитки...', 'cat_id': 3},
        # Категория 4
        {'name': 'Кимоно для карате', 'price': 4993, 'desc': 'Классическое белое кимоно...', 'cat_id': 4},
        {'name': 'Пояс для кимоно', 'price': 2000, 'desc': 'Хлопковый пояс...', 'cat_id': 4},
        {'name': 'Перчатки для каратэ', 'price': 7200, 'desc': 'Специальные перчатки...', 'cat_id': 4},
        {'name': 'Защита головы', 'price': 16500, 'desc': 'Шлем для защиты головы...', 'cat_id': 4},
        {'name': 'Защита голени и стопы', 'price': 9800, 'desc': 'Комплект защиты...', 'cat_id': 4},
    ]

    for p_data in products_data:
        Product.objects.create(
            name=p_data['name'],
            price=p_data['price'],
            description=p_data['desc'],
            count=10,
            is_active=True,
            category=category_objects[p_data['cat_id']]
        )
    
    print(f"Успешно добавлено {len(products_data)} товаров!")

if __name__ == '__main__':
    populate()