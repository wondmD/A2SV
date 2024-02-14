class BrowserHistory:

    def __init__(self, homepage: str):
        self.hompage = [homepage]
        self.currunt = 0


    def visit(self, url: str) -> None:
        self.hompage = self.hompage[:self.currunt+1]
        self.hompage.append(url)
        self.currunt = len(self.hompage) - 1

       
    def back(self, steps: int) -> str:
        if self.currunt - steps <= 0:
            self.currunt = 0
        else:
            self.currunt -= steps
        return self.hompage[self.currunt]

    def forward(self, steps: int) -> str:
        self.currunt += steps
        if self.currunt >= len(self.hompage):
            self.currunt = len(self.hompage) - 1

        return self.hompage[self.currunt]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)