import pytest
from apartments.HerzliyaApartment import HerzliyaApartment


@pytest.fixture()
def herzliya_apartment():
    return HerzliyaApartment([12, 13, 15, 12], 2000, 30, 0)


@pytest.mark.test
def test_calc_arnona_herzliya(herzliya_apartment):
    """
    this test check the function which calculate herzliya's arnona
    by size of room and arnona's price
    :param herzliya_apartment:
    :return None:
    # """
    try:
        assert herzliya_apartment.calc_arnona() == 1380.0
    except ValueError as e:
        print(e)
