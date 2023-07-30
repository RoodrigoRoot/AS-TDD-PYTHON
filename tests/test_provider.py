from unittest import TestCase
from unittest.mock import patch

from freezegun import freeze_time

from api_ninja.weather import send_request_temperature


class ProviderAPINinjaTestCase(TestCase):

    def setUp(self) -> None:
        self.city = 'Acapulco'
        self.country = 'Mexico'

    @patch('api_ninja.weather.requests')
    @freeze_time('2023-01-25')
    def test_get_temperature_succesfully(self, mock_requests):
        mock_requests.get.return_value.json.return_value = {
            "wind_speed": 5.66,
            "wind_degrees": 210,
            "temp": 7,
            "humidity": 87,
            "sunset": 1615658463,
            "min_temp": 7,
            "cloud_pct": 75,
            "feels_like": 2,
            "sunrise": 1615616341,
            "max_temp": 8
        }
        expected_response = {
            'temperature': 7,
            'min_temperature': 7,
            'max_temperature':8,
            'date': '2023-01-25' ,
            'success': True
        }


        response = send_request_temperature(
            city=self.city,
            country=self.country
        )

        self.assertDictEqual(response, expected_response)

    @patch('api_ninja.weather.requests')
    def test_get_temperature_fail(self, mock_requests):
        expected_response = {
            'success': False
        }

        response = send_request_temperature(
            city=self.city,
            country=self.country
        )

        mock_requests.get.return_value.raise_for_status.side_effect = Exception()

        self.assertDictEqual(response, expected_response)

