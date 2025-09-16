def print_product_names(product_names, index=0):
    if index < len(product_names):
        print(product_names[index])
        print_product_names(product_names, index + 1)


def find_product_by_name(products, product_name, index=0):
    product_keys = list(products.keys())

    if index >= len(product_keys):
        print("Товар не  знайдено.")
        return

    if product_keys[index] == product_name:
        product_info = products[product_name]
        print(f"Товар знайдено: {product_name} | Ціна: {product_info['Ціна']} грн | "
              f"Залишок: {product_info['Залишок']} шт.")
        return

    find_product_by_name(products, product_name, index + 1)
