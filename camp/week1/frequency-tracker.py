class FrequencyTracker:

    def __init__(self):
        self.d =defaultdict(int)
        self.df =defaultdict(int)
    def add(self, number: int) -> None:
        self.df[self.d[number]] -=1
        self.d[number] +=1
        self.df[self.d[number]] +=1

    def deleteOne(self, number: int) -> None:
        self.df[self.d[number]] -=1
        self.d[number] = max(0, self.d[number]-1)
        self.df[self.d[number]] +=1
    def hasFrequency(self, frequency: int) -> bool:
        return (self.df[frequency] > 0)

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)