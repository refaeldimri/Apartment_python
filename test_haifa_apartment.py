import inspect
import json
import sys

import pytest
from apartments.Utilities import Utilities
from apartments.HaifaApartment import HaifaApartment
import dotenv
import os

dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def haifa_apartment():
    room_list = json.loads(os.getenv("LIST_ROOMS_SIZE"))
    meter_price = float(os.getenv("METER_PRICE"))
    price_arnona = float(os.getenv("HAIFA_ARNONA"))
    price_arnona_haifa = float(os.getenv("ARNONA_HAIFA"))
    return HaifaApartment(room_list, meter_price, price_arnona, price_arnona_haifa)


@pytest.mark.test
def test_calc_arnona_haifa(haifa_apartment):
    """
    this test check the function which calculate haifa's arnona
    by size of room and arnona's price
    :param haifa_apartment:
    :return None:
    # """
    try:
        assert haifa_apartment.calc_arnona() == 874
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


@pytest.mark.test
def test_calc_apartment_price(haifa_apartment):
    """
    This test check the function which calculate the apartment's price in haifa
    by area of the apartment, the basic price, and the increase the price by area
    :param haifa_apartment:
    :return price:
    # """
    try:
        assert haifa_apartment.apartment_price() == 104000
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


@pytest.mark.test
def test_get_set_room_list(haifa_apartment):
    """
    this test check the function which calculate haifa's arnona
    by size of room and arnona's price
    :param haifa_apartment:
    :return None:
    # """
    try:
        assert haifa_apartment.room_list == [12, 15, 13, 12]
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


@pytest.mark.test
def test_apartment_area(haifa_apartment):
    """
    this test check the function which calculate herzliya's arnona
    by size of room and arnona's price
    :param herzliya_apartment:
    :return None:
    # """
    try:
        assert haifa_apartment.apartment_area() == 52
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
