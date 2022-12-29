import NodeTypes.Node as Ntype

class MyStack:

    count: int
    head: Ntype.Node

    def __init__(self):
       self.count=0
    

    def push(self,input:int=None):
        if (input == None):
            return None
        if (self.count==0):
            self.head=Ntype.Node(val=input)
        else:
            node1=Ntype.Node(val=input)
            node1.NextNode=self.head
            self.head=node1
        
        
        self.count+=1
        return input

    def pop(self):
        if (self.count==0 or self.head==None):
            return "stop"

        val =self.head.val

        if (self.count==1):
            self.head=None
            self.count=0
        else:
            self.head=self.head.NextNode
            self.count=0
        self.count-=1
        return val
        
