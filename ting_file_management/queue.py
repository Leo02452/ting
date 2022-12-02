class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self._data != []:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if index not in range(len(self._data)):
            raise IndexError
        return self._data[index]
