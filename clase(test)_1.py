def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_empty_list():
    assert calculate_total([]) == 0


def test_single_product():
    products = [{"name": "notebook", "price": 5}]
    assert calculate_total(products) == 5


def test_multiple_products():
    products = [{"name": "notebook", "price": 5}, {"name": "book", "price": 7}]
    assert calculate_total(products) == 12


if __name__ == "__main__":
    test_empty_list()
    test_single_product()
    test_multiple_products()
    print("Todas las pruebas pasaron")
