class ATM:

    def __init__(self):
        self.banknotes=[0,0,0,0,0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        out_order = [500,200,100,50,20]
        with_amount = [0,0,0,0,0]
        for i in range(5):
            a = self.banknotes[abs(i-4)]
            with_amount[i] = amount//out_order[i]
            if with_amount[i] > a:
                with_amount[i] = a
                amount -= a*out_order[i]
            else :
                amount = amount % out_order[i]
        if amount == 0:
            for i in range(5):
                if self.banknotes[abs(4-i)] - with_amount[i] < 0:
                    return ([-1])
            for i in range(5):
                self.banknotes[abs(4-i)] -= with_amount[i]
            return (with_amount[::-1])
        else :
            return ([-1])
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)