class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self.prev = self  # 자기로 향하는 링크
        
    def __str__(self):
        return str(self.key)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
        
    def __iter__(self):
        v = self.head.next
        while v.key != None:
            yield v
            v = v.next
        
    def __str__(self):
        return " -> ".join(str(v) for v in self)
        
    def __len__(self):
        return self.size
    
    def show(self):
        cur_node = self.head
        while cur_node.next.key != None:
            print(cur_node.key, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.key)
        
    def splice(self, a, b, x):
        if a==None or b==None or x==None:
            return
        ap = a.prev  #ap is previous node of a
        bn = b.next  #bn is next node of b
        # cut [a..b]
        ap.next = bn
        bn.prev = ap
        # insert [a..b] after x
        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
        
    def moveAfter(self, a, x):
        self.splice(a, a, x)
        
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
        
    def insertAfter(self, a, key):
        v = Node(key)
        self.splice(v, v, a)
        self.size += 1
        
    def insertBefore(self, a, key):
        v = Node(key)
        self.splice(v, v, a.prev)
        self.size += 1
        
    def pushFront(self, key):
        self.insertAfter(self.head, key)
        
    def pushBack(self, key):
        self.insertBefore(self.head, key)
        
    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        x.prev.next, x.next.prev = x.next, x.prev
        del x
        self.size -= 1
        
    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key
    
    def popBack(self):
        if self.head.next == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key        
        
    def search(self, key):
        v = self.head.next
        while v.key:
            if str(v.key) == str(key):
                return v
            v = v.next
        return v.key
        
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
        
    def first(self):
        if self.size == 0:
            return None
        return self.head.next
        
    def last(self):
        if self.size == 0:
            return None
        return self.head.prev
        
    def join(self, l):
        self.splice(l.head.next, l.head.prev, self.head.prev)
        
    def split(self, x):
        new_d = DoublyLinkedList()
        self.splice(x, self.head.prev, new_d.head)
        return new_d
    
    def printList(self):
        v = self.head.next
        print('h ->',end=' ')
        while v.key:
            print(v.key, '->', end=' ')
            v = v.next
        print('h')
