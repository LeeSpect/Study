class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key) # print(node)일 경우 str((self.key, self.value))

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
    
    def __str__(self):
        return " -> ".join(str(v) for v in self)

    def pushFront(self, key, value=None):  # O(1)
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key, value=None):  # O(n)
        new_node = Node(key, value)
        tail = self.head
        if tail == None:  # if len(self)==0:
            self.head = new_node
        else:
            while tail.next!= None:  # tail 노드 찾기
                tail = tail.next
            tail.next = new_node
        self.size+=1

        # v = Node(key)
        # if len(self) == 0:
        #   self.head = v
        # else:
        #   tail=self.head
        #   while tail.next != None:...

    def popFront(self):  # O(1)
        if self.head == None:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key  # or return (key, value)

    def popBack(self):  # O(n)
        if len(self) == 0:
            return None
        else:
            prev, tail, = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = tail.next
            self.size -= 1
            key = tail.key
            del tail
            return key  # or return (key, value)

    def search(self, key):  # O(n)
        v = self.head
        while v != None:
            if v.key == key: return v
            v = v.next
        return v  # None
    
    # def search(self, key):  # for Loop 이용
    #     for v in self:
    #         if v.key == key: return v
    #     return None

    def remove(self, v):
        if self.size==0 or self.search(v)==None:
            return False
        elif self.head == v:
            self.popFront()
            return True
        else:
            prev,tail = None, self.head
            while tail.next != v:
                prev = tail
                tail = tail.next
            prev = tail
            tail = tail.next
            if tail.next == None:
                self.popBack()
            else:
                prev.next = tail.next
                self.size -= 1
            return True

    def __len__(self):
        return self.size

    def __iter__(self):  # generator
        v = self.head
        while v != None:
            yield v
            v = v.next
