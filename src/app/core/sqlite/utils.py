import math

# Function to return distance between 2 points
def get_distance(
    input_latitude: float, 
    input_longitude: float, 
    latitude_radians_cos: float, 
    longitude_radians: float, 
    latitude_radians_sin: float
) -> float:

    # multiplier for distance in km
    multiplier = 6371 
    
    return multiplier * \
        math.acos(
            math.cos(math.radians(input_latitude)) *
            latitude_radians_cos *
            math.cos(longitude_radians - math.radians(input_longitude) ) +
            math.sin(math.radians(input_latitude)) * latitude_radians_sin
        )