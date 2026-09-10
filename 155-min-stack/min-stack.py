class MinStack:

    def __init__(self):
        self.st=[]
        self.mnst=[]

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mnst:
            self.mnst.append(value)
        else:
            self.mnst.append(min(value,self.mnst[-1]))

    def pop(self) -> None:
        self.mnst.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mnst[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
