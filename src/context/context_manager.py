# --------------------------------------------------- #
#         Module Under Developmenmt (build 0)         #
# --------------------------------------------------- #

from contextvars import ContextVar

context_collector = ContextVar(
    "current_collector",
    default=None
)