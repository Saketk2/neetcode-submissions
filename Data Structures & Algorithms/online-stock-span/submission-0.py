class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        length = 1
        for val in range(len(self.stack) - 1, -1, -1):
            if self.stack[val] <= price:
                length += 1
            else:
                break
        self.stack.append(price)
        return length

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)