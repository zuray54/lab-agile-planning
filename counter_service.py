class CounterService:
    """Simple in-memory counter service."""

    def __init__(self):
        self._counter = 0

    def increment(self):
        self._counter += 1
        return self._counter

    def get_current_value(self):
        return self._counter
