shopping_list = {}

def add_item(item, quantity=0):
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity

def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
    else:
        print(f"Товар '{item}' не найден в списке.")

def edit_quantity(item, quantity):
    if item in shopping_list:
        shopping_list[item] = quantity
    else:
        print(f"Товар '{item}' не найден в спиксе.")

def view_list():
    return shopping_list
