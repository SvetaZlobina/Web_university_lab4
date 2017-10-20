# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self._values_set = set()
        if isinstance(items, list):
            self._items_gen = (elem for elem in items)
        else:
            self._items_gen = items
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        for item in self._items_gen:
            is_str = isinstance(item, str)
            if (not is_str) and (item not in self._values_set):
                self._values_set.add(item)
                return item
            elif is_str:
                if self.ignore_case and (item.lower() not in self._values_set):
                    self._values_set.add(item.lower())
                    return item
                if (not self.ignore_case) and (item not in self._values_set):
                    self._values_set.add(item)
                    return item
        else:
            raise StopIteration()

    def __iter__(self):
        return self

