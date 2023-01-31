from abc import ABC, abstractmethod
import dotenv
import os
dotenv.load_dotenv()


class Apartment(ABC):

    def __init__(self, room_list, meter_price, price_arnona, discount_arnona=0):
        """
        Constructor the class Apartment
        :param room_list:
        :param meter_price:
        :param price_arnona:
        """
        if not isinstance(meter_price, int) and not isinstance(meter_price, float):
            raise ValueError(os.getenv("METER_PRICE_IS_NOT_NUMBER"))
        if meter_price <= 0:
            raise ValueError(os.getenv("METER_PRICE_IS_NOT-POSITIVE"))
        if not isinstance(price_arnona, int) and not isinstance(price_arnona, float):
            raise ValueError(os.getenv("price_arnona_is_not_number"))
        if price_arnona <= 0:
            raise ValueError(os.getenv("price_arnona_is_not_positive"))
        if discount_arnona < 0 or discount_arnona > 1:
            raise ValueError(os.getenv("DISCOUNT_ARNONA_IS_NOT_FRACTION"))
        if not isinstance(discount_arnona, int) and not isinstance(discount_arnona, float):
            raise ValueError(os.getenv("DISCOUNT_ARNONA_IS_NOT_NUMBER"))
        if not isinstance(room_list, list):
            raise ValueError(os.getenv("ROOM_LIST_IS_NOT_LIST"))
        if all([isinstance(item, int) for item in room_list]) and all([isinstance(item, float) for item in room_list]):
            raise ValueError(os.getenv("ROOM_LIST_CONTAINS_CHARS_OR_NEG_NUMBER"))

        self.room_list = room_list
        self.price = meter_price
        self.price_arnona = price_arnona
        self._kitchen = "kitchen"
        self.discount_arnona = discount_arnona

    # this method will be implemented by the inherited classes
    @abstractmethod
    def calc_arnona(self):
        """
        This function sum all the room in the apartment and calculate the arnona price
        :return int:
        """
        pass

    @property
    def kitchen(self):
        """
        Property GET to kitchen field
        :return self.kitchen:
        """
        return self._kitchen

    @kitchen.setter
    def kitchen(self, string):
        """
        SET value to kitchen field
        :param string:
        :return:
        """
        self._kitchen = string

    @kitchen.deleter
    def kitchen(self):
        """
        delete the kitchen field
        :return:
        """
        del self._kitchen

    def apartment_area(self):
        return sum(self.room_list)

    # this method will be implemented by the inherited classes
    @abstractmethod
    def apartment_price(self):
        pass
