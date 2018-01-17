class Queue(object):
    def __init__(self):
        self.__list = []
    def enqueue(self,item):
        self.__list.append(item)
    def dequeue(self):
        return self.__list.pop(0)
    def is_empty():
        return self.__list == []
    def size():
        return len(self.__list)

if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())