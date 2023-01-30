from apartments.Apartment import Apartment
from apartments.HerzliyaApartment import HerzliyaApartment


if __name__ == '__main__':
    a = HerzliyaApartment([12, 13, 15, 12], 1000, 30)

    print(a.kitchen)
    a.kitchen = "fff"
    print(a.kitchen)

    print(a.calc_arnona()) ## 12*30 + 13*30 + 15*30 + 12*15 = 1380 arnona
    print(a.apartment_area()) ## 12+13+15+12 = 52
    print(a.apartment_price())  ## 50 * 1000 + 2 * 1000 * 1.1 = 52200


    

