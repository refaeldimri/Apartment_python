from apartments.Apartment import Apartment
from apartments.HerzliyaApartment import HerzliyaApartment


if __name__ == '__main__':
    a = HerzliyaApartment([12, 13, 15, 12], 2000, 30)

    print(a.kitchen)
    a.kitchen = "fff"
    print(a.kitchen)

    print(a.calc_arnona())


    

