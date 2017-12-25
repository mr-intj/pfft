from PyQt5.QtCore import QObject, pyqtSignal


class MruList(QObject):
    """Manages a most-recently-used list of strings"""

    # The list contents have changed - arguments are str:old_value, str:new_value
    changed = pyqtSignal(list, list)

    def __init__(self, items=None, max_len=8):
        """Constructor
        :type items: list of str
        :type max_len: int
        """
        super(MruList, self).__init__()

        if items is None:
            items = []
        assert max_len >= len(items)
        self._items = items
        self._max_len = max_len

    def __repr__(self):
        """Returns representation of the object
        :rtype str - e.g.: MruList(['/home/bob/clip2.wav', '/home/bob/clip1.wav'], 8)
        """
        return "{}({}, {})".format(self.__class__.__name__, self._items, self._max_len)

    def clear(self):
        """Erases all strings in the list"""
        old_value = self._items
        self._items = []

        if old_value != self.items:
            self.changed.emit(old_value, self._items)

    def contains(self, text):
        """Returns True if the specified string is in the list
        :type text: str - the string to locate
        :rtype bool - True if the specified string is in the list, otherwise False
        """
        lc_text = text.lower()
        lc_items = [item.lower() for item in self._items]

        return lc_text in lc_items

    def count(self):
        """Returns a count of strings in the list
        :rtype int - The size of the MRU list (0..max_len)
        """
        return len(self._items)

    def get(self, index):
        """Returns a string by index
        :type index: int - index of the string (0..[max_len-1])
        :rtype str - The string at the specified index, or an empty string if none exists
        """
        if 0 <= index < len(self._items):
            # ...remove and return it
            return self._items[index]

        return ''

    def index_of(self, text):
        """Returns the index of the specified string
        :type text: str - the string to locate
        :rtype int - The index of the specified string (0..[max_len-1]), or -1 if not found
        """
        lc_text = text.lower()
        lc_items = [item.lower() for item in self._items]

        return lc_items.index(lc_text) if lc_text in lc_items else -1

    def push(self, text):
        """Adds the specified string to the front of the list, or moves it to the front if it's already in the list.
        :type text: str - the string to add
        """
        # None, empty, or whitespace-only text is ignored
        text = '' if text is None else text.strip()
        if not text:
            return

        # Get the index of the item in the list, or -1 if not in list
        index = self.index_of(text)

        old_value = list(self._items)

        if index == -1:
            # Insert the new item at the front of the list
            self._items.insert(0, text)

            # truncate list to (max_len) items
            del self._items[self._max_len:]
        # If the item is in the list, but not already at the front...
        elif index > 0:
            # ...move it to the front
            self._items.insert(0, self._items.pop(index))

        if old_value != self._items:
            self.changed.emit(old_value, self._items)

    def pop(self, text):
        """Removes the specified string from the list."""
        # None, empty, or whitespace-only text is ignored
        text = '' if text is None else text.strip()
        if text:
            # Get the index of the item in the list, or -1 if not in list
            index = self.index_of(text)

            # If the item is in the list...
            if index >= 0:
                # ...remove item from the list and return it
                old_value = list(self._items)

                result = self._items.pop(index)

                self.changed.emit(old_value, self._items)

                return result

        return ''
