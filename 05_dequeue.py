class Deque(object):
    def __init__(self):
        self.__list = []
    def add_front(self, item):
        self.__list.insert(0,item)
    def add_rear(self, item):
        self._list.append(item)
    def pop_front(self):
        return self.__list.pop(0)
    def pop_rear(self):
        return self.__list.pop()
    def is_empty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    s = Deque()
    s.add_front(1)
    s.add_front(2)
    s.add_front(3)
    s.add_front(4)
    s.add_front(5)
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())