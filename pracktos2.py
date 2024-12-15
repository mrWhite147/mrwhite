
# Пользователи
users = [
    {'username': 'user', 'password': 'user', 'role': 'user', 'history': [], 'cart': []},
    {'username': 'admin', 'password': 'admin', 'role': 'admin'}
]
# Товары
products = [
    {'name': 'Видеокарта MSI GeForce RTX 4070 Ventus 2X E OC 12GB', 'price': 65000, 'category': 'Комплектующие для ПК', 'quantity': 10},
    {'name': 'SSD диск Samsung 980 PRO 1 Тб MZ-V8P1T0BW', 'price': 100000, 'category': 'Комплектующие для ПК', 'quantity': 5},
    {'name': 'Amd Процессор CPU AMD Ryzen 7 7700 OEM', 'price': 30000, 'category': 'Комплектующие для ПК', 'quantity': 20},
    {'name': 'Видеокарта MSI GeForce RTX 4070 Super 12G Gaming X Slim', 'price': 82500, 'category': 'Комплектующие для ПК', 'quantity': 15}, 
    {'name': 'Фигурка FUNKO POP! Attack on Titan S5: Mikasa Ackerman', 'price': 2000, 'category': 'Фигурки', 'quantity': 20} ,
    {'name': 'Фигурка Funko POP! Animation Bleach Sosuke Aizen', 'price': 1600, 'category': 'Фигурки', 'quantity': 11} ,
    {'name': '17,3" Ноутбук Gigabyte AORUS 15 BFX black (BXF-74KZ554SD)', 'price': 224700, 'category': 'Ноутбуки', 'quantity': 5}
]

# Авторизация
def authenticate():
    print("Добро пожаловать в Магазинчик!")
    username = input("Логин: ")
    password = input("Пароль: ")
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    print("Неверный логин или пароль.")
    return None


# Меню пользователя
def user_menu(user):
    while True:
        print("Меню пользователя:")
        print("1. Просмотреть каталог товаров")
        print("2. Добавить товар в корзину")
        print("3. Просмотреть корзину")
        print("4. Оформить заказ")
        print("5. Просмотреть историю заказов")
        print("6. Выйти")

        choice = input("Выберите действие: ")
        try:
            if choice == '1':
                print_products(products)
            elif choice == '2':
                add_to_cart(user)
            elif choice == '3':
                print_cart(user)
            elif choice == '4':
                checkout(user)
            elif choice == '5':
                print(f"История заказов: {user['history']}")
            elif choice == '6':
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")


# Меню админа
def admin_menu():
    while True:
        print("Меню администратора:")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Изменить количество товара")
        print("4. Выйти")

        choice = input("Выберите действие: ")
        try:
            if choice == '1':
                add_product()
            elif choice == '2':
                delete_product()
            elif choice == '3':
                change_product_quantity()
            elif choice == '4':
                break
            else:
                print("Неверный выбор.")
        except Exception as e:
            print(f"Ошибка: {e}")


def print_products(product_list):
    for i, product in enumerate(product_list):
        print(f"{i+1}. {product['name']}: Цена - {product['price']}, Количество - {product['quantity']}")


def add_to_cart(user):
    print_products(products)
    try:
        product_index = int(input("Введите номер товара: ")) -1
        if 0 <= product_index < len(products):
            product = products[product_index].copy() 
            if product['quantity'] > 0:
                user['cart'].append(product)
                product['quantity'] -=1
                print(f"Товар '{product['name']}' добавлен в корзину.")
            else:
                print("Товар закончился")
        else:
            print("Неверный номер товара.")
    except ValueError:
        print("Некорректный ввод.")

def print_cart(user):
    if user['cart']:
        print("Ваша корзина:")
        for product in user['cart']:
            print(f"{product['name']}: Цена - {product['price']}")
        total = sum(product['price'] for product in user['cart'])
        print(f"Итоговая стоимость: {total}")
    else:
        print("Корзина пуста.")

def checkout(user):
    if user['cart']:
        total = sum(product['price'] for product in user['cart'])
        user['history'].append({'items': user['cart'].copy(), 'total': total})
        user['cart'] = []
        print(f"Заказ оформлен. Итоговая сумма: {total}")
    else:
        print("Корзина пуста.")

def add_product():
    name = input("Название: ")
    price = float(input("Цена: "))
    category = input("Категория: ")
    quantity = int(input("Количество: "))
    products.append({'name': name, 'price': price, 'category': category, 'quantity': quantity})
    print("Товар добавлен.")

def delete_product():
    print_products(products)
    try:
        product_index = int(input("Введите номер товара для удаления: ")) - 1
        if 0 <= product_index < len(products):
            del products[product_index]
            print("Товар удален.")
        else:
            print("Неверный номер товара.")
    except ValueError:
        print("Некорректный ввод.")


def change_product_quantity():
    print_products(products)
    try:
        product_index = int(input("Введите номер товара: ")) - 1
        if 0 <= product_index < len(products):
            new_quantity = int(input("Введите новое количество: "))
            products[product_index]['quantity'] = new_quantity
            print("Количество товара изменено.")
        else:
            print("Неверный номер товара.")
    except ValueError:
        print("Некорректный ввод.")


if __name__ == "__main__":
    user = authenticate()
    if user:
        if user['role'] == 'admin':
            admin_menu()
        else:
            user_menu(user)

