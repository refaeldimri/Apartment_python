import json
from apartments.Apartment import Apartment
import dotenv
import os

dotenv.load_dotenv()


class HerzliyaApartment(Apartment):

    def __init__(self, room_list, meter_price, price_arnona, discount_arnona=0):
        """
        Constructor of HerzliyaApartment class
        :param room_list:
        :param meter_price:
        :param price_arnona:
        """
        super().__init__(room_list, meter_price, price_arnona, discount_arnona)

    def calc_arnona(self):
        """
        This function calculate the house's arnona by the size of the rooms
        and the arnona price per meter, the fourth room get discount of 50%
        :return: sum of arnona by all the rooms
        """
        list_arnona_by_rooms = \
            [
            room_size * self.price_arnona
            if index != int(os.getenv("DISCOUNT_ROOM"))
            else room_size * self.price_arnona * float(os.getenv("DISCOUNT"))
            for index, room_size in enumerate(self.room_list)
            ]

        return sum(list_arnona_by_rooms) * (1 - self.discount_arnona)

    def apartment_price(self):
        """
        This function calculate the apartment's price by AREA and price per meter
        :return int:
        """
        apartment_size = json.loads(os.getenv("LIST_OF_SIZE_APARTMENT"))
        area = self.apartment_area()
        price = 0
        if area > apartment_size[2]:
            price = apartment_size[1] * self.meter_price + apartment_size[1] * \
                    self.meter_price * float(os.getenv("FIRST_INCREASE_PRICE_BY_PERCENT"))
            price = price + (float(os.getenv("SECOND_INCREASE_PRICE_BY_PERCENT")) *
                             self.meter_price * (area - apartment_size[2]))
        else:
            if apartment_size[1] <= area <= apartment_size[2]:
                price += apartment_size[1] * self.meter_price + (area - apartment_size[1]) * self.meter_price * 1.1
            else:
                price += area * self.meter_price
        return price

