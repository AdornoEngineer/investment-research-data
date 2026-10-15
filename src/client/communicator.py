from pathlib import Path
from datetime import date

import requests
from requests import Response
from re import Match

from utils.validators import validate_date_format, validate_date_existence, validate_date_greater_than


class Communicator:
    
    def __int__() -> None:
        pass
    
    def get_selic(self, start_date:str = None, end_date:str = None) -> None:
        """
        Return the last year SELIC rate if no arguments are given.
        """
        
        LAST_YEAR:str = str(date.today().year - 1)
        start_date = start_date if start_date is not None else f"01/01/{LAST_YEAR}"
        end_date = end_date if end_date is not None else f"31/12/{LAST_YEAR}"
        
        for input_date in [start_date, end_date]:
            result: Match | None = validate_date_format(input_date)
            if result is None:
                """Exception Handling"""
                pass
            
            result: bool = validate_date_existence(input_date)
            if not result:
                """Exception Handling"""
                pass
        
        result:bool = validate_date_greater_than(start_date, end_date)
        if result:
            """Exceptiong Handling"""
            pass
        
        # Exception Strategy under development/technical decision.
        # Connection test
        #source_path:str = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=csv&dataInicial={start_date}&dataFinal={end_date}"
        #response:Response = requests.get(source_path, timeout=30)
        #Path("file.csv").write_bytes(response.content)


        return True