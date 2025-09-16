from data_input import input_product
from calculations import calculate_stock_value, calculate_discount
from general import print_product_names, find_product_by_name


def main():
    # Введення товарів
    products = input_product()
    print("\n=== Введені товари ===")
    for product, details in products.items():
        print(f"{product}: Ціна = {details['Ціна']} грн | Залишок = {details['Залишок']} шт.")

    # Розрахунок вартості залишку
    print("\n=== Вартість залишків ===")
    calculate_stock_value(products)

    # Розрахунок знижок
    print("\n=== Знижки ===")
    calculate_discount(products)

    # Виведення списку товарів
    print("\n=== Список товарів ===")
    product_names = list(products.keys())
    print_product_names(product_names)

    # Приклад пошуку товару
    print("\n=== Пошук  товару ===")
    while True:
        search_name = input("Введіть назву товару для пошуку (або 'stop' для виходу): ")
        if search_name.lower() == "stop":
            break
        find_product_by_name(products, search_name)


if __name__ == "__main__":
    main()
