from apartments.Apartment import Apartment
import dotenv
import os

dotenv.load_dotenv()


class HerzliyaApartment(Apartment):

    def __init__(self, room_list, meter_price, price_arnona):
        super().__init__(room_list, meter_price, price_arnona)

    def calc_arnona(self):
        list_arnona_by_rooms = \
             [
                 room_size * self.price_arnona
                 if index != int(os.getenv("DISCOUNT_ROOM"))
                 else room_size * self.price_arnona * float(os.getenv("DISCOUNT"))
                 for index, room_size in enumerate(self.room_list)
             ]
        return sum(list_arnona_by_rooms)
