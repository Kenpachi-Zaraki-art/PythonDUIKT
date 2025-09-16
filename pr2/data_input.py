def input_product():
    products = {}
    while True:
        name = input("Введіть назву товару або 'stop' щоб закінчити: ")
        if name.lower() == 'stop':
            break
        try:
            price = float(input(f"Введіть ціну для {name}: "))
            stock = int(input(f"Введіть залишок на складі для {name}: "))
            products[name] = {'Ціна': price, 'Залишок': stock}
        except ValueError:
            print("Помилка вводу! Ціна має бути числом, залишок — цілим числом.")
    return products
