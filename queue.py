
class Elem:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.root = None
        self.length = 0

    def enqueue(self, value):
        if self.length == 0:
            self.root = Elem(value, None)
            self.length = 1
            return
        else:
            if self.length == 1:
                self.root.next = Elem(value, None)
                self.length = 2
                return
            else:
                if self.length >= 2:
                    current = self.root
                    while current.next != None:
                        current = current.next
                    current.next = Elem(value, None)
                    self.length = self.length + 1
                return

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            value = self.root.value
            self.root = self.root.next
            self.length = self.length - 1
            print("Значение удаленного элемента =", value)

    def size(self):
        print("Длинна очереди =", self.length)

    def print(self):
        qu = self.root
        print ("Элементы очереди = ")
        while qu != None:
            print(qu.value, end='')
            qu = qu.next
        print()
