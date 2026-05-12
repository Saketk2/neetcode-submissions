class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        length = 0
        index = len(self.stack) - 1
        if self.stack:
            while index >= 0 and self.stack[index][0] <= price:
                if index == 0:
                    length += 1
                    break
                length += self.stack[index][1]
                index -= self.stack[index][1]
            self.stack.append((price, length + 1))
        else:
            self.stack.append((price, 1))
        return length + 1


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)