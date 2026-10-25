# --------------------------------------------------- #
#         Module Under Developmenmt (build 0)         #
# --------------------------------------------------- #

from enum import Enum

class ErrorCodes(Enum):
    
    # Critical Errors:
    INVALID_FORMAT:str = "TYP_0001"
    
    # Accumulative Errors:
    NONEXISTENT_DATE:str = "VAL_0001"
    DATE_GRTN:str = "VAL_0002"
    FUTURE_DATE:str = "VAL_0003"
    RNG_NOT_SUPPORTED = "VAL_0004"
    MAX_DATE = "VAL_0005"