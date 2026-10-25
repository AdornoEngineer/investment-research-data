from contextvars import ContextVar

context_collector = ContextVar(
    "current_collector",
    default=None
)