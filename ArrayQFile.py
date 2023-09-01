from array import array


class ArrayQ:

    def __init__(self):
        self.__array = array('l', [])

    def enqueue(self, x):
        self.__array.append(x)

    def dequeue(self):
        if self.isEmpty():
            print('Kön är tom')
        else:
            x = self.__array.pop(0)
            return x

    def isEmpty(self):
        if len(self.__array) < 1:
            return True
        else:
            return False

    def size(self):
        n = len(self.__array)
        return n
