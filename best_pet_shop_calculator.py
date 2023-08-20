"""
This module calculates which pet shop option is cheaper given
a number of dogs and date.

Author: Marcela Prata Silvério
Date: 2023-08-20
"""

from datetime import datetime


class PriceTable:
    """
    A class representing a price table.

    Attributes:
        id (int): The price table identifier.
        week_day_price (float): The price during the week.
        weekend_day_price (float): The price during the weekend.
    """
    def __init__(self, id: int, week_day_price: float, weekend_day_price: float) -> None:
        """
        Initializes a PriceTable object.

        Parameters:
            id (int): The price table identifier.
            week_day_price (float): The price during the week.
            weekend_day_price (float): The price during the weekend.
        """
        self.id = id
        self.week_day_price = week_day_price
        self.weekend_day_price = weekend_day_price


class Product:
    """
    A class representing a product.

    Attributes:
        id (int): The product identifier.
        name (str): The name of the product.
        price_table (PriceTable): The price table of the product.
    """
    def __init__(self, id: int, name: str, price_table: PriceTable) -> None:
        """
        Initializes a Product object.

        Parameters:
            id (int): The product identifier.
            name (str): The name of the product.
            price_table (PriceTable): The price table of the product.
        """
        self.id = id
        self.name = name
        self.price_table = price_table

    def price_by_week_day(self, week_day: int) -> float:
        """
        The price of the product in the day specified

        Parameters:
            week_day (int): The week day number (0 - 6).
        Returns:
            float: The price in that day
        """
        return self.price_table.weekend_day_price if week_day in [5, 6] else self.price_table.week_day_price


class PetShop:
    """
    A class representing a pet shop.

    Attributes:
        id (int): The pet shop identifier.
        name (str): The name of the pet shop.
        distance (float): The distance in meters from you.
        products (list[Product]): The products of the petshop.
    """
    def __init__(self, id: int, name: str, distance: float, products: list[Product]) -> None:
        """
        Initializes a PetShop object.

        Parameters:
            id (int): The pet shop identifier.
            name (str): The name of the pet shop.
            distance (float): The distance in meters from you.
            products (list[Product]): The products of the petshop.
        """
        self.id = id
        self.name = name
        self.distance = distance
        self.products = products

    def calculate_total_price(self, week_day: int, products: dict[int]) -> float:
        """
        Calculates the total price of products chosen in the store.

        Parameters:
            week_day (int): The week day number (0 - 6).
            products (dict[int]): A list of dictionarys containing the producsts chosen
                (example: {[{'id': 1, 'quantity': 10}, {'id': 2, 'quantity': 5}]}).
        Returns:
            float: The total price of products
        """
        price = 0
        for product in products:
            price += list(filter(lambda pet_shop_product: pet_shop_product.id ==
                          product['id'], self.products))[0].price_by_week_day(week_day) * product['quantity']

        return price


class PetShopsManager:
    """
    A class representing an entity responsible for performing actions
    with pet shops.

    Attributes:
        pet_shops (list[PetShop]): A list of pet shops.
    """
    def __init__(self, pet_shops: list[PetShop]) -> None:
        """
        Initializes a PetShopManager object.

        Parameters:
            pet_shops (list[PetShop]): A list of pet shops.
        """
        self.pet_shops = pet_shops

    def calculate_best_pet_shop_option(self, week_day: int, small_dogs_quantity: int, big_dogs_quantity: int) -> dict[PetShop, float]:
        """
        Calculates the best pet shop option considering that the there are two products in a petshop:
        "Small Dog Bath" (id = 1) and "Big Dog Bath" (id = 2).

        Parameters:
            week_day (int): The week day number (0 - 6).
            small_dogs_quantity (int): The quantity of small dogs.
            big_dogs_quantity (int): The quantity of big dogs.
        Returns:
            dict[PestShop, float]: A dictionary containing the best pet shop and its price.
        """
        best_option = {
            'pet_shop': None,
            'price': None
        }

        for pet_shop in self.pet_shops:
            products = [{'id': 1, 'quantity': small_dogs_quantity}, {'id': 2, 'quantity': big_dogs_quantity}]
            price = pet_shop.calculate_total_price(week_day, products)

            if (best_option['price'] is None) or ((price < best_option['price']) or
                    ((price == best_option['price']) and (pet_shop.distance < best_option['pet_shop'].distance))):
                best_option = {
                    'pet_shop': pet_shop,
                    'price': price
                }

        return best_option


if __name__ == "__main__":
    pet_shops = [
        PetShop(
            1,
            "Meu Canino Feliz",
            2000,
            [
                Product(1, "Small Dog Bath", PriceTable(1, 20, 24)),
                Product(2, "Big Dog Bath", PriceTable(2, 40, 48)),
            ],
        ),
        PetShop(
            2,
            "Vai Rex",
            1700,
            [
                Product(1, "Small Dog Bath", PriceTable(1, 15, 20)),
                Product(2, "Big Dog Bath", PriceTable(2, 50, 55)),
            ],
        ),
        PetShop(
            3,
            "ChowChawgas",
            800,
            [
                Product(1, "Small Dog Bath", PriceTable(1, 30, 30)),
                Product(2, "Big Dog Bath", PriceTable(2, 45, 45)),
            ],
        ),
    ]

    try:
        bath_date, small_dogs_quantity, big_dogs_quantity = input('Entre com as informações: ').split()
        pet_shops_manager = PetShopsManager(pet_shops)

        best_option = pet_shops_manager.calculate_best_pet_shop_option(datetime.strptime(bath_date, "%d/%m/%Y").weekday(), int(small_dogs_quantity), int(big_dogs_quantity))

        print('============ Melhor Pet Shop ============')
        print('Nome: ' + best_option['pet_shop'].name, 'Preço: R$' + format(float(best_option['price']), '.2f'), sep=' | ')
        print('=========================================')
    except:
        print('================================================= Erro =================================================')
        print('A entrada dos dados deve seguir o padrão: <data> <quantidade de cães pequenos> <quantidade cães grandes>')
        print('Exemplo: 03/08/2018 3 5')
        print('========================================================================================================')
