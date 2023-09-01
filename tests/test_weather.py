from unittest import TestCase
from unittest.mock import patch
from weather.weather import get_temperatures


class WeatherTestCase(TestCase):

    def setUp(self) -> None:
        self.city = 'Acapulco'
        self.country = 'Mexico'


    @patch('weather.weather.send_request_temperature')
    def test_get_temperatures_succesfully(self, mock_send_request_temperature):
        temperatures = {
            'temperature': 7,
            'min_temperature': 7,
            'max_temperature':8,
            'date': '2023-01-25' ,
            'success': True
        }
        mock_send_request_temperature.return_value = temperatures
        expected_response = f"La temperatura es {temperatures['temperature']} con un mínimo de {temperatures['min_temperature']}"

        response = get_temperatures(
            city=self.city,
            country=self.country,
        )

        self.assertEqual(response, expected_response)

    @patch('weather.weather.send_request_temperature')
    def test_get_temperatures_failed(self, mock_send_request_temperature):
        mock_send_request_temperature.return_value = {
            'success': False
        }

        expected_response = "Hubo un error en la ejecución. Favor de intentar más tarde"

        response = get_temperatures(
            city=self.city,
            country=self.country,
        )

        self.assertEqual(response, expected_response)


    @patch('weather.weather.send_request_temperature')
    def test_city_is_empty_failed(self, mock_send_request_temperature):

        expected_response = "No se permiten valores vacíos, por favor verifica los datos que ingresaste"

        response = get_temperatures(
            city='',
            country=self.country,
        )

        self.assertEqual(response, expected_response)
        self.assertFalse(mock_send_request_temperature.called)

    @patch('weather.weather.send_request_temperature')
    def test_country_is_empty_failed(self, mock_send_request_temperature):
        expected_response = "No se permiten valores vacíos, por favor verifica los datos que ingresaste"

        response = get_temperatures(
            city=self.city,
            country='',
        )

        self.assertEqual(response, expected_response)
        self.assertFalse(mock_send_request_temperature.called)
