from dataclasses import dataclass
from datetime import date
from typing import Dict


@dataclass
class ProviderDTO:
    tempeture: int
    min_tempeture: int
    max_tempeture: int

    @property
    def response(self) -> Dict:
        return {
            'temperature': self.tempeture,
            'min_temperature': self.min_tempeture,
            'max_temperature': self.max_tempeture,
            'date': str(date.today()),
            'success': True
        }
