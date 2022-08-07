from app.core.logger import logger
from app.nearest_hawkercentre.models import InputLatLon
from app.nearest_hawkercentre.models import NearestHawkerCentre
from app.nearest_hawkercentre.models import NearestHawkerCentreEndpointLog
from app.nearest_hawkercentre.utils import get_nearest_hawkercentre
from fastapi import APIRouter

router = APIRouter()

@router.post("/nearest_hawkercentre", response_model=NearestHawkerCentre)
async def nearest_hawkercentre(
    param: InputLatLon
):

    response = get_nearest_hawkercentre(param)

    logger.info(
        NearestHawkerCentreEndpointLog(
            param=param,
            response=response
        ).json()
    )
    return response
