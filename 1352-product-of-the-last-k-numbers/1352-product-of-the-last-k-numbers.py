class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1] # Prefix product array
        self.rightMostZeroIndex = float('inf')

    def add(self, num: int) -> None:
        # If num is 0, then extende the prefix array with the same last element
        # Change the index of right most 0 to current index
        if not num:
            self.prefix.append(self.prefix[-1])
            self.rightMostZeroIndex = len(self.prefix) - 1
        # Else normally calculate
        else:
            self.prefix.append(self.prefix[-1]*num)

    def getProduct(self, k: int) -> int:
        # Calculate the starting index from where numbers to be summed, according to k
        index = len(self.prefix) - k - 1
        # If there is a 0 to the right to starting index then simply return 0
        if index < self.rightMostZeroIndex:
            return 0
        # Otherwise calculate the return value
        return self.prefix[-1]//self.prefix[index]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)