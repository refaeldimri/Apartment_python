import inspect
import json
import sys

import pytest
from apartments.Utilities import Utilities
from apartments.HerzliyaApartment import HerzliyaApartment
import dotenv
import os

dotenv.load_dotenv()
utilities = Utilities()


@pytest.fixture()
def herzliya_apartment():
    room_list = json.loads(os.getenv("LIST_ROOMS_SIZE"))
    meter_price = int(os.getenv("METER_PRICE"))
    price_arnona = int(os.getenv("HERZLIYA_ARNONA"))
    return HerzliyaApartment(room_list, meter_price, price_arnona)


@pytest.mark.test
def test_calc_arnona_herzliya(herzliya_apartment):
    """
    this test check the function which calculate herzliya's arnona
    by size of room and arnona's price
    :param herzliya_apartment:
    :return None:
    # """
    try:
        assert herzliya_apartment.calc_arnona() == 1380
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


@pytest.mark.test
def test_calc_apartment_price(herzliya_apartment):
    """
    This test check the function which calculate the apartment's price in herzliya
    by area of the apartment, the basic price, and the increase the price by area
    :param herzliya_apartment:
    :return price:
    # """
    try:
        assert herzliya_apartment.apartment_price() == 104400
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))


@pytest.mark.test
def test_get_set_room_list(herzliya_apartment):
    """
    this test check the function which calculate herzliya's arnona
    by size of room and arnona's price
    :param herzliya_apartment:
    :return None:
    # """
    try:
        assert herzliya_apartment.room_list == [12, 15, 13, 12]
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))

@pytest.mark.test
def test_get_set_room_list(herzliya_apartment):
    """
    this test check the function which calculate herzliya's arnona
    by size of room and arnona's price
    :param herzliya_apartment:
    :return None:
    # """
    try:
        assert herzliya_apartment.room_list == [12, 15, 13, 12]
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))

@pytest.mark.test
def test_apartment_area(herzliya_apartment):
    """
    this test check the function which calculate herzliya's arnona
    by size of room and arnona's price
    :param herzliya_apartment:
    :return None:
    # """
    try:
        assert herzliya_apartment.apartment_area() == 52
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_PASS"))
    except AssertionError:
        utilities.write_to_file(str(inspect.currentframe().f_code.co_name) + " " + os.getenv("TEST_FAILED"))
