def city_country(city, country, population):
    """Mengembalikan nama kota, negara, dan populasi."""
    return f"{city.title()}, {country.title()} – population {population}"

#jadikan parameter populasi opsional
def city_country(city, country, population=None):
    """Mengembalikan nama kota, negara, dan populasi jika tersedia."""

    if population:
        return f"{city.title()}, {country.title()} – population {population}"

    return f"{city.title()}, {country.title()}"

#tambah pengujian kedua
from city_functions import city_country


def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'


def test_city_country_population():
    result = city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile – population 5000000'