class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here
        self.size = size
        self.queue = [None]*size
        self.rear = -1
        self.front = -1

    def enqueue(self, value: int) -> bool:
        # Write code here
        if (self.rear==(self.size-1) and self.front==0) or (self.front==self.rear+1):
            return False
        else:
             if self.front==-1:
                self.front=0
                self.rear=0
             else:
                #if self.rear==self.size-1:
                 #   self.rear=0
                #else:
                self.rear=(self.rear+1)%self.size
             self.queue[self.rear]=value
             return True
               
    def dequeue(self) -> bool:
        # Write code here
        if (self.front == -1): 
            return False
        else:
             if (self.front == self.rear):
                temp=self.queue[self.front]
                #del self.queue[self.front]
                self.front = -1
                self.rear = -1
                return True
             else:
                temp = self.queue[self.front]
                #del self.queue[self.front]
                self.front = (self.front + 1)%self.size
                return True
  
    def get_front(self) -> int:
        # Write code here
        if (self.front == -1): 
            return -1
        else:
            return self.queue[self.front]
        
    def get_rear(self):
        # Write code here
        if (self.front == -1): 
            return -1
        else:
            return self.queue[self.rear]
        
    def is_empty(self):
        # Write code here
        if self.front==-1:
            return True
        else:
            return False
        
    def is_full(self):
        # Write code here
        if (self.rear==(self.size-1) and self.front==0) or (self.front==self.rear+1):
            return True
        else:
            return False

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
