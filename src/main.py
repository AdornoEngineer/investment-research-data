# --------------------------------------------------- #
#         Module Under Developmenmt (build 0)         #
# --------------------------------------------------- #

from client.communicator import Communicator
from exception.handler import ExceptionHandler
from context.context_manager import context_collector

if __name__ == "__main__":
    handler = ExceptionHandler()
    token = context_collector.set(handler)
    
    communicator = Communicator()
    result = communicator.get_selic("01/01/2025", "31/12/2025")
    
    errors = handler.get_errors()