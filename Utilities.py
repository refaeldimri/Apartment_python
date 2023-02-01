import os
from datetime import datetime
import dotenv

dotenv.load_dotenv()
os.chdir(os.getcwd())


class Utilities(object):
    file = None

    def write_to_file(self, string):
        """
        This function get a string and write it to self.file.
        :param string:
        :return None:
        """
        dotenv.load_dotenv()
        os.chdir(os.getcwd())
        self.file = open(os.getenv("FILENAME"), "a")
        string += datetime.now().strftime(", " + os.getenv("TIMESTAMP") + "\n")
        self.file.write(string)
        self.file.flush()
        self.file.close()

    def check_parameter_apartment(self, room_list, meter_price, price_arnona, discount_arnona):
        if not isinstance(meter_price, int) and not \
                isinstance(meter_price, float):
            raise ValueError(os.getenv("METER_PRICE_IS_NOT_NUMBER"))

        if meter_price <= 0:
            raise ValueError(os.getenv("METER_PRICE_IS_NOT-POSITIVE"))

        if not isinstance(price_arnona, int) and not \
                isinstance(price_arnona, float):
            raise ValueError(os.getenv("price_arnona_is_not_number"))

        if price_arnona <= 0:
            raise ValueError(os.getenv("price_arnona_is_not_positive"))

        if discount_arnona < 0 or discount_arnona > 1:
            raise ValueError(os.getenv("DISCOUNT_ARNONA_IS_NOT_FRACTION"))

        if not isinstance(discount_arnona, int) and not \
                isinstance(discount_arnona, float):
            raise ValueError(os.getenv("DISCOUNT_ARNONA_IS_NOT_NUMBER"))

        if not isinstance(room_list, list):
            raise ValueError(os.getenv("ROOM_LIST_IS_NOT_LIST"))

        if all([isinstance(item, int) for item in room_list]) and \
                all([isinstance(item, float) for item in room_list]):
            raise ValueError(os.getenv("ROOM_LIST_CONTAINS_CHARS_OR_NEG_NUMBER"))

