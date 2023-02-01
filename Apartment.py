import inspect
import sys
from abc import ABC, abstractmethod
import dotenv
import os
from apartments.Utilities import Utilities

dotenv.load_dotenv()


class Apartment(ABC):
    utilities = Utilities()

    def __init__(self, room_list, meter_price,
                 price_arnona, discount_arnona=0):
        """
        Constructor the class Apartment
        :param room_list:
        :param meter_price:
        :param price_arnona:
        """
        try:
            self.utilities.check_parameter_apartment(room_list, meter_price, price_arnona, discount_arnona)
        except ValueError:
            self.utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + "object is does not created")
            sys.exit(1)
        self._room_list = room_list
        self._meter_price = meter_price
        self._price_arnona = price_arnona
        self._kitchen = os.getenv("KITCHEN_TYPE")
        self._discount_arnona = discount_arnona

    # this method will be implemented by the inherited classes
    @abstractmethod
    def calc_arnona(self):
        """
        This function sum all the room in the apartment and calculate the arnona price
        :return int:
        """
        pass

    @property
    def room_list(self):
        """
        Property GET to room_list field
        :return self.room_list:
        """
        return self._room_list

    @room_list.setter
    def room_list(self, list_of_rooms):
        """
        SET value to room_list field
        :param list_of_rooms:
        :return:
        """
        self._room_list = list_of_rooms

    @property
    def meter_price(self):
        """
        Property GET to meter_price field
        :return self.room_list:
        """
        return self._meter_price

    @meter_price.setter
    def meter_price(self, price_per_meter):
        """
        SET value to meter_price field
        :param price_per_meter:
        :return:
        """
        self.meter_price = price_per_meter

    @property
    def price_arnona(self):
        """
        Property GET to price_arnona field
        :return self.price_arnona:
        """
        return self._price_arnona

    @price_arnona.setter
    def price_arnona(self, arnona):
        """
        SET value to price_arnona field
        :param price_arnona:
        :return:
        """
        self._price_arnona = arnona

    @property
    def discount_arnona(self):
        """
        Property GET to price_arnona field
        :return self.price_arnona:
        """
        return self._discount_arnona

    @discount_arnona.setter
    def discount_arnona(self, discount_arnona):
        """
        SET value to price_arnona field
        :param price_arnona:
        :return:
        """
        self._discount_arnona = discount_arnona

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
        """
        This function get list of room size
        and return the size of the apartment
        :return sum of apartment area:
        """
        return sum(self._room_list)

    # this method will be implemented by the inherited classes
    @abstractmethod
    def apartment_price(self):
        pass
