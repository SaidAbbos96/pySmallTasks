class MyStack():
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[self.count() - 1]

    def count(self):
        return len(self.list)

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        self.index = self.count() - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()

        result = self.list[self.index]
        self.index -= 1
        return result


stact = MyStack()
stact.push(1)
stact.push(2)
stact.push(3)

print(stact.pop())
print(stact.peek())
print(stact.count())


stact.push(4)
stact.push(5)
stact.push(6)

for el in stact:
    print(el)