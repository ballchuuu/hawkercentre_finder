router_prefix = "/finder"

class TestNearestHawkerCentre:
    def test_successful_endpoint(self, auth_client):
        response = auth_client.post(
            f"{router_prefix}/nearest_hawkercentre",
            json={
                "latitude": 1.3,
                "longitude": 103.9,
                "num_hawkercentres": 5
            }
        )

        assert response.status_code == 200

    def test_wrong_input(self, auth_client):
        response = auth_client.post(
            f"{router_prefix}/nearest_hawkercentre",
            json={
                "test": 0
            }
        )

        assert response.status_code == 422

    def test_wrong_endpoint(self, auth_client):
        response = auth_client.post(
            "/test",
            json={
                "test": 0
            }
        )

        assert response.status_code == 404
