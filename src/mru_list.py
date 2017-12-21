class MruList:
    def __init__(self, items=[], max_len=8):
        assert max_len >= len(items)
        self.items = items
        self.max_len = max_len

    def clear(self):
        self.items = []

    def count(self):
        return len(self.items)

    def get(self, index):
        if 0 <= index < len(self.items):
            # ...remove and return it
            return self.items[index]

        return ''

    def index_of(self, text):
        lc_text = text.lower()
        lc_items = [item.lower() for item in self.items]

        return lc_items.index(lc_text) if lc_text in lc_items else -1

    def push(self, text):
        # None, empty, or whitespace-only text is ignored
        text = '' if text is None else text.strip()
        if not text:
            return

        # Get the index of the item in the list, or -1 if not in list
        index = self.index_of(text)

        if index == -1:
            # Insert the new item at the front of the list
            self.items.insert(0, text)

            # truncate list to (max_len) items
            del self.items[self.max_len:]
        # If the item is in the list, but not already at the front...
        elif index > 0:
            # ...move it to the front
            self.items.insert(0, self.items.pop(index))

    def pop(self, text):
        # None, empty, or whitespace-only text is ignored
        text = '' if text is None else text.strip()
        if text:
            # Get the index of the item in the list, or -1 if not in list
            index = self.index_of(text)

            # If the item is in the list...
            if index >= 0:
                # ...remove and return it
                return self.items.pop(index)

        return ''
