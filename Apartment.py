from abc import ABC, abstractmethod
import dotenv
import os
dotenv.load_dotenv()


class Apartment(ABC):

    def __init__(self, room_list, meter_price, price_arnona):
        """
        Constructor the class Apartment
        :param room_list:
        :param meter_price:
        :param price_arnona:
        """
        self.room_list = room_list
        self.price = meter_price
        self.price_arnona = price_arnona
        self._kitchen = "kitchen"

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
