from typing import Dict

from api_ninja.weather import send_request_temperature


def get_temperatures(city: str, country: str) -> str:

    if not city or not country:
        return "No se permiten valores vacíos, por favor verifica los datos que ingresaste"

    temperatures = send_request_temperature(city=city, country=country)

    if not temperatures['success']:
        return "Hubo un error en la ejecución. Favor de intentar más tarde"

    return format_message_temperature_response(temperatures=temperatures)


def format_message_temperature_response(temperatures: Dict) -> str:
    return f"La temperatura es {temperatures['temperature']} con un mínimo de {temperatures['min_temperature']}"
