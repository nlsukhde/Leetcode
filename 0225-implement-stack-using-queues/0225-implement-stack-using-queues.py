from collections import deque
#appendleft and pop are only allowed
#appendleft will add to the left 
#pop will deal with the right

#appendright will add to the right
#popLeft will deal with the left

#only allowed to 
class MyStack:

    #addd to left remove from right
    # 2, 1
    # 1
    #actual stack 
    #2
    #1

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q1.appendleft(x)
        self.q2.appendleft(x)

    def pop(self) -> int:
        
        #once q2 is empty we stop
        #will exit once length of q2 is 1
        self.q1 = deque()
        while(len(self.q2) > 1):
            popped = self.q2.pop()
            self.q1.appendleft(popped)
            print("appended " + str(popped) + " to q1")
        
        #the final value will be the stack pop we need to return
        retval= self.q2.pop()

        #q1 has been holding our reformed list
        self.q2 = deque(self.q1)

        return retval

        
 
    def top(self) -> int:
        while(len(self.q2) > 1):

            self.q2.pop()
        
        retval = self.q2.pop()
        self.q2 = deque(self.q1)
        return retval
        

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()