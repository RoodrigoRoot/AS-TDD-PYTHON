import requests
from typing import Dict
from api_ninja.weather_dto import ProviderDTO


def send_request_temperature(city: str, country: str) -> Dict:
    try:
        api_url = f"https://api.api-ninjas.com/v1/weather?city={city}&country={country}"
        headers = {'X-Api-Key':'HmyzCASvWeLnERQ3gGbI2w==H5531EtNmz4kHADA'}

        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        result = response.json()

        return ProviderDTO(
            tempeture=result['temp'],
            min_tempeture=result['min_temp'],
            max_tempeture=result['max_temp'],
        ).response

    except Exception as e:
        print(f"Error: {e}")
        return { 'success': False }
