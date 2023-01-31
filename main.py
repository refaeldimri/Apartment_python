import json
import os
from apartments.Apartment import Apartment
from apartments.HerzliyaApartment import HerzliyaApartment
from apartments.HaifaApartment import HaifaApartment


if __name__ == '__main__':
    try:
        a = HerzliyaApartment([12, 13, 15, 12], 30, 30, 0)
    except ValueError as e:
        print(e)
    # res = json.loads(os.getenv("LIST_ROOMS_SIZE"))

    #
    # a.kitchen = "fff"
    # print(a.kitchen)
    #
    print(a.calc_arnona()) ## 12*30 + 13*30 + 15*30 + 12*15 = 1380 arnona
    print(a.apartment_area()) ## 12+13+15+12 = 52
    print(a.apartment_price())  ## 50 * 1000 + 2 * 1000 * 1.1 = 52200


    

