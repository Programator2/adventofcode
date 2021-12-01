from collections import UserList


class BlessedList(UserList):
    """A more or less complete user-defined wrapper around list objects."""
    def _ensure_index(self, i):
        """Ensure that `i` exists in the list"""
        if i >= len(self.data):
            self.data.extend([0] * (i - len(self.data) + 1))

    def __getitem__(self, i):
        if isinstance(i, slice):
            self._ensure_index(i.stop - 1)
            return self.__class__(self.data[i])
        else:
            self._ensure_index(i)
            return self.data[i]

    def __setitem__(self, i, item):
        self._ensure_index(i)
        self.data[i] = item

    def insert_at(self, items, i):
        self._ensure_index(i + len(items) - 1)
        self.data[i:i+len(items)] = items
