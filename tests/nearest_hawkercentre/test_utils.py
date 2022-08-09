from unittest.mock import patch

from app.nearest_hawkercentre.models import InputLatLon
from app.nearest_hawkercentre.models import NearestHawkerCentre
from app.nearest_hawkercentre.utils import get_nearest_hawkercentre

def test_successful_get_nearest_hawkercentre():
    test_input = InputLatLon(
        latitude=1.3,
        longitude=103.9,
        num_hawkercentres=5
    )
    test = get_nearest_hawkercentre(test_input)

    assert len(test.results) == 5
    assert type(test) == NearestHawkerCentre

@patch("app.nearest_hawkercentre.utils.settings")
def test_invalid_table_get_nearest_hawkercentre(mock_settings):
    mock_settings.hawkercentre_table_name = "test"
    test_input = InputLatLon(
        latitude=1.3,
        longitude=103.9,
        num_hawkercentres=5
    )
    test = get_nearest_hawkercentre(test_input)

    assert len(test.results) == 0
    assert type(test) == NearestHawkerCentre
