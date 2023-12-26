class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)  
        self.pointer = 1 

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        chunk = []
        if idKey == self.pointer:
            while self.pointer < len(self.stream) and self.stream[self.pointer]:
                chunk.append(self.stream[self.pointer])
                self.pointer += 1
        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)