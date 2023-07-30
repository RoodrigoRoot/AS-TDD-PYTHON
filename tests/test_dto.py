from unittest import TestCase

from api_ninja.weather_dto import ProviderDTO
from freezegun import freeze_time


class ProviderDTOTestCase(TestCase):

    @freeze_time('2023-01-25')
    def test_return_successfully_response(self):
        expected_values = {
            'temp': 7,
            'min_temp': 7,
            'max_temp': 8
        }
        expected_response = {
            'temperature': 7,
            'min_temperature': 7,
            'max_temperature':8,
            'date': '2023-01-25' ,
            'success': True
        }

        response_dto = ProviderDTO(
            tempeture=expected_values['temp'],
            min_tempeture=expected_values['min_temp'],
            max_tempeture=expected_values['max_temp'],
        ).response
        print(response_dto)

        self.assertDictEqual(response_dto, expected_response)

