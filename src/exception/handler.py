# --------------------------------------------------- #
#         Module Under Developmenmt (build 0)         #
# --------------------------------------------------- #

from exception.error_codes import ErrorCodes

class ExceptionHandler:
    
    def __init__(self, max_error:int = 100) -> None:
        self._errors = list()
        self._max_errors = max_error
        
    def get_errors(self) -> list:
        return self._errors
    
    def set_error(self, error:ErrorCodes, input_field:str = None) -> None:
        if len(self._errors) >= self._max_errors:
            # Internal Logging operation
            return
        
        self._errors.append([error, input_field] if input_field is not None else [error])