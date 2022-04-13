class Node():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        
class AVLTree():
    def __init__(self,*args):
        self.root=None
        self.height=-1
        self.balance=0
        
        if len(args)==1:
            for i in args[0]:
                self.Insert(i)
                
    def IsLeaf(self):
        return self.height==0
    
    def Insert(self, key):
        new_node=Node(key)
        now=self.root
        if now==None:
            self.root=new_node
            self.root.left=AVLTree()
            self.root.right=AVLTree()
            print('Inserted key['+str(key)+']')
        elif key < now.key:
            now.left.Insert(key)
        elif key > now.key:
            now.right.Insert(key)
        else:
            print('Key['+str(key)+'] already in tree.')
        self.Rebalance()
        
    def Delete(self, key):
        now=self.root
        if now!=None:
            if now.key==key:
                print('Deleting ... '+str(key))
                if now.left.root==None and now.right.root==None:
                    now=None
                elif now.left.root==None:
                    now=now.right.root
                elif now.right.root==None:
                    now=now.left.root
                else:
                    replacement=self.LogicalSuccessor(now)
                    if replacement!=None:
                        print('Found replacement for '+str(key)+' -> '+str(replacement.key))#?
                        now.key=replacement.key
                        now.right.Delete(replacement.key)
            elif key<now.key:
                now.left.Delete(key)
            elif key>now.key:
                now.right.Delete(key)
            self.Rebalance()
        else:
            return
        
    def logicalPredecessor(self,node):  # find the biggest valued node in LEFT child
        node=node.left.root
        if node!=None:
            while node.right!=None:
                if node.right.root==None:
                    return node
                else:
                    node=node.right.root
        return node
        
    def logicalSuccessor(self,node):  # find the smallest valued node in RIGHT child
        node=node.right.root
        if node!=None:  # just a sanity check
            while node.left!=None:
                if node.left.root==None:
                    return node
                else:
                    node=node.left.root
        return node
    
    def Rebalance(self):  # Revalance a particular (sub) tree
        # key inserted, Let's check if we're balanced
        self.UpdateHeights(False)
        self.UpdateBalances(False)
        # 현재 노드(루트, U)의 BF 절대값이 2 이상이면
        # 불균형트리이므로 rotation 수행
        while self.balance<-1 or self.balance>1:
            # U의 Balance Factor가 2 이상이면
            # U의 왼쪽 서브트리 높이가 오른쪽보다 크므로
            # 시나리오1 혹은 시나리오2에 해당
            if self.balance>1:
                # U의 왼쪽 자식노드의 왼쪽 서브트리보다
                # 오른쪽 서브트리의 높이가 클 경우 시나리오2에 해당
                # 우선 single left rotation
                if self.root.left.balance<0:
                    self.root.left.LRotate()
                    # rotation이 됐으므로 BF 업데이트
                    self.UpdateHeights()
                    self.UpdateBalances()
                # U의 왼쪽 자식노드의 왼쪽 서브트리가
                # 오른쪽 서브트리보다 높이가 클 경우 시나리오1에 해당
                # single right rotation (시나리오2도 이 작업 수행)
                self.RRotate()
                # rotation이 됐으므로 BF 업데이트
                self.UpdateHeights()
                self.UpdateBalances()
                
            # U의 Balance Factor가 -1 이하이면
            # U의 오른쪽 서브트리 높이가 왼쪽보다 크므로
            # 시나리오3 혹은 시나리오4에 해당
            if self.balance<-1:
                # U의 오른쪽 자식노드의 오른쪽 서브트리보다
                # 왼쪽 서브트리의 높이가 클 경우 시나리오3에 해당
                # 우선 single right rotation
                if self.root.right.balance>0:
                    self.root.right.RRotate()
                    # rotation이 됐으므로 BF 업데이트
                    self.UpdateHeights()
                    self.UpdateBalances()
                # U의 오른쪽 자식노드의 왼쪽 서브트리보다
                # 올느쪽 서브트리보다 높이가 클 경우 시나리오4에 해당
                # single left rotation (시나리오2도 이 작업 수행)
                self.LRotate()
                # rotation이 됐으므로 BF 업데이트
                self.UpdateHeights()
                self.UpdateBalances()
            
    def RRotate(self):
        # Rotate left pivoting on self
        print('Rotation '+str(self.root.key)+' right')
        A=self.root
        B=self.root.left.root
        T=B.right.root
        self.root=B
        B.right.root=A
        A.left.root=T
        
    def LRotate(self):
        # Rotate left pivoting on self
        print('Rotating '+str(self.root.key)+' left')
        A=self.root
        B=self.root.right.root
        T=B.left.root
        self.root=B
        B.left.root=A
        A.right.root=T
        
    def UpdateHeights(self,recurse=True):
        if self.root==None:
            self.height=-1
        else:
            if recurse:
                if self.root.left!=None:
                    self.root.left.UpdateHeights()
                if self.root.right!=None:
                    self.root.right.UpdateHeights()
            self.height=max(self.root.left.height,self.root.right.height)+1
            
    def UpdateBalances(self,recurse=True):
        if self.root==None:
            self.balance=0
        else:
            if recurse:
                if self.root.left!=None:
                    self.root.left.UpdateBalances()
                if self.root.right!=None:
                    self.root.right.UpdateBalances()
            self.balance=self.root.left.height-self.root.right.height
            
    def CheckBalanced(self):
        if self==None or self.root==None:
            return True
        
        # We always need to make sure we are balanced
        self.UpdateHeights()
        self.UpdateBalances()
        return ((abs(self.balance) < 2) and self.root.left.CheckBalanced() and self.root.right.CheckBalanced())
                
    def InorderTraverse(self):
        if self.root==None:
            return []
        inlist=[]
        l=self.root.left.InorderTraverse()
        for i in l:
            inlist.append(i)
            
        inlist.append(self.root.key)
        
        l=self.root.right.InorderTraverse()
        for i in l:
            inlist.append(i)
            
        return inlist
        
# 출처: https://tbtb7-sw.tistory.com/172
