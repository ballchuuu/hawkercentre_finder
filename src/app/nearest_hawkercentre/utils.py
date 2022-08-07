from app.core.sqlite.client import sqlite3
from app.core.logger import logger
from app.core.config import settings

from app.nearest_hawkercentre.models import InputLatLon
from app.nearest_hawkercentre.models import HawkerCentre
from app.nearest_hawkercentre.models import NearestHawkerCentre

def get_nearest_hawkercentre(
    input: InputLatLon
) -> NearestHawkerCentre:

    # SQL query to return nearest hawker centre by geodesic distance
    query = f'''  
        SELECT 
            name,
            photourl
        FROM {settings.hawkercentre_table_name}
        ORDER BY get_distance(
            {input.latitude},
            {input.longitude},
            latitude_radians_cos,
            longitude_radians,
            latitude_radians_sin)
        LIMIT {input.num_hawkercentres}
    '''
    try:
        sqlite3.cur.execute(query)
        sql_result = sqlite3.cur.fetchall()
    except Exception as e:
        logger.error(f"SQLITE3 | {e} | {query}")
        # return empty list if error
        return NearestHawkerCentre(results=[])

    results = [HawkerCentre(name=r[0], photourl=r[1]) for r in sql_result]

    return NearestHawkerCentre(results=results)

