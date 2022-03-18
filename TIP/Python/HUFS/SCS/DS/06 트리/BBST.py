# class Node:
#     def __init__(self, key, parent=None, left=None, right=None):
#         self.key=key
#         self.parent=parent
#         self.left=left
#         self.right=right
 
class Node:
    def __init__(self, key):
        self.key=key
        self.parent=self.left=self.right=None
        
    def __str__(self):
        return str(self.key)
    
class BST:
    def __init__(self):
        self.root=None
        self.size=0
        
    def __len__(self):
        return self.size
        
    def preorder(self,v): #노드 v와 자손 노드를 preorder로 방문하면서 출력 MLR
        if v!=None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)
            
    def inorder(self,v): # LMR
        if v!=None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)
    
    def postorder(self,v):
        if v!=None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')

    def find_loc(self, key):
        if self.size==0: return None
        p = None
        v = self.root
        while v:
            if v.key == key: return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p
    
    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None
        
    def insert(self, key):
        p=self.find_loc(key)
        if p==None or p.key!=key:
            v=Node(key)
            if p==None:
                self.root=v
            else:
                v.parent=p
                if p.key>key:
                    p.left=v
                else:
                    p.right=v
            self.size+=1
            return v
        else:
            return None
                
    
    def deleteByMerging(self,x):
        a,b,pt = x.left, x.right, x.parent
        if a==None: c=b
        else: #a!=None
            c,m=a,a
            while m.right:
                m = m.right
            if b: b.parent = m
            m.right=b
        if self.root == x:
            self.root=c
            if c: c.parent = None
        else:
            if pt.left == x: pt.left = c
            else: pt.right = c
            if c: c.parent = pt
        self.size-=1
        
    def deleteByCopying(self,x):
        a,b,pt=x.left,x.right,x.parent
        if a:
            y=a
            while y.right:
                y=y.right
            ypt=y.parent
            x.key=y.key
            if y.left:
                yl=y.left
                if ypt==x:
                    x.left=yl
                    yl.parent=x
                else:
                    ypt.right=yl
                    yl.parent=ypt
                y.parent,y.left=None,None
            else:
                if ypt==x:
                    x.left=None
                else:
                    ypt.right=None
                y.parent=None
        elif b:
            y=b
            while y.left:
                y=y.left
            ypt=y.parent
            x.key=y.key
            if y.right:
                yr=y.right
                if x==ypt:
                    x.right=yr
                    yr.parent=x
                else:
                    ypt.left=yr
                    yr.parent=ypt
                y.parent,y.right=None,None
            else:
                y.parent=None
                if ypt==x:
                    x.right=None
                else:
                    ypt.right=None
        elif pt:
            if x==pt.left:
                pt.left=None
            else:
                pt.right=None
            x.parent=None
        else:
            self.root=None
        self.size-=1
        
    def height(self, x):
        if x == None: return -1
        else:
            l = self.height(x.left)
            r = self.height(x.right)
            x.height = max(l, r) + 1
            return x.height
        
    def number(self, x):
        if x == None:
            return 0
        else:
            l = self.number(x.left)
            r = self.number(x.right)
            x.number = l+r+1
            return x.number
        
    def rotateLeft(self, x):
        if x == None: return
        z = x.right
        if z == None: return
        b = z.left
        z.parent = x.parent
        if x.parnet:
            if x.parent.right == x:
                x.parent.right = z
            else:
                x.parent.left = z
        z.left = x
        x.parent = z
        x.right = b
        if b:
            b.parent = x
        if x == self.root:
            self.root = z
        
    def rotateRight(self, x):
        if x == None: return
        z = x.left
        if z == None: return  # if x==None: nothing changed
        b = z.right           # b == None 인 경우도 가능
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        z.right = x
        x.parent = z
        x.left = b
        if b:
            b.parent = x
        if x == self.root:
            self.root = z
