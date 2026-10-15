import logging

class ExceptionHandler(logging.Handler):
    
    def __init__(self) -> None:
        super().__init__()
        self.errors = list()
        
    @property
    def error(self) -> list:
        return self.errors
    
    @error.setter
    def error(self, error) -> None:
        self.errors.append(error)