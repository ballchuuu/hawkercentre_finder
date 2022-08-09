from typing import List

from pydantic import BaseModel

###
# Nearest HawkerCentre Endpoint Input
###
class InputLatLon(BaseModel):
    latitude: float
    longitude: float
    num_hawkercentres: int = 5

###
# Nearest HawkerCentre Endpoint Outputs
###
class HawkerCentre(BaseModel):
    name: str = ""
    photourl: str = None

class NearestHawkerCentre(BaseModel):
    results: List[HawkerCentre] = []

###
# Logging
###
class NearestHawkerCentreEndpointLog(BaseModel):
    param: InputLatLon
    response: NearestHawkerCentre
