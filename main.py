import json
import os
import dotenv
from apartments.HerzliyaApartment import HerzliyaApartment
from apartments.HaifaApartment import HaifaApartment
dotenv.load_dotenv()

if __name__ == '__main__':
    room_list = json.loads(os.getenv("LIST_ROOMS_SIZE"))
    meter_price = int(os.getenv("METER_PRICE"))
    price_arnona = int(os.getenv("HERZLIYA_ARNONA"))

    a = HerzliyaApartment(room_list, meter_price, price_arnona)
    print("==========================")

    print(room_list)
    print(meter_price)
    print(price_arnona)
    print("==========================")
    print(a.calc_arnona())
    print(a.apartment_area())
    print(a.apartment_price())
    print("==========================")

    # a.kitchen = "fff"
    # print(a.kitchen)
    #
    # print(a.calc_arnona()) ## 12*30 + 15*30 + 13*30 + 12*15 = 1380 arnona
    # print(a.apartment_area()) ## 12+13+15+12 = 52
    # print(a.apartment_price())  50*2000 + 2*2200=


    room_list = json.loads(os.getenv("LIST_ROOMS_SIZE"))
    meter_price = int(os.getenv("METER_PRICE"))
    price_arnona = int(os.getenv("HAIFA_ARNONA"))
    price_arnona_haifa = float(os.getenv("ARNONA_HAIFA"))

    b = HaifaApartment(room_list, meter_price, price_arnona, price_arnona_haifa)
    print("==========================")

    print(room_list)
    print(meter_price)
    print(price_arnona)
    print("==========================")
    print(b.calc_arnona())
    print(b.apartment_area())
    print(b.apartment_price())
    print("==========================")


    # print(a.calc_arnona()) ## 12*30 + 15*30 + 13*30 + 12*15 = 1380 arnona
    # print(a.apartment_area()) ## 12+13+15+12 = 52
    # print(a.apartment_price())  50*2000 + 2*2200=


    

