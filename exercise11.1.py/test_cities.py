from city_functions import cityy_country

def test_city_country():
    result = cityy_country('Santiago', "Chile")
    assert result == 'Santiago, Chile'