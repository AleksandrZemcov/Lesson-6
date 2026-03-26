import auth


def create_item():
    title = input('Введите название авто')
    price = int(input('Введите стоимость авто'))
    id = get_max_id() + 1
    new_item = {
        'title': title,
        'price': price,
        'id': id
    }
    items.append(new_item)
    print('Товар успешно добавлен в каталог!')

def delete_item():
    id_removed = int(input('Введите ID товара, который требуется удалить'))
    for item in items:
        if item['id'] == id_removed:
            items.remove(item)
            print('Товар успешно удален из каталога!')
            for cart_item in cart:
                if cart_item['id'] == id_removed:
                    cart.remove(cart_item)
                    print('Товар успешно удален из корзины!')
            break
    else:
        print('Товар не найден!')


def change_item():
    """Изменение стоимости товара"""
    id_edit = int(input('Введите ID товара, для которого меняем цену\n'))
    for item in items:
        if item['id'] == id_edit:
            item['price'] = int(input('Введите новую цену'))
            print('Стоимость товара обновлена!')
            break
    else:
        print("Вы ввели несуществующий ID")
