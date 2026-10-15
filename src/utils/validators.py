import re
from typing import Any
from datetime import datetime

def validate_date_format(input_date:str) -> bool:
    
    return re.fullmatch(r"[0-9]{2}[/\\|-][0-9]{2}[/\\|-][0-9]{4}", str(input_date))

def validate_date_existence(input_date:str):

    try:
        datetime.strptime(input_date, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def validate_date_greater_than(start_date:str, end_date:str) -> None:
    
    f_start_date = datetime.strptime(start_date, "%d/%m/%Y")
    f_end_date = datetime.strptime(end_date, "%d/%m/%Y")
    
    return f_start_date > f_end_date