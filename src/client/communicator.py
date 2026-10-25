from pathlib import Path
from datetime import date

import requests
from requests import Response
from re import Match

from utils.validators import validate_date_format, date_to_standard, validate_date_existence, validate_future_date, validate_date_greater_than, validate_max_range
from exception.handler import ExceptionHandler
from context.context_manager import context_collector
from exception.error_codes import ErrorCodes

class Communicator:
    
    def __int__(self) -> None:
        pass
    
    def get_selic(self, start_date:str = None, end_date:str = None) -> None:
        """
        Return the last year SELIC rate if no arguments are given.
        
        """
        
        inputs = ["start_date", "end_date"]
        handler:ExceptionHandler = context_collector.get()
        flag:bool = False
        fd_date_flag:bool = False
        
        LAST_YEAR:str = str(date.today().year - 1)
        start_date = start_date if start_date is not None else f"01/01/{LAST_YEAR}"
        end_date = end_date if end_date is not None else f"31/12/{LAST_YEAR}"
        input_dates:list = [start_date, end_date]
        
        for pos, input_date in enumerate(input_dates):
            
            if not isinstance(input_date, str):
                handler.set_error(ErrorCodes.INVALID_FORMAT, inputs[pos])
                flag = True
                continue

            input_date = input_date.replace(" ", "")
            
            result: Match | None = validate_date_format(input_date)
            if result is None:
                
                handler.set_error(ErrorCodes.INVALID_FORMAT, inputs[pos])
                flag = True
                continue

            input_date = date_to_standard(input_date)
            input_dates[pos] = input_date
            
            result: bool = validate_date_existence(input_date)
            if not result:
                handler.set_error(ErrorCodes.NONEXISTENT_DATE, inputs[pos])
                flag = True
                continue
            
            if not flag:
                result:bool = validate_future_date(input_date)
                if result:
                    handler.set_error(ErrorCodes.FUTURE_DATE, inputs[pos])
                    fd_date_flag = True
        
        if not flag:
            result:bool = validate_date_greater_than(*input_dates)
            
            if result:
                handler.set_error(ErrorCodes.DATE_GRTN)
                flag = True
                
        if not flag:
            result:bool = validate_max_range(input_dates[0], input_dates[1])
            
            if result:
                handler.set_error(ErrorCodes.MAX_DATE)
                flag = True
            
        if not flag and not fd_date_flag:
            source_path:str = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=csv&dataInicial={input_dates[0]}&dataFinal={input_dates[1]}"
            #response:Response = requests.get(source_path, timeout=30)
            #Path("file.csv").write_bytes(response.content)
            return True
        
        return False