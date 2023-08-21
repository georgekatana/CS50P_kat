class Jar:
    def __init__(self,capacity=12,size=0):
        if capacity<0:
            raise ValueError
        self._capacity = capacity
        self._size = size

    def __str__(self):
        cookie = "🍪"
        return f"{self._size*cookie}"

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("The Jar is full")

    def withdraw(self, n):
        if self.size >= n:
            self.size -= n
        else:
            raise ValueError("No more cookies left to withdraw")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

def main():
    jar = Jar()
    jar.deposit(int(input(": ")))
    jar.withdraw(int(input(": ")))

if __name__ == "__main__":
    main()
