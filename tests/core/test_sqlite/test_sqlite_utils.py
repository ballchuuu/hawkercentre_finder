from app.core.sqlite.utils import get_distance
import math

def test_distance():

    # calculating dist between (1N,0E) and (2N,0E)
    input_latitude = 1.0
    input_longitude = 1.0
    latitude_radians_cos = math.cos(math.radians(2.0))
    longitude_radians = math.radians(1.0)
    latitude_radians_sin = math.sin(math.radians(2.0))

    result = get_distance(    
        input_latitude,
        input_longitude,
        latitude_radians_cos,
        longitude_radians,
        latitude_radians_sin)
    
    # result is based on US National Hurriance Centre website
    # https://www.nhc.noaa.gov/gccalc.shtml
    assert round(result) == 111