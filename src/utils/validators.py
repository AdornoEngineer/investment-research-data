import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

def validate_date_format(input_date:str) -> bool:
    
    return re.fullmatch(r"[0-9]{2}[/\\|-][0-9]{2}[/\\|-][0-9]{4}", str(input_date))

def date_to_standard(input_date:str) -> str:
    
    result:str = re.sub(r"[\\|\-]", "/", input_date)
    
    return result

def validate_date_existence(input_date:str) -> bool:

    try:
        datetime.strptime(input_date, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def validate_future_date(input_date:str) -> bool:
    
    target_date:datetime = datetime.strptime(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
    input_date_cleared:datetime = datetime.strptime(input_date, "%d/%m/%Y")
    
    if input_date_cleared > target_date:
        return True
    return False       
    
def validate_date_greater_than(start_date:str, end_date:str) -> bool:
    
    f_start_date = datetime.strptime(start_date, "%d/%m/%Y")
    f_end_date = datetime.strptime(end_date, "%d/%m/%Y")
    
    return f_start_date > f_end_date

def validate_max_range(start_date:str, end_date:str, max_y:int = 10, max_m:int = 0, max_d: int = 0) -> bool:
    
    f_start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
    f_end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
    
    delta = relativedelta(f_end_date, f_start_date)
    
    if delta.years > max_y:
        return True
    elif delta.years == max_y and delta.months > max_m:
        return True
    elif delta.years == max_y and delta.months == max_m and delta.days > max_d:
        return True

    return False