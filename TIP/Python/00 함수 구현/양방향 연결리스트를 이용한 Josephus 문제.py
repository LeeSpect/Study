class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.next = self.prev = self
        self.value = value
    def __str__(self):
        return str(self.key)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v) for v in self)
    def __len__(self):
        return self.size

    def show(self):
        cur_node = self.head
        while cur_node.next.key != None:
            print(cur_node.key, end = ' -> ')
            cur_node = cur_node.next
        print(cur_node.key)
    
    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        ap = a.prev
        bn = b.next
        ap.next = bn
        bn.prev = ap
        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
        
    def moveAfter(self, a, x):
        self.splice(a, a, x)
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
        
    def insertAfter(self, x, key):
        v = Node(key)
        self.splice(v, v, x)
        self.size += 1
    def insertBefore(self, x, key):
        v = Node(key)
        self.splice(v, v, x.prev)
        self.size += 1
        
    def pushFront(self, key):
        self.insertAfter(self.head, key)
    def pushBack(self, key):
        self.insertBefore(self.head, key)
        
    def remove(self, x):
        if x == None or self.head == x:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
        self.size -= 1
        
    def popFornt(self):
        self.remove(self.head.next)
    def popBack(self):
        self.remove(self.head.prev)

def josephus(n, k):
    L = DoublyLinkedList()
    for key in range(1, n+1):
        L.pushBack(key)
    
    first = L.head.next
    while len(L) > 1:
        for i in range(k):
            if first.next.key == None:
                first = first.next.next
            else:
                first = first.next
        if first.prev.key == None:
            L.remove(first.prev.prev)
        else:
            L.remove(first.prev)
    if first.key != None:
        return first.key
    else:
        return first.next.key
            

n, k = map(int,input().split())
print(josephus(n, k))
