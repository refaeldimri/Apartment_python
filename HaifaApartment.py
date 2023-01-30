from apartments.Apartment import Apartment
import dotenv
import os

dotenv.load_dotenv()


class HaifaApartment(Apartment):

    def __init__(self, room_list,
                 meter_price, price_arnona, discount_arnona=1):
        """
        Constructor the HerzliyaApartment class
        :param room_list:
        :param meter_price:
        :param price_arnona:
        """
        super().__init__(room_list, meter_price,
                         price_arnona, discount_arnona)

    def calc_arnona(self):
        """
        This function calculate the house's arnona by the size of the rooms
        and the arnona price per meter, the forth room get discount of 50%
        :return: sum of arnona by all the rooms
        """
        list_arnona_by_rooms = \
            [
                 room_size * self.price_arnona
                 if index != int(os.getenv("DISCOUNT_ROOM"))
                 else room_size * self.price_arnona * float(os.getenv("DISCOUNT"))
                 for index, room_size in enumerate(self.room_list)
            ]
        return sum(list_arnona_by_rooms) * self.discount_arnona

    def apartment_price(self):
        pass
