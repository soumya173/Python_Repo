class PriorityQueueBase:
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def _empty(self):
        return len(self) == 0