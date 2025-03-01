class IterableWithGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.start, self.end):
            yield i

# Приклад використання
iterable = IterableWithGenerator(1, 5)

for value in iterable:
    print(value)
