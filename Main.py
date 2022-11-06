'''
add_at_head, add_at_tail, add_at_index, get, delete_at_index, get, get_previous_next
10, 3, [1,2], 1, 1, 1, 1
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
        if self.head is None:
            self.add_at_head(data)
        
        else:
            itr = self.head
            
            while itr.next != self.head:
                itr = itr.next
            
            n = Node(data)
            n.next = self.head
            n.prev = itr
            itr.next = n
            self.head.prev = n
            return True
        

    def add_at_head(self, data) -> bool:
        # Write code here
        n = Node(data)
        
        if self.head is None:
            self.head = n
            n.next = n
            n.prev = n
            return True
        
        else:
            n.next = self.head
            n.prev = self.head.prev
            self.head.prev.next = n
            self.head.prev = n
            self.head = n
            return True
        

    def add_at_index(self, index, data) -> bool:
        # Write code here
        if index < 0 or index > self.getLength():
            return False
        
        elif index == 0:
            self.add_at_head(data)
            return True
        
        elif index == self.getLength():
            self.add_at_tail(data)
            return True
        
        else:
            itr = self.head
            
            for i in range(index - 1):
                itr = itr.next
            
            n = Node(data)
            
            n.next = itr.next
            n.prev = itr
            
            itr.next = n
            n.next.prev = n
            
            return True

    def get(self, index) -> int:
        # Write code here
        if index < 0 or index > self.getLength() or self.head is None:
            return -1
        
        elif index == 0:
            return self.head.data
        
        elif index == self.getLength():
            return self.head.prev.data
        
        else:
            itr = self.head
            
            for i in range(index):
                itr = itr.next
            
            return itr.data
        

    def delete_at_index(self, index) -> bool:
        # Write code here
        if index < 0 or index > self.getLength() or self.head is None:
            return False
        
        else:
            itr = self.head
            
            for i in range(index):
                itr = itr.next
            
            itr.prev.next = itr.next
            itr.next.prev = itr.prev
            
            if index == 0:
                self.head = itr.next
            
            return True

    def get_previous_next(self, index) -> list:
        # Write code here
        if index < 0 or index > self.getLength():
            return False
        
        l = []
        
        itr = self.head
        
        for i in range(index):
            itr = itr.next
        
        l.append(itr.prev.data)
        l.append(itr.next.data)
        
        return l
    
    def getLength(self):
        
        if self.head is None:
            return 0
        
        elif self.head.next == self.head:
            return 1
        
        else:
            length = 0
            itr = self.head
            while itr.next != self.head:
                length += 1
                itr = itr.next
            
            return length + 1


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
